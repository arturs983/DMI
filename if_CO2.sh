#!/bin/bash
a=$1
#if (()) ... fi
#if (())... elif (()) ... elif (()) ... elese ... fi 
if (( $a > 0 )); then
   echo "Galvenais zars (jā apakšzars) -> tad, kad $a ir >0 "
elif (( $a == 1 )); then
   echo "Alternatīvs zars (tikai jā gadījumā) -> tad, kad $a ir >1"
else
   echo "Galvenais zars (nē apakšzars) -> tad, kad $a nav >0 "
fi
