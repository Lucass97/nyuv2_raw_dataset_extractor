# NyuV2 Raw Dataset Extractor

The NyuV2 Raw Dataset Extractor is a Python project that aims to process the raw dataset provided by **NyuV2** and perform various operations such as *fill depth colorization* and *undistortion* on the depth maps and RGB images. Additionally, it synchronizes the frames to create a video sequence. This implementation is a partial Python adaptation of the official **NyuV2 toolbox**, which is developed in MATLAB.

> To obtain more information, please refer to the official link [here](https://cs.nyu.edu/~silberman/datasets/nyu_depth_v2.html).



## Table of Contents
- [Installation](#installation)
- [Download Raw Dataset](#download-raw-dataset)
- [Usage](#usage)
- [Command Line Arguments](#command-line-arguments)
- [Extract All Script](#extract-all-script)


## Installation

To use the NyuV2 Raw Dataset Extractor, follow these steps:

1. Clone the repository:
   ```shell
   git clone https://github.com/your/repository.git
   ```

2. Navigate to the project directory:
   ```shell
   cd nyuv2-raw-dataset-extractor
   ```

3. Create and activate a virtual environment (optional but recommended):
   ```shell
   python3 -m venv venv
   source venv/bin/activate
   ```
   > To create a new virtual environment (venv), use the guide at the following [link](https://docs.python.org/3/library/venv.html).

4. Install the required dependencies:
   ```shell
   pip install -r requirements.txt
   ```

## Download Raw Dataset

To download the raw NYUv2 dataset, you can use the provided `download-raw-dataset.sh` script located in the `data/raw` directory. The script automatically downloads the required dataset files and verifies their integrity using MD5 checksums.

To download the dataset, follow these steps:

1. Open a terminal and navigate to the project directory:

```shell
cd nyuv2-raw-dataset-extractor/data/raw
```

2. Give execute permission to the `download-raw-dataset.sh` script:
```shell
chmod +x download-raw-dataset.sh
```

2. Execute the `download-raw-dataset.sh` script:
```shell
./download-raw-dataset.sh
```

The script will download the necessary dataset files and display progress messages. It will also calculate the MD5 checksums of the downloaded files and verify their integrity.

## Usage

To use the NyuV2 Raw Dataset Extractor, execute the `extractor.py` script with the desired command line arguments. The script processes the raw dataset and performs the specified operations on the data.

```shell
python extractor.py 
      --path <path_to_raw_dataset>
      --output_dir <output_directory>
      [--undistort] [--save-undistort-diff] [--fill-depth]
```

### Command Line Arguments

The following command line arguments are available for the NyuV2 Raw Dataset Extractor:

- `--path` (default: *"data/raw/basement.zip"*) - Specifies the relative path to the raw dataset archive file in ZIP format.
- `--output_dir` - (default: *"data/extracted"*) Specifies the output directory where the processed data will be saved.
- `--undistort` (default: *True*) - Enables undistortion of RGB and depth images.
- `--save-undistort-diff` (default: *False*) - Saves the difference between the original and undistorted images.
- `--fill-depth` (*default*: *False*) - Uses the fill depth colorization algorithm.

## Extract All Script

The `extract-all.sh` script provided allows for the extraction and processing of multiple ZIP files from a specified directory. It automates the extraction process using the `extract.py` script for each ZIP file found in the `data/raw` directory. The resulting data will be saved in the `data/extracted` directory.

To utilize the `extract-all.sh` script, follow these steps:

1. Open a terminal and navigate to the project directory.

2. Ensure that you have set up the required dependencies and the virtual environment, as described in the installation instructions.

3. Provide execute permission to the `extract-all.sh` script:

```shell
chmod +x extract-all.sh
```

4. Run the `extract-all.sh` script:

```shell
./extract-all.sh
```

The script will iterate over all the ZIP files found in the `data/raw` directory. For each file, it will execute the `extract.py` script with the specified command line arguments, extracting the data and performing any necessary processing. The extracted data will be saved in the `data/extracted` directory.