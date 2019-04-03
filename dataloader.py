import sys
sys.path.append('..')
from autograd import Variable, Matrix

class DataLoader:

    def __init__(self, X: Matrix, y: Matrix=None):
        """
        :param X: The examples to iterate through.
        :param y: The outputs of the examples to iterate through. If None, then 
            this DataLoader is used for test data, and y_batch will not be returned in the  iterable.
        """
        self.X = X
        self.y = y
        if y is not None and len(X) != len(y):
            print('The lengths of X and y passed into DataLoader do not agree.')
            raise ValueError

    def __iter__(self):
        for i in range(len(self.X)):
            yield Matrix([self.X[i]]), Matrix([self.y[i]])

    def __len__(self):
        return len(self.X)
