; ModuleID = './tests/cpubench/cpubench.c'
source_filename = "./tests/cpubench/cpubench.c"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

%struct._IO_FILE = type { i32, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, %struct._IO_marker*, %struct._IO_FILE*, i32, i32, i64, i16, i8, [1 x i8], i8*, i64, i8*, i8*, i8*, i8*, i64, i32, [20 x i8] }
%struct._IO_marker = type { %struct._IO_marker*, %struct._IO_FILE*, i32 }
%struct.timespec = type { i64, i64 }
%struct.__mpz_struct = type { i32, i32, i64* }
%struct.__mpf_struct = type { i32, i32, i64, i64* }
%struct.MD5state_st = type { i32, i32, i32, i32, i32, i32, [16 x i32], i32 }
%struct.utsname = type { [65 x i8], [65 x i8], [65 x i8], [65 x i8], [65 x i8], [65 x i8] }

@x = global i64 0, align 8
@y = global i64 0, align 8
@pnum = global i32 0, align 4
@tpnums = global i32 0, align 4
@.str = private unnamed_addr constant [73 x i8] c"%sWARN: Unable to max out priority. Did you not run this app as root?%s\0A\00", align 1
@.str.1 = private unnamed_addr constant [6 x i8] c"\1B[33m\00", align 1
@.str.2 = private unnamed_addr constant [5 x i8] c"\1B[0m\00", align 1
@.str.3 = private unnamed_addr constant [14 x i8] c"--printdigits\00", align 1
@.str.4 = private unnamed_addr constant [11 x i8] c"--nodigits\00", align 1
@.str.5 = private unnamed_addr constant [13 x i8] c"--dumpdigits\00", align 1
@.str.6 = private unnamed_addr constant [17 x i8] c"--singlethreaded\00", align 1
@.str.7 = private unnamed_addr constant [16 x i8] c"--multithreaded\00", align 1
@stderr = external global %struct._IO_FILE*, align 8
@.str.8 = private unnamed_addr constant [695 x i8] c"%sError: Invalid command-line arguments!%s\0AUsage: cpubench [value] [threading] [parameter]\0AValue: Any number from 1 to 2^32-1\0A(in case of single threaded bench, it will be used to compute primes from 1 to n (where n = value between 1 and 2^32-1) or n digits of PI (where n = value between 1 and 2^32-1)\0AParameter:\0A--printdigits : Prints all digits of PI on console\0A--nodigits : Suppresses printing of digits of PI on console (Use this when doing multithreaded bench)\0A--dumpdigits : Saves all the digits of PI to a text file\0AThreading:\0A--singlethreaded : Stresses only one core (PI)\0A--multithreaded : Stresses all the cores (PRIMES)\0A\0AUsage example: cpubench 50000 --singlethreaded --printdigits\0A\00", align 1
@.str.9 = private unnamed_addr constant [6 x i8] c"\1B[31m\00", align 1
@.str.10 = private unnamed_addr constant [67 x i8] c"%s\0A---------------------------------------------------------------\00", align 1
@.str.11 = private unnamed_addr constant [6 x i8] c"\1B[32m\00", align 1
@.str.12 = private unnamed_addr constant [45 x i8] c"\0ACPU Bench v1.0 beta (%s)\0ABuild date: %s %s\0A\00", align 1
@.str.13 = private unnamed_addr constant [12 x i8] c"Feb 28 2021\00", align 1
@.str.14 = private unnamed_addr constant [9 x i8] c"22:48:51\00", align 1
@.str.15 = private unnamed_addr constant [68 x i8] c"---------------------------------------------------------------%s\0A\0A\00", align 1
@.str.16 = private unnamed_addr constant [41 x i8] c"%sError: Digit cannot be lower than 1%s\0A\00", align 1
@.str.17 = private unnamed_addr constant [76 x i8] c"Performing single-threaded benchmarking [PI]\0AComputing %lu digits of PI...\0A\00", align 1
@.str.18 = private unnamed_addr constant [31 x i8] c"Here are the digits:\0A\0A%.1s.%s\0A\00", align 1
@.str.19 = private unnamed_addr constant [13 x i8] c"pidigits.txt\00", align 1
@.str.20 = private unnamed_addr constant [2 x i8] c"w\00", align 1
@.str.21 = private unnamed_addr constant [30 x i8] c"%sError while opening file%s\0A\00", align 1
@.str.22 = private unnamed_addr constant [9 x i8] c"%.1s.%s\0A\00", align 1
@.str.23 = private unnamed_addr constant [37 x i8] c"MD5 checksum (for verification): %s\0A\00", align 1
@.str.24 = private unnamed_addr constant [79 x i8] c"Performing multi-threaded benchmarking [Primes]\0AComputing primes under %lu...\0A\00", align 1
@.str.25 = private unnamed_addr constant [28 x i8] c"Total primes found are %lu\0A\00", align 1
@.str.26 = private unnamed_addr constant [4 x i8] c"%lu\00", align 1
@.str.27 = private unnamed_addr constant [10 x i8] c"Goodbye!\0A\00", align 1
@start = common global %struct.timespec zeroinitializer, align 8
@end = common global %struct.timespec zeroinitializer, align 8
@pstart = common global %struct.timespec zeroinitializer, align 8
@pend = common global %struct.timespec zeroinitializer, align 8
@i = common global i64 0, align 8
@ti = common global i64 0, align 8
@constant1 = common global i64 0, align 8
@constant2 = common global i64 0, align 8
@constant3 = common global i64 0, align 8
@precision = common global i64 0, align 8
@digest = common global [16 x i8] zeroinitializer, align 16
@oput = common global i8* null, align 8
@u = common global i32 0, align 4
@bits = common global double 0.000000e+00, align 8
@v1 = common global [1 x %struct.__mpz_struct] zeroinitializer, align 16
@v2 = common global [1 x %struct.__mpz_struct] zeroinitializer, align 16
@v3 = common global [1 x %struct.__mpz_struct] zeroinitializer, align 16
@v4 = common global [1 x %struct.__mpz_struct] zeroinitializer, align 16
@v5 = common global [1 x %struct.__mpz_struct] zeroinitializer, align 16
@V1 = common global [1 x %struct.__mpf_struct] zeroinitializer, align 16
@V2 = common global [1 x %struct.__mpf_struct] zeroinitializer, align 16
@V3 = common global [1 x %struct.__mpf_struct] zeroinitializer, align 16
@total = common global [1 x %struct.__mpf_struct] zeroinitializer, align 16
@tmp = common global [1 x %struct.__mpf_struct] zeroinitializer, align 16
@res = common global [1 x %struct.__mpf_struct] zeroinitializer, align 16
@exponent = common global i64 0, align 8
@context = common global %struct.MD5state_st zeroinitializer, align 4
@.str.28 = private unnamed_addr constant [24 x i8] c"Total iterations: %lu\0A\0A\00", align 1
@.str.29 = private unnamed_addr constant [34 x i8] c"Done!\0A\0ATime taken (seconds): %lf\0A\00", align 1
@.str.30 = private unnamed_addr constant [5 x i8] c"%02x\00", align 1

