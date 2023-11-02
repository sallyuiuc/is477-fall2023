import utils
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np
import matplotlib.pyplot as plt

# Save the accuracy results to a file
with open('results/adult_reconstruction_results.txt', 'w') as result_file:
    for condition, accuracy in zip(conditions, accuracies):
        result_file.write(f'Condition: {condition}\nAccuracy: {accuracy}\n\n')

# Save the plot to a PDF file
plt.savefig('results/income_threshold.pdf')

