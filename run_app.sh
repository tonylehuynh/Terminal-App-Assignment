#!/bin/bash

# Check if Python is installed
if ! command -v python &> /dev/null; then
  echo 'Error: 
    This program runs on Python, but it looks like Python is not installed.
    To install Python, head to https://www.python.org/downloads/' >&2
  exit 1
fi

# Check Python version
PYTHON_VERSION=$(python --version)
MIN_VERSION="3.11.1"

if [[ "$PYTHON_VERSION" < "$MIN_VERSION" ]]; then
  echo "Error: This program requires Python $MIN_VERSION or higher." >&2
  echo "Please head to https://www.python.org/downloads/ or ensure you update Python on your device." >&2
  exit 1
fi


pip install virtualenv

virtualenv venv

pip install pandas>=1.5.2 matplotlib>=3.6.2 pytest>=7.2.0

# Check if user has git installed
if ! command -v git &> /dev/null; then
  echo "Error: Git is not installed. Please install Git before running this script." >&2
  exit 1
fi

git clone https://github.com/tonylehuynh/Terminal-App-Assignment.git

python app.py


# Check if python is installed and RIGHT VERSION

# Install virtual environemnts

# Clone the github repo

# Install requirments. Then run python app