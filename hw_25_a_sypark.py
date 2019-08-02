#(1) Drawing unix history

from graphviz import Digraph

Lay_en = ['dot', 'neato', 'fdp', 'sfdp', 'twopi', 'circo']
for lay in Lay_en :
    UH = Digraph('Drawing Unix History', filename='DUH.gv', engine = lay)
    UH.attr('node', color = 'goldenrod2', style = 'filled', size= '7.5')

    UH.node('7th Edition')
    UH.node('32V')
    UH.node('V7M')
    UH.node('Xenix')
    UH.node('Uniplus+')
    UH.edge('7th Edition','32V')
    UH.edge('7th Edition','V7M')
    UH.edge('7th Edition','Xenix')
    UH.edge('7th Edition','Uniplus+')
    UH.node('8th Edition')
    UH.node('9th Edition')
    UH.edge('8th Edition','9th Edition')


    UH.node('2 BSD')
    UH.node('2.8 BSD')
    UH.node('Ultrix-11')
    UH.node('2.9 BSD')
    UH.edge('1 BSD', '2 BSD')
    UH.edge('2 BSD', '2.8 BSD')
    UH.edge('2.8 BSD', 'Ultrix-11')
    UH.edge('2.8 BSD', '2.9 BSD')

    UH.node('3 BSD')
    UH.edge('32V', '3 BSD')
    UH.node('4 BSD')
    UH.edge('3 BSD', '4 BSD')
    UH.node('4.1 BSD')
    UH.edge('4 BSD', '4.1 BSD')
    UH.node('4.2 BSD')
    UH.edge('4.1 BSD', '4.2 BSD')
    UH.edge('4.1 BSD', '2.8 BSD')
    UH.edge('4.1 BSD', '8th Edition')
    UH.node('4.3 BSD')
    UH.edge('4.2 BSD', '4.3 BSD')
    UH.edge('4.2 BSD', 'Ultrix-32')

    UH.render('uh_'+lay, view=True)
    
#'dot' layout engine이 제일 효율적으로 unix history를 표현할 수 있다.


#(2) Draw Red Black Tree

import graphviz

TR = graphviz.Digraph('Draw Rea Black Tree', engine = 'dot')
TR.attr('node', shape = 'circle', color = 'black', style = 'filled',fontname='Helvetica', fontcolor='white', fontsize = '30', rankdir = 'LR')
TR.node('13')
TR.node('1')
TR.node('11')
TR.node('15')
TR.node('25')
TR.attr('node', fillcolor = 'red')
TR.node('8')
TR.node('17')
TR.node('22')
TR.node('27')
TR.attr('node', shape = 'record', fillcolor = 'black', label='NIL')
TR.node('a1')
TR.node('6', shape = 'circle', fillcolor = 'red',fontname='Helvetica', fontcolor='white', fontsize = '30', label='6')
TR.edges([('13','8'),('13','17')])
TR.edges([('8','1'),('8','11')])
TR.edges([('17','15'), ('17','25')])
TR.edge('1','a1') 
TR.edge('1','6')
TR.edges([('6','a2'), ('6','a3')])
TR.edges([('11','a4'), ('11','a5')])
TR.edges([('15','a6'), ('15','a7')])
TR.edges([('25','22'), ('25','27'), ('22','a8'), ('22','a9'), ('27','a10'), ('27','a11')])

TR
