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
$ pip3 install pytest
$ pip3 install pytest-benchmark
$ pip3 install pygal
```

### Using virtualenv
```
$ pip3 install virtualenv
$ virtualenv venv
$ python3 -m virtualenv venv
$ source venv/bin/activate

$ pip3 install pytest
$ pip3 install pytest-benchmark
$ pip3 install pygal

$ deactivate
```

## Running the tests
```
$ ./run.sh cpubench
$ sudo ./tests/cpubench 50000 --singlethreaded --printdigits
```

```
$ python3 -m pytest main.py
```

## Examples

![Alt text](screenshots/screenshot1.PNG?raw=true "Title")

![Alt text](screenshots/screenshot2.PNG?raw=true "Title")

![Alt text](screenshots/screenshot3.PNG?raw=true "Title")


## Acknowledgments
https://github.com/theblixguy/CPUBench

https://pypi.org/project/pytest-benchmark/

