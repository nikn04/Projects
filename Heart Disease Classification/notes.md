# Heart Disease Classification 


** Implementing Decision Trees: **

Implements a decision tree classifier to predict heart disease using the Cleveland Heart Disease dataset from the UCI Machine Learning Repository. The project starts with data preprocessing to handle missing values, followed by training a pruned decision tree, evaluating its performance, and experimenting with advanced techniques to optimize accuracy. The baseline pruned model achieves a test accuracy of 81.33%, with later enhancements reaching up to 84%.

## Dataset
The Cleveland Heart Disease dataset (`processed.cleveland.data`) contains 303 patient records with 14 attributes, including age, cholesterol, and heart disease diagnosis (`hd`, 0–4). Missing values are denoted by `?`.

1.  **Library Imports:**
    *   Importing essential libraries:
        *   `pandas` for data manipulation and DataFrame handling.
        *   `numpy` for numerical computations.
        *   `matplotlib.pyplot` for creating visualizations and plots.
        *   `DecisionTreeClassifier` from `sklearn.tree` to build the decision tree model.
        *   `plot_tree` to visualize the decision tree.
        *   `train_test_split` from `sklearn.model_selection` to split the data into training and testing sets.
        *   `cross_val_score` to perform cross-validation for model evaluation.
        *   `confusion_matrix` and `ConfusionMatrixDisplay` from `sklearn.metrics` to analyze the model's predictions.

2.  **Data Loading:**
    *   Loaded the dataset directly from the UCI Machine Learning Repository using `pd.read_csv()`.  Since the CSV file lacked a header row, we specified `header=None`.

3.  **Data Preprocessing and Feature Engineering:**
    *   Assigned descriptive names to the columns based on the dataset's documentation for clarity.
    *   Separated the dataset into feature matrix `X` (independent variables) and target variable `y` (dependent variable 'hd' for heart disease).
    *   Explored the data types and unique values in each column.
    *   Utilized one-hot encoding with `pd.get_dummies()` on categorical features (`cp`, `restecg`, `slope`, and `thal`). This converts each category into a binary column, preventing the model from assuming ordinal relationships between categories.
    *   Converted the target variable `y` into a binary classification problem (0 for no heart disease, 1 for heart disease).

4.  **Data Splitting:**
    *   Split the preprocessed data into training and testing sets using `train_test_split`. The `random_state` parameter was set to ensure reproducibility.

5.  **Model Building and Training:**
    *   Initialized a `DecisionTreeClassifier` with a specified `random_state` for reproducibility.
    *   Trained the decision tree model using the training data (`X_train`, `y_train`) with the `.fit()` method.

6.  **Visualization:**
    *   Visualized the decision tree using `plot_tree`, which provides insights into the model's decision-making process.

7.  **Evaluation and Tuning:**
    *   Used a confusion matrix to evaluate the performance of the classification model.
    *   Used cross validation to see how accurate the model is.
    *   Used Grid Search CV to find the best parameters for the model and improve the accuracy.

8. **Feature Engineering:**
    * After using GridSearch to find the best hyperparameters, the final model's performance depends on how well the features represent the underlying patterns in the data. Further feature engineering at this stage would involve analyzing the feature importances provided by the decision tree, combining or transforming existing features to create new ones, or even revisiting the one-hot encoding to ensure it's optimally configured. It's an iterative process of creating, evaluating, and refining features to maximize the model's predictive power.

## Hyperparameter Tuning and Model Optimization

1.  **Hyperparameter Tuning (GridSearchCV):**
    *   Performed hyperparameter tuning using `GridSearchCV` with the following grid:
        *   `max_depth=[3, 5, 7, 10]`
        *   `min_samples_split=[2, 5, 10]`
        *   `min_samples_leaf=[1, 2, 4]`
    *   The best combination found was `max_depth=7`, `min_samples_leaf=4`, and `min_samples_split=2`.
    *   However, the test accuracy was `0.7733`, indicating potential overfitting.

2.  **Feature Engineering:**
    *   Attempted to convert columns `ca` and `thal` to floats, but this resulted in a drop in accuracy to the `0.7833–0.8` range.

3.  **Class Weights:**
    *   To address class imbalance in the binary target variable `y` (0: 53.87%, 1: 46.13%), added `class_weight='balanced'`.
    *   This improved the test accuracy to `0.8267–0.83`.

4.  **Cross-Validation:**
    *   Conducted 5-fold cross-validation on a pruned model, achieving a mean accuracy of `0.7945` with a standard deviation of `0.0603`.

5.  **Expanded Tuning:**
    *   Expanded the tuning grid to include `criterion='entropy'`, which yielded the same best test result of `0.8267`.

6.  **Ensemble Methods:**
    *   Experimented with ensembling by combining multiple decision trees using a voting classifier, resulting in an accuracy of `0.8133`.

7.  **Final Push:**
To maximize accuracy beyond the baseline 0.8133 and stabilize or exceed the peak of 0.8267–0.83, the following refinements were applied:
   *  Cross-Validation on Weighted Model: A 5-fold CV on a weighted decision tree (`max_depth=3`, `class_weight='balanced'`) yielded a mean CV accuracy of 0.7982, with a test accuracy of 0.8267, confirming robustness.
   *  Feature Selection: Using only `ca`, `cp`, `thal`, `oldpeak`, test accuracy reached 0.84.
   *  Bagging with Weighted Trees: `BaggingClassifier` with 10 weighted trees achieved a test accuracy of 0.8333.

8.  **Results:**
   *  Baseline: 81.33% (pruned tree, `max_depth=3`, no class weights).
   *  Best Achieved: 82.67% (weighted model, `max_depth=3`, `class_weight='balanced'`; peaked at 83% in some runs).
- **Final Push Outcomes**:
  - Weighted Model CV: Test accuracy 82.67%, CV mean 0.7982.
  - Feature Selection: 84%.
  - Bagging: 83.33%.
- **Challenges**: Numeric conversion of `ca` and `thal` underperformed (0.7833–0.8); deeper trees overfit (e.g., 0.7867); small dataset (297 samples) limits gains beyond ~0.83.
