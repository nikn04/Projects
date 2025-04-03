# Finlatics
A project for financial analytics and insights, focusing on online advertising performance.

## Dataset Overview
This repository analyzes the online advertising performance of "Company X" from **April 1, 2020, to June 30, 2020**, with all transactions in US dollars. The dataset, managed by "Advert Firm A," includes metrics on ad campaigns, user interactions, and financial outcomes.

### Key Metrics
- **Day**: Date of the campaign.
- **Campaign**: Segmentation variable targeting specific user groups.
- **User Engagement**: Level of user interaction with ads.
- **Banner**: Size of the ad served.
- **Placement**: Publisher space (e.g., websites or apps) where ads are displayed.
- **Displays**: Number of ads served.
- **Cost**: Price paid by "Advert Firm A" for ad placements.
- **Clicks**: Number of user clicks on ads.
- **Revenue**: Amount paid by Company X to "Advert Firm A" for clicks.
- **Post Click Conversions**: On-site transactions within 30 days post-click.
- **Post Click Sales Amount**: Monetary value of those transactions.

### Additional Notes
- **Engagement**: Reflects user types based on behavior/characteristics.
- **Banner**: Defines ad size/impression.
- **Placement**: General publisher type (no specific names).

## Synopsis of Actions
The goal is to analyze the dataset and answer the following questions to uncover trends, correlations, and performance insights:

1. **Trend Analysis**
   - Examine the overall trend in user engagement over the campaign period.
   - Identify seasonal patterns or fluctuations in displays and clicks.
   - Analyze trends in post-click sales amounts over time.
   - Investigate post-click conversion rate patterns by day of the week.
   - Compare user engagement between weekdays and weekends.

2. **Impact of Ad Size (Banner)**
   - Assess how banner size affects click numbers.
   - Evaluate user engagement variation across banner sizes.
   - Analyze cost per click (CPC) across banner sizes.
   - Determine if specific banner sizes consistently outperform others in ROI.

3. **Placement Performance**
   - Identify which placements yield the highest displays and clicks.
   - Determine placement types with the highest post-click conversion rates.
   - Analyze the distribution of post-click conversions across placements.
   - Evaluate cost-effectiveness of placements for conversions.

4. **Financial Analysis**
   - Investigate correlation between ad serving costs and revenue from clicks.
   - Calculate average revenue per click for Company X.
   - Assess correlation between user engagement levels and revenue.
   - Examine campaign effectiveness by ad size and placement for ROI.
   - Analyze CPC variation across campaigns.

5. **Conversion Insights**
   - Identify campaigns with the highest post-click conversion rates.
   - Evaluate campaign effectiveness across user engagement types for conversions.
   - Detect cost-effective campaigns for generating conversions.

6. **Outlier Detection**
   - Identify outliers in cost, clicks, or revenue for further investigation.

## Folder Structure
- **ML/**: Machine learning models and notebooks
  - `Sales_Prediction_Dataset.ipynb`: Notebook for analysis (to be updated with this data).
- **Data/**: Raw datasets
  - `raw_data.csv`: Online advertising performance data (to be added).

## Getting Started
1. Clone the repo: `git clone https://github.com/YourUsername/finlatics.git`
2. Load `Data/raw_data.csv` into `ML/Sales_Prediction_Dataset.ipynb`.
3. Follow the analysis questions above to explore the dataset.

## Next Steps
- Import the dataset into the repository.
- Update `Sales_Prediction_Dataset.ipynb` with scripts to address the listed questions.
- Visualize trends and correlations using Python (e.g., Pandas, Matplotlib, Seaborn).