; Function Attrs: noinline nounwind optnone uwtable
define i32 @main(i32, i8**) #0 {
  %3 = alloca i32, align 4
  %4 = alloca i32, align 4
  %5 = alloca i8**, align 8
  %6 = alloca i32, align 4
  %7 = alloca i64, align 8
  %8 = alloca i32, align 4
  %9 = alloca i8*, align 8
  %10 = alloca i32, align 4
  %11 = alloca i32, align 4
  %12 = alloca i32, align 4
  %13 = alloca i32, align 4
  %14 = alloca %struct.utsname, align 1
  %15 = alloca i8*, align 8
  %16 = alloca %struct._IO_FILE*, align 8
  %17 = alloca i8*, align 8
  %18 = alloca i64, align 8
  %19 = alloca i8*, align 8
  %20 = alloca i8*, align 8
  store i32 0, i32* %3, align 4
  store i32 %0, i32* %4, align 4
  store i8** %1, i8*** %5, align 8
  %21 = call i32 @omp_get_max_threads()
  store i32 %21, i32* %6, align 4
  %22 = load i32, i32* %6, align 4
  call void @omp_set_num_threads(i32 %22)
  store i64 10000, i64* %7, align 8
  store i32 10, i32* %8, align 4
  store i32 0, i32* %10, align 4
  store i32 0, i32* %11, align 4
  store i32 0, i32* %12, align 4
  %23 = call i32 @setpriority(i32 0, i32 0, i32 -20) #6
  store i32 %23, i32* %13, align 4
  %24 = load i32, i32* %13, align 4
  %25 = icmp eq i32 %24, -1
  br i1 %25, label %26, label %28

; <label>:26:                                     ; preds = %2
  %27 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([73 x i8], [73 x i8]* @.str, i32 0, i32 0), i8* getelementptr inbounds ([6 x i8], [6 x i8]* @.str.1, i32 0, i32 0), i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.str.2, i32 0, i32 0))
  br label %28

; <label>:28:                                     ; preds = %26, %2
  %29 = load i32, i32* %4, align 4
  %30 = icmp eq i32 %29, 4
  br i1 %30, label %31, label %83

; <label>:31:                                     ; preds = %28
  %32 = load i8**, i8*** %5, align 8
  %33 = getelementptr inbounds i8*, i8** %32, i64 3
  %34 = load i8*, i8** %33, align 8
  %35 = call i32 @strcmp(i8* %34, i8* getelementptr inbounds ([14 x i8], [14 x i8]* @.str.3, i32 0, i32 0)) #7
  %36 = icmp eq i32 %35, 0
  br i1 %36, label %49, label %37

; <label>:37:                                     ; preds = %31
  %38 = load i8**, i8*** %5, align 8
  %39 = getelementptr inbounds i8*, i8** %38, i64 3
  %40 = load i8*, i8** %39, align 8
  %41 = call i32 @strcmp(i8* %40, i8* getelementptr inbounds ([11 x i8], [11 x i8]* @.str.4, i32 0, i32 0)) #7
  %42 = icmp eq i32 %41, 0
  br i1 %42, label %49, label %43

; <label>:43:                                     ; preds = %37
  %44 = load i8**, i8*** %5, align 8
  %45 = getelementptr inbounds i8*, i8** %44, i64 3
  %46 = load i8*, i8** %45, align 8
  %47 = call i32 @strcmp(i8* %46, i8* getelementptr inbounds ([13 x i8], [13 x i8]* @.str.5, i32 0, i32 0)) #7
  %48 = icmp eq i32 %47, 0
  br i1 %48, label %49, label %83

; <label>:49:                                     ; preds = %43, %37, %31
  %50 = load i8**, i8*** %5, align 8
  %51 = getelementptr inbounds i8*, i8** %50, i64 1
  %52 = load i8*, i8** %51, align 8
  %53 = load i32, i32* %8, align 4
  %54 = call i64 @strtol(i8* %52, i8** %9, i32 %53) #6
  store i64 %54, i64* %7, align 8
  %55 = load i8**, i8*** %5, align 8
  %56 = getelementptr inbounds i8*, i8** %55, i64 2
  %57 = load i8*, i8** %56, align 8
  %58 = call i32 @strcmp(i8* %57, i8* getelementptr inbounds ([17 x i8], [17 x i8]* @.str.6, i32 0, i32 0)) #7
  %59 = icmp eq i32 %58, 0
  %60 = zext i1 %59 to i64
  %61 = select i1 %59, i32 1, i32 0
  store i32 %61, i32* %12, align 4
  %62 = load i8**, i8*** %5, align 8
  %63 = getelementptr inbounds i8*, i8** %62, i64 2
  %64 = load i8*, i8** %63, align 8
  %65 = call i32 @strcmp(i8* %64, i8* getelementptr inbounds ([16 x i8], [16 x i8]* @.str.7, i32 0, i32 0)) #7
  %66 = icmp eq i32 %65, 0
  %67 = zext i1 %66 to i64
  %68 = select i1 %66, i32 0, i32 1
  store i32 %68, i32* %12, align 4
  %69 = load i8**, i8*** %5, align 8
  %70 = getelementptr inbounds i8*, i8** %69, i64 3
  %71 = load i8*, i8** %70, align 8
  %72 = call i32 @strcmp(i8* %71, i8* getelementptr inbounds ([14 x i8], [14 x i8]* @.str.3, i32 0, i32 0)) #7
  %73 = icmp eq i32 %72, 0
  %74 = zext i1 %73 to i64
  %75 = select i1 %73, i32 1, i32 0
  store i32 %75, i32* %10, align 4
  %76 = load i8**, i8*** %5, align 8
  %77 = getelementptr inbounds i8*, i8** %76, i64 3
  %78 = load i8*, i8** %77, align 8
  %79 = call i32 @strcmp(i8* %78, i8* getelementptr inbounds ([13 x i8], [13 x i8]* @.str.5, i32 0, i32 0)) #7
  %80 = icmp eq i32 %79, 0
  %81 = zext i1 %80 to i64
  %82 = select i1 %80, i32 1, i32 0
  store i32 %82, i32* %11, align 4
  br label %86

