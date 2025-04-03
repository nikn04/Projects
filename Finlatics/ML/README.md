# Sales Prediction Analysis

This project analyzes advertising expenditure data to predict product sales. The analysis uses a dataset containing information on advertising spending across different platforms (TV, Radio, and Newspaper) and the corresponding sales figures.

## Dataset Description

The dataset includes the following columns:

-   **TV:** Amount spent on TV advertising.
-   **Radio:** Amount spent on Radio advertising.
-   **Newspaper:** Amount spent on Newspaper advertising.
-   **Sales:** Number of units sold.

## Project Objectives

The primary goals of this project are to:

1.  Calculate the average amount spent on TV advertising.
2.  Determine the correlation between radio advertising expenditure and product sales.
3.  Identify the advertising medium with the highest impact on sales.
4.  Build a linear regression model to predict sales based on advertising expenditures.
5.  Evaluate the model's performance with and without data normalization.
6.  Assess the impact of using only Radio and Newspaper advertising expenditures as predictors.

## Code Description

The Python script `sales_prediction.py` performs the following steps:

1.  **Data Loading and Preprocessing:**
    -   Loads the dataset from an Excel file (`advertising_sales_data.xlsx`).
    -   Fills any missing values with the mean of their respective columns.

2.  **Data Analysis:**
    -   Calculates and prints the average TV advertising expenditure.
    -   Calculates and prints the correlation between radio advertising and sales.
    -   Identifies and prints the advertising medium with the highest correlation to sales.

3.  **Linear Regression Modeling:**
    -   Splits the data into training and testing sets.
    -   Trains a linear regression model using all advertising mediums as predictors.
    -   Visualizes the predicted sales against the actual sales using a scatter plot.
    -   Predicts sales for a new set of advertising expenditures (\$200 on TV, \$40 on Radio, \$50 on Newspaper).

4.  **Model Evaluation and Comparison:**
    -   Normalizes the dataset using `MinMaxScaler` and retrains the linear regression model.
    -   Evaluates the performance of the normalized model using the $R^2$ score.
    -   Trains another linear regression model using only Radio and Newspaper expenditures as predictors and evaluates its performance.


## Results

The script will output the following information:

-   Average amount spent on TV advertising.
-   Correlation between radio advertising expenditure and product sales.
-   Advertising medium with the highest impact on sales.
-   A plot visualizing actual vs. predicted sales.
-   Predicted sales for a given set of advertising expenditures.
-   Model score on normalized data.
-   Model score when only Radio and Newspaper are used as predictors.

These results provide insights into the effectiveness of different advertising mediums and the impact of data normalization on the sales prediction model.

Additionally a presentation was prepared to address key concerns in a rather effective concise manner.
