#!/bin/bash

if [ "1"=="$#" ]; then
clang -S -emit-llvm tests/$1.c -o tests/$1.ll
opt -S -O3 -aa -basicaa -tbaa -licm tests/$1.ll -o tests/$1_opt.ll
llc tests/$1_opt.ll
clang tests/$1_opt.s -o tests/$1 -fopenmp=libiomp5 -lgmp -lssl -lcrypto
objdump -D tests/$1 > tests/$1.dump

# python code 
# python3 main.py $1
# llc tests/$1_opt_fuzzer.ll
# clang tests/$1_opt_fuzzer.s -o tests/$1_fuzzer -fopenmp=libiomp5 -lgmp -lssl -lcrypto
# objdump -D tests/$1_fuzzer > tests/$1_fuzzer.dump
fi
