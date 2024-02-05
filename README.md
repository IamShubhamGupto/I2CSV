# Image 2 CSV

This repository is a submission for the MathPix take home challenge. The goal is to develop a pipeline that can generate synthesized images containing normal distribution data which is to be extracted and stored in a CSV file format. The synthesized data has the following conditions:
- The rows and columns may not always be in the same place
- The font style, size, and weight may vary
- After points, the other stats may have different orderings and some may not always be included
- The title may vary in content and placement
- data is normally distrbuted

## Installation
```
git clone git@github.com:IamShubhamGupto/I2CSV.git
cd I2CSV
conda env create -f environment.yml
```

## Run
```
cd scripts
conda activate py310
python generate_synth.py -h
usage: generate_synth.py [-h] [--size SIZE] [--num_sheets NUM_SHEETS]
                         [--mean_point MEAN_POINT]
                         [--stddev_point STDDEV_POINT]
                         [--mean_rebound MEAN_REBOUND]
                         [--stddev_rebound STDDEV_REBOUND]
                         [--mean_assist MEAN_ASSIST]
                         [--stddev_assist STDDEV_ASSIST]
                         [--mean_steal MEAN_STEAL]
                         [--stddev_steal STDDEV_STEAL]
                         [--mean_block MEAN_BLOCK]
                         [--stddev_block STDDEV_BLOCK]
                         [--mean_turnover MEAN_TURNOVER]
                         [--stddev_turnover STDDEV_TURNOVER]
                         [--mean_foul MEAN_FOUL]
                         [--stddev_foul STDDEV_FOUL]

Generate synthetic data.

options:
  -h, --help            show this help message and exit
  --size SIZE           number of players per sheet
  --num_sheets NUM_SHEETS
                        number of sheets to generate
  --mean_point MEAN_POINT
                        mean points value
  --stddev_point STDDEV_POINT
                        standard deviation points value
  --mean_rebound MEAN_REBOUND
                        mean rebounds value
  --stddev_rebound STDDEV_REBOUND
                        standard deviation rebound value
  --mean_assist MEAN_ASSIST
                        mean assists value
  --stddev_assist STDDEV_ASSIST
                        standard deviation assists value
  --mean_steal MEAN_STEAL
                        mean steal value
  --stddev_steal STDDEV_STEAL
                        standard deviation steal value
  --mean_block MEAN_BLOCK
                        mean blocks value
  --stddev_block STDDEV_BLOCK
                        standard deviation blocks value
  --mean_turnover MEAN_TURNOVER
                        mean blocks value
  --stddev_turnover STDDEV_TURNOVER
                        standard deviation blocks value
  --mean_foul MEAN_FOUL
                        mean fouls value
  --stddev_foul STDDEV_FOUL
                        standard deviation blocks value
```

### Contribution
#### Pre-commit
We use [pre-commit](https://pre-commit.com/) to keep the notebooks clean.
In order to use pre-commit, run the following command in the repo top-level directory:
The pre commit

```bash
$ pre-commit install
```

At this point, pre-commit will automatically be run every time you make a commit.

#### Environment
[!WARNING]
This repository was tested and built on an M1 MacBook Pro.

To update conda environment files:

Linux or Mac
```shell
conda env export --no-builds | grep -v "prefix" > environment.yml
```

Windows
```shell
conda env export --no-builds | findstr -v "prefix" > environment.yml
```
