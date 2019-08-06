#25장
# 25-A
#1번
from graphviz  import Digraph
engines=['dot','neato','fdp','sfdp','twopi','circo']

for engine in engines:
    g=Digraph('Drawing Unix History', engine=str(engine))

    g.attr('node', style='filled', color='goldenrod2', size='7.5')

    g.edge('7th Edition','32V')
    g.edge('7th Edition','V7M')
    g.edge('7th Edition','Xenix')
    g.edge('7th Edition','UniPlus+')
    g.edge('8th Edition','9th Edition')

    g.edge('1 BSD', '2 BSD')
    g.edge('2 BSD', '2.8 BSD')
    g.edge('2.8 BSD', 'Ultrix-11')
    g.edge('2.8 BSD', '2.9 BSD')
    g.edge('32V', '3 BSD')
    g.edge('3 BSD', '4 BSD')
    g.edge('4 BSD', '4.1 BSD')
    g.edge('4.1 BSD', '4.2 BSD')
    g.edge('4.1 BSD', '2.8 BSD')
    g.edge('4.1 BSD', '8th Edition')
    g.edge('4.2 BSD', '4.3 BSD')
    g.edge('4.2 BSD', 'Ultrix-32')


    g.render(filename='gviz/DUH.'+str(engine)+' engine', view=True)


# 25-A
# 2번
from graphviz  import Digraph
g= Digraph('Red-Black Tree', engine='dot')
g.attr('graph', ratio='0.5')
g.attr('node', style='filled', fillcolor='red', shape='circle', width='0.6', 
       fontname='Helvetica',fontsize='24', fontweight='bold',fontcolor='white', fixedsize='true')
g.node('8')
g.node('17')
g.node('22')
g.node('27')

g.attr('node', style='filled', fillcolor='black', shape='circle', width='0.6', 
       fontname='Helvetica',fontsize='24', fontweight='bold',fontcolor='white', fixedsize='true')
g.node('13')
g.node('1')
g.node('11')
g.node('15')
g.node('25')

g.attr('node', style='filled', fillcolor='black', shape='record', label="NIL", width='0.4', height='0.25', 
       fontname='Helvetica',fontsize='16', fontweight='bold',fontcolor='white')
g.node('n1')
g.node('n2')
g.node('n3')
g.node('n4')
g.node('n5')
g.node('n6')
g.node('n7')
g.node('n8')
g.node('n9')
g.node('n10')
g.node('n11')

g.attr('node', label=r"\N",style='filled', fillcolor='red', shape='circle', width='0.6', 
       fontname='Helvetica',fontsize='24', fontweight='bold',fontcolor='white', fixedsize='true')
g.node('6')

g.edges([('13','8'),('13','17')])
g.edges([('8','1'),('8','11'),('17','15'),('17','25')])
g.edges([('1','n1'),('1','6'),('11','n4'),('11','n5'),('15','n6'),('15','n7'),('25','22'),('25','27')])
g.edges([('6','n2'),('6','n3'),('22','n8'),('22','n9'),('27','n10'),('27','n11')])
       
g.render(filename="gviz/red-black tree", view=True)


#30장
#30-A
#(1)

import numpy as np
a=np.zeros(10)
print(a)


#(2)
a[4]=1
print(a)


#(3)
a=np.arange(10,50)
print(a)


#(4)
a=np.arange(0,25)
b=a.reshape(5,5)
print(b)

#(5)
a=np.eye(5)
print(a)


#(6)
np.random.seed(5)
a=np.random.random(size=(5,5))
b=a.min()
c=a.max()
print(a)
print(b)
print(c)


#(7)

a=np.ones((4,3))
b=np.random.random((3,2))
c=np.dot(a,b)
print(a)
print(b)
print(c)


#(8)
d=c.transpose()
print(d)


#(9)
a=np.arange(0,25).reshape(5,5)
b=np.arange(25,50).reshape(5,5)
c=a+b
d=a-b
print(a)
print(b)
print(c)
print(d)

#31장

import numpy as np
import pandas as pd
#31-A

exam_data = {'name':['Anastasia', 'Catherine', 'Cahill', 'James','Emily', 
             'Michael','Monica','Laura','Kevin','Jordan'],
            'score':[13,9.5,16.5, np.nan,11,20,17,np.nan, 8.5, 19],
            'attempts':[1,3,3,2,2,3,2,3,2,1],
            'quality':['yes','no','yes','no','no','yes','yes','no','no','yes']}
labels=['a','b','c','d','e','f','g','h','i','j']

df = pd.DataFrame(exam_data, index=labels)



#(1-1)
print(df[['name','score']])


#(1-2)
print(df.iloc[:3])


#(1-3)
print(df[['name','score']].iloc[[1,2,5,6]])


#(1-4)
print(df[(df['attempts']>2)])


#(2-1)
print(df[df['score'].isnull()])


#(2-2)
print(df[(df['attempts']<2) & (df['score']>15)])


#(2-3)
print(df['attempts'].sum())


#(2-4)
print(df['score'].mean())



#(3-1)
data={'name' : "Saya", 'score': 17.5, 'attempts': 2, 'qualify': "yes"}
df.loc['k']=data
print(df)


#(3-2)
df=df.drop('k',axis=0)
print(df)


#(3-3)
del df['attempts']
print(df)



#(3-4)
grouped=df.groupby('attempts')
print(grouped['score'].sum())


#(3-5)
exam2_data = {'name':['Anastasia', 'Catherine', 'Ronaldo', 'James','Messi', 
             'Michael','Monica','Laura','Klassen','Jonas'],
            'score2':[11,20,16.5, np.nan,10,15,20,np.nan,8,8]}
labels2=['a','b','c','d','e','f','g','h','i','j']

df2 = pd.DataFrame(exam2_data, index=labels2)
print(df2)
print(df)


df3=pd.merge(df, df2, left_index=True, right_index=True)
print(df3)




