#!/bin/bash

pytest /tests/test_outputs.py -rA --ctrf /app/ctrf.json
status=$?

if [ $status -eq 0 ]; then
  echo 1 > /app/reward.txt
else
  echo 0 > /app/reward.txt
fi