; <label>:83:                                     ; preds = %43, %28
  %84 = load %struct._IO_FILE*, %struct._IO_FILE** @stderr, align 8
  %85 = call i32 (%struct._IO_FILE*, i8*, ...) @fprintf(%struct._IO_FILE* %84, i8* getelementptr inbounds ([695 x i8], [695 x i8]* @.str.8, i32 0, i32 0), i8* getelementptr inbounds ([6 x i8], [6 x i8]* @.str.9, i32 0, i32 0), i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.str.2, i32 0, i32 0))
  call void @exit(i32 1) #8
  unreachable

; <label>:86:                                     ; preds = %49
  %87 = call i32 @uname(%struct.utsname* %14) #6
  %88 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([67 x i8], [67 x i8]* @.str.10, i32 0, i32 0), i8* getelementptr inbounds ([6 x i8], [6 x i8]* @.str.11, i32 0, i32 0))
  %89 = getelementptr inbounds %struct.utsname, %struct.utsname* %14, i32 0, i32 4
  %90 = getelementptr inbounds [65 x i8], [65 x i8]* %89, i32 0, i32 0
  %91 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([45 x i8], [45 x i8]* @.str.12, i32 0, i32 0), i8* %90, i8* getelementptr inbounds ([12 x i8], [12 x i8]* @.str.13, i32 0, i32 0), i8* getelementptr inbounds ([9 x i8], [9 x i8]* @.str.14, i32 0, i32 0))
  %92 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([68 x i8], [68 x i8]* @.str.15, i32 0, i32 0), i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.str.2, i32 0, i32 0))
  %93 = load i64, i64* %7, align 8
  %94 = icmp ult i64 %93, 1
  br i1 %94, label %95, label %98

; <label>:95:                                     ; preds = %86
  %96 = load %struct._IO_FILE*, %struct._IO_FILE** @stderr, align 8
  %97 = call i32 (%struct._IO_FILE*, i8*, ...) @fprintf(%struct._IO_FILE* %96, i8* getelementptr inbounds ([41 x i8], [41 x i8]* @.str.16, i32 0, i32 0), i8* getelementptr inbounds ([6 x i8], [6 x i8]* @.str.9, i32 0, i32 0), i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.str.2, i32 0, i32 0))
  call void @exit(i32 1) #8
  unreachable

; <label>:98:                                     ; preds = %86
  %99 = load i32, i32* %12, align 4
  %100 = icmp eq i32 %99, 1
  br i1 %100, label %101, label %137

; <label>:101:                                    ; preds = %98
  %102 = load i64, i64* %7, align 8
  %103 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([76 x i8], [76 x i8]* @.str.17, i32 0, i32 0), i64 %102)
  %104 = load i64, i64* %7, align 8
  %105 = call i8* @clc_pi(i64 %104)
  store i8* %105, i8** %15, align 8
  %106 = load i32, i32* %10, align 4
  %107 = icmp eq i32 %106, 1
  br i1 %107, label %108, label %113

; <label>:108:                                    ; preds = %101
  %109 = load i8*, i8** %15, align 8
  %110 = load i8*, i8** %15, align 8
  %111 = getelementptr inbounds i8, i8* %110, i64 1
  %112 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([31 x i8], [31 x i8]* @.str.18, i32 0, i32 0), i8* %109, i8* %111)
  br label %113

; <label>:113:                                    ; preds = %108, %101
  %114 = load i32, i32* %11, align 4
  %115 = icmp eq i32 %114, 1
  br i1 %115, label %116, label %131

; <label>:116:                                    ; preds = %113
  %117 = call %struct._IO_FILE* @fopen(i8* getelementptr inbounds ([13 x i8], [13 x i8]* @.str.19, i32 0, i32 0), i8* getelementptr inbounds ([2 x i8], [2 x i8]* @.str.20, i32 0, i32 0))
  store %struct._IO_FILE* %117, %struct._IO_FILE** %16, align 8
  %118 = icmp eq %struct._IO_FILE* %117, null
  br i1 %118, label %119, label %122

; <label>:119:                                    ; preds = %116
  %120 = load %struct._IO_FILE*, %struct._IO_FILE** @stderr, align 8
  %121 = call i32 (%struct._IO_FILE*, i8*, ...) @fprintf(%struct._IO_FILE* %120, i8* getelementptr inbounds ([30 x i8], [30 x i8]* @.str.21, i32 0, i32 0), i8* getelementptr inbounds ([6 x i8], [6 x i8]* @.str.9, i32 0, i32 0), i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.str.2, i32 0, i32 0))
  call void @exit(i32 -1) #8
  unreachable

