# STAT 159 HW2: Serena Williams Visualization

## Project Overview

This project reproduces a visualization of Serena Williams' professional tennis matches, inspired by a graphic published in The New York Times.

The scatter plot shows Serena Williams' age at each match and the age difference between her and her opponents. Blue represents wins, while red represents losses.

## Data Source

The raw match data comes from Tennis Abstract:

https://www.tennisabstract.com/jsmatches/SerenaWilliamsCareer.js

The dataset contains 1,038 match records.

## Project Structure

- `data/`: Raw JavaScript data and cleaned CSV dataset
- `scripts/download_data.py`: Downloads the raw data
- `scripts/clean_data.py`: Cleans the data and calculates player ages
- `scripts/plot_serena.py`: Creates the scatter plot
- `figures/`: Generated visualization
- `report.md`: Markdown report containing the plot and discussion
- `report.html`: HTML report
- `report.pdf`: PDF report
- `Makefile`: Automates the workflow
- `environment.yml`: Conda environment specification

## Requirements

- Python 3.13
- pandas
- matplotlib
- Quarto
- TinyTeX for PDF generation
- GNU Make

To create the Conda environment:

    conda env create -f environment.yml
    conda activate stat159-hw02

If TinyTeX is not installed:

    quarto install tinytex

## Reproducing the Analysis

Run the following command from the project directory:

    make all

The Makefile is intended to automate data processing, visualization, and report generation.

Alternatively, the Python scripts can be executed individually:

    python scripts/download_data.py
    python scripts/clean_data.py
    python scripts/plot_serena.py

To generate the reports:

    quarto render report.md --to html
    quarto render report.md --to pdf

## Visualization

![Serena Williams Age Comparison](figures/serena_age_plot.png)

## Results

The plot shows that Serena Williams frequently played against older opponents early in her career. As her career progressed, she increasingly competed against younger opponents.

## Cleaning Generated Files

Once the complete Makefile is configured, run:

    make clean

This removes generated outputs so the workflow can be reproduced.