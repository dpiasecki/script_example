#!/bin/bash

FIRST=$1
SECOND=$2

NUMERIC=^[0-9]+$

if ! [[ "$FIRST" =~ $NUMERIC ]]
  then
  echo "First input is not a number"
elif ! [[ "$SECOND" =~ $NUMERIC ]]
  then
  echo "Second input is not a number" 
else
  TOTAL=$(($FIRST + $SECOND))
fi

echo $TOTAL