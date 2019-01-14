from abc import ABC, abstractmethod
import pandas as pd
from sklearn.model_selection import train_test_split

class Model(ABC):
    
    data = None
    
    def __init__(self, data):
        self.data = data
        super().__init__()
        
    @abstractmethod
    def transform_data(self):
        return 0
    
    @abstractmethod
    def fit_model(self, y):
        return 0