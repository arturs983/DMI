
#!/bin/bash
#4.piemērs
echo "Tiek pildīts skripts: "$0
#echo $0
#echo $n
echo "Skripta nodoto argumentu skaitu"$#
echo "Skripta nodoti argumenti (attēlošana/grupēšana 1):"$*
echo "Skriptam nodoti argumenti (attēlošana/grupēšana):"$@
#echo $?
echo "Skriptam piešķirtias procesa numurs" $$
#echo $!

#3.piemers
#NAME="Vaards Uzvaards"
#echo $NAME
#unset NAME
#echo $NAME

#2.piemērs
#readonly NAME
#echo $NAME
#NAME="Uzvaards Vaards"
#echo $NAME

#1. piemērs
#NAME="Vaards Uzvaards"
#echo $NAME
