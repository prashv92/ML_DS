import numpy as np
import pandas as pd
from sklearn import linear_model

class LinearRegression(Model):
    
    def __init__(self, data):
        self.data = data
        #super().__init__()
    
    def cost_function(X,Y,B):
        m = len(Y)
        J = np.sum((Y - X.dot(B))**2)/(2*m)
        return J
    
    def gradient_descent(X, Y, B, alpha, numIterations):
        costJ = cost_function(X,Y,B)
        costMatrix = list().append(costJ)
        m = len(Y)
        
        for i in range(numIterations):
            
            B = B - alpha*(X.T.dot(Y-X.dot(B)))/m
            costJ = cost_function(X,Y,B)
            costMatrix.append(costJ)
            
        return B
                           
                           
    def rmse(Y, PredY):
        return np.sqrt((sum(Y-PredY)**2)/len(Y))
        
        
    def rSquared(Y, PredY):
        yBar = np.mean(Y)
        sumSqTotal = sum((Y-yBar)**2)
        sumSqResidual = sum((Y-PredY)**2)
        return 1 - (sumSqResidual/sumSqTotal)
    
    
    def transform_data(self):
        for c in self.data.columns:
            if self.data[c].dtype == 'object':
                lbl = LabelEncoder()
                lbl.fit(list(self.data[c].values))
                trainData[c] = lbl.transform(list(self.data[c].values))
    
    #TODO: Update function to be similar to other models.
    def fit_model(self):
        self.model = linear_model.LinearRegression()
        
        self.model.fit(X,Y)
        
        return self.model
    
    def split_data(self,y,percent):
        self.x_train, self.x_test, self.y_train, self.y_test  = train_test_split(
            self.data[self.data.columns.difference([str(y)])], self.data[str(y)],test_size=percent, random_state=42)
        