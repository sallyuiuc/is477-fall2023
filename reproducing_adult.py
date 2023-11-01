import utils
import os
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd 

from utils import run_regression

#Field names as specified in adult.names
colums=["age","workclass","fnlwgt","education","education-num","marital-status","occupation","relationship","race","sex","capital-gain","capital-loss","hours-per-week","native-country","income"]

#read the training and test data into their respective data frames
orig_train_data=pd.read_csv('data/adult/adult/adult.data',names=columns,sep=',',engine='python')
orig_train_data=pd.read_csv('data/adult/adult/adult.test',names=columns,sep=',',skiprows=1,engine='python')

full_data['income']=full_data['income'].replace('<=50k',0).replace('>50k',1)
full_data['income']=full_data['income'].replace('<=50k.',0).replace('>50k.',1)

#calculate the training set size based on the original data
pct_train=len(orig_train_da)/len(full_data)
print(f'Number if rows:{len(full_data)}')

#drop duplicate or unused columns
full_data.drop(['fnlwgt','education-num'],axis=1,inplace=True)


# run the logistic regression for a the full data
overall_accuracy= run_regression(full_data,pct_train,dummy_cols)

# run the logistic regression for a subset of the data
black_data=full_data[full_data['race']]=='Black'
black_accuracy=run_regression(black_data,pct_train,dummy_cols)

female_data=full_data[full_data['sex']=='Female']
female_accuracy=run_regression(female_data,pct_train,dummy_cols)

# report the accuracy of the three conditions

print(f'accuacry;{round(overall_accuracy,3)},'
      f'{round(black_accuracy,3)},'
      f'{round(female_accuracy,3)}')

# Save the accuracy results to a file
with open('results/uci_adult_results.txt','w') as result_file:
    for condition, accuracy in zip(conditions, accuracies):
        result_file.write(f'Condition: {condition}\nAccuracy: {accuracy}\n\n')
