# Drawing Unix History

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

# Drawing Red-Black Tree as example
