#!/bin/bash

if [ "1"=="$#" ]; then
clang -S -emit-llvm tests/$1.c
opt -S -O3 -aa -basicaa -tbaa -licm tests/$1.ll -o tests/$1_opt.ll
llc tests/$1_opt.ll
clang tests/$1_opt.s -o tests/$1 -fopenmp=libiomp5 -lgmp -lssl -lcrypto
objdump -D tests/$1 > tests/$1.dump
fi
