from models.IR_model import IR

import os

class IRController:
    def __init__(self) -> None:
        self.IR = IR()

    def build(self):
        # return excutable_file_name

        # opt -S -O2 -aa -basicaa -tbaa -licm {target_file.ll}
        os.system('opt -S -O2 -aa -basicaa -tbaa -licm {}'.format(self.IR.source_name))
        pass

    def insert(self):
        pass

    def __call__(self, *args, **kwds) -> None:
        # self.insert()
        # self.build()
        pass
