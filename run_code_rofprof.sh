#!/bin/bash
for_start=$1
for_end=$2
case=$3

declare -a tccg_problem_sizes=(
    "0"                         # 
    "312 312 24 312"          #  1
    "312 24 296 312"          #  2
    "72 72 24 72 72"          #  3
    "72 24 72 72 72"          #  4
    "72 72 24 72 72"          #  5
    "48 32 24 32 48 32"       #  6
    "48 32 32 24 48 48"       #  7
    "48 24 32 32 48 32"       #  8
    "72 72 72 72 72"          #  9
    "72 72 72 72 72"          # 10
    "72 72 72 72 72"          # 11
    "5136 5120 5136"          # 12
    "312 296 296 312"         # 13
    "312 296 312 312"         # 14
    "312 296 296 312"         # 15
    "312 312 296 296"         # 16
    "312 312 296 296"         # 17
    "312 296 296 312"         # 18
    "72 72 72 72 72"          # 19
    "72 72 72 72 72 72"       # 20
    "72 72 72 72 72 72"       # 21
    "72 72 72 72 72 72"       # 22
    "72 72 72 72 72 72"       # 23
    "72 72 72 72 72 72"       # 24
    "72 72 72 72 72 72"       # 25
    "72 72 72 72 72 72"       # 26
    "72 72 72 72 72 72"       # 27
    "72 72 72 72 72 72"       # 28
    "72 72 72 72 72 72"       # 29
    "72 72 72 72 72 72"       # 30
    "24 16 16 24 16 16 24"    # 31
    "24 16 16 24 16 16 24"    # 32
    "24 16 16 24 16 16 24"    # 33
    "24 16 16 24 16 16 24"    # 34
    "24 16 16 24 16 16 24"    # 35
    "24 16 16 24 16 16 24"    # 36
    "24 16 16 16 24 16 24"    # 37
    "24 16 16 16 24 16 24"    # 38
    "24 16 16 16 24 16 24"    # 39
    "24 16 16 16 24 16 24"    # 40
    "24 16 16 16 24 16 24"    # 41
    "24 16 16 16 24 16 24"    # 42
    "24 16 16 24 16 16 24"    # 43
    "24 16 16 24 16 16 24"    # 44
    "24 16 16 24 16 16 24"    # 45
    "24 16 16 24 16 16 24"    # 46
    "24 16 16 24 16 16 24"    # 47
    "24 16 16 24 16 16 24")   # 48

#
#   [2] make
#

mkdir allcode_$case
cp main_codes_float/* allcode_$case/
cp Makefile allcode_$case/
cp inputmetricsnew.txt allcode_$case/

mv temp* allcode_$case

cp data-tccg-detail.py allcode_$case/

cd allcode_$case/

for number in $( seq $for_start $for_end )
do
    if [ ${number} -lt 10 ]
    then 
        make k_tccg_0${number}
    else
        make k_tccg_${number}
    fi
done

for number in $( seq $for_start $for_end )
do
    if [ ${number} -lt 10 ]
    then
        # rocprof --stats -o output_0${number}.csv  ./k_tccg_0${number} ${tccg_problem_sizes[$number]} |& tee output_0${number}.txt
        rocprof --stats -i inputmetricsnew.txt  -o output_0${number}.csv  ./k_tccg_0${number} ${tccg_problem_sizes[$number]} |& tee output_0${number}.txt
        cat output_0${number}.csv >> output_0${number}.txt
    else
        # rocprof --stats -o output_${number}.csv  ./k_tccg_${number} ${tccg_problem_sizes[$number]} |& tee output_${number}.txt
        rocprof --stats -i inputmetricsnew.txt -o output_${number}.csv  ./k_tccg_${number} ${tccg_problem_sizes[$number]} |& tee output_${number}.txt
        cat  output_${number}.csv >> tee output_${number}.txt
    fi
done

mkdir isa_output/
mv *.s isa_output/

rm *hip-amdgcn-amd-amdhsa-gfx908*
rm *host-x86_64-unknown-linux-gnu*
rm *amdgcn-amd-amdhsa-gfx1030*

python3 data-tccg-detail.py $for_start $for_end |& tee cogent_tccg_results_$case.txt

mkdir Outputs
mv output* Outputs/

mkdir codes 
mv *.h codes/
mv *.cpp codes/

rm *.hipfb
