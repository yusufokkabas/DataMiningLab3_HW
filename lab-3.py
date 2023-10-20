import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.preprocessing import KBinsDiscretizer
dF = pd.read_csv('lab-3-data.csv', delimiter=';')
print(dF)
# Remove unimportant attributes. In this case I wanna drop FirstName and LastName and keep StudentID as primary key
columnstToRemove = ['FirstName', 'LastName']
dF = dF.drop(columns=columnstToRemove)
print("After Removing", dF)
# Fill in missing values with the most repeated value
# Only Age column has missing value
mode = dF['Age'].mode()[0]
dF.fillna(mode, inplace=True)
print("After Filling", dF)
# Correcting encoding errors
# We have errors with Gender, ParentEncouragement and CollegePlans
gender_mapping = {
    'M': 'Male',
    '1': 'Male'
}
dF['Gender'] = dF['Gender'].replace(gender_mapping)
parent_encouragement_mapping = {
    'Not': 'Not Encouraged'
}
dF['ParentEncouragement'] = dF['ParentEncouragement'].replace(
    parent_encouragement_mapping)
college_plans_mapping = {
    'Not': 'Does not plan to attend',
    'P': 'Plans to attend'
}
dF['CollegePlans'] = dF['CollegePlans'].replace(college_plans_mapping)
print("After Mapping", dF)
# MinMax Normalization Range [1,4]
minmax_scale = preprocessing.MinMaxScaler(feature_range=(1, 4))
minmax_scale.fit(dF[['AverageGrade']])
dF['AverageGrade'] = minmax_scale.transform(dF[['AverageGrade']])
print("Print after min-max scaler", dF)
# Remove Noisy Data for Age , ParentIncome, AverageGrades
mode_age = dF['Age'].mode()[0]
dF['Age'] = np.where((dF['Age'] < 10) | (dF['Age'] > 60), mode_age, dF['Age'])
mode_income = dF['ParentIncome'].mode()[0]
dF['ParentIncome'] = np.where((dF['ParentIncome'] < 7300) | (
    dF['ParentIncome'] > 80630), mode_income, dF['ParentIncome'])
mode_iq = dF['IQ'].mode()[0]
dF['IQ'] = np.where((dF['IQ'] < 60) | (dF['IQ'] > 140), mode_iq, dF['IQ'])
mode_average_grade = dF['IQ'].mode()[0]
dF['AverageGrade'] = np.where((dF['AverageGrade'] < 0) | (
    dF['AverageGrade'] > 100), mode_average_grade, dF['AverageGrade'])
print("After removing noisy data", dF)
# Equal Depth and Smoothing by bin boundaries method
dF = dF.sort_values(by='IQ')
print(dF)
# bin_size = len(dF) // 4
# boundaries = [dF['IQ'].iloc[i * bin_size] for i in range(1, 4)]
# print(boundaries)
# dF['Bin'] = np.digitize(dF['IQ'], boundaries)
# print(dF)
# Sample data

# Define the bin boundaries
bin_boundaries = [79, 86, 100, 102, 105, 110,
                  120, 129]  # Define your desired boundaries

# Assign data points to bins based on bin boundaries
dF['Bin'] = pd.cut(dF['IQ'], bins=bin_boundaries,
                   labels=False, include_lowest=True)

# Calculate the bin mean for each bin
bin_means = dF.groupby('Bin')['IQ'].mean()

# Replace values in each bin with the bin mean
dF['IQ'] = dF['Bin'].map(bin_means)

# Drop the 'Bin' column (optional)
dF = dF.drop(columns=['Bin'])

# Print the smoothed DataFrame
print("After Smoothing", dF)
# Fixed k-Interval k=5 for Parent Income
vmin = dF['ParentIncome'].min()
vmax = dF['ParentIncome'].max()
k = 5
w = (vmax - vmin) / k
boundaries = []
boundaries.append(vmin)
for i in range(1, k):
    cut_point = vmin + i * w
    boundaries.append(cut_point)
boundaries.append(vmax)
interval_labels = ["Very Low", "Low", "Medium", "High", "Very High"]
dF['ParentIncome'] = pd.cut(
    dF['ParentIncome'], bins=boundaries, labels=interval_labels, include_lowest=True)
print("After fixed k Interval", dF)
# Define a dictionary for the concept hierarchy levels
country_to_continent = {
    'Panama': 'Center America',
    'El Salvador': 'Center America',
    'Canada': 'North America',
    'Greenland': 'North America',
    'Argentina': 'South America',
    'Brazil': 'South America'
}
dF['Region'] = dF['Region'].replace(country_to_continent)
print("After concept hierachy levels", dF)
dF.to_csv('preProcessedData.csv',index=False)
