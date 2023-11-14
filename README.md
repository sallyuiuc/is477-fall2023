IS477 Reproduction of UCI Adult DATABASE

Overview

This is assignment 1 for the IS477 course Data Management Curation and Reproducibility. To make sure the study results are correct, the project will use a normal logistic regression model on two sets of data: the original UCI Adult dataset and the rebuilt version of the dataset that is shown in the paper. The project wants to see how fair and accurate machine learning models are when it is making predictions about people from different groups. For machine learning and data processing, we will use Python 3.0 to run the dataset. This repository serves to reproduce specific results from the paper"Retiring Adult: New Dataset for Fair Machine Learning." For version control and code management, we will use Git and Github desktop applications. Results include the model's performance measures, datasets that have been cleaned and preprocessed,well-documented code, and a detailed README that can be used again and again.

Data Availability
Origin of Datasets
1.UCI Adult Dataset: This dataset was obtained from the UCI Machine Learning Repository. Becker, Barry and Kohavi, Ronny(1996). Adult. UCI Machine Learning Repository
https://archive.ics.uci.edu/static/public/2/adult.zip 

2. Reconstructed Dataset: This dataset was derived from IPUMS CPS data the dataset is part of the Folktables repository
https://raw.githubusercontent.com/socialfoundations/folktables/main /adult_reconstruction.csv

Copyright and Licensing

UCI Adult Dataset The dataset is generally available for public use for educational and research purposes.This dataset is licensed under a Creative Commons Attribution 4.0 International CCBY 4.0 license.
Reconstructed Dataset The data itself is governed by the terms of use provided by the Census Bureau. The data are intended for replication purposes only. Individuals analyzing the data for other purposes must submit a separate data extract request directly via IPUMS CPS. Individuals are not to redistribute the data without permission.

Justification for Inclusion/exclusion of Datasets
Including the reconstructed dataset directly in this repository because this dataset are only intended for replication purpose due to copyright considerations


Software License

This project is licensed under the MIT License. The dataset and results are giving back to the open-source community and let people use the software for free. The License is Permissive. The MIT License is easy to understand and lets anyone use,change,and share the program. For its Compatibility,a lot of other agreements work with the MIT license which makes it easier to work with other open-source projects. It does not have Strong Copyleft if user make some changes to something using the MIT License,you don't have to share it under the same license.This is different from licenses that have strict copyleft rules. This gives us more options for how to use and improve it in the future.It is widedly used the MIT license is a well-known license in the open-source world and it gives people the examples and considerations for the rules will be clear and followed.


Data License

The data and models in this repository are licensed uder the Creative Commons Attribution 4.0 International license CCBY4.0. By using the CCBY 4.0 license it is easier for people to share data that can be used upon while still making sure that the original makers get credit.
With the attribution the license says that people who use your data and models must give you credit,link back to the license, and say if they made any changes. This makes sure that people who contributed are properly credited. MIT license for our software. It lets both academic and business users use, change, and share the licensed data. The license can be used anywhere in the world,even if your country doesn’t have copyright rules that protect it. 

Reproducing
Here are instructions for you to set up your environment and run the script

1.Information about the environment:Product Name: macOS ProductVersion: 13.2.1 BuildVersion:22D68
2.Installing the Dependencies
install the following required python package:pip install certifi==2023.7.22 charset-normalizer==3.3.0 idna==3.4 requests==2.31.0 urllib3 ==2.0.4
3.Running Script Running Script for assignment 2
Execute your script: python prepare_data.py
Running Script for assignment 3:
Run first: python scripts/reproducing _adult.py to get accuracy in uci_adult_results.txt(results directory)
Run next: python scripts/reproduce_reconstructed.py to get accuracy in adult_reconstruction_results.txt and income threshold figure in income_threshold.pdf(results directory)

To return the data preparation script:
clone this repository
if you have docker installed run the following:
docker run–rm -v${PWD}:/IS477 username/is477-fall2023 python prepare_data.py

Prerequisites
Ensure you have Python 3.x installed on your machine.If you decide to use Docker Install Docker Desktop on your machine.Create a Docker Hub account if you dont already have one.

Analysis

a. Do the regression results match those reported in the original paper for the UCI Adult data?

To compare the results of your reproduction with the original paper, you should provide a summary of the accuracy results obtained from running reproducing_adult.py. You can analyze and compare the accuracy metrics you obtained with those reported in the original paper. Mention any significant discrepancies, if present, and discuss possible reasons for the differences.

b. Do the regression results using the reconstructed data with the default threshold match the results of the regression using the original UCI Adult data?

In this section, summarize the results obtained from running reproducing_reconstruction.py with the default threshold. Compare these results to those obtained from running reproducing_adult.py (original UCI Adult data). Analyze whether the accuracy results with the reconstructed data match those of the original UCI Adult data. Discuss any similarities or differences you observe.
