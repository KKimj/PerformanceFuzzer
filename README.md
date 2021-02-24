# PerformanceFuzzer
PerformanceFuzzer

## Getting Started
```
$ git clone https://github.com/KKimj/PerformanceFuzzer
```

### Prerequisites
```
$ sudo apt update && sudo apt upgrade
$ sudo apt-get install libgmp3-dev
$ pip3 install pytest-benchmark
```

## Running the tests
```
$ ./run.sh cpubench
$ sudo ./tests/cpubench 50000 --singlethreaded --printdigits

```

## Acknowledgments
https://github.com/theblixguy/CPUBench

https://pypi.org/project/pytest-benchmark/

