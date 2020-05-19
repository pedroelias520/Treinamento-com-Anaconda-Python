import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np

#Plot Graphic
plt.xlabel('xlabel') ;
plt.ylabel('ylabel') ;
plt.plot([13,14,15,16,17,18],[1.081550,1.080690,1.080920,1.081430,1.081730,1.082160] ,label= 'Seven',color='#b3e400')
plt.plot([13,14,15,16,17,18],[1.081550,1.080690,1.081040,1.081430,1.081730,1.082070] ,label= 'EUR/USD',color="red")
plt.legend()
plt.title('Teste de prévia dia 15/05/2020 13:00 - 17:00 - H1')
plt.show()

#Bar Graphic
x=[1,2,3,4]
y=[2,5,8,12]
plt.bar(x,y,color='red')
plt.show()

#Scatter Graphic
x=[1,2,3,4]
y=[5,2,5,12]
plt.scatter(x,y)
plt.show()

#Pie Graphics
label = ['floresta','deserto']
dados=[10,120]
fig,ax = plt.subplots()
ax.pie(dados,labels=label,autopct='%1.1f%%')
plt.show()

#3d Graphic
fig = plt.figure()
ax = fig.gca(projection='3d')
x,y,z = axes3d.get_test_data(0.01)
#graf = ax.contourf(x,y,z)
graf = ax.plot_wireframe(x,y,z)
plt.show()