; <label>:122:                                    ; preds = %116
  %123 = load %struct._IO_FILE*, %struct._IO_FILE** %16, align 8
  %124 = load i8*, i8** %15, align 8
  %125 = load i8*, i8** %15, align 8
  %126 = getelementptr inbounds i8, i8* %125, i64 1
  %127 = call i32 (%struct._IO_FILE*, i8*, ...) @fprintf(%struct._IO_FILE* %123, i8* getelementptr inbounds ([9 x i8], [9 x i8]* @.str.22, i32 0, i32 0), i8* %124, i8* %126)
  %128 = load %struct._IO_FILE*, %struct._IO_FILE** %16, align 8
  %129 = call i32 @fclose(%struct._IO_FILE* %128)
  br label %130

; <label>:130:                                    ; preds = %122
  br label %131

; <label>:131:                                    ; preds = %130, %113
  %132 = load i8*, i8** %15, align 8
  %133 = call i8* @clc_md5(i8* %132)
  store i8* %133, i8** %17, align 8
  %134 = load i8*, i8** %17, align 8
  %135 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([37 x i8], [37 x i8]* @.str.23, i32 0, i32 0), i8* %134)
  %136 = load i8*, i8** %15, align 8
  call void @free(i8* %136) #6
  br label %157

; <label>:137:                                    ; preds = %98
  %138 = load i32, i32* %12, align 4
  %139 = icmp eq i32 %138, 0
  br i1 %139, label %140, label %156

; <label>:140:                                    ; preds = %137
  %141 = load i64, i64* %7, align 8
  %142 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([79 x i8], [79 x i8]* @.str.24, i32 0, i32 0), i64 %141)
  %143 = load i64, i64* %7, align 8
  %144 = call i32 @clc_prime(i64 %143)
  %145 = sext i32 %144 to i64
  store i64 %145, i64* %18, align 8
  %146 = load i64, i64* %18, align 8
  %147 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([28 x i8], [28 x i8]* @.str.25, i32 0, i32 0), i64 %146)
  %148 = call noalias i8* @malloc(i64 9) #6
  store i8* %148, i8** %19, align 8
  %149 = load i8*, i8** %19, align 8
  %150 = load i64, i64* %18, align 8
  %151 = call i32 (i8*, i8*, ...) @sprintf(i8* %149, i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str.26, i32 0, i32 0), i64 %150) #6
  %152 = load i8*, i8** %19, align 8
  %153 = call i8* @clc_md5(i8* %152)
  store i8* %153, i8** %20, align 8
  %154 = load i8*, i8** %20, align 8
  %155 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([37 x i8], [37 x i8]* @.str.23, i32 0, i32 0), i8* %154)
  br label %156

; <label>:156:                                    ; preds = %140, %137
  br label %157

; <label>:157:                                    ; preds = %156, %131
  %158 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([10 x i8], [10 x i8]* @.str.27, i32 0, i32 0))
  ret i32 0
}

declare i32 @omp_get_max_threads() #1

declare void @omp_set_num_threads(i32) #1

; Function Attrs: nounwind
declare i32 @setpriority(i32, i32, i32) #2

declare i32 @printf(i8*, ...) #1

; Function Attrs: nounwind readonly
declare i32 @strcmp(i8*, i8*) #3

; Function Attrs: nounwind
declare i64 @strtol(i8*, i8**, i32) #2

declare i32 @fprintf(%struct._IO_FILE*, i8*, ...) #1

; Function Attrs: noreturn nounwind
declare void @exit(i32) #4

; Function Attrs: nounwind
declare i32 @uname(%struct.utsname*) #2

; Function Attrs: noinline nounwind optnone uwtable
define internal i8* @clc_pi(i64) #0 {
  %2 = alloca i64, align 8
  %3 = alloca i64, align 8
  %4 = alloca double, align 8
  store i64 %0, i64* %2, align 8
  %5 = load i64, i64* %2, align 8
  %6 = udiv i64 %5, 15
  %7 = add i64 %6, 1
  store i64 %7, i64* %3, align 8
  store i64 545140134, i64* @constant1, align 8
  store i64 13591409, i64* @constant2, align 8
  store i64 640320, i64* @constant3, align 8
  %8 = call i32 @clc_log2(i32 10)
  %9 = uitofp i32 %8 to double
  store double %9, double* @bits, align 8
  %10 = load i64, i64* %2, align 8
  %11 = uitofp i64 %10 to double
  %12 = load double, double* @bits, align 8
  %13 = fmul double %11, %12
  %14 = fadd double %13, 1.000000e+00
  %15 = fptoui double %14 to i64
  store i64 %15, i64* @precision, align 8
  %16 = load i64, i64* @precision, align 8
  call void @__gmpf_set_default_prec(i64 %16)
  call void (%struct.__mpz_struct*, ...) @__gmpz_inits(%struct.__mpz_struct* getelementptr inbounds ([1 x %struct.__mpz_struct], [1 x %struct.__mpz_struct]* @v1, i32 0, i32 0), %struct.__mpz_struct* getelementptr inbounds ([1 x %struct.__mpz_struct], [1 x %struct.__mpz_struct]* @v2, i32 0, i32 0), %struct.__mpz_struct* getelementptr inbounds ([1 x %struct.__mpz_struct], [1 x %struct.__mpz_struct]* @v3, i32 0, i32 0), %struct.__mpz_struct* getelementptr inbounds ([1 x %struct.__mpz_struct], [1 x %struct.__mpz_struct]* @v4, i32 0, i32 0), %struct.__mpz_struct* getelementptr inbounds ([1 x %struct.__mpz_struct], [1 x %struct.__mpz_struct]* @v5, i32 0, i32 0), i8* null)
  call void (%struct.__mpf_struct*, ...) @__gmpf_inits(%struct.__mpf_struct* getelementptr inbounds ([1 x %struct.__mpf_struct], [1 x %struct.__mpf_struct]* @res, i32 0, i32 0), %struct.__mpf_struct* getelementptr inbounds ([1 x %struct.__mpf_struct], [1 x %struct.__mpf_struct]* @tmp, i32 0, i32 0), %struct.__mpf_struct* getelementptr inbounds ([1 x %struct.__mpf_struct], [1 x %struct.__mpf_struct]* @V1, i32 0, i32 0), %struct.__mpf_struct* getelementptr inbounds ([1 x %struct.__mpf_struct], [1 x %struct.__mpf_struct]* @V2, i32 0, i32 0), %struct.__mpf_struct* getelementptr inbounds ([1 x %struct.__mpf_struct], [1 x %struct.__mpf_struct]* @V3, i32 0, i32 0), %struct.__mpf_struct* getelementptr inbounds ([1 x %struct.__mpf_struct], [1 x %struct.__mpf_struct]* @total, i32 0, i32 0), i8* null)
  call void @__gmpf_set_ui(%struct.__mpf_struct* getelementptr inbounds ([1 x %struct.__mpf_struct], [1 x %struct.__mpf_struct]* @total, i32 0, i32 0), i64 0)
  call void @__gmpf_sqrt_ui(%struct.__mpf_struct* getelementptr inbounds ([1 x %struct.__mpf_struct], [1 x %struct.__mpf_struct]* @tmp, i32 0, i32 0), i64 10005)
  call void @__gmpf_mul_ui(%struct.__mpf_struct* getelementptr inbounds ([1 x %struct.__mpf_struct], [1 x %struct.__mpf_struct]* @tmp, i32 0, i32 0), %struct.__mpf_struct* getelementptr inbounds ([1 x %struct.__mpf_struct], [1 x %struct.__mpf_struct]* @tmp, i32 0, i32 0), i64 426880)
  %17 = call i32 @clock_gettime(i32 4, %struct.timespec* @start) #6
  %18 = load i64, i64* %3, align 8
  %19 = sub i64 %18, 1
  %20 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([24 x i8], [24 x i8]* @.str.28, i32 0, i32 0), i64 %19)
  store i64 0, i64* @i, align 8
  br label %21

