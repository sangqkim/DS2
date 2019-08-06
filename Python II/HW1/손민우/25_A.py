from graphviz import Digraph

# 1
layout = ['dot', 'neato', 'fdp', 'sfdp', 'twopi', 'circo']

for engine in layout:
	A = Digraph(engine=engine)
	A.attr('node', color='goldenrod2', style='filled', size='7.5')
	A.edge('7th Edition', '32V')
	A.edge('7th Edition', 'V7M')
	A.edge('7th Edition', 'Xenix')
	A.edge('7th Edition', 'UniPlus+')
	A.edge('8th Edition', '9th Edition')
	A.edge('1 BSD', '2 BSD')
	A.edge('2 BSD', '2.8 BSD')
	A.edge('2.8 BSD', 'Ultrix-11')
	A.edge('2.8 BSD', '2.9 BSD')
	A.edge('32V', '3 BSD')
	A.edge('3 BSD', '4 BSD')
	A.edge('4 BSD', '4.1 BSD')
	A.edge('4.1 BSD', '4.2 BSD')
	A.edge('4.1 BSD', '2.8 BSD')
	A.edge('4.1 BSD', '8th Edition')
	A.edge('4.2 BSD', '4.3 BSD')
	A.edge('4.2 BSD', 'Ultrix-32')
	'''
	'''
	A.render('7th edition(' + str(engine) + '_engine)')

# 2
g = Digraph(comment='Red-Blak Tree', engine='dot')
g.attr('graph', ratio='.5')

g.attr('node', style='filled', color='black', shape='circle', width='.6', fontsize='24', fontcolor='white', fixedsize='true')
g.node('13')
g.node('1')
g.node('11')
g.node('15')
g.node('25')

g.attr('node', fillcolor='red', fixedsize='true')
g.node('8')
g.node('17')
g.node('6')
g.node('22')
g.node('27')

g.attr('node', fillcolor='black', shape='record', label='NIL', width='.4', height='.25', fontcolor='white', fontsize='10')
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

g.edges([('13', '8'), ('13', '17')])
g.edges([('8', '1'), ('8', '11'), ('17', '15'), ('17', '25')])
g.edges([('1', 'n1'), ('1', '6'), ('11', 'n4'), ('11', 'n5'), ('15', 'n6'), ('15', 'n7'), ('25', '22'), ('25', '27')])
g.edges([('6', 'n2'), ('6', 'n3'), ('22', 'n8'), ('22', 'n9'), ('27', 'n10'), ('27', 'n11')])
g.render('rbt', view=True)