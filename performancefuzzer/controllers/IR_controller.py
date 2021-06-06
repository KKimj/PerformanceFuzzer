from models.IR_model import IR

import os
import subprocess

class IRController:
    def __init__(self,
            path = '/home/kkimj/PerformanceFuzzer/tests/cpubench/',
            source_name = 'cpubench.c',
            target_name = 'cpubench_opt',
            compile_option = '-fopenmp=libiomp5 -lgmp -lssl -lcrypto',
            execute_arguments = ' 50000 --singlethreaded --printdigits',
            ) -> None:

        self.IR = IR()

        self.path = path
        
        source_name = source_name[:-2] if source_name.endswith('.c') else source_name
        target_name = source_name if target_name is None else target_name

        self.source = self.path + source_name
        self.target = self.path + target_name

        self.map = {
            'source' : self.source,
            'source_c' : self.source+'.c',
            'source_ll' : self.source+'.ll',
            'source_s' : self.source+'.s',

            'target' : self.target,
            'target_c' : self.target+'.c',
            'target_ll' : self.target+'.ll',
            'target_s' : self.target+'.s',

            'compile_option' : compile_option,
            'execute_arguments' : execute_arguments, 

            'functions_num' : 0,
            'functions' : [
                # {
                #     'name' : '',
                #     'labels_num' : 0,
                # },
            ],
        }


    def build(self) -> str:
        # return excutable_file_name

        # opt -S -O2 -aa -basicaa -tbaa -licm {target_file.ll}
        opt_command = 'opt -S -O2 -aa -basicaa -tbaa -licm {target_ll} -o {target_ll}'.format_map(self.map)
        os.system(opt_command)

        # llc {target_file.ll} -o {target_file.out}
        llc_command = 'llc {target_ll} -o {target_s}'.format_map(self.map)
        os.system(llc_command)


        # clang test.s -o test  -fopenmp=libiomp5 -lgmp -lssl -lcrypto
        clang_command = 'clang {target_ll} -o {target} {compile_option}'.format_map(self.map)
        os.system(clang_command)

        # executing output file
        # os.system(' {target} {execute_arguments}'.format_map(self.map))
        return self.target

    def execute(self):
        # executing output file
        os.system(' {target} {execute_arguments}'.format_map(self.map))
        

    def profiling(self):
        # compile .c to .ll
        # clang -S -emit-llvm {source_file.c} -o {target_file.ll}
        clang_command = 'clang -S -emit-llvm {source_c} -o {target_ll}'.format_map(self.map)
        os.system(clang_command)
        
        lines = self.readlines()
        for line in lines:
            # funtions
            if line.find('define') >= 0:
                # define i32 @main(i32, i8**) #0 {
                function_name_start_idx = line.find('@') + 1
                function_name_end_idx = line.find('(')
                functions_name = line[function_name_start_idx:function_name_end_idx]

                self.map['functions'].append({
                    'name' : '',
                    'labels_num' : 0,
                })
                self.map['functions_num'] += 1
                self.map['functions'][-1]['name'] = functions_name

            # labels
            if line.find('<label>') >= 0:
                # ; <label>:26:                                     ; preds = %2
                # print(line)
                self.map['functions'][-1]['labels_num'] += 1

        # results
        profile_result = 'functions num : {functions_num}'.format_map(self.map)
        print(profile_result)

        functions = self.map['functions']
        for function in functions:
            print(function)

    def insert(self):
        pass

    def read(self):
        cat_command = 'cat {source_ll}'.format_map(self.map)
        line = os.popen(cat_command).read()
        return line

    def readlines(self):
        cat_command = 'cat {source_ll}'.format_map(self.map)
        lines = os.popen(cat_command).readlines()
        return lines

    def write(self, lines = None,) -> int:
        if lines is not None:
            ll_file = open('{target_ll}'.format_map(self.map), 'w')

            ll_file.writelines(lines)

            ll_file.close()
        return 0



    def __call__(self, *args, **kwds) -> None:
        # self.insert()
        # self.build()
        pass

    def test(self):
        self.profiling()
        
        lines = self.readlines()
        self.write(lines)

        self.build()
        
        self.execute()
        

if __name__ == '__main__':
    print('IR Controller!')
    IRController().test()
