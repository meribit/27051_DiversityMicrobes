# 27051_DiversityMicrobes
Files for exercises for the DTU 27051 course Diversity and application of microorganisms

# Analyzing Microbial Communities with python 


## Background

**Why?**
Soil microbiomes harbor vast, largely uncultured diversity with important ecological roles and untapped natural products; overcoming cultivation barriers is a central challenge. In a [recent publication](https://doi.org/10.1016/j.soilbio.2025.109938) we investigated the use of Live-FISH for soil microbial communties to potentially improve cultivation.

**What is Live‑FISH?** Live-Fluorescence in situ Hybridization (Live-FISH) is a fixation‑free variant of FISH that introduces rRNA‑targeted probes into living cells, enabling taxon‑specific labeling of cells that can then be sorted based on the fluorescence label for downstream cultivation. 

**Who is alive?** To determine the viable cell fractions, we included a propidium monoazide (PMA) treatment. PMA crosslinks DNA of dead cells when exposed to 470 nm LED light inhibiting downstream PCR amplification.

**What?** We sampled soil in Dyrehaven, Denmark and prepared microbial cell extracts from the soil and applied Live-FISH. There are four biological replicates for soil, viable cells and viable cells after Live-FISH. We amplified and sequenced the V3-V4 region of the 16S rRNA gene to characterise the microbial community.

You now want to know: 

#### 1. How does the richness and diversity of the soil microbial community change when the cells are extracted and Live-FISH is applied?

#### 2. How similar are the microbial communities between the soil, the viable extracted cells and the viable cells after Live-FISH to each other?


We will use the [scikit-bio](https://scikit.bio/index.html) libary, an open‑source Python library for bioinformatics, providing data structures and algorithms for analyzing biological and omics data.

## Setup your environment

The analysis assumes you have python installed on your local machine and can access it via an Unix/Linux terminal or Command Prompt/PowerShell.

If you know how to work with VS Code, you can also run the analysis in there.

If you need to install python, go to the [website](https://www.python.org/downloads/) and follow the instructions there or consider installing [miniconda](https://docs.conda.io/en/latest/miniconda.html).

### 1. Make a new conda environment

make a conda environment

`conda create -n scikit`

activate the new conda environment called `scikit`

`conda activate scikit`

run `which python` to check which python is used in the environment 

you can see all your current conda envrionments with 

`conda env list`


### 2. Install relveant libraries


once your conda envrionment is activated install the following libraries


install the scikit-bio package

`conda install -c conda-forge scikit-bio jupyter matplotlib`

if you run `conda list` once the installation is done, you can see all the libraries installed in your current conda environmnet

## Run the diversity analysis

Download the git hub repository and unzip the files. Put the files into a folder where you want to run your analysis. Then change to that directory in your terminal with `cd`

for example `cd /Users/Microbial_Diversity/Exercise5_python`

To check that the files are there and use `ls -l` to list all files and folders in your current directory.


### Option 1: jupyter notebook - groupwork5.ipynb

A [Jupyter](https://jupyter.org/) Notebook is an interactive workspace that lets you combine code, text, and visualizations in a single, shareable document.

If you are in the folder where the jupyter notebook is run the following to open the notebook in your browser. This should automatically open your default browser with the python code.

`jupyter notebook groupwork5.ipynb`

If the notebook is not in your current folder, you can also use the full path to where it is located.

You can run the python code sections from the jupyter notebook and directly see the output below each cell.

You can stop the notebook from your terminal with Ctr + C for example.


### Option 2: run python script - exercise5.py

run `which python` to check which python is used in the environment, you might have python3 installed and didn't make an alias for python == python3 then you need to type python3

To run the python script make sure it is in your current directory or use the full path to it.

If you run the python script, it will output some information along the way and create three plots showing richness, shannon diversity and a Principal Coordinate Analysis (PCoA) to inspect beta diversity between the samples.

`python3 exercise5.py`


### Option 3: use python interface and run commands seperately

to open the python interface you can also run `python` or `python3`.
In there you can run individual python commands. Option 1 and 2 are preferred but this is an alternative for running short commands or trying things out. However, a jupyter notebook is likely more suitable and more reproducible.

### Backup Option 4: Use jupyter-lite run python online - exercise5_online.ipynb

If you cannot run python on your local machine there is an alternative to run it online via [jupyter-lite](https://jupyter.org/try-jupyter/lab/index.html). Open the jupyter-lite and upload the notebook and the asv_table.tsv file by drag & drop on to the left panel. Open the notebook and run the code. You can open the png files online or download them. 
