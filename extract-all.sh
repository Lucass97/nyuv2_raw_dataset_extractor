#!/bin/bash

# Colors
Red='\e[0;31m';
BRed='\e[1;31m';
BIRed='\e[1;91m';
Gre='\e[0;32m';
BGre='\e[1;32m';
BBlu='\e[1;34m';
BWhi='\e[1;37m';
RCol='\e[0m';

zip_dir="data/raw"

source venv/bin/activate

# Iterate over all ZIP files in the directory
for zip_file in "${zip_dir}"/*.zip; do
    
    echo "Running extract.py script for file: ${zip_file}"

    python3 extract.py --path "${zip_file}" --output_dir "data/extracted" --undistort --fill-depth

done

deactivate
