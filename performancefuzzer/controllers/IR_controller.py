from models.IR_model import IR

import os

class IRController:
    def __init__(self, path = './tests/cpubench/', filename = 'cpubench.c') -> None:
        self.IR = IR()

        self.path = path
        self.filename = filename

        self.source = self.path + self.filename
        self.target = self.path + self.filename + '.ll'


    def build(self):
        # return excutable_file_name

        # opt -S -O2 -aa -basicaa -tbaa -licm {target_file.ll}
        opt_command = 'opt -S -O2 -aa -basicaa -tbaa -licm {target}'.format(target = self.target)
        os.system(opt_command)

        # clang test.s -o test  -fopenmp=libiomp5 -lgmp -lssl -lcrypto
        clang_command = 'clang {target} -o {bench} {compile_option}'.format(compile_option = '-fopenmp=libiomp5 -lgmp -lssl -lcrypto')
        os.system(clang_command)
        pass

    def profiling(self):
        # clang -S -emit-llvm {source_file.c} -o {target_file.ll}
        command = 'clang -S -emit-llvm {source} -o {target}'.format(source = self.source, target = self.target)
        os.system(command)
        pass

    def insert(self):
        pass

    def read(self):
        pass

    def readlines(self):
        pass

    def write(self):
        pass

    def __call__(self, *args, **kwds) -> None:
        # self.insert()
        # self.build()
        pass

    def test(self):
        self.profiling()
        lines = os.popen('cat '+self.target).readlines()

        print(lines)
        for line in lines:
            print(line)


if __name__ == '__main__':
    print('IR Controller!')
    IRController().test()