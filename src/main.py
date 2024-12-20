# Import Libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load Dataset
df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv')

# Data Preparation
y = df['logS']
x = df.drop('logS', axis=1)

# Split Data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=100)

# Train Linear Regression Model
lr = LinearRegression()
lr.fit(x_train, y_train)

# Predictions
y_pred = lr.predict(x_test)

# Evaluate Model Performance
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

# Comparison with Another Model (Optional Extension)
# Placeholder for adding RandomForest or other models for comparison.

# Save Model Performance
results = {
    "Model": ["Linear Regression"],
    "Mean Squared Error": [mse],
    "R-squared": [r2]
}
results_df = pd.DataFrame(results)
results_df.to_csv('model_performance.csv', index=False)

print("Model performance saved to 'model_performance.csv'")
