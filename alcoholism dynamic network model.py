
import matplotlib
matplotlib.use('TkAgg')
from pylab import *
from collections import Counter

import networkx as nx
from pylab import *


con=randint(20,50) #total connections(Assumption value)
a=[]
names=['a','b','c','d','e','f','h','i','j','k','l','m','n','o','p','q','r','s','t','u']
n=len(names)
node_colors=[]
g = nx.Graph()
node_id={}
th = 0.5 #Threshold
# Here green(0)=teetotalers; blue(1)=Social drinkers; red(2)=addicts

    
for i in range(con):
    b=randint(n)
    c=randint(n)
    k=rand()
    b1=names[b]
    c1=names[c]
    g.add_edge(b1,c1,weight=k)

    

    
def initialize():
    global g,pos
    global countr,countb,countg
    countr=[]
    countb=[]
    countg=[]
    node_colors.clear()
    a.clear()
    for i in range(n):
        a.append(randint(3))
    for j in range(n):
        g.add_node(names[j])
        if a[j] == 0:
            node_id[names[j]]=0
        elif a[j] == 1:
            node_id[names[j]]=1
        else:
            node_id[names[j]]=2

    for j in g.nodes():
        if node_id[j] == 0:
            node_colors.append('green')
        elif node_id[j] == 1:
            node_colors.append('blue')
        else:
            node_colors.append('red')
    
    pos = nx.spring_layout(g)

    
def observe():
    global g,pos
    subplot(1, 2, 1)
    cla()
    nx.draw(g, with_labels = True, vmin = 0, vmax = 2, pos = pos,
           node_color = node_colors)
    subplot(1, 2, 2)
    cla()
    plot(countr,'red')
    plot(countb,'blue')
    plot(countg,'green')

    
def update():
    global g,pos,countg,countb,countr
    counter=Counter(node_id.values())
    countr.append(counter[2])
    countb.append(counter[1])
    countg.append(counter[0])
    for p in g.nodes():
        #i = choice(list(g.nodes))
        nbs = list(g.neighbors(p))
        weights_g=[]
        weights_b=[]
        weights_r=[]        
        for j in nbs:
            if node_id[j]==0:                                    #green neighbors
                weights_g.append(g[p][j]['weight'])
            elif node_id[j]==1:                                  #blue neighbors
                weights_b.append(g[p][j]['weight'])
            else:                                               #red neighbors
                weights_r.append(g[p][j]['weight'])
        gr_sum=sum(weights_g)
        b_sum=sum(weights_b)
        r_sum=sum(weights_r)
        gr=(gr_sum)/len(nbs)
        b=(b_sum)/len(nbs)
        r=(r_sum)/len(nbs)
        if (max(gr,b,r) > th):
            if max(gr,b,r)==gr:
                node_id[p]= 1 if node_id[p] == 2 else 0  
            elif max(gr,b,r)==b:
                node_id[p]=1   
            elif max(gr,b,r)==r:
                node_id[p]= 1 if node_id[p] == 0 else 2  
    node_colors.clear()   
    for j in g.nodes():
        if node_id[j] == 0:
            node_colors.append('green')
        elif node_id[j] == 1:
            node_colors.append('blue')
        else:
            node_colors.append('red')
    if random()>0.8:
        b=randint(n)
        c=randint(n)
        b1=names[b]
        c1=names[c]
        g.add_edge(b1,c1,weight=random())
    if random()>0.8:
        b=randint(n)
        c=randint(n)
        b1=names[b]
        c1=names[c]
        if g.has_edge(b1,c1) == True:
            g.remove_edge(b1,c1)
    pos = nx.spring_layout(g, pos = pos, iterations = 2, k = 1)

import pycxsimulator
pycxsimulator.GUI().start(func=[initialize, observe, update])

