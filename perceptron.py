import numpy as np
import torch

class Perceptron:
    """Class implementing a simple perceptron for binary classification
    """

    def __init__(self, epochs=480, learning_rate=0.01, seed=42):
        """Constructor for the Perceptron class.

        Args:
            epochs (int, optional): Number of iterations. Defaults to 480.
            learning_rate (float, optional): Learning Rate (lies between 0.0 and 1.0). Defaults to 0.01.
            seed (int, optional): Random seed used for reproducibility. Defaults to 42 ;)

        Returns:
            None: Returns None
        """
        self.epochs = epochs
        self.learning_rate = learning_rate
        self.seed = seed
        return None

    def fit(self, X, y):
        """Fits the data to the perceptron model.

        Args:
            X (array-like, shape = [num_datapoints, num_features]): Feature matrix.
            y (array-like, shape = [num_datapoints, 1]): Target values or labels.

        Returns:
            self: An object
        """
        return None

    def perceptronInput(self, X):
        """Calculates the value of the net input to be given to the perceptron for prediction.

        Args:
            X: The feature matrix from the data

        Returns:
            int: The net input that the perceptron receives before it predicts the class
        """
        return np.dot(X, self.W) + self.b

    def predict(self, X):
        """Predicts the output generated by the perceptron.

        Args:
            X (array-like, shape = [num_datapoints, num_features]): Feature matrix.

        Returns:
            label: The class or the label after one iteration of the perceptron
        """
        if self.perceptronInput(X) >= 0.0:
            return 1
        return 0
