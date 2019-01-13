from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import Model

class RandomForestModel(Model):
    
    classify = False
    model = None
    X = None
    y = None
    
    def __init__(data, classify):
        self.data = data
        self.classfiy = classify
        super.__init__(data)
        
    
    def transform_data():
        for c in self.data.columns:
            if self.data[c].dtype == 'object':
                lbl = LabelEncoder()
                lbl.fit(list(self.data[c].values))
                trainData[c] = lbl.transform(list(self.data[c].values))
    
    def fit_data():
        if self.classify:
                model = RandomForestClassifier()
        else:
            model = RandomForestRegressor()
            
        if self.model:
            model.fit(self.data)
        else:
            print('Model uninstantiated. Please check model')
        
        return model
    
    