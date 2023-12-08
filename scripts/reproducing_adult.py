# the purpose if this script is to implement a standard logistic regression model training on the reconstruced data to compare to the results reported in the paper
import utils
import os
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd 
from utils import run_regression

if not os.path.exists("results/"):
    os.mkdir("results/")

# The following will be converted to dumny variables for regression
columns=["age", "workclass", "fnlwgt", "education", "education-num",
          "marital-status", "occupation", "relationship", "race", "sex",
          "capital-gain", "capital-loss", "hours-per-week", "native-country",
          "income"]

train_path = "data/adult/adult.data"
test_path = "data/adult/adult.test"

train_df = pd.read_csv(train_path, names = columns)
test_df = pd.read_csv(test_path, names = columns)

full_df = pd.concat([train_df, test_df])

#calculate the training set size based on the original data
pct_train=len(train_df)/len(full_df)
print(f'Number if rows:{len(full_df)}')

# Convert predictor to binary value. Note that the test data contains "."
full_df['income'] = full_df['income'].replace(' <=50K', 0).replace(' >50K', 1)
full_df['income'] = full_df['income'].replace(' <=50K.', 0).replace(' >50K.', 1)

# Drop duplicate or unused columns
full_df.drop(['fnlwgt', 'education-num'] , axis=1, inplace=True)

# Remove rows with missing values
full_df.replace('?', np.nan, inplace=True)
full_df.dropna(inplace=True)
print(f'Number of rows after dropna : {len(full_df)}')

# Categorical variables that need to be converted to dummy/indicator variables.
dummy_cols = ['workclass', 'education', 'marital-status', 'occupation', 'relationship',
              'race', 'sex', 'native-country']

# Run the logistic regression for the full data
overall_accuracy = run_regression(full_df, pct_train, dummy_cols)

# Run the logistic regression for a subset of the data
black_data = full_df[full_df['race'] == ' Black']
print("len(black_data), ", len(black_data))
black_accuracy = run_regression(black_data, pct_train, dummy_cols)

# Run the logistic regression for a subset of the data
female_data = full_df[full_df['sex'] == ' Female']
print("len(female_data), ", len(female_data))
female_accuracy = run_regression(female_data, pct_train, dummy_cols)

# Report the accuracy of the three conditions.
print(f'Accuracy: {round(overall_accuracy, 3)}, '
      f'{round(black_accuracy, 3)}, '
      f'{round(female_accuracy, 3)}')

with open("results/uci_adult_results.txt", "w") as f:
    f.write(f'Accuracy: {round(overall_accuracy, 3)}, '
      f'{round(black_accuracy, 3)}, '
      f'{round(female_accuracy, 3)}')
    
