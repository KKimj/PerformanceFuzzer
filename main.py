import argparse
import os
import time
import numpy

class BenchmarkTime:

    def __init__(self):
        self.min = None
        self.max = None
        self.prev = None
        self.origin = None
    
    def Update(self, _min, _max, _now): # def setTime ? 
        if self.origin == None:
            self.origin = _now
        self.min = _min
        self.max = _max
        self.prev = _now
    
    def isFaster(self, _min, _max, _now):
        if self.min == None:
            return True

        # TODO 1: would like to improve
        if self.min > _min:
            return True
        return False

class PerformanceFuzzer:

    def __init__(self, dirName, fileName = "main", testName = "0"):
        self.dirName = dirName

        if fileName.endswith('.c'):
            fileName = fileName[:-2]
        self.fileName = fileName

        self.filePath = "./tests/"+self.dirName+"/"+self.fileName
        
        self.source = self.filePath
        self.target = self.filePath + testName

        if os.path.isfile(self.filePath+".c") == False:
            print("File not exist!")
            quit()

        if os.path.isfile(self.filePath+"_opt.ll") == False:
            print("Build!")
            self.Build()

        self.warmup = 0
        self.round = 2
        self.time = BenchmarkTime()
    
    def updateSource(self): # TODO 3: What is the best name of method?
        os.system('cp '+self.target+'_opt.ll '+self.filePath+'_final.ll')
        os.system('cp '+self.target+' '+self.filePath+'_final')
        self.source = self.target

    def setTarget(self, testName = "0"):
        self.target = self.filePath + testName
    
    
    def BenchmarkSetup(self, _warmup, _round):
        self.warmup = _warmup
        self.round = _round
            
    def Run(self):
        start = time.time()
        os.system(self.target+" 50000 --singlethreaded --printdigits")
        self.time_now = time.time() - start
        return self.time_now

    def Benchmark(self):
        for i in range(self.warmup):
            self.Run()
        
        _tmp = self.Run()

        _avg = _tmp
        _min = _tmp
        _max = _tmp
        
        
        for i in range(self.round - 1):
            _tmp = self.Run()

            _avg += _tmp

            if _min > _tmp:
                _min = _tmp
            
            if _max < _tmp:
                _max = _tmp

        _avg /= self.round
        
        if self.time.isFaster(_min, _max, _avg):
            self.time.Update(_min, _max, _avg)
            return True # TODO 2-1: Is it the right design?
        else:
            return False # TODO 2-2: Is it the right design?

        

    
    def Build(self):
        os.system("clang -S -emit-llvm "+ self.filePath+".c "+ " -o " + self.filePath+".ll")
        os.system("opt -S -O3 -aa -basicaa -tbaa -licm "+self.filePath+".ll " +" -o "+self.filePath+"_opt.ll")

    def NOP(self):
        return '  call void asm sideeffect "NOP;", ""()\n'

    def Insert(self, nop_count = 0):    
        file_opt_ll = open(self.source+"_opt.ll", "r")
        file_fuz_ll = open(self.target+"_opt.ll", "w")
        
        insert_flag = False
        
        while True:
            line = file_opt_ll.readline()
            file_fuz_ll.write(line)
            if not line:
                break

            if insert_flag and len(line.strip()) <= 0:
                continue

            if insert_flag and line.startswith("}"):
                insert_flag = False
            
            if insert_flag and line.strip().startswith("ret"):
                insert_flag = False

            if insert_flag and line.strip().startswith("br"):
                insert_flag = False
            

            if not insert_flag and line.startswith("define i32 @main") and line.endswith("{"):
                insert_flag = True

            if not insert_flag and line.startswith("define internal fastcc i32") and line.endswith("{"):
                insert_flag = True

            if not insert_flag and line.startswith("; <label>"):
                insert_flag = True
            
            if insert_flag and nop_count > 0 and numpy.random.choice(numpy.arange(1, 7), p=[0.1, 0.05, 0.05, 0.2, 0.4, 0.2]):
                file_fuz_ll.write('  call void asm sideeffect "NOP;", ""()\n')
                nop_count -= 1
                
            print(line)

        file_opt_ll.close()
        file_fuz_ll.close()

        # os.system("llc "+self.target+"_opt_fuzzer.ll"+" -o " + self.target + "_opt_fuzzer.s")
        # os.system("clang "+ self.target+"_opt_fuzzer.s" + " -o " + self.target + " -fopenmp=libiomp5 -lgmp -lssl -lcrypto")
        # os.system("objdump -D "+ self.target + " > " + self.target + ".dump")

        os.system("llc "+self.target+"_opt.ll"+" -o " + self.target + "_opt.s" + " && " + "clang "+ self.target+"_opt.s" + " -o " + self.target + " -fopenmp=libiomp5 -lgmp -lssl -lcrypto" + " && " + "objdump -D "+ self.target + " > " + self.target + ".dump")


def tester_original(benchmark):
    # global performanceFuzzer
    performanceFuzzer = PerformanceFuzzer("cpubench", "cpubench")
    performanceFuzzer.Insert(nop_count = 0)
    result = benchmark(performanceFuzzer.Run)
    assert result > 2

def tester_nop10(benchmark):
    # global performanceFuzzer
    performanceFuzzer = PerformanceFuzzer("cpubench", "cpubench", testName = "10")
    performanceFuzzer.Insert(nop_count = 10)
    result = benchmark(performanceFuzzer.Run)
    assert result > 2