; <label>:21:                                     ; preds = %42, %1
  %22 = load i64, i64* @i, align 8
  %23 = load i64, i64* %3, align 8
  %24 = icmp ult i64 %22, %23
  br i1 %24, label %25, label %45

; <label>:25:                                     ; preds = %21
  %26 = load i64, i64* @i, align 8
  %27 = mul i64 %26, 3
  store i64 %27, i64* @ti, align 8
  %28 = load i64, i64* @i, align 8
  %29 = mul i64 6, %28
  call void @__gmpz_fac_ui(%struct.__mpz_struct* getelementptr inbounds ([1 x %struct.__mpz_struct], [1 x %struct.__mpz_struct]* @v1, i32 0, i32 0), i64 %29)
  %30 = load i64, i64* @constant1, align 8
  call void @__gmpz_set_ui(%struct.__mpz_struct* getelementptr inbounds ([1 x %struct.__mpz_struct], [1 x %struct.__mpz_struct]* @v2, i32 0, i32 0), i64 %30)
  %31 = load i64, i64* @i, align 8
  call void @__gmpz_mul_ui(%struct.__mpz_struct* getelementptr inbounds ([1 x %struct.__mpz_struct], [1 x %struct.__mpz_struct]* @v2, i32 0, i32 0), %struct.__mpz_struct* getelementptr inbounds ([1 x %struct.__mpz_struct], [1 x %struct.__mpz_struct]* @v2, i32 0, i32 0), i64 %31)
  %32 = load i64, i64* @constant2, align 8
  call void @__gmpz_add_ui(%struct.__mpz_struct* getelementptr inbounds ([1 x %struct.__mpz_struct], [1 x %struct.__mpz_struct]* @v2, i32 0, i32 0), %struct.__mpz_struct* getelementptr inbounds ([1 x %struct.__mpz_struct], [1 x %struct.__mpz_struct]* @v2, i32 0, i32 0), i64 %32)
  %33 = load i64, i64* @ti, align 8
  call void @__gmpz_fac_ui(%struct.__mpz_struct* getelementptr inbounds ([1 x %struct.__mpz_struct], [1 x %struct.__mpz_struct]* @v3, i32 0, i32 0), i64 %33)
  %34 = load i64, i64* @i, align 8
  call void @__gmpz_fac_ui(%struct.__mpz_struct* getelementptr inbounds ([1 x %struct.__mpz_struct], [1 x %struct.__mpz_struct]* @v4, i32 0, i32 0), i64 %34)
  call void @__gmpz_pow_ui(%struct.__mpz_struct* getelementptr inbounds ([1 x %struct.__mpz_struct], [1 x %struct.__mpz_struct]* @v4, i32 0, i32 0), %struct.__mpz_struct* getelementptr inbounds ([1 x %struct.__mpz_struct], [1 x %struct.__mpz_struct]* @v4, i32 0, i32 0), i64 3)
  %35 = load i64, i64* @constant3, align 8
  %36 = load i64, i64* @ti, align 8
  call void @__gmpz_ui_pow_ui(%struct.__mpz_struct* getelementptr inbounds ([1 x %struct.__mpz_struct], [1 x %struct.__mpz_struct]* @v5, i32 0, i32 0), i64 %35, i64 %36)
  %37 = load i64, i64* @ti, align 8
  %38 = and i64 1, %37
  %39 = icmp eq i64 %38, 1
  br i1 %39, label %40, label %41

; <label>:40:                                     ; preds = %25
  call void @__gmpz_neg(%struct.__mpz_struct* getelementptr inbounds ([1 x %struct.__mpz_struct], [1 x %struct.__mpz_struct]* @v5, i32 0, i32 0), %struct.__mpz_struct* getelementptr inbounds ([1 x %struct.__mpz_struct], [1 x %struct.__mpz_struct]* @v5, i32 0, i32 0))
  br label %41

