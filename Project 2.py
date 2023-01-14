# EDA on Vehicle Insurance Customer Data
import pandas as pd
import numpy as np

# 1
customer_details = pd.read_csv('./customer_details.csv')
customer_policy = pd.read_csv('./customer_policy_details.csv')
customer_details.columns = ['customer_id', 'Gender', 'age', 'driving licence present',
                            'region code', 'previously insured', 'vehicle age', 'vehicle damage']
customer_policy.columns = ['customer_id',
                           'annual premium', 'sales channel code', 'vintage', 'response']


# 2
# 2 i)
print("Total null value of 'customer_id' is ",
      customer_details['customer_id'].isnull().sum())
# print("Total empty values in each column in customer_details :")
# print("Total null value of 'Gender' is ",
#       customer_details['Gender'].isnull().sum())
# print("Total null value of 'age' is ", customer_details['age'].isnull().sum())
# print("Total null value of 'driving licence present' is ",
#       customer_details['driving licence present'].isnull().sum())
# print("Total null value of 'region code' is ",
#       customer_details['region code'].isnull().sum())
# print("Total null value of 'previously insured' is ",
#       customer_details['previously insured'].isnull().sum())
# print("Total null value of 'vehicle age' is ",
#       customer_details['vehicle age'].isnull().sum())
# print("Total null value of 'vehicle damage' is ",
#       customer_details['vehicle damage'].isnull().sum())
#
# print("Total empty values in each column in customer_policy :")
print("Total null value of 'customer_id' is ",
      customer_policy['customer_id'].isnull().sum())
# print("Total null value of 'annual premium (in Rs)' is ",
#       customer_policy['annual premium (in Rs)'].isnull().sum())
# print("Total null value of 'sales channel code' is ",
#       customer_policy['sales channel code'].isnull().sum())
# print("Total null value of 'vintage' is ",
#       customer_policy['vintage'].isnull().sum())
# print("Total null value of 'response' is ",
#       customer_policy['response'].isnull().sum())

# 2 i)
print("Droped null values of customer_id is :",
      customer_details['customer_id'].count(), customer_policy['customer_id'].count())

print("Replace all null values for numeric columns by mean is :",
      customer_details.mean(), customer_policy.mean())

print("Replace all null values for categorical value by mode is :",
      customer_details.mode(), customer_policy.mode())

# 2 ii)
Q1 = np.percentile(customer_details['age'], 25)
Q3 = np.percentile(customer_details['age'], 75)
IQR = Q3 - Q1
print("Outliers is :", Q1 - 1.51 * IQR)

# 2 iii) There is only strip in string so
print("Whitespace for gender is :", customer_details['Gender'].str.strip())

# 2 iv) Only for string
print("Case correction to all gender to convert as title :",
      customer_details['Gender'].str.title())

# 2 v)
print(pd.get_dummies(customer_details))
print(pd.get_dummies(customer_policy))

# 2 vi)
print("Drop Duplicates for both file is :",
      customer_details.drop_duplicates(), customer_policy.drop_duplicates())

# 3
merge = pd.merge(customer_details, customer_policy, on='customer_id')
print("Master table is :", merge)

# 4
# i)
print("Gender wise average annual premium is :",
      merge.groupby(['Gender']).mean()['annual premium'])

# ii)
print("age wise average annual premium is :",
      merge.groupby(['age']).mean()['annual premium'])

# iii)
print(merge.groupby(['Gender']).count())

# iv)
print("vehicle age wise average annual premium is :",
      merge.groupby(['vehicle age']).mean()['annual premium'])

# 5)
print("Correlation coefficient is :", merge['age'].corr(
    merge['annual premium']), "So its is 'There is No Relationship'")

# Rough Work
# print(customer_details['customer_id'].dropna(),
#       customer_details['customer_id'].count())
# print(customer_details['customer_id'].count())

# print(customer_details.isnull().sum())
# print(customer_details.isnull().sum())
# print(customer_policy.isnull().sum())
# print(customer_details['customer_id'].fillna())
# print(customer_details)
# print(customer_policy)
# print(customer_policy)