def tester_nop50(benchmark):
    # global performanceFuzzer
    performanceFuzzer = PerformanceFuzzer("cpubench", "cpubench", testName = "50")
    performanceFuzzer.Insert(nop_count = 50)
    result = benchmark(performanceFuzzer.Run)
    assert result > 2

def tester_nop100(benchmark):
    # global performanceFuzzer
    performanceFuzzer = PerformanceFuzzer("cpubench", "cpubench", testName = "100")
    performanceFuzzer.Insert(nop_count = 100)
    result = benchmark(performanceFuzzer.Run)
    assert result > 2

def tester_nop150(benchmark):
    # global performanceFuzzer
    performanceFuzzer = PerformanceFuzzer("cpubench", "cpubench", testName = "150")
    performanceFuzzer.Insert(nop_count = 150)
    result = benchmark(performanceFuzzer.Run)
    assert result > 2

def tester_nop200(benchmark):
    # global performanceFuzzer
    performanceFuzzer = PerformanceFuzzer("cpubench", "cpubench", testName = "200")
    performanceFuzzer.Insert(nop_count = 200)
    result = benchmark(performanceFuzzer.Run)
    assert result > 2

def tester_nop250(benchmark):
    # global performanceFuzzer
    performanceFuzzer = PerformanceFuzzer("cpubench", "cpubench", testName = "250")
    performanceFuzzer.Insert(nop_count = 250)
    result = benchmark(performanceFuzzer.Run)
    assert result > 2

def tester_nop290(benchmark):
    # global performanceFuzzer
    performanceFuzzer = PerformanceFuzzer("cpubench", "cpubench", testName = "290")
    performanceFuzzer.Insert(nop_count = 290)
    result = benchmark(performanceFuzzer.Run)
    assert result > 2

# def tester_nop500(benchmark):
#     # global performanceFuzzer
#     performanceFuzzer = PerformanceFuzzer("cpubench", "cpubench", testName = "500")
#     performanceFuzzer.Insert(nop_count = 500)
#     result = benchmark(performanceFuzzer.Run)
#     assert result > 2

# def tester_nop1000(benchmark):
#     # global performanceFuzzer
#     performanceFuzzer = PerformanceFuzzer("cpubench", "cpubench", testName = "1000")
#     performanceFuzzer.Insert(nop_count = 1000)
#     result = benchmark(performanceFuzzer.Run)
#     assert result > 2


# def tester_nop3000(benchmark):
#     # global performanceFuzzer
#     performanceFuzzer = PerformanceFuzzer("cpubench", "cpubench", testName = "3000")
#     performanceFuzzer.Insert(nop_count = 3000)
#     result = benchmark(performanceFuzzer.Run)
#     assert result > 2


# def tester_nop5000(benchmark):
#     # global performanceFuzzer
#     performanceFuzzer = PerformanceFuzzer("cpubench", "cpubench", testName = "5000")
#     performanceFuzzer.Insert(nop_count = 5000)
#     result = benchmark(performanceFuzzer.Run)
#     assert result > 2

# def tester_nop7000(benchmark):
#     # global performanceFuzzer
#     performanceFuzzer = PerformanceFuzzer("cpubench", "cpubench", testName = "7000")
#     performanceFuzzer.Insert(nop_count = 7000)
#     result = benchmark(performanceFuzzer.Run)
#     assert result > 2

# def tester_nop10000(benchmark):
#     # global performanceFuzzer
#     performanceFuzzer = PerformanceFuzzer("cpubench", "cpubench", testName = "10000")
#     performanceFuzzer.Insert(nop_count = 10000)
#     result = benchmark(performanceFuzzer.Run)
#     assert result > 2

# def tester_nop20000(benchmark):
#     # global performanceFuzzer
#     performanceFuzzer = PerformanceFuzzer("cpubench", "cpubench", testName = "20000")
#     performanceFuzzer.Insert(nop_count = 20000)
#     result = benchmark(performanceFuzzer.Run)
#     assert result > 2

def main(filename_list, option_list):
    if len(filename_list) == 1:
        performanceFuzzer = PerformanceFuzzer(filename_list[0])
    elif len(filename_list) == 2:
        performanceFuzzer = PerformanceFuzzer(filename_list[0], filename_list[1])

    performanceFuzzer.Insert()

    _improveCount = 0
    for i in range(10):
        if performanceFuzzer.Benchmark():
            performanceFuzzer.updateSource()
            _improveCount += 1
            performanceFuzzer.setTarget(str(_improveCount))
            performanceFuzzer.Insert(i*50)
            print("improved! %f"%(performanceFuzzer.time.prev))
    
    print("%f -> %f : avgtime %f  %f%% faster nop count : %d"%(performanceFuzzer.time.origin, performanceFuzzer.time.min, performanceFuzzer.time.prev, (performanceFuzzer.time.origin-performanceFuzzer.time.min)/performanceFuzzer.time.origin*100, _nop_count))



def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(nargs='+' ,help='Example) index.html', dest='filename')
    parser.add_argument('--optional', '-o', nargs='*', help='Example) save', default=[], dest='option')

    filename_list = parser.parse_args().filename
    option_list = parser.parse_args().option

    return filename_list, option_list


if __name__ == '__main__':
    filename_list, option_list = get_arguments()
    main(filename_list, option_list)