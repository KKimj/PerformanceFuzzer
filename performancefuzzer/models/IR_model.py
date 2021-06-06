class IR:
    def __init__(self, path, source_name, target_name, compile_options, execute_arguments) -> None:
        self.path = path
        self.source = path + source_name
        self.target = path + target_name
        self.compile_options = compile_options
        self.execute_arguments = execute_arguments

        self.map = {
            'path' : self.path,

            'source' : self.source,
            'source_c' : self.source+'.c',
            'source_ll' : self.source+'.ll',
            'source_s' : self.source+'.s',

            'target' : self.target,
            'target_c' : self.target+'.c',
            'target_ll' : self.target+'.ll',
            'target_s' : self.target+'.s',

            'compile_options' : self.compile_options,
            'execute_arguments' : self.execute_arguments, 

            'functions_num' : 0,
            'functions' : [
                # {
                #     'name' : '',
                #     'labels_num' : 0,
                # },
            ],
        }