; <label>:41:                                     ; preds = %40, %25
  call void @__gmpz_mul(%struct.__mpz_struct* getelementptr inbounds ([1 x %struct.__mpz_struct], [1 x %struct.__mpz_struct]* @v1, i32 0, i32 0), %struct.__mpz_struct* getelementptr inbounds ([1 x %struct.__mpz_struct], [1 x %struct.__mpz_struct]* @v1, i32 0, i32 0), %struct.__mpz_struct* getelementptr inbounds ([1 x %struct.__mpz_struct], [1 x %struct.__mpz_struct]* @v2, i32 0, i32 0))
  call void @__gmpf_set_z(%struct.__mpf_struct* getelementptr inbounds ([1 x %struct.__mpf_struct], [1 x %struct.__mpf_struct]* @V1, i32 0, i32 0), %struct.__mpz_struct* getelementptr inbounds ([1 x %struct.__mpz_struct], [1 x %struct.__mpz_struct]* @v1, i32 0, i32 0))
  call void @__gmpz_mul(%struct.__mpz_struct* getelementptr inbounds ([1 x %struct.__mpz_struct], [1 x %struct.__mpz_struct]* @v3, i32 0, i32 0), %struct.__mpz_struct* getelementptr inbounds ([1 x %struct.__mpz_struct], [1 x %struct.__mpz_struct]* @v3, i32 0, i32 0), %struct.__mpz_struct* getelementptr inbounds ([1 x %struct.__mpz_struct], [1 x %struct.__mpz_struct]* @v4, i32 0, i32 0))
  call void @__gmpz_mul(%struct.__mpz_struct* getelementptr inbounds ([1 x %struct.__mpz_struct], [1 x %struct.__mpz_struct]* @v3, i32 0, i32 0), %struct.__mpz_struct* getelementptr inbounds ([1 x %struct.__mpz_struct], [1 x %struct.__mpz_struct]* @v3, i32 0, i32 0), %struct.__mpz_struct* getelementptr inbounds ([1 x %struct.__mpz_struct], [1 x %struct.__mpz_struct]* @v5, i32 0, i32 0))
  call void @__gmpf_set_z(%struct.__mpf_struct* getelementptr inbounds ([1 x %struct.__mpf_struct], [1 x %struct.__mpf_struct]* @V2, i32 0, i32 0), %struct.__mpz_struct* getelementptr inbounds ([1 x %struct.__mpz_struct], [1 x %struct.__mpz_struct]* @v3, i32 0, i32 0))
  call void @__gmpf_div(%struct.__mpf_struct* getelementptr inbounds ([1 x %struct.__mpf_struct], [1 x %struct.__mpf_struct]* @V3, i32 0, i32 0), %struct.__mpf_struct* getelementptr inbounds ([1 x %struct.__mpf_struct], [1 x %struct.__mpf_struct]* @V1, i32 0, i32 0), %struct.__mpf_struct* getelementptr inbounds ([1 x %struct.__mpf_struct], [1 x %struct.__mpf_struct]* @V2, i32 0, i32 0))
  call void @__gmpf_add(%struct.__mpf_struct* getelementptr inbounds ([1 x %struct.__mpf_struct], [1 x %struct.__mpf_struct]* @total, i32 0, i32 0), %struct.__mpf_struct* getelementptr inbounds ([1 x %struct.__mpf_struct], [1 x %struct.__mpf_struct]* @total, i32 0, i32 0), %struct.__mpf_struct* getelementptr inbounds ([1 x %struct.__mpf_struct], [1 x %struct.__mpf_struct]* @V3, i32 0, i32 0))
  br label %42

; <label>:42:                                     ; preds = %41
  %43 = load i64, i64* @i, align 8
  %44 = add i64 %43, 1
  store i64 %44, i64* @i, align 8
  br label %21

; <label>:45:                                     ; preds = %21
  call void @__gmpf_ui_div(%struct.__mpf_struct* getelementptr inbounds ([1 x %struct.__mpf_struct], [1 x %struct.__mpf_struct]* @total, i32 0, i32 0), i64 1, %struct.__mpf_struct* getelementptr inbounds ([1 x %struct.__mpf_struct], [1 x %struct.__mpf_struct]* @total, i32 0, i32 0))
  call void @__gmpf_mul(%struct.__mpf_struct* getelementptr inbounds ([1 x %struct.__mpf_struct], [1 x %struct.__mpf_struct]* @total, i32 0, i32 0), %struct.__mpf_struct* getelementptr inbounds ([1 x %struct.__mpf_struct], [1 x %struct.__mpf_struct]* @total, i32 0, i32 0), %struct.__mpf_struct* getelementptr inbounds ([1 x %struct.__mpf_struct], [1 x %struct.__mpf_struct]* @tmp, i32 0, i32 0))
  %46 = call i32 @clock_gettime(i32 4, %struct.timespec* @end) #6
  %47 = load i64, i64* getelementptr inbounds (%struct.timespec, %struct.timespec* @end, i32 0, i32 0), align 8
  %48 = load i64, i64* getelementptr inbounds (%struct.timespec, %struct.timespec* @start, i32 0, i32 0), align 8
  %49 = sub nsw i64 %47, %48
  %50 = sitofp i64 %49 to double
  %51 = load i64, i64* getelementptr inbounds (%struct.timespec, %struct.timespec* @end, i32 0, i32 1), align 8
  %52 = load i64, i64* getelementptr inbounds (%struct.timespec, %struct.timespec* @start, i32 0, i32 1), align 8
  %53 = sub nsw i64 %51, %52
  %54 = sitofp i64 %53 to double
  %55 = fdiv double %54, 1.000000e+09
  %56 = fadd double %50, %55
  store double %56, double* %4, align 8
  %57 = load double, double* %4, align 8
  %58 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([34 x i8], [34 x i8]* @.str.29, i32 0, i32 0), double %57)
  %59 = load i64, i64* %2, align 8
  %60 = call i8* @__gmpf_get_str(i8* null, i64* @exponent, i32 10, i64 %59, %struct.__mpf_struct* getelementptr inbounds ([1 x %struct.__mpf_struct], [1 x %struct.__mpf_struct]* @total, i32 0, i32 0))
  store i8* %60, i8** @oput, align 8
  call void (%struct.__mpz_struct*, ...) @__gmpz_clears(%struct.__mpz_struct* getelementptr inbounds ([1 x %struct.__mpz_struct], [1 x %struct.__mpz_struct]* @v1, i32 0, i32 0), %struct.__mpz_struct* getelementptr inbounds ([1 x %struct.__mpz_struct], [1 x %struct.__mpz_struct]* @v2, i32 0, i32 0), %struct.__mpz_struct* getelementptr inbounds ([1 x %struct.__mpz_struct], [1 x %struct.__mpz_struct]* @v3, i32 0, i32 0), %struct.__mpz_struct* getelementptr inbounds ([1 x %struct.__mpz_struct], [1 x %struct.__mpz_struct]* @v4, i32 0, i32 0), %struct.__mpz_struct* getelementptr inbounds ([1 x %struct.__mpz_struct], [1 x %struct.__mpz_struct]* @v5, i32 0, i32 0), i8* null)
  call void (%struct.__mpf_struct*, ...) @__gmpf_clears(%struct.__mpf_struct* getelementptr inbounds ([1 x %struct.__mpf_struct], [1 x %struct.__mpf_struct]* @res, i32 0, i32 0), %struct.__mpf_struct* getelementptr inbounds ([1 x %struct.__mpf_struct], [1 x %struct.__mpf_struct]* @tmp, i32 0, i32 0), %struct.__mpf_struct* getelementptr inbounds ([1 x %struct.__mpf_struct], [1 x %struct.__mpf_struct]* @V1, i32 0, i32 0), %struct.__mpf_struct* getelementptr inbounds ([1 x %struct.__mpf_struct], [1 x %struct.__mpf_struct]* @V2, i32 0, i32 0), %struct.__mpf_struct* getelementptr inbounds ([1 x %struct.__mpf_struct], [1 x %struct.__mpf_struct]* @V3, i32 0, i32 0), %struct.__mpf_struct* getelementptr inbounds ([1 x %struct.__mpf_struct], [1 x %struct.__mpf_struct]* @total, i32 0, i32 0), i8* null)
  %61 = load i8*, i8** @oput, align 8
  ret i8* %61
}

