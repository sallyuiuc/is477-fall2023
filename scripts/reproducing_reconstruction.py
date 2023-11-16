import pandas as pd
from utils import run_regression

# read the source data

reconstructed_data = pd.read_csv('./Data/folkables/adults_reconstruction.csv',sep=',',engine='python')


# The following will be converted to dumny variables for regression
dummy_cols=["workclass","fnlwgt","education","education-num","marital-status","occupation","relationship","race","sex","capital-gain","capital-loss","hours-per-week","native-country","income"]

# Make a copy of the dataframe and create an income threshold based on UCI Adult baseline
thresholded_data =reconstructed_data.copy()
thresholded_data.loc[thresholded_data['income']<= 50000,'income']=0
thresholded_data.loc[thresholded_data['income']> 50000,'income']=1
pct_train=0.3

accuracy=run_regression(thresholded_data,pct_train,dummy_cols)

# black instances
black_data= thresholded_data[thresholded_data['race']=='Black']
black_accuracy=run_regression(black_data,pct_train,dummy_cols)

female_data=thresholed_data[thresholded_dat['gender']=='Female']
female_accuracy=run_regression(female_data,pct_train,dummy_cols)
# report the accuracy of the three conditions
print(f'accuacry;{round(overall_accuracy,3)},'
      f'{round(black_accuracy,3)},'
      f'{round(female_accuracy,3)}')
    # Save the accuracy results to a file
with open('results/adult_reconstruction_results.txt','w') as result_file:
  result_file.write(f'Accuracy:{round(accuracy,3)},'
  f'{round(black_accuracy,3)},'
  f'{round(female_accuracy,3)}')

# Fit regression models and report accuracy at multiple income threshold levels
accuracy_df = pd.DataFrame(columns=['accuracy'])
for threshold in range(15000,85000,5000):
    thresholded_data=reconstructed_data.copy()
    thresholded_data.loc[thresholded_data['income']<= threshold,'income']=0
    thresholded_data.loc[thresholded_data['income']> threshold,'income']=1
    accuracy =run_regression(thresholded_data,pct_train,dummy_cols)
    accuracy_df.loc[threshold]=accuracy

    #plot accuracy v income threshold
    plt =accuracy_df.plot.line(xlim={10000,85000},ylim={0.65,1.00},xlabel='Income threshold',ylabel='Accuracy',legend=False)
    plt.figure.savefin('results/income_threshold.pdf')
    
