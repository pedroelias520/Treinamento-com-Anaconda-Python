import pandas as pd
from numpy import * 
from sklearn import LabelEncoder

dados  = pd.read_csv('AppleStore.csv')
atributos_previsores = dados.iloc[:,0:14]
atributo_meta = dados.iloc[:,14]

onehots