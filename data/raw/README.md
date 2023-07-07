## Extract All Script

The `extract-all.sh` script provided allows for the extraction and processing of multiple ZIP files from a specified directory. It automates the extraction process using the `extract.py` script for each ZIP file found in the `data/raw` directory. The resulting data will be saved in the `data/extracted` directory.

To utilize the `extract-all.sh` script, follow these steps:

1. Ensure that you have set up the required dependencies and the virtual environment, as described in the installation instructions.

2. Provide execute permission to the `extract-all.sh` script:

```shell
chmod +x extract-all.sh
```

3. Run the `extract-all.sh` script:

```shell
./extract-all.sh
```

The script will iterate over all the ZIP files found in the `data/raw` directory. For each file, it will execute the `extract.py` script with the specified command line arguments, extracting the data and performing any necessary processing. The extracted data will be saved in the `data/extracted` directory.