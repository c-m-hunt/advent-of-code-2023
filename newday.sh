#!/bin/bash

# Function to check if a file exists
check_file_existence() {
    if [ -e "$1" ]; then
        echo "Error: File '$1' already exists."
        exit 1
    fi
}

# Check if exactly one argument is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <number>"
    exit 1
fi

# Validate if the argument is a number
if ! [[ $1 =~ ^[0-9]+$ ]]; then
    echo "Error: Argument must be a number."
    exit 1
fi

# Define file names
input_file="advent/input/$1.txt"
input_test_file="advent/input/${1}_test.txt"
day_file="advent/day$1.py"
day_test_file="advent/tests/day${1}_test.py"

# Check if any of the destination files already exists
check_file_existence "$input_file"
check_file_existence "$input_test_file"a
check_file_existence "$day_file"
check_file_existence "$day_test_file"

# Create new blank files
touch "$input_file"
touch "$input_test_file"

# Copy the template files to the destination files
cp advent/template.py "$day_file"
cp advent/tests/testtemplate.py "$day_test_file"

# Replace 'day = None' with 'day = X' in the copied files using perl
perl -pi -e "s/day = None/day = $1/" "$day_file"
perl -pi -e "s/day = None/day = $1/" "$day_test_file"

echo "Files created successfully"