declare %struct._IO_FILE* @fopen(i8*, i8*) #1

declare i32 @fclose(%struct._IO_FILE*) #1

; Function Attrs: noinline nounwind optnone uwtable
define internal i8* @clc_md5(i8*) #0 {
  %2 = alloca i8*, align 8
  %3 = alloca i8*, align 8
  store i8* %0, i8** %2, align 8
  %4 = call noalias i8* @malloc(i64 33) #6
  store i8* %4, i8** %3, align 8
  %5 = call i32 @MD5_Init(%struct.MD5state_st* @context)
  %6 = load i8*, i8** %2, align 8
  %7 = load i8*, i8** %2, align 8
  %8 = call i64 @strlen(i8* %7) #7
  %9 = call i32 @MD5_Update(%struct.MD5state_st* @context, i8* %6, i64 %8)
  %10 = call i32 @MD5_Final(i8* getelementptr inbounds ([16 x i8], [16 x i8]* @digest, i32 0, i32 0), %struct.MD5state_st* @context)
  store i32 0, i32* @u, align 4
  br label %11

; <label>:11:                                     ; preds = %26, %1
  %12 = load i32, i32* @u, align 4
  %13 = icmp slt i32 %12, 16
  br i1 %13, label %14, label %29

; <label>:14:                                     ; preds = %11
  %15 = load i8*, i8** %3, align 8
  %16 = load i32, i32* @u, align 4
  %17 = mul nsw i32 %16, 2
  %18 = sext i32 %17 to i64
  %19 = getelementptr inbounds i8, i8* %15, i64 %18
  %20 = load i32, i32* @u, align 4
  %21 = sext i32 %20 to i64
  %22 = getelementptr inbounds [16 x i8], [16 x i8]* @digest, i64 0, i64 %21
  %23 = load i8, i8* %22, align 1
  %24 = zext i8 %23 to i32
  %25 = call i32 (i8*, i64, i8*, ...) @snprintf(i8* %19, i64 3, i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.str.30, i32 0, i32 0), i32 %24) #6
  br label %26

; <label>:26:                                     ; preds = %14
  %27 = load i32, i32* @u, align 4
  %28 = add nsw i32 %27, 1
  store i32 %28, i32* @u, align 4
  br label %11

; <label>:29:                                     ; preds = %11
  %30 = load i8*, i8** %3, align 8
  ret i8* %30
}

; Function Attrs: nounwind
declare void @free(i8*) #2

; Function Attrs: noinline nounwind optnone uwtable
define internal i32 @clc_prime(i64) #0 {
  %2 = alloca i64, align 8
  %3 = alloca double, align 8
  store i64 %0, i64* %2, align 8
  %4 = call i32 @clock_gettime(i32 4, %struct.timespec* @pstart) #6
  store i64 2, i64* @x, align 8
  br label %5

; <label>:5:                                      ; preds = %28, %1
  %6 = load i64, i64* @x, align 8
  %7 = load i64, i64* %2, align 8
  %8 = icmp ule i64 %6, %7
  br i1 %8, label %9, label %31

; <label>:9:                                      ; preds = %5
  store i32 1, i32* @pnum, align 4
  store i64 2, i64* @y, align 8
  br label %10

; <label>:10:                                     ; preds = %21, %9
  %11 = load i64, i64* @y, align 8
  %12 = load i64, i64* @x, align 8
  %13 = icmp ult i64 %11, %12
  br i1 %13, label %14, label %24

; <label>:14:                                     ; preds = %10
  %15 = load i64, i64* @x, align 8
  %16 = load i64, i64* @y, align 8
  %17 = urem i64 %15, %16
  %18 = icmp eq i64 %17, 0
  br i1 %18, label %19, label %20

; <label>:19:                                     ; preds = %14
  store i32 0, i32* @pnum, align 4
  br label %24

; <label>:20:                                     ; preds = %14
  br label %21

; <label>:21:                                     ; preds = %20
  %22 = load i64, i64* @y, align 8
  %23 = add i64 %22, 1
  store i64 %23, i64* @y, align 8
  br label %10

