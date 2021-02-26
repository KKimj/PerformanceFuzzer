import argparse
import os.path
class PerformanceFuzzer:
    def __init__(self, dirName, fileName = "main"):
        self.dirName = dirName

        if fileName.endswith('.c'):
            fileName = fileName[:-2]
        self.fileName = fileName

        self.filePath = "./tests/"+self.dirName+"/"+self.fileName

        if os.path.isfile(self.filePath+".c") == False:
            print("File not exist!")
            quit()

        if os.path.isfile(self.filePath+"_opt.ll") == False:
            print("Makefile!")
            self.Build()
            

    def Run(self):
        pass

    def Build(self):
        pass

    def NOP(self):
        return '  call void asm sideeffect "NOP;", ""()\n'

    def Insert(self):    
        file_opt_ll = open(self.filePath+"_opt.ll", "r")
        file_fuz_ll = open(self.filePath+"_opt_fuzzer.ll", "w")
        
        nop_count = 1
        

        insert_flag = False
        while True:
            line = file_opt_ll.readline()
            file_fuz_ll.write(line)
            if not line:
                break

            if insert_flag and len(line) < 0:
                insert_flag = False

            if insert_flag and line.startswith("}"):
                insert_flag = False

            if not insert_flag and line.startswith("; <label>") and nop_count > 0:
                insert_flag = True
            
            if insert_flag and nop_count > 0:
                file_fuz_ll.write('  call void asm sideeffect "NOP;", ""()\n')
                nop_count -= 1
                
            print(line)

        file_opt_ll.close()
        file_fuz_ll.close()



def main(filename_list, option_list):
    if len(filename_list) == 1:
        performanceFuzzer = PerformanceFuzzer(filename_list[0])
    elif len(filename_list) == 2:
        performanceFuzzer = PerformanceFuzzer(filename_list[0], filename_list[1])

    performanceFuzzer.Insert()
    performanceFuzzer.Run()



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