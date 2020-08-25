import pandas as pd
from numpy import * 
from sklearn.preprocessing import StandardScaler

dados  = pd.read_csv('AppleStore.csv')
atributos_previsores = dados.iloc[:,6:10]
atributo_meta = dados.iloc[:,2]



onehots = pd.get_dummies(data=atributos_previsores,columns=['rating_count_tot','rating_count_ver','user_rating','user_rating_ver'])
atributos_previsores = onehots.values 

scaler = StandardScaler()
atributos_previsores_transformed = scaler.fit_transform(atributos_previsores)