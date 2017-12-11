#!/bin/bash

TIMESTAMP=1420070400
QUANT=0
VAR=0
COR[0]=00BFFF
COR[1]=ADFF2F
COR[2]=4169E1
COR[3]=FF4500
COR[4]=C71585
COR[5]=4B0082
COR[6]=DC143C
COR[7]=008080
COR[8]=EE82EE
COR[9]=0000FF

while IFS="," read NOME ESCOLA CIDADE SERIE X
do
	ACTION=A
	NOVO=yes
	NOME=`echo -e "$NOME" | sed -e "s/\b\(.\)/\u\1/g"`
	ESCOLA=`echo -e "$ESCOLA" | sed -e "s/\b\(.\)/\u\1/g"`
	CIDADE=`echo -e "$CIDADE" | sed -e "s/\b\(.\)/\u\1/g"`
 	if [ $QUANT != 0 ]
	then
		for i in `seq 0 $QUANT`
		do
			if [ "$ESCOLA" == "${ESCOLAS[$QUANT]}" ]
			then ACTION=M ; NOVO=no
			fi
		done
	fi
	if [ "$NOVO" == "yes" ]
	then let "QUANT++" ; COR=`echo "${COR[$VAR]}"|bc` ; let "VAR++"
	ESCOLAS[$QUANT]=$ESCOLA
	fi
	TIMESTAMP=`echo "$TIMESTAMP+$RANDOM%21600"|bc`
echo "$TIMESTAMP|$NOME|$ACTION|$CIDADE/$ESCOLA/$SERIE|$COR"
done < media/tabela_temp > media/tabela
