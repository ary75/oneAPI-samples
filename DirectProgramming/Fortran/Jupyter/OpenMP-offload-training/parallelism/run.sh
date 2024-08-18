#!/bin/bash
source /opt/intel/oneapi/setvars.sh > /dev/null 2>&1
/bin/echo "##" $(whoami) is running OMP_Offload Module3 -- Parallelism - 1 of 1 main.cpp/main.f90
echo "########## Compiling"
ifx -fiopenmp -fopenmp-targets=spir64 main.f90 -o bin/a.out || exit $?
echo "########## Executing"
cd bin
./a.out
echo "########## Done"
