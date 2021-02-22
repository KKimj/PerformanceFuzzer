#!/bin/bash

if [ "1"=="$#" ]; then
clang -S -emit-llvm $1.c
opt -S -O3 -aa -basicaa -tbaa -licm $1.ll -o $1_opt.ll
llc $1_opt.ll
clang $1_opt.s -o $1 -fopenmp=libiomp5 -lgmp -lssl -lcrypto
objdump -D $1 > $1.dump
fi
