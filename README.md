# Brain Connectivity Visualization in a Connectogram

## Overview

This project utilizes the MNE-Python library to visualize brain connectivity using a circular layout. The visualization represents the connectivity between different brain regions based on experimental and control data of mice with autism, highlighting regions with significant differences in connectivity.

## Requirements

- Python 
- MNE-Python
- Matplotlib
- Pandas
- NumPy

## Project Structure

- **Brain_region_names.xlsx:** Excel file containing a list of brain areas.
- **results_experimental.xlsx:** Excel file with experimental data.
- **results_control.xlsx:** Excel file with control data.
- **visualization_script.py:** Python script for generating brain connectivity visualization.

## Usage

1. Install the required libraries mentioned in the `Requirements` section.
2. Place the necessary data files (`Brain_region_names.xlsx`, `results_experimental.xlsx`, `results_control.xlsx`) in the project directory.
3. Run the `connectogramWithMne.py` script to generate the brain connectivity visualization.

## Description

1. **Data Preparation:**
   - Reads brain region names from `Brain_region_names.xlsx`.
   - Loads experimental and control data from `results_experimental.xlsx` and `results_control.xlsx` respectively.
   - Combines the data arrays based on certain conditions and extracts significant values (p-value < 0.05).

2. **Visualization:**
   - Constructs a circular layout for brain regions using MNE-Python's `circular_layout` function.
   - Utilizes `plot_connectivity_circle` to create a connectivity visualization based on the processed data.
   - The visualization uses a color scheme to represent the connectivity strength between different brain regions. The lower the pvalue 
  	is, the stronger the color shade, indicating a higher significance in the value of number of tracts between two brain regions.

## Notes

- Ensure all required data files are in the correct format and located in the project directory before running the script.
- Experiment with different parameters in the visualization script (such as colormap, node colors, etc.) to explore variations in the visualization.