; <label>:24:                                     ; preds = %19, %10
  %25 = load i32, i32* @tpnums, align 4
  %26 = load i32, i32* @pnum, align 4
  %27 = add nsw i32 %25, %26
  store i32 %27, i32* @tpnums, align 4
  br label %28

; <label>:28:                                     ; preds = %24
  %29 = load i64, i64* @x, align 8
  %30 = add i64 %29, 1
  store i64 %30, i64* @x, align 8
  br label %5

; <label>:31:                                     ; preds = %5
  %32 = call i32 @clock_gettime(i32 4, %struct.timespec* @pend) #6
  %33 = load i64, i64* getelementptr inbounds (%struct.timespec, %struct.timespec* @pend, i32 0, i32 0), align 8
  %34 = load i64, i64* getelementptr inbounds (%struct.timespec, %struct.timespec* @pstart, i32 0, i32 0), align 8
  %35 = sub nsw i64 %33, %34
  %36 = sitofp i64 %35 to double
  %37 = load i64, i64* getelementptr inbounds (%struct.timespec, %struct.timespec* @pend, i32 0, i32 1), align 8
  %38 = load i64, i64* getelementptr inbounds (%struct.timespec, %struct.timespec* @pstart, i32 0, i32 1), align 8
  %39 = sub nsw i64 %37, %38
  %40 = sitofp i64 %39 to double
  %41 = fdiv double %40, 1.000000e+09
  %42 = fadd double %36, %41
  store double %42, double* %3, align 8
  %43 = load double, double* %3, align 8
  %44 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([34 x i8], [34 x i8]* @.str.29, i32 0, i32 0), double %43)
  %45 = load i32, i32* @tpnums, align 4
  ret i32 %45
}

; Function Attrs: nounwind
declare noalias i8* @malloc(i64) #2

; Function Attrs: nounwind
declare i32 @sprintf(i8*, i8*, ...) #2

; Function Attrs: noinline nounwind optnone uwtable
define internal i32 @clc_log2(i32) #0 {
  %2 = alloca i32, align 4
  store i32 %0, i32* %2, align 4
  %3 = load i32, i32* %2, align 4
  %4 = icmp ule i32 %3, 1
  br i1 %4, label %5, label %6

; <label>:5:                                      ; preds = %1
  br label %11

; <label>:6:                                      ; preds = %1
  %7 = load i32, i32* %2, align 4
  %8 = sub i32 %7, 1
  %9 = call i32 @llvm.ctlz.i32(i32 %8, i1 true)
  %10 = sub nsw i32 32, %9
  br label %11

; <label>:11:                                     ; preds = %6, %5
  %12 = phi i32 [ 0, %5 ], [ %10, %6 ]
  ret i32 %12
}

declare void @__gmpf_set_default_prec(i64) #1

declare void @__gmpz_inits(%struct.__mpz_struct*, ...) #1

declare void @__gmpf_inits(%struct.__mpf_struct*, ...) #1

declare void @__gmpf_set_ui(%struct.__mpf_struct*, i64) #1

declare void @__gmpf_sqrt_ui(%struct.__mpf_struct*, i64) #1

declare void @__gmpf_mul_ui(%struct.__mpf_struct*, %struct.__mpf_struct*, i64) #1

; Function Attrs: nounwind
declare i32 @clock_gettime(i32, %struct.timespec*) #2

declare void @__gmpz_fac_ui(%struct.__mpz_struct*, i64) #1

declare void @__gmpz_set_ui(%struct.__mpz_struct*, i64) #1

declare void @__gmpz_mul_ui(%struct.__mpz_struct*, %struct.__mpz_struct*, i64) #1

declare void @__gmpz_add_ui(%struct.__mpz_struct*, %struct.__mpz_struct*, i64) #1

declare void @__gmpz_pow_ui(%struct.__mpz_struct*, %struct.__mpz_struct*, i64) #1

declare void @__gmpz_ui_pow_ui(%struct.__mpz_struct*, i64, i64) #1

declare void @__gmpz_neg(%struct.__mpz_struct*, %struct.__mpz_struct*) #1

declare void @__gmpz_mul(%struct.__mpz_struct*, %struct.__mpz_struct*, %struct.__mpz_struct*) #1

declare void @__gmpf_set_z(%struct.__mpf_struct*, %struct.__mpz_struct*) #1

declare void @__gmpf_div(%struct.__mpf_struct*, %struct.__mpf_struct*, %struct.__mpf_struct*) #1

declare void @__gmpf_add(%struct.__mpf_struct*, %struct.__mpf_struct*, %struct.__mpf_struct*) #1

declare void @__gmpf_ui_div(%struct.__mpf_struct*, i64, %struct.__mpf_struct*) #1

declare void @__gmpf_mul(%struct.__mpf_struct*, %struct.__mpf_struct*, %struct.__mpf_struct*) #1

declare i8* @__gmpf_get_str(i8*, i64*, i32, i64, %struct.__mpf_struct*) #1

declare void @__gmpz_clears(%struct.__mpz_struct*, ...) #1

declare void @__gmpf_clears(%struct.__mpf_struct*, ...) #1

; Function Attrs: nounwind readnone speculatable
declare i32 @llvm.ctlz.i32(i32, i1) #5

declare i32 @MD5_Init(%struct.MD5state_st*) #1

declare i32 @MD5_Update(%struct.MD5state_st*, i8*, i64) #1

; Function Attrs: nounwind readonly
declare i64 @strlen(i8*) #3

declare i32 @MD5_Final(i8*, %struct.MD5state_st*) #1

; Function Attrs: nounwind
declare i32 @snprintf(i8*, i64, i8*, ...) #2

attributes #0 = { noinline nounwind optnone uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #2 = { nounwind "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #3 = { nounwind readonly "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #4 = { noreturn nounwind "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #5 = { nounwind readnone speculatable }
attributes #6 = { nounwind }
attributes #7 = { nounwind readonly }
attributes #8 = { noreturn nounwind }

!llvm.module.flags = !{!0}
!llvm.ident = !{!1}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{!"clang version 6.0.0-1ubuntu2 (tags/RELEASE_600/final)"}
