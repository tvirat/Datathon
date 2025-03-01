import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

# Load data
data = pd.read_csv('subway-data.csv')

# Data Wrangling
data['Date'] = pd.to_datetime(data['Date'])
data['Hour'] = data['Time'].apply(lambda x: int(x.split(':')[0]))
data['Minute'] = data['Time'].apply(lambda x: int(x.split(':')[1]))
data['DayOfWeek'] = data['Date'].dt.dayofweek
data['Delayed'] = data['Min Delay'] > 0

# RandomForestClassifier requires the feature to be numerical
# We have to encode categorical variables (Station, Bound, and Line)
for column in ['Station', 'Bound', 'Line']:
    le = LabelEncoder()
    data[column] = le.fit_transform(data[column])

print(data.head())

features = ['Hour', 'Minute', 'DayOfWeek', 'Station', 'Line', 'Bound', 'Min Gap']
X = data[features]
y = data['Delayed']

# Splitting the data into 80% training data and 20% test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
print(y_pred)
print(f'Accuracy: {accuracy_score(y_test, y_pred)}')
