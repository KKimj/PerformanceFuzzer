class BenchmarkTime:
    def __init__(self):
        pass
    pass

# IR Code insert policy
class InsertPolicy:
    def __init__(self):
        pass

    @staticmethod
    def data_padding():
        # data memory area

        # Globla memory

        # Stack memory
        pass

    @staticmethod
    def instruction_padding():
        # code memory area
        
        # Program level

        # Function level

        # Lable level
        pass
    
    @staticmethod
    def insert(source, target):
        #parameter handling
        if source.endswith('.ll'):
            source = source[:-3]
        if target.endswith('.ll'):
            target = target[:-3]
        
        # file load
        source_file = open(source+".ll", "r")
        target_file = open(target+".ll", "w")

        # parsing

        # insertion

        # close file
        source_file.close()
        target_file.close()

        # file build
        os.system("llc "+target+".ll"+" -o " + target + ".s" + " && " + "clang "+ target+".s" + " -o " + target + " -fopenmp=libiomp5 -lgmp -lssl -lcrypto" + " && " + "objdump -D "+ target + " > " + target + ".dump")

        pass

    pass



class PerformanceFuzzer:
    # __init__ to setup filename
    def __init__(self):
        self.source = None
        self.target = None

        self.config = {
            'round' : 5,
            'warmup' : 2,
            'iteration' : 5,
        }
        pass

    # configure to Setup benchmark, insert policy
    def configure(self, warmup = 2, round = 5, iteration = 5):
        self.config = {
            'round' : round,
            'warmup' : warmup,
            'iteration' : iteration,
        }

    # run, fuzzing
    def run(self):
        for round in range(1, self.config['round']+1):
            for warmup in range(1, self.config['warmup']+1):
                pass

            for iteration in range(1, self.config['iteration']+1):
                pass
        pass

    # execute file 
    def test(self):
        pass

    # execute file 
    def execute(self):
        pass

    pass

