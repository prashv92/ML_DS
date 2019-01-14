from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from model import Model

class RandomForestModel(Model):
    
    classify = True
    model = None
    X = None
    y = None
    
    def __init__(self, data, classify):
        self.data = data
        self.classify = classify
        #super().__init__()
        
              
    def transform_data(self):
        for c in self.data.columns:
            if self.data[c].dtype == 'object':
                lbl = LabelEncoder()
                lbl.fit(list(self.data[c].values))
                trainData[c] = lbl.transform(list(self.data[c].values))
    
    def fit_model(self):
        if self.classify:
                print(self.classify)
                self.model = RandomForestClassifier()
        else:
            self.model = RandomForestRegressor()
            
        #x_train, x_test, y_train, y_test = self.split_data(self.data, 0.3)
        if None != self.model:
            self.model.fit(self.x_train, self.y_train)
        else:
            print('Model uninstantiated. Please check model')
        
        return self.model
    
    def split_data(self,y,percent):
        self.x_train, self.x_test, self.y_train, self.y_test  = train_test_split(
            self.data[self.data.columns.difference([str(y)])], self.data[str(y)],test_size=percent, random_state=42)
            
    