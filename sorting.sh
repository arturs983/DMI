#!/bin/bash

a=$1
b=$2
c=$3
#if (()) ... fi
#if (()) ... elif (()) .. elif (()) ... elif(()) ... else .. fi
if (( $a > 0 )); then
echo "Galv. zars (jā apakšzars) -> tad, kad $a ir >0"
elif (( $a == 0 )); then
echo "Alt. zars (tikai jā gadījumā) -> tad, kad $a ir >1"
else
echo "Galv. zars (nē apakšzars) -> tad, kad $a nav >0 "
fi

if [ $1 -gt $2 -a $1 -gt $2 ]
#if (( $a > $b && $a > $b ))
then
max=$1
elif [ $2 -gt $1 -a $2 -gt $3 ]
#elif (( $b > $a && $b > $c ))
then
max=$2
elif [ $3 -gt $1 -a $3 -gt $2 ]
#elif (( $b > $a && $b > $c ))
then
max=$3
fi

if [ $1 -lt $2 -a $1 -lt $2 ]
#if (( $a > $b && $a > $b ))
then
min=$1
elif [ $2 -lt $1 -a $2 -lt $3 ]
#elif (( $b > $a && $b > $c ))
then
min=$2
elif [ $3 -lt $1 -a $3 -lt $2 ]
#elif (( $b > $a && $b > $c ))
then
min=$3
fi

vid=$(($1+$2+$3))
echo $vid
vid=$((vid/3))

echo "Lielākais skaitlis ir "$max
echo "Mazākais skaitlis ir "$min
echo "Vidējais skaitlis ir "$vid
