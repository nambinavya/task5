# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectFromModel

# Load sample dataset (Iris dataset)
data = load_iris()
X = data.data
y = data.target

# Convert to DataFrame for easier manipulation
df = pd.DataFrame(X, columns=data.feature_names)
df['target'] = y

# Display the first few rows of the DataFrame
print("Original DataFrame:")
print(df.head())

# Feature Engineering: Generate new features
df['sepal_length_to_width_ratio'] = df['sepal length (cm)'] / df['sepal width (cm)']
df['petal_length_to_width_ratio'] = df['petal length (cm)'] / df['petal width (cm)']

# Display the DataFrame with new features
print("\nDataFrame with New Features:")
print(df.head())

# Separate features and target variable
X = df.drop(columns=['target'])
y = df['target']

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA for dimensionality reduction
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Display the explained variance ratio of the principal components
print("\nExplained Variance Ratio of Principal Components:")
print(pca.explained_variance_ratio_)

# Feature Selection using Feature Importance from Random Forest
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X, y)

# Get feature importances
importances = rf.feature_importances_

# Display feature importances
print("\nFeature Importances from Random Forest:")
for feature, importance in zip(X.columns, importances):
    print(f"{feature}: {importance}")

# Select features based on importance
selector = SelectFromModel(rf, threshold='mean', prefit=True)
X_selected = selector.transform(X)

# Display selected features
selected_features = X.columns[selector.get_support()]
print("\nSelected Features based on Importance:")
print(selected_features)

# Final dataset with selected features
df_selected = pd.DataFrame(X_selected, columns=selected_features)

print("\nFinal DataFrame with Selected Features:")
print(df_selected.head())
