#25-A. Drawing Unix History
import graphviz as gv
engines = ['dot', 'neato', 'fdp', 'sfdp', 'twopi', 'circo']
for engine in engines:
    dot = gv.Digraph(engine=engine)
    dot.attr('node', style='filled', color='goldenrod2', width='0.75')
    dot.edges([('7th Edition', '32V'), ('7th Edition', 'V7M'), ('7th Edition', 'Xenix'), ('7th Edition', 'UniPlus+')])
    dot.edge('8th Edition', '9th Edition')
    dot.edge('1 BSD', '2 BSD')
    dot.edge('2 BSD', '2.8 BSD')
    dot.edges([('2.8 BSD', 'Ultrix-11'), ('2.8 BSD', '2.9 BSD')])
    dot.edge('32V', '3 BSD')
    dot.edge('3 BSD', '4 BSD')
    dot.edge('4 BSD', '4.1 BSD')
    dot.edges([('4.1 BSD', '4.2 BSD'), ('4.1 BSD', '2.8 BSD'), ('4.1 BSD', '8th Edition')])
    dot.edges([('4.2 BSD', '4.3 BSD'), ('4.2 BSD', 'Ultrix-32')])
    dot.render('./25_A_1_engine_'+engine, view=True)

# 25-A-2. Draw Red-Black Tree as shown below
import graphviz as gv
dot = gv.Digraph(engine='dot')
# black dot with label
dot.attr('node', style='filled', color='black', fontcolor='white')
for label in ['13', '1', '11', '15', '25']:
    dot.node(label)
# NILs
dot.attr('node', shape='rectangle')
for nil_id in ['1-1', '6-1', '6-2', '11-1', '11-2', '15-1', '15-2', '22-1', '22-2', '27-1', '27-2']:
    dot.node(nil_id, label='NIL')
# red dot
dot.attr('node', color='red', shape='circle')
for label in ['8', '17', '6', '22', '27']:
    dot.node(label)
# connections
dot.edges([('13', '8'), ('13', '17')])
dot.edges([('8', '1'), ('8', '11'), ('17', '15'), ('17', '25')])
dot.edges([('1', '1-1'), ('1', '6'), ('11', '11-1'), ('11', '11-2'), ('15', '15-1'), ('15', '15-2'), ('25', '22'), ('25', '27')])
dot.edges([('6', '6-1'), ('6', '6-2'), ('22', '22-1'), ('22', '22-2'), ('27', '27-1'), ('27', '27-2')])
dot.render('./25_A_2', view=True)
               
