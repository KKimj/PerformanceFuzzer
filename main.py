import argparse
import os
import time
import numpy
from src.performancefuzzer import PerformanceFuzzer
from src.performancefuzzer import BenchmarkTime


def tester_original(benchmark):
    # global performanceFuzzer
    performanceFuzzer = PerformanceFuzzer("cpubench", "cpubench")
    result = benchmark(performanceFuzzer.Run, isOriginal = True)
    assert result != 0

def tester_final(benchmark):
    # global performanceFuzzer
    performanceFuzzer = PerformanceFuzzer("cpubench", "cpubench")
    result = benchmark(performanceFuzzer.Run, isFinal = True)
    assert result != 0

def main(filename_list, _warmup, _round, _cpubench_arg):
    if len(filename_list) == 1:
        performanceFuzzer = PerformanceFuzzer(filename_list[0], verbose=True)
    elif len(filename_list) == 2:
        performanceFuzzer = PerformanceFuzzer(filename_list[0], filename_list[1], verbose=True)

    input('Press any key to start')

    performanceFuzzer.BenchmarkSetup(_warmup, _round, _cpubench_arg)
    performanceFuzzer.Insert()

    _nop_count = 0
    _improveCount = 0
    for i in range(10):
        if performanceFuzzer.Benchmark():
            performanceFuzzer.updateSource()
            _improveCount += 1
            performanceFuzzer.setTarget(str(_improveCount))
            
            _nop_count = i*50
            performanceFuzzer.Insert(_nop_count)

            print("improved! %f"%(performanceFuzzer.time.prev))
    
    print("%f -> %f : avgtime %f  %f%% faster nop count : %d"%(performanceFuzzer.time.origin, performanceFuzzer.time.min, performanceFuzzer.time.prev, (performanceFuzzer.time.origin-performanceFuzzer.time.min)/performanceFuzzer.time.origin*100, _nop_count))
    print("Run\n$ python3 -m pytest main.py --benchmark-histogram")



def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(nargs='+' ,help='Example) index.html', dest='filename')

    parser.add_argument('--warmup', '-w', nargs=None, type=int , default = 1, help='warmup before benchmark')
    parser.add_argument('--round', '-r', nargs=None, type=int, default = 4, help='number of running test')
    parser.add_argument('--cpubench', '-cpu', nargs=None, type=int, default = 50000, help='argument for cpubench')


    filename_list = parser.parse_args().filename
    _warmup = parser.parse_args().warmup
    _round = parser.parse_args().round
    _cpubench_arg = parser.parse_args().cpubench

    return filename_list, _warmup, _round, _cpubench_arg


if __name__ == '__main__':
    filename_list, _warmup, _round, _cpubench_arg = get_arguments()
    main(filename_list, _warmup, _round, _cpubench_arg)