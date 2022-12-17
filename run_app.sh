#!/bin/bash

if ! command -v python &> /dev/null; then
  echo 'Error: 
    This program runs on Python, but it looks like Python is not installed.
    To install Python, head to https://installpython3.com/' >&2
  exit 1
fi

pip install pandas>=1.5.2 matplotlib>=3.6.2 pytest>=7.2.0

python app.py



