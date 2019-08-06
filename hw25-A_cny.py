# 25-A-1 : Drawing Unix History

from graphviz import Digraph
engines = ['dot', 'neato', 'fdp', 'sfdp', 'twopi', 'circo']
for engine in engines:
    g = Digraph('G', engine=engine)
    g.node_attr.update(style='filled', color='goldenrod2', width='0.75')
    g.edges([('7th Edition', '32V'),('7th Edition', 'V7M'),('7th Edition', 'Xenix'),('7th Edition', 'UniPlus+')])
    g.edges([('8th Edition', '9th Edition')])
    g.edges([('1 BSD','2 BSD'),('2 BSD','2.8 BSD'), ('2.8 BSD','Ultrix-11'), ('2.8 BSD','2.9 BSD')])
    g.edges([('32V','3 BSD'),('3 BSD', '4 BSD'), ('4 BSD','4.1 BSD'), ('4.1 BSD','4.2 BSD'), ('4.1 BSD','2.8 BSD'), ('4.1 BSD', '8th Edition')])
    g.edges([('4.2 BSD','4.3 BSD'), ('4.2 BSD','Ultrix-32')])
    g.render('./25_A_1_'+engine, view=True)

# 25-A-2 : Drawing Red-Black Tree as example

from graphviz import Digraph
g = Digraph('Red-Black Tree', engine = 'dot')
g.attr('graph', ration='0.8')

#NIL 
g.attr('node', style='filled', fillcolor='black', fontcolor='white', shape='record', width='0.4', label='NIL', height='0.25')
nil_nodes = ['1L', '6L', '6R', '11L', '11R', '15L', '15R', '22L', '22R', '27L', '27R']
for node in nil_nodes:
    g.node( node, label='NIL')

#Black Dot
g.attr('node', style='filled', fillcolor='black', fontcolor='white', shape='circle', width='0.6')
black_nodes = ['13', '1', '11', '15', '25']
for node in black_nodes:
    g.node( node, label=node)

#Red Dot
g.attr('node', style='filled', fillcolor='red', fontcolor='white', shape='circle', width='0.6')
red_nodes = ['8','17','6','22','27']
for node in red_nodes:
    g.node( node, label=node)

#edges
g.edges([('13',  '8'), ( '13', '17'), 
         ( '8',  '1'), (  '8', '11'),
         ('17', '15'), ( '17', '25'),
         ( '1', '1L'), (  '1',  '6'),
         ( '6', '6L'), (  '6', '6R'),
         ('11','11L'), ( '11','11R'),
         ('15','15L'), ( '15','15R'),
         ('25', '22'), ( '25', '27'),
         ('22','22L'), ( '22','22R'),
         ('27','27L'), ( '27','27R')])

g.render('./25_A_2_Red-Black_Tree', view=True)
