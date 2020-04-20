import pandas as pd 
data = { 
    'Alunos' :['Caio','George'],
    'Idade' :[15,15],
    'Notas' : [8,9]        
}

df = pd.DataFrame(data,columns=['Alunos','Idade','Notas'])


