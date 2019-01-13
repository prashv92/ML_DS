import pandas as pd

class Model():
    
    def __init__(data):
        self.data = data
        
    @abstractmethod
    def transform_data():
        return 0
    
    @abstractmethod
    def fit_model():
        return 0
        