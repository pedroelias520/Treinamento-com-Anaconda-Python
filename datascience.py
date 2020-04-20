import pandas as pd 
data = { 
    'Alunos' :['Caio','George','Elias','Sousa','Andersson','Alucard','Dracula','Doom Guy','Simon Belmonth','Ryu','Ken'],
    'Idade' :[15,15,19,18,37,999,999,38,27,26,25],
    'Notas' : [8.0,9.0,7.0,8.0,8.0,10.0,10.0,9.5,5.5,6.6,8.7]        
}

df = pd.DataFrame(data,columns=['Alunos','Idade','Notas'])
df.describe()
df=df.drop([0,1])
print(df.drop('Idade',axis=1))



