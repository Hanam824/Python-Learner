import pandas as pd
import statsmodels.api as sm
import matplotlib.pylot as plt

# load the data from the uploaded file
file_path = 'OSL_Example.csv'
data = pd.read_csv(file_path)

# Extract the independent and dependent variables
X = data['Avertising_spend'] # Independent variable
Y = data['Sales_Revenue'] # Dependent variable

# Add a constant to the independent variable to account for the itercept
X_with_const = sm.add_constant(X)

# Perform OLS regression
model = sm.OLS(Y, X_with_const)
result = model.fit()

# print the summary of the regression
print(result.sumary())

# plot the data points
plt.scatter(X, Y, color='blue', label='Data Points')

# plot the regression line
predicted_Y = results.predict(X_with_const)
plt.plot(X, predicted_Y, color='red', label='Regression Line')

# Add labels and legend
plt.xlabel('Advertising Spend')
plt.ylabel('Sales Revenue')
plt.title('OLS Regression: Sales Revenue vs Advertising Spend')
plt.legend()
plt.show()