from src.performancefuzzer.models.IR_model import IRModel

import os

class IRController:
    def __init__(self) -> None:
        self.IR = IRModel()

    def build(self):
        # return excutable_file_name

        # opt -S -O2 -aa -basicaa -tbaa -licm {target_file.ll}
        os.system('opt -S -O2 -aa -basicaa -tbaa -licm {}'.format(self.IR.source_name))
        pass

    def insert(self):
        pass

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        # self.insert()
        # self.build()
        pass
