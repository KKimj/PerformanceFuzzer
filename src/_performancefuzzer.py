class BenchmarkTime:
    def __init__(self):
        pass
    pass

# IR Code insert policy
class InsertPolicy:
    def __init__(self):
        pass
    
    # Static method ?
    def insert(self):
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
    def configure(self):
        pass

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

