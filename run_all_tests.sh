#!/usr/bin/env bash

# This script calls the test script for every *.test file in "tests"
# for every python script in here. The format must be tests/script_name

root=`pwd`
for program in *.py; do
  test_dir=tests/$program
  prog=$root/$program

  if [ ! -d $test_dir ]; then
    continue
  fi

  echo "In $test_dir"
  fail=0
  cd $test_dir
  for file in *.test; do
    ../test.sh $file $prog
  	if [ $? != 0 ]; then
  		fail=$((fail+1))
  	fi
  done
  cd - > /dev/null
done

if [ $fail -gt 0 ]; then
	echo "$fail falure(s)"
	exit 1
else
	echo "All pass"
fi
