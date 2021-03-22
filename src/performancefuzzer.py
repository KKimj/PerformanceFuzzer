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
        if self.min is None:
            return True
        if self.min > _min:
            return True
        return False

class PerformanceFuzzer:
    def __init__(self, dirName, fileName = "main", testName = "0", _warmup = 2, _round = 8, _cpubench_arg = 50000):
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

        self.warmup = _warmup
        self.round = _round
        self.cpubench_arg = " "+str(_cpubench_arg) + " --singlethreaded --printdigits"
        self.time = BenchmarkTime()

        '''
        Counting how many lables are in IR file
        Counting how many Functions are in IR file
        ''' 
        self.lable_count = 0
        self.function_count = 0
        
        file_opt_ll = open(self.source+"_opt.ll", "r")
        while True:
            line = file_opt_ll.readline()
            if not line:
                break

            if line.strip().startswith("; <label>"):
                self.lable_count += 1

            if line.strip().startswith("define internal fastcc"):
                self.function_count += 1
                
        file_opt_ll.close()


    def NOP(self):
        return '  call void asm sideeffect "NOP;", ""()\n'

    def Insert_Program_Begin(self, code = '  call void asm sideeffect "NOP;", ""()\n', insert_count = 10):
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
            

            if not insert_flag and line.strip().startswith("define i32 @main"):
                insert_flag = True

            
            while insert_flag and insert_count > 0 :
                file_fuz_ll.write(code)
                insert_count -= 1
                
            print(line)

        file_opt_ll.close()
        file_fuz_ll.close()
        os.system("llc "+self.target+"_opt.ll"+" -o " + self.target + "_opt.s" + " && " + "clang "+ self.target+"_opt.s" + " -o " + self.target + " -fopenmp=libiomp5 -lgmp -lssl -lcrypto" + " && " + "objdump -D "+ self.target + " > " + self.target + ".dump")
    
    def Insert_Program_Last(self, code = '  call void asm sideeffect "NOP;", ""()\n', insert_count = 10):
        file_opt_ll = open(self.source+"_opt.ll", "r")
        file_fuz_ll = open(self.target+"_opt.ll", "w")
        
        insert_flag = False
        
        while True:
            line = file_opt_ll.readline()
            
            if not line:
                break

            if insert_flag and line.startswith("}"):
                insert_flag = False
            
            if insert_flag and line.strip().startswith("ret"):
                insert_flag = False

            if insert_flag and line.strip().startswith("br"):
                insert_flag = False
            

            if not insert_flag and line.strip().startswith("define i32 @main"):
                insert_flag = True

            
            while insert_flag and insert_count > 0 and len(line.strip()) == 0 :
                file_fuz_ll.write(code)
                insert_count -= 1
            
            '''
            code write 부분을 뒤에
            '''

            file_fuz_ll.write(line)
            print(line)

        file_opt_ll.close()
        file_fuz_ll.close()
        os.system("llc "+self.target+"_opt.ll"+" -o " + self.target + "_opt.s" + " && " + "clang "+ self.target+"_opt.s" + " -o " + self.target + " -fopenmp=libiomp5 -lgmp -lssl -lcrypto" + " && " + "objdump -D "+ self.target + " > " + self.target + ".dump")
 


    def Insert_Program_Random(self, code = '  call void asm sideeffect "NOP;", ""()\n', insert_count = 10):
        pass

    def Insert_Function_Begin(self, code = '  call void asm sideeffect "NOP;", ""()\n', insert_count = 10, function_number = 1):
        pass

    def Insert_Function_Last(self, code = '  call void asm sideeffect "NOP;", ""()\n', insert_count = 10, function_number = 1):
        pass

    def Insert_Function_Random(self, code = '  call void asm sideeffect "NOP;", ""()\n', insert_count = 10, function_number = 1):
        pass
    
    

    def Insert_Lable_Begin(self, code = '  call void asm sideeffect "NOP;", ""()\n', insert_count = 10, label_number = 1):
        label_number = (label_number - 1) % self.lable_count + 1
        
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
            

            # if not insert_flag and line.strip().startswith("define internal fastcc i32"):
            #     insert_flag = True

            if not insert_flag and line.strip().startswith("; <label>"):
                if label_number > 0:
                    label_number -= 1
                    continue
                else:
                    insert_flag = True
            
            while insert_flag and insert_count > 0:
                file_fuz_ll.write(code)
                insert_count -= 1
                
            print(line)

        file_opt_ll.close()
        file_fuz_ll.close()
        os.system("llc "+self.target+"_opt.ll"+" -o " + self.target + "_opt.s" + " && " + "clang "+ self.target+"_opt.s" + " -o " + self.target + " -fopenmp=libiomp5 -lgmp -lssl -lcrypto" + " && " + "objdump -D "+ self.target + " > " + self.target + ".dump")

    

    def Insert_Lable_Last(self, code = '  call void asm sideeffect "NOP;", ""()\n', insert_count = 10, label_number = 1):
        label_number = (label_number - 1) % self.lable_count + 1
        
        file_opt_ll = open(self.source+"_opt.ll", "r")
        file_fuz_ll = open(self.target+"_opt.ll", "w")
        
        insert_flag = False
        
        while True:
            line = file_opt_ll.readline()
            if not line:
                break

            if insert_flag and line.startswith("}"):
                insert_flag = False
            
            if insert_flag and line.strip().startswith("ret"):
                insert_flag = False

            if insert_flag and line.strip().startswith("br"):
                insert_flag = False
            

            # if not insert_flag and line.strip().startswith("define internal fastcc i32"):
            #     insert_flag = True

            if not insert_flag and line.strip().startswith("; <label>"):
                if label_number > 0:
                    label_number -= 1
                    continue
                else:
                    insert_flag = True
            
            while insert_flag and insert_count > 0 and len(line.strip()) == 0:
                file_fuz_ll.write(code)
                insert_count -= 1
                
            print(line)
            file_fuz_ll.write(line)
            
        file_opt_ll.close()
        file_fuz_ll.close()
        os.system("llc "+self.target+"_opt.ll"+" -o " + self.target + "_opt.s" + " && " + "clang "+ self.target+"_opt.s" + " -o " + self.target + " -fopenmp=libiomp5 -lgmp -lssl -lcrypto" + " && " + "objdump -D "+ self.target + " > " + self.target + ".dump")

    

    def Insert_Lable_Random(self, code = '  call void asm sideeffect "NOP;", ""()\n', insert_count = 10, label_number = 1):
        pass

    InsertPolicy = [
        Insert_Program_Begin,
        Insert_Program_Last,
        Insert_Program_Random,
        Insert_Lable_Begin,
        Insert_Lable_Last,
        Insert_Lable_Random ]
    
    def updateSource(self): # TODO 3: What is the best name of method?
        os.system('cp '+self.target+'_opt.ll '+self.filePath+'_final.ll')
        os.system('cp '+self.target+' '+self.filePath+'_final')
        self.source = self.target

    def setTarget(self, testName = "0"):
        self.target = self.filePath + testName
    
    
    def BenchmarkSetup(self, _warmup, _round, _cpubench_arg):
        self.warmup = _warmup
        self.round = _round
        self.cpubench_arg = " "+str(_cpubench_arg) + " --singlethreaded --printdigits"
            
    def Run(self, isOriginal = False, isFinal = False):
        start = time.time()
        if isOriginal:
            os.system(self.filePath+self.cpubench_arg)
        elif isFinal:
            os.system(self.filePath+"_final"+self.cpubench_arg)
        else:
            os.system(self.target+self.cpubench_arg)
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
        os.system("clang "+ self.filePath+"_opt.s" + " -o " + self.filePath + " -fopenmp=libiomp5 -lgmp -lssl -lcrypto")
        os.system("objdump -D "+ self.filePath + " > " + self.filePath + ".dump")


    

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
            

            # if not insert_flag and line.strip().startswith("define i32 @main") and line.strip().endswith("{"):
            if not insert_flag and line.strip().startswith("define i32 @main"):
                insert_flag = True

            # if not insert_flag and line.strip().startswith("define internal fastcc i32") and line.strip().endswith("{"):
            if not insert_flag and line.strip().startswith("define internal fastcc i32"):
                insert_flag = True

            if not insert_flag and line.strip().startswith("; <label>"):
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
