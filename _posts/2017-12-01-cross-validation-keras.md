---
layout: post
title: "Cross Validation on Keras"
description: "script to implement cross-validation on Keras model"
category: machine-learning
---

This script will help you iplement cross-validation on Keras model.

* * *


Load dataset:

```
(X_train, y_train), (X_test, y_test) = mnist.load_data()
```

Structure to apply Cross Validation:

```
from sklearn.cross_validation import StratifiedKFold

def load_data():
    # load your data using this function

def create model():
    # create your model using this function

def train_and_evaluate__model(model, data[train], labels[train], data[test], labels[test)):
    model.fit...
    # fit and evaluate here.

if __name__ == "__main__":
    n_folds = 10
    data, labels, header_info = load_data()
    skf = StratifiedKFold(labels, n_folds=n_folds, shuffle=True)

    for i, (train, test) in enumerate(skf):
            print "Running Fold", i+1, "/", n_folds
            model = None # Clearing the NN.
            model = create_model()
            train_and_evaluate_model(model, data[train], labels[train], data[test], labels[test))
```

* * *


Resource: 
- <a href="https://github.com/fchollet/keras/issues/1711">https://github.com/fchollet/keras/issues/1711</a>