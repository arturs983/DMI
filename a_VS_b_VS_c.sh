#!/bin/bash

echo "Cienījamais lietotājs, lūdzu, ievadi pirmo skaitli: "
read a
echo "Cienījamais lietotājs, lūdzu, ievadi otro skaitli: "
read b
echo "Cienījamais lietotājs, lūdzu, ievadi trešo skaitli: "
read c

if (( $a > $b && $a > $c ))
then
echo 'Lielākais skaitlis ir '$a
elif (( $b > $a && $b > $c ))
then
echo 'Lielākais skaitlis ir'$b
elif (( $c > $a && $c > $b ))
then
echo 'Lielākais skaitlis ir '$c
fi




