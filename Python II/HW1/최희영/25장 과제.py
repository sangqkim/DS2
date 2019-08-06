
# 1번 과제

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


# 2번 과제


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
