# Data Analysis

## Description

Solutions for all data analysis course projects using Python at freeCodeCamp.

## Installation

```shell
git clone https://github.com/Vasyl-Poremchuk/data-analysis
cd data_analysis
python -m venv venv
venv\Scripts\activate (Windows) or source venv/bin/activate (Linux or macOS)
pip install -r requirements.txt
```

## Mean-Variance-Standard Deviation Calculator

### Task description

Create a function named **calculate()** that uses Numpy to output the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.
The input of the function should be a list containing 9 digits. The function should convert the list into a 3 x 3 Numpy array, and then return a dictionary containing the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix.
The returned dictionary should follow this format:
```python
{
  "mean": [axis1, axis2, flattened],
  "variance": [axis1, axis2, flattened],
  "standard_deviation": [axis1, axis2, flattened],
  "max": [axis1, axis2, flattened],
  "min": [axis1, axis2, flattened],
  "sum": [axis1, axis2, flattened],
}
```

NOTE: You can get more detailed information by following this [freeCodeCamp](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/mean-variance-standard-deviation-calculator) link.

## Demographic Data Analyzer

### Task description

In this challenge you must analyze demographic data using Pandas. You are given a dataset of demographic data that was extracted from the 1994 Census database.

NOTE: You can get more detailed information by following this [freeCodeCamp](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/demographic-data-analyzer) link.

## Medical Data Visualizer

### Task description

In this project, you will visualize and make calculations from medical examination data using Matplotlib, Seaborn, and Pandas. The dataset values were collected during medical examinations.

NOTE: You can get more detailed information by following this [freeCodeCamp](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/medical-data-visualizer) link.

## Page View Time Series Visualizer

### Task description

For this project you will visualize time series data using a line chart, bar chart, and box plots. You will use Pandas, Matplotlib, and Seaborn to visualize a dataset containing the number of page views each day on the freeCodeCamp.org forum from 2016-05-09 to 2019-12-03. The data visualizations will help you understand the patterns in visits and identify yearly and monthly growth.

NOTE: You can get more detailed information by following this [freeCodeCamp](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/page-view-time-series-visualizer) link.

## Sea Level Predictor

### Task description

You will analyze a dataset of the global average sea level change since 1880. You will use the data to predict the sea level change through year 2050.

NOTE: You can get more detailed information by following this [freeCodeCamp](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/sea-level-predictor) link.
