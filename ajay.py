from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score

fin_df = df_data.dropna()
X = fin_df['Unnamed: 0'].values.reshape(-1, 1)
y = fin_df['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Using Lasso Regression as the regressor
regressor = Lasso(alpha=0.1) 
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

# Calculate Mean Squared Error
mse = mean_squared_error(y_test, y_pred)
print(f'Lasso Regression Mean Squared Error: {mse}')
