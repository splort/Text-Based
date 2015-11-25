#!/usr/bin/env bash

# This script will use each text file as a stream of input (commands from a user)
# and send it to the game, while matching all CHECK lines in the same text. The
# test "passes" if all CHECK lines are found on the output.
#
# CHECK lines can contain regular expressions.

syntax="`basename $0` test_file game_file"

if [ "$1" = "" ] || [ "$2" = "" ]; then
  echo $syntax
  exit 1
fi
if [ ! -f $1 ]; then
  echo "Test file $1 doesn't exist"
  exit 1
fi
if [ ! -f $2 ]; then
  echo "Game file $2 doesn't exist"
  exit 1
fi
test_file=$1
program=$2

# Run the test without the CHECK lines, captures the result
echo "Testing $test_file..."
out=`grep -v CHECK $test_file | python2 $program`
if [ $? != 0 ]; then
  echo "Error executing $program"
  exit 1
fi

# For each CHECK line, check output
cat $test_file | \
while read line; do
  line=`echo $line | grep "CHECK:" | sed -e 's/CHECK: //'`
  if [ "$line" != "" ]; then
    if echo $out | grep -q "$line"; then
      echo -e "\t+PASS"
    else
      touch ${test_file}.fail
      echo -e "\t-FAIL: $line"
    fi
  fi
done

# Return success if all pass
if [ -f ${test_file}.fail ]; then
  rm ${test_file}.fail
  exit 1
fi
