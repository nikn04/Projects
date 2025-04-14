# CryptoVision: High-Accuracy Closing Price Prediction for Cryptocurrencies

## Goal
This project aims to predict the daily closing prices of four cryptocurrencies—Bitcoin (BTC), Ethereum (ETH), Dogecoin (DOGE), and Bitcoin Cash (BCH)—using historical data from January 1, 2023, to April 8, 2025.
Three models—Linear Regression (LR), Support Vector Machine (SVM), and Long Short-Term Memory (LSTM) neural networks—are implemented independently, with an ensemble of LR and LSTM (90% LR + 10% LSTM) to potentially boost performance.

## Steps Involved

1. **Fetch Historical Data**
   - Use `yfinance` to download daily OHLCV (Open, High, Low, Close, Volume) data for each cryptocurrency from Yahoo Finance.
   - Add a `DateNumber` column by converting dates to ordinal numbers for numerical modeling.

2. **Add Useful Features**
   - Create lagged closing prices (`Yesterday_Close`, `Two_Days_Ago_Close`, `Three_Days_Ago_Close`) to capture recent trends.
   - Compute moving averages (`Five_Day_Avg`, `Ten_Day_EMA`) for trend analysis.
   - Calculate Relative Strength Index (RSI) to measure momentum.
   - Include volatility (`Daily_Volatility`) and volume change (`Volume_Change`) metrics.
   - Add Bollinger Bands (`BB_Upper`, `BB_Lower`) for price range insights.

3. **Prepare Data**
   - Define `X` as the feature set (16 features shifted by 1 day) and `y` as the target (closing price).
   - Scale `X` and `y` to a 0–1 range using `MinMaxScaler` for model compatibility.
   - Split data into 80% training and 20% testing sets, preserving time order (no shuffling).

4. **Linear Regression Model**
   - Fit an LR model to predict scaled `y` from `X`.
   - Unscale predictions and compute MSE and R².

5. **Support Vector Machine (SVM) Model**
   - Use SVR with an RBF kernel (`C=1000`, `epsilon=0.01`) for non-linear regression.
   - Predict, unscale, and evaluate with MSE and R².

6. **LSTM Model**
   - Prepare 15-day sequences of closing prices for time-series learning.
   - Build a two-layer LSTM (250 and 150 units) with dropout (0.2) and a dense layer (50 units, ReLU).
   - Train with RMSprop (learning rate 0.0001), Huber loss, and early stopping (patience=10).
   - Predict, unscale, and evaluate.

7. **Ensemble (LR + LSTM)**
   - Align LR and LSTM prediction lengths to the smaller test size.
   - Combine predictions: 90% LR + 10% LSTM.
   - Evaluate the ensemble with MSE and R².
   - Plot actual vs. predicted prices.

8. **Display Results**
   - Print MSE and R² for LR, SVM, LSTM, and the ensemble for each cryptocurrency.
   - Summarize all results at the end.

## Models: Advantages and Drawbacks

### Linear Regression (LR)
- **Advantages**:
  - Simple and fast to train, making it computationally efficient.
  - Performs well when relationships between features (e.g., lagged prices, RSI) and the target are roughly linear.
  - Reliable baseline with consistent results (e.g., Ethereum R² = 0.9684).
- **Drawbacks**:
  - Assumes linearity, which may not fully capture crypto’s volatile, non-linear patterns.
  - Limited ability to model complex temporal dependencies.

### Support Vector Machine (SVM)
- **Advantages**:
  - Handles non-linear relationships via the RBF kernel, potentially capturing crypto price swings.
  - Robust to outliers with proper tuning of `C` and `epsilon`.
- **Drawbacks**:
  - Sensitive to hyperparameter choices—poor tuning led to negative R² (e.g., Bitcoin R² = -21.3785).
  - Scales poorly with large datasets and can be slow to train.
  - Struggles with time-series structure without sequence-aware preprocessing.

### Long Short-Term Memory (LSTM)
- **Advantages**:
  - Designed for time-series data, excels at learning long-term dependencies (e.g., 15-day sequences).
  - Can model non-linear patterns and temporal trends in crypto prices.
- **Drawbacks**:
  - Computationally intensive and slow to train (150 epochs per crypto).
  - Prone to overfitting or instability (e.g., Dogecoin R² = 0.1883 vs. Bitcoin R² = 0.7419).
  - Requires careful tuning (layers, units, dropout, learning rate).

### Ensemble (LR + LSTM)
- **Advantages**:
  - Combines LR’s stability with LSTM’s temporal insight, potentially improving over individual models.
  - Weighted approach (90% LR + 10% LSTM) leverages LR’s strength while adding a small LSTM boost.
- **Drawbacks**:
  - Relies on LSTM’s consistency—if LSTM underperforms (e.g., Dogecoin), it drags the ensemble down.
  - Adds complexity without guaranteed gains (e.g., Ethereum R² = 0.9423 vs. LR’s 0.9684).

## Why an Ensemble Model Was Considered
The ensemble of LR and LSTM was introduced to balance their strengths and weaknesses:
- **LR’s Reliability**: LR consistently delivers high R² scores (e.g., 0.9264–0.9684 across cryptos), making it a strong anchor.
- **LSTM’s Temporal Edge**: LSTM could capture time-series patterns LR misses, especially in volatile markets like crypto.
- **Complementary Strengths**: Combining a simple, linear model with a complex, sequential one might push R² to higher values by averaging out individual errors.
- **Rationale**: Crypto prices are noisy—combining models could smooth predictions and reduce overfitting risks. However, LSTM’s inconsistency (e.g., R² ranging from 0.1883 to 0.8533) often limits the ensemble’s benefit, as seen in results where it rarely beats standalone LR.

SVM was excluded from the ensemble due to its erratic performance (e.g., negative R² values), making it less reliable for blending. Instead, it’s kept standalone.

## Running the Code
1. **Requirements**: Install dependencies (`pip install yfinance pandas numpy scikit-learn tensorflow matplotlib`).
2. **Execution**: Run the script in a Python environment. It fetches data, trains models, and outputs results/plots for each cryptocurrency.
3. **Output**: Expect MSE and R² scores for LR, SVM, LSTM, and the LR+LSTM ensemble, plus a plot per crypto.
