import os
import subprocess
from models.benchmark_model import Benchmark

class BenchmarkController:
    def __init__(self, command='', verbos = 1) -> None:
        self.benchmark = Benchmark()
        self.verbos = verbos
        self.command = command
        self.command = './tests/cpubench/cpubench 50000 --singlethreaded --printdigits > tmp.tmp'
        # self.command = 'pwd'

    def perf(self) -> dict:
        self.perf_command = 'sudo perf stat -r 5  2>&1'
        # self.perf_command = 'sudo perf stat 2>&1'
        # self.perf_command = 'sudo perf stat -r 2'
        # self.perf_command = 'sudo perf stat -e cycles,instructions,cache-references,cache-misses,bus-cycles -a'
        
        task_clock, CPUs_utilized, context_switches, cpu_migrations, page_faults, cycles, instructions, branches, branch_misses, time, user_time, sys_time = tuple([-1] * 12)

        popen = os.popen(self.perf_command+' '+self.command)
        # result = popen.read()
        lines = popen.readlines()
        for line in lines:
            if self.verbos == 3:
                print(line)
            if not line:
                continue
            line = line.strip()
            values = line.split()

            if line.find('task-clock') >= 0:
                task_clock = float(values[0].replace(',', ''))

            if line.find('context-switches') >= 0:
                context_switches = int(values[0].replace(',', ''))

            if line.find('CPUs utilized') >= 0:
                CPUs_utilized = values[values.index('CPUs')-1]

            if line.find('cpu-migrations') >= 0:
                cpu_migrations = int(values[0].replace(',', ''))

            if line.find('page-faults') >= 0:
                page_faults = int(values[0].replace(',', ''))

            if line.find('cycles') >= 0:
                cycles = int(values[0].replace(',', ''))

            if line.find('instructions') >= 0:
                instructions = int(values[0].replace(',', ''))

            if line.find('branches') >= 0:
                branches = int(values[0].replace(',', ''))

            if line.find('branch-misses') >= 0:
                branch_misses = int(values[0].replace(',', ''))
            
            if line.find('time') >= 0:
                time = float(values[0].replace(',', ''))

                
            if line.find('sys') >= 0:
                sys_time = float(values[0].replace(',', ''))

            if line.find('user') >= 0:
                user_time = float(values[0].replace(',', ''))
            
              

        results = {
            'task_clock' : task_clock,
            'CPUs_utilized' : CPUs_utilized,

            'context_switches' : context_switches,
            'cpu_migrations' : cpu_migrations,
            'page_faults' : page_faults,

            'cycles' : cycles,   
            'instructions' : instructions,
            'branches' : branches,
            'branch_misses' : branch_misses,

            'time' : time,
            'user_time' : user_time,
            'sys_time' : sys_time,
        }            

        self.fromJson(results)        
        return results
        
    def toJson(self) -> dict:
        json = {
            'task_clock' : self.benchmark.task_clock,
            'CPUs_utilized' : self.benchmark.CPUs_utilized,

            'context_switches' : self.benchmark.context_switches,
            'cpu_migrations' : self.benchmark.cpu_migrations,
            'page_faults' : self.benchmark.page_faults,

            'cycles' : self.benchmark.cycles,   
            'instructions' : self.benchmark.instructions,
            'branches' : self.benchmark.branches,
            'branch_misses' : self.benchmark.branch_misses,
            
            'time' : self.benchmark.time,
            'user_time' : self.benchmark.user_time,
            'sys_time' : self.benchmark.sys_time,
        }
        return json
    
    def fromJson(self, json) -> None:
        self.benchmark.task_clock = json['task_clock']
        self.benchmark.CPUs_utilized = json['CPUs_utilized']

        self.benchmark.context_switches = json['context_switches']
        self.benchmark.cpu_migrations = json['cpu_migrations']
        self.benchmark.page_faults = json['page_faults']

        self.benchmark.cycles = json['cycles']
        self.benchmark.instructions = json['instructions']
        self.benchmark.branches = json['branches']
        self.benchmark.branch_misses = json['branch_misses']

        self.benchmark.time = json['time']
        self.benchmark.user_time = json['user_time']
        self.benchmark.sys_time = json['sys_time']
        

    @property
    def time(self) -> float:
        return self.benchmark.time

if __name__ == '__main__':
    benchmarkController = BenchmarkController(verbos=3)
    benchmarkController.perf()
    print(benchmarkController.toJson())
    print(benchmarkController.time)

