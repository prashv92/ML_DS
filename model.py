import pandas as pd
from sklearn.model_selection import train_test_split

class Model():
    
    def __init__(data):
        self.data = data
        
    @abstractmethod
    def transform_data():
        return 0
    
    @abstractmethod
    def fit_model():
        return 0
    
    def split_training(percent, y):
        x_train, x_test, y_train, y_test  = train_test_split(
            self.data[seld.data.columns.difference([y])], trainData.y,test_size=percent, random_state=42)
        
        return x_train, x_test, y_train, y_test
        