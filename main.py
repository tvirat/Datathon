import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

# Load data
data = pd.read_csv('subway-data.csv')

# Data Wrangling
data = data[data['Station'].str.contains('STATION', case=False, na=False) &
            ~data['Station'].str.contains(' TO', case=False, na=False) &
            ~data['Station'].str.contains(r'\(', case=False, na=False) &
            ~data['Station'].str.contains('-', case=False, na=False)]
data = data[data['Line'].isin(['YU', 'BD', 'SHP'])]

data['Date'] = pd.to_datetime(data['Date'])
data['Hour'] = data['Time'].apply(lambda x: int(x.split(':')[0]))
data['Minute'] = data['Time'].apply(lambda x: int(x.split(':')[1]))
data['DayOfWeek'] = data['Date'].dt.dayofweek
data['Delayed'] = data['Min Delay'] > 0


# RandomForestClassifier requires the feature to be numerical
# We have to encode categorical variables (Station, Bound, and Line)
label_encoders = {} # A Mapping between categorical variables and their encoded values
for column in ['Station', 'Bound', 'Line']:
    le = LabelEncoder()
    data[column] = le.fit_transform(data[column])
    label_encoders[column] = dict(zip(le.classes_, le.transform(le.classes_)))

print(label_encoders)

print(data.head())

features = ['Hour', 'Minute', 'DayOfWeek', 'Station', 'Line', 'Bound']
X = data[features]
y = data['Delayed']

# Splitting the data into 80% training data and 20% test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

print(X_train)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
print(y_pred)
print(f'Accuracy: {accuracy_score(y_test, y_pred)}')


def perdict_if_delay(hour: int, minute: int, day_of_week: int, station: str, line: str, bound: str) -> bool:
    try:
        input_df = pd.DataFrame([{
            'Hour': hour,
            'Minute': minute,
            'DayOfWeek': day_of_week,
            'Station': label_encoders['Station'][station],
            'Line': label_encoders['Line'][line],
            'Bound': label_encoders['Bound'][bound]
        }])
        return model.predict(input_df)[0]
    except KeyError:
        return "invalid input"

# print(perdict_if_delay(10, 20, 1, 'BAY STATION', 'YU', 'B'))

def perdict_delay_prob(hour: int, minute: int, day_of_week: int, station: str, line: str, bound: str) -> tuple[str, int]:
    try:
        input_df = pd.DataFrame([{
            'Hour': hour,
            'Minute': minute,
            'DayOfWeek': day_of_week,
            'Station': label_encoders['Station'][station],
            'Line': label_encoders['Line'][line],
            'Bound': label_encoders['Bound'][bound]
        }])
        return station, model.predict_proba(input_df)[0][1]
    except KeyError:
        return "invalid input"

# print(perdict_delay_prob(10, 20, 1, 'BAY STATION', 'YU', 'B'))
