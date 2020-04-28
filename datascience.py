import pandas as pd 
data = { 
    'Alunos' :['Caio','George','Elias','Sousa','Andersson','Alucard','Dracula','Doom Guy','Simon Belmonth','Ryu','Ken'],
    'Idade' :[15,15,19,18,37,999,999,38,27,26,25],
    'Notas' : [8.0,9.0,7.0,8.0,8.0,10.0,10.0,9.5,5.5,6.6,8.7]        
}
#Adding a DataFrame(to Analyse)
df = pd.DataFrame(data,columns=['Alunos','Idade','Notas'])

#Describing DataFrame
df.describe()

#Droping any elements of DataFrame
df=df.drop([0,1])
print(df.drop('Idade',axis=1))


#Showing how many items in all columns
df.count()
# Alunos  9 
# Notas   9 
# Idade   9 


#Showing Columns of the DataFrame
df.columns
#Index(['Alunos', 'Idade', 'Notas'], dtype='object')

# Showing (Columns,Lines)
df.shape
#(9, 3)

#Showing max values of the specific columns 
df['Idade'].max()
df['Notas'].max()
df['Alunos'].max()
#Showing max values of all columns 
df.max()
# Alunos    Sousa
# Idade       999
# Notas        10

#Showing min values of the specific columns 
df['Idade'].min()
df['Notas'].min()
df['Alunos'].min()
#Showing min values of all columns 
df.min()
# Alunos    Alucard
# Idade          18
# Notas         5.5

#Showing the mean of the columns 
df.mean()
# Idade : 243.11
# Notas : 8.1444
# Not Show of String columns(It's automatic)

#Showing the median of all columns
df.median()
# Idade : 27.0
# Notas : 8.0 
# Not show of the string columns(It's automatic) 

#Showing the sum of elements of the columns
df.sum()
#Showing sum of values of the specific columns 
df['Idade'].sum() # Idade 2188
df['Notas'].sum() # Notas 73.3
df['Alunos'].sum() # Alunos 'EliasSousaAnderssonAlucardDraculaDoom GuySimon BelmonthRyuKen'

#incrementing 10 in all elements of columns : Idade and Notas 
df['Idade'].add(10)
df['Notas'].add(10)
#Not add in string columns

#decrementing 10 in all elements of columns : Idade and Notas 
df['Notas'].sub(10)
df['Idade'].sub(10)
#Not add in string columns

#multiplying by 10 all elements of columns : Idade and Notas 
df['Idade'].mul(10)
df['Notas'].mul(10)
#Not add in string columns

#Dividing by 10 all elements of columns : Idade and Notas 
df['Idade'].div(10)
df['Notas'].div(10)
#Not add in string columns

#function loc to localization of items in the Dataframe
print(df.loc[df['Idade'] > 12.0])


