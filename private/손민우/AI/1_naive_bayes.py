#!/usr/bin/env python
# coding: utf-8

# # Naive bayes

# Install requirments

# In[1]:



# Import dependencies

# In[4]:


import pandas as pd
import numpy as np
from scipy.stats import norm, bernoulli


# In[21]:


def read_dataset():
    def _read_dataset(data):
        np_data = data.values.astype(np.float32)
        X = np_data[:, 1:]
        Y = np_data[:, :1]
        return (X, Y)
    train_data = pd.read_csv('https://raw.githubusercontent.com/bckim92/ds2_practice/master/naive_bayes/train_data.csv').drop('Fare', axis=1)
    class_names = list(train_data.columns)[1:]
    train_data = _read_dataset(train_data)
    test_data = pd.read_csv('https://raw.githubusercontent.com/bckim92/ds2_practice/master/naive_bayes/test_data.csv').drop('Fare', axis=1)
    test_data = _read_dataset(test_data)
    return train_data, test_data, class_names

def compute_accuracy(predictions, answers):
    assert len(predictions) == len(answers),         "Num predictions %d and num answers %d does not match" % (len(predictions), len(answers))

    num_correct = 0
    for prediction, answer in zip(predictions, answers):
        if prediction == answer:
            num_correct += 1
    return float(num_correct) / len(predictions)


# Now let's look into data

# In[22]:





# In[23]:


class NaiveBayesClassifier(object):
    def __init__(self, num_classes=2):
        self._num_classes = num_classes
        self._feature_prob_functions = {}
        self._class_prior = []

    def fit(self, train_X, train_Y, is_continuous):
        for class_id in range(self._num_classes):
            class_indices = np.where(train_Y == float(class_id))[0]
            class_features = np.take(train_X, class_indices, axis=0)
            class_means = np.mean(class_features, axis=0)
            class_stds = np.std(class_features, axis=0)
            class_prior = np.log(float(len(class_indices)) / len(train_Y))

            feature_prob_functions = []
            for idx, continuous in enumerate(is_continuous):
                if continuous:
                    prob_function = norm(class_means[idx], class_stds[idx]).pdf # Probability density function
                else:
                    prob_function = bernoulli(class_means[idx]).pmf # Probability mass function
                feature_prob_functions.append(prob_function)
            self._feature_prob_functions[class_id] = feature_prob_functions
            self._class_prior.append(class_prior)

    def predict(self, test_X, use_variable):
        predictions = []
        for test_x in test_X:
            output_prob = []
            for class_id in range(self._num_classes):
                cum_prob = self._class_prior[class_id]             
                for using, x, prob_function in zip(use_variable, test_x, 
                                                   self._feature_prob_functions[class_id]):
                    if using:
                        cum_prob += np.log(prob_function(x))
                output_prob.append(cum_prob)
            prediction = np.argmax(output_prob)
            predictions.append(prediction)
        return predictions
      
def run_naive_bayes(train_data, test_data, is_continuous, use_variable):
    train_X, train_Y = train_data
    test_X, test_Y = test_data

    nb_classifier = NaiveBayesClassifier()
    nb_classifier.fit(train_X, train_Y, is_continuous)
    pred_Y = nb_classifier.predict(test_X, use_variable)
    accuracy = compute_accuracy(pred_Y, test_Y)

    return accuracy


# Run code!

# In[25]:
if __name__ == '__main__':
    train_data, test_data, class_names = read_dataset()
    print(class_names)
    is_continuous = [True] * 1 + [False] * 8 + [True] * 2
    use_variable = [True] * 11
    accuracy = run_naive_bayes(train_data, test_data, is_continuous, use_variable)
    print("Accuracy : {}".format(accuracy))


# In[ ]:




