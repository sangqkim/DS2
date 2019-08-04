import graphviz as gv

ps = gv.Digraph(name= 'pet-shop', node_attr={'shape': 'planetext'})

ps.node('parrot')
ps.node('dead')
ps.edge('parrot', 'dead')
ps.graph_attr['rankdir'] = 'LR'
ps.edge_attr.update(arrowhead='vee', arrowsize='2')
ps.render('test_out\pet-shop', view = True)