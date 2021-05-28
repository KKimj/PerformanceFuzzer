import os
from performancefuzzer.models.benchmark_model import Benchmark

class BenchmarkController:
    def __init__(self, verbos = 1) -> None:
        self.verbos = verbos

        self.benchmark = Benchmark()

        self.command = './tests/cpubench/cpubench 50000 --singlethreaded --printdigits > tmp.tmp'
        # self.command = 'pwd'

    def perf(self):
        self.perf_command = 'sudo perf stat -r 2  2>&1'
        # self.perf_command = 'sudo perf stat -e cycles,instructions,cache-references,cache-misses,bus-cycles -a'

        popen = os.popen(self.perf_command+' '+self.command)
        # result = popen.read()
        results = popen.read()
        for result in results.splitlines():
            values = result.strip().split()
            if not values:
                continue
            if values[-1].strip() == 'time':
                if self.verbos == 3:
                    print(values)
                self.benchmark.time = float(values[0])

            if values[-1].strip() == 'user':
                self.benchmark.user_time = float(values[0])
                # print(float(values[0]))
            if values[-1].strip() == 'sys':
                self.benchmark.sys_time = float(values[0])
                # print(float(values[0]))
                   
        if self.verbos == 2:
            print(results)
        

    @property
    def time(self) -> float:
        return self.benchmark.user_time+self.benchmark.sys_time

if __name__ == '__main__':
    benchmarkController = BenchmarkController(verbos=3)
    benchmarkController.perf()
    # print(benchmarkController.time)

