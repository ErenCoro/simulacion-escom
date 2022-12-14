from mpb22.eda.base import DatasetSummary
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



class TabularDatasetSummary(DatasetSummary):
    def __init__(self, filepath, features = None, labels = None):
        self.filepath = filepath
        self.features = features 
        self.labels = labels


        if not os.path.exists(filepath):
             raise TypeError

        self.df = pd.read_csv(self.filepath)


    def list_features(self):
        features = self.features
        labels = self.labels

        if (features == None):
            features_name = self.df.columns
            features_name = set(features_name)
            if (labels == None):
                pass
            else: 
                for i in labels:
                    features_name.remove(i)
        else: 
            features_name = set(features)   
        return features_name
        
        


    def list_labels(self):
        label = self.labels
        if (label == None):
            list_labels = set()
        else:
            list_labels = set(label)   
        return list_labels



    def count_categorical(self):
        features = self.list_features()
        #labels = self.list_labels()
        #total = features.copy()
        #total.update(labels)


        df = self.df.drop(columns=[col for col in self.df if col not in features])
        categorical_data = df.select_dtypes(exclude=[np.number])
        count_categorical = categorical_data.shape[1]
        return count_categorical



    def count_numerical(self):
        features = self.list_features()
        #labels = self.list_labels()
        #total = features.copy()
        #total.update(labels)


        df = self.df.drop(columns=[col for col in self.df if col not in features])
        numeric_data = df.select_dtypes(include=[np.number])
        count_numeric = numeric_data.shape[1]
        return count_numeric



    def statistics(self):
        values = {}

##################################   FEATURES 
        df_features = self.df

        if self.features == None:
            features_name = list(df_features.columns)

            #quitar etiquetas de las caracteristicas       
            if self.labels == None:
                pass
            else: 
                for i in self.labels:
                    features_name.remove(i)

        else:
            features_name = self.features 

   
        feature =  df_features[features_name]

########################################

        ## caracteristicas 
        for i,j  in zip(feature, feature.dtypes):
            if(pd.api.types.is_numeric_dtype(j) == True):
                tipo = 'numerical'
                mean = feature[i].mean()
                mode = feature[i].mode()
                median = feature[i].median()
                std =  feature[i].std()
                n_null = feature[i].isnull().sum()
                n_total = feature[i].count()
            else: 
                tipo = 'categorical'
                mean = None
                mode = feature[i].mode()
                median = None
                std = None 
                n_null = feature[i].isnull().sum()
                n_total = feature[i].count()

            values[i] ={'type': tipo, 'mean': mean,  'mode': mode[0], 'median': median,  'std':std,  'n_null': n_null,  'n_total': n_total + n_null}
        return values 


    def histogram(self, feature, bins = 10):
        if(pd.api.types.is_numeric_dtype(self.df[feature].dtypes) ==False):
            data = self.df[feature].values.tolist()
            dictionary = {x:data.count(x) for x in data}
            keys, values = dictionary.keys(), dictionary.values()
            return list(keys), list(values)


        else:
            data = self.df[feature].values.tolist()
            counts,bins, bars = plt.hist(data, bins ) 
            bines = bins[1:].tolist()
            count = counts.tolist()
            return bines, count
