import os
from models.benchmark_model import Benchmark

class BenchmarkController:
    def __init__(self, command='', verbos = 1) -> None:
        self.benchmark = Benchmark()
        self.verbos = verbos
        self.command = command
        self.command = './tests/cpubench/cpubench 50000 --singlethreaded --printdigits > tmp.tmp'
        # self.command = 'pwd'

    def perf(self):
        self.perf_command = 'sudo perf stat -r 2  2>&1'
        self.perf_command = 'sudo perf stat 2>&1'
        # self.perf_command = 'sudo perf stat -r 2'
        # self.perf_command = 'sudo perf stat -e cycles,instructions,cache-references,cache-misses,bus-cycles -a'
        time = -1
        user_time = -1
        sys_time = -1
        cycles = -1

        popen = os.popen(self.perf_command+' '+self.command)
        # result = popen.read()
        lines = popen.readlines()
        for line in lines:
            if not line:
                continue
            line = line.strip()
            values = line.split()
            
            if line.find('time') >= 0:
                time = float(values[0])

                if self.verbos >= 3:
                    print(line, values)

            if line.find('cycles') >= 0:
                cycles = values[0].replace(',', '')
                cycles = int(cycles)
                
            if line.find('sys') >= 0:
                sys_time = float(values[0])

                if self.verbos >= 3:
                    print(line, values)

            if line.find('user') >= 0:
                user_time = float(values[0])

                if self.verbos >= 3:
                    print(line, values)
        
        results = {
            'time' : time,
            'user_time' : user_time,
            'sys_time' : sys_time,
            'cycles' : cycles,
        }
        if self.verbos >= 2:
            print(results)
        
        return results
        

    @property
    def time(self) -> float:
        return self.benchmark.user_time+self.benchmark.sys_time

if __name__ == '__main__':
    benchmarkController = BenchmarkController(verbos=3)
    benchmarkController.perf()
    # print(benchmarkController.time)

