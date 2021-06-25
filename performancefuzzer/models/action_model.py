'''Action model'''

class Action:
    def __init__(self, file_num = 0, function_num = 0, label_num = 0, method_num = 0, method_count = 0, code = ''):
        self.file_num = file_num
        self.function_num = function_num
        self.label_num = label_num

        self.method_num = method_num
        self.method_count = method_count

        self.code = code