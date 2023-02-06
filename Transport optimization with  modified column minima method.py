# Question: optimizing the transportation cost
# #Data: 25 lorries with capacities: 5, 10, 15 and 20 tonnes, 123 customers and 4 depots. 
#Constraints:
#a. lorries capacity
#b. Each lorry can't travel more than 250 miles
#c. Each lorry can't make more than 5 stops.
#d. Each lorry has to end its journey in one of the depots.
# There is a penalty fee of £1000 to fail to deliver to customers who tanks volume are less than 15% of their total capacity.
# Importing the required libraries
import pandas as pd
import numpy as np
import math
import networkx as nx
import random
from scipy.spatial import distance
import json
import numpy as np
# Putting the data in python arrays with python
df=pd.read_csv('locations')
df1=pd.read_csv('links')
coordinates=np.array(df[['x', 'y']])
customers=np.array(df.loc[df['is_customer']==True])
# displaced data

links=np.array(df1[['id1', 'id2']])

distances=[]
for i in range(len(coordinates)):
  distances.append([])
  for j in range(len(coordinates)):

    dist=math.sqrt((coordinates[i][0]-coordinates[j][0])**2+(coordinates[i][1]-coordinates[j][1])**2)
    distances[i].append(dist)
edges=[]
for i in range(len(links)): 
    edges.append({})
    edges[i]['key']=links[i][0]
    edges[i]['links']=[]
    for j in range(len(links)):
      if(links[i][0]==links[j][0]):
        edges[i]['links'].append(links[j][1])
        
#print(edges)
g = nx.Graph()
all_edges=[]
for i in range(len(edges)):
  links=edges[i]['links']
  key=edges[i]['key']
  for j in range(len(links)):
    
    one=links[j]
    link=[key,one,distances[key][one]]
    if(not link in all_edges):

      g.add_edge(key,one,weight=distances[key][one])
      all_edges.append([key,one,distances[key][one]])


depots=[{'id':523},{'id':124},{'id':373},{'id':116}]
# lorries capacities, location and their associated costs
lorries=[{'lorry_id': '523-0', 'capacity': 5, 'cpm': 1.0, 'cptm': 1.5, 'loc': [], 'location': 523, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '523-1', 'capacity': 5, 'cpm': 1.0, 'cptm': 1.5, 'loc': [], 'location': 523, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '523-2', 'capacity': 12, 'cpm': 1.5, 'cptm': 1.0, 'loc': [], 'location': 523, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '523-3', 'capacity': 12, 'cpm': 1.5, 'cptm': 1.0, 'loc': [], 'location': 523, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '523-4', 'capacity': 22, 'cpm': 2.0, 'cptm': 0.5, 'loc': [], 'location': 523, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '124-0', 'capacity': 5, 'cpm': 1.0, 'cptm': 1.5, 'loc': [], 'location': 124, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '124-1', 'capacity': 5, 'cpm': 1.0, 'cptm': 1.5, 'loc': [], 'location': 124, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '124-2', 'capacity': 5, 'cpm': 1.0, 'cptm': 1.5, 'loc': [], 'location': 124, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '124-3', 'capacity': 12, 'cpm': 1.5, 'cptm': 1.0, 'loc': [], 'location': 124, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '124-4', 'capacity': 12, 'cpm': 1.5, 'cptm': 1.0, 'loc': [], 'location': 124, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '124-5', 'capacity': 12, 'cpm': 1.5, 'cptm': 1.0, 'loc': [], 'location': 124, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '124-6', 'capacity': 22, 'cpm': 2.0, 'cptm': 0.5, 'loc': [], 'location': 124, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '124-7', 'capacity': 22, 'cpm': 2.0, 'cptm': 0.5, 'loc': [], 'location': 124, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '373-0', 'capacity': 5, 'cpm': 1.0, 'cptm': 1.5, 'loc': [], 'location': 373, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '373-1', 'capacity': 5, 'cpm': 1.0, 'cptm': 1.5, 'loc': [], 'location': 373, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '373-2', 'capacity': 5, 'cpm': 1.0, 'cptm': 1.5, 'loc': [], 'location': 373, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '373-3', 'capacity': 12, 'cpm': 1.5, 'cptm': 1.0, 'loc': [], 'location': 373, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '373-4', 'capacity': 12, 'cpm': 1.5, 'cptm': 1.0, 'loc': [], 'location': 373, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '373-5', 'capacity': 12, 'cpm': 1.5, 'cptm': 1.0, 'loc': [], 'location': 373, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '373-6', 'capacity': 12, 'cpm': 1.5, 'cptm': 1.0, 'loc': [], 'location': 373, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '373-7', 'capacity': 22, 'cpm': 2.0, 'cptm': 0.5, 'loc': [], 'location': 373, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '373-8', 'capacity': 22, 'cpm': 2.0, 'cptm': 0.5, 'loc': [], 'location': 373, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '373-9', 'capacity': 22, 'cpm': 2.0, 'cptm': 0.5, 'loc': [], 'location': 373, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '116-0', 'capacity': 5, 'cpm': 1.0, 'cptm': 1.5, 'loc': [], 'location': 116, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '116-1', 'capacity': 12, 'cpm': 1.5, 'cptm': 1.0, 'loc': [], 'location': 116, 'current': 0, 'stops': 0, 'miles': 0}]
costs={'523-0': [1.0, 1.5], '523-1': [1.0, 1.5], '523-2': [1.5, 1.0], '523-3': [1.5, 1.0], '523-4': [2.0, 0.5], '124-0': [1.0, 1.5], '124-1': [1.0, 1.5], '124-2': [1.0, 1.5], '124-3': [1.5, 1.0], '124-4': [1.5, 1.0], '124-5': [1.5, 1.0], '124-6': [2.0, 0.5], '124-7': [2.0, 0.5], '373-0': [1.0, 1.5], '373-1': [1.0, 1.5], '373-2': [1.0, 1.5], '373-3': [1.5, 1.0], '373-4': [1.5, 1.0], '373-5': [1.5, 1.0], '373-6': [1.5, 1.0], '373-7': [2.0, 0.5], '373-8': [2.0, 0.5], '373-9': [2.0, 0.5], '116-0': [1.0, 1.5], '116-1': [1.5, 1.0]}
# Finding possible lorries which can be able to deliver without violating our given constraints (defined above)

def possible_lorries(lorries,c,demands,custo_ids,under_threshold,under_ids):
    if(len(under_threshold)>0):

      target=under_threshold[c]['id']
      required=under_threshold[c]['demand']
    else:
      target=demands[c]['id']
      required=demands[c]['demand']
    vehicles=[]
    for i in range(len(lorries)):
      stops=0  
      if(lorries[i]['current']>=required):
        to_customer=nx.single_source_dijkstra(g,source=lorries[i]['location'],target=target,weight='weight')[0]      
        to_depot=nx.single_source_dijkstra(g,source=target,target=nearby_depot(target),weight='weight')[0]
        total_d=lorries[i]['miles']+to_customer+to_depot
        stops=lorries[i]['stops']+1
        
        if(total_d<=250 and stops<=5):
          vehicles.append(i)
      elif(lorries[i]['current']<required):
         depot=nearby_depot(lorries[i]['location'])
         depot_d=nx.single_source_dijkstra(g,source=lorries[i]['location'],target=depot,weight='weight')[0]
         to_customer=nx.single_source_dijkstra(g,source=depot,target=target,weight='weight')[0]
         to_depot=nx.single_source_dijkstra(g,source=target,target=nearby_depot(target),weight='weight')[0]
         total_d=lorries[i]['miles']+depot_d+to_customer+to_depot
         stops=lorries[i]['stops']+2
         if(total_d<=250 and stops<=5):
           vehicles.append(i)
    return vehicles
# From all the possible lorries, we compute the cost of delivering to the first customer in the list. 
def cheapest_provider(options,c,lorries,demands,custo_ids,under_threshold,under_ids): 
  if len(under_threshold)>0:
    end=under_ids[c]
    demand=under_threshold[c]['demand']
    
  elif len(under_threshold)==0:
    end=custo_ids[c]
    demand=demands[c]['demand']
  for i in range(len(options)):
     cost=0
     v=options[i]
     location=lorries[v]['location']
     id=lorries[v]['lorry_id']
     available=lorries[v]['current']-demand
     current_volume=lorries[v]['current']
     journey=nx.single_source_dijkstra(g,source=lorries[v]['location'],target=end,weight='weight')[1]
     for j in range(len(journey)):
         if j<len(journey)-1 and journey[j] in custo_ids:
            index=custo_ids.index(journey[j])
            if lorries[v]['stops']>4 and available>=demands[index]['demand']:
              
              distance=nx.single_source_dijkstra(g,source=location,target=journey[j],wieght='weight')[0]
              cost+=costs[id][0]*distance+costs[id][1]*current_volume
              current_volume-=demands[index]['demand']
              available-=demands[index]['demand']
              location=journey[j]
            elif lorries[v]['stops']>4 and available<demands[index]['demand'] and available>0:
               distance=nx.single_source_dijkstra(g,source=location,target=journey[j],wieght='weight')[0]
               cost+=costs[id][0]*distance+costs[id][1]*current_volume
               current_volume-=available
               available=0
               location=journey[j]

         elif j==len(journey)-1:
            distance=nx.single_source_dijkstra(g,source=location,target=end,weight='weight')[0]
            cost+=costs[id][0]*distance+costs[id][1]*current_volume

     if i==0:
       min=cost
       pick=v  
     elif i>0:
       if cost<min:
         pick=v
         min=cost

  return pick
# Firstly we deliver to those customers who tanks volume are less than 15%. However, the lorry can meet on its way if it encounters other customers; only if that doesn't violate the given constraints
def deliver1(lorries,v,c,customer_id,target,demands,custo_ids,under_threshold,under_ids):
  available=lorries[v]['current']-demands[target]['demand']
  given_to_others=0
  miles=nx.single_source_dijkstra(g,source=lorries[v]['location'],target=customer_id,weight='weight')
  for i in range(1,len(miles[1])):
    
    if(i<len(miles[1])-1):
      if(miles[1][i] in custo_ids ):
        index=custo_ids.index(miles[1][i])
       

        if(lorries[v]['stops']<4 and available>=demands[index]['demand']):

         lorries[v]['location']=demands[index]['id']
         lorries[v]['stops']+=1
         given_to_others+=demands[index]['demand']
         available-=demands[index]['demand']
         lorries[v]['loc'].append([demands[index]['id'],-demands[index]['demand']])
         demands[index]['demand']=0
         del demands[index]
         del custo_ids[index]
         if(miles[1][i] in under_ids):
           indice=under_ids.index(miles[1][i])
          
           del under_threshold[indice]
           del under_ids[indice]
        elif(lorries[v]['stops']<4 and available<demands[index]['demand'] and available>0):
         lorries[v]['location']=demands[index]['id']
         lorries[v]['stops']+=1
         fore=available
         given_to_others+=available
         if(demands[index]['id'] in under_ids):
           indice=under_ids.index(demands[index]['id'])
           under_threshold[indice]['demand']-=available
           demands[index]['demand']-=available
           lorries[v]['loc'].append(demands[index]['id'],-available)
           available=0
         if(miles[1][i] in under_ids):
           indice=under_ids.index(miles[1][i])
           under_threshold[indice]['demand']-=fore
           fore=0
    elif i==len(miles[1])-1:
      id=miles[1][i]
      
      lorries[v]['miles']+=miles[0]
      lorries[v]['location']=id
      if(len(under_threshold)>0):
        pos=under_ids.index(id)
        indice=custo_ids.index(id)
        lorries[v]['current']-=(under_threshold[pos]['demand']+given_to_others)
        lorries[v]['loc'].append([customer_id,-under_threshold[pos]['demand']])
        under_threshold[pos]['demand']=0
        lorries[v]['stops']+=1
     
        
        del under_threshold[pos]
        del under_ids[pos]
        
        del demands[indice]
        del custo_ids[indice]
        
      elif(len(under_threshold)==0):
        indice=custo_ids.index(id)
        lorries[v]['current']-=(demands[indice]['demand']+given_to_others)
        lorries[v]['loc'].append([demands[indice]['id'],-demands[indice]['demand']])
        demands[indice]['demand']=0
    
        lorries[v]['stops']+=1
        del demands[indice]
        del custo_ids[indice]
#When the lorry doesn't have enough petroleum, it can go back to the depot to charge
def depot_and_deliver1(lorries,v,c,customer_id,target,demands,custo_ids,under_threshold,under_ids):
  depot=nearby_depot(lorries[v]['location'])
  journey=nx.single_source_djikstra(g,source=lorries[v]['location'],target=depot,weight='weight')
  #for i in range(1,len(journey[1])):
  for i in range(1,len(journey[1])):
    

    id=journey[1][i]
    index=custo_ids.index(id)
    if i<len(journey[1])-1:
        if(lorries[v]['stops']<3 and id in custo_ids and lorries[v]['current']>=demands[index]['demand']):
          lorries[v]['location']=demands[index]['id']
          lorries[v]['current']-=demands[index]['demand']
          lorries[v]['loc'].append([demands[index]['id'],-demands[index]['demand']])
          lorries[v]['stops']+=1
          del demands[index]
          del custo_ids[index]
          if(journey[1][i] in under_ids):
            index=under_ids.index(journey[1][i])
            del under_ids[index]
            del under_threshold[index]

         
        elif(id in custo_ids and lorries[v]['current']>0 and lorries[v]['current']<demands[index]['demand'] and lorries[v]['stops']<3):
           lorries[v]['location']=demands[index]['id']
           demands[index]['demand']-=lorries[v]['current']
          
           lorries[v]['loc'].append([demands[index]['id'],-lorries[v]['current']])
           if(demands[index]['id'] in under_ids):
            indice=under_ids.index(demands[index]['id'])
            under_threshold[indice]['demand']-=lorries[v]['current']
            lorries[v]['current']=0
            lorries[v]['stops']+=1
    elif i==len(journey[1][i]-1):

      lorries[v]['location']=depot 
      load=lorries[v]['capacity']-lorries[v]['current']
      lorries[v]['loc'].append([depot,load])
      lorries[v]['current']=lorries[v]['capacity']
      lorries[v]['miles']+=journey[0]
      lorries[v]['stops']+=1
 # Delivery to other customers, when the customers with that threshold of 15% are visited or if delivering to them would violate the constraints
def deliver(lorries,v,c,journey,demands,custo_ids,under_threshold,under_ids):
  #customers=ds=nx.single_source_dijkstra(g,source=lorries[v]['location'],target=c,weight='weight')
  given_to_others=0
  
  available=lorries[v]['current']-demands[c]['demand']
  for i in range(1,len(journey[1])):
    if(i<len(journey[1])-1):

      if(journey[1][i] in custo_ids):
        id=journey[1][i]
        index=custo_ids.index(id)
      #total+=demands[index]['demand']
        if(lorries[v]['stops']<4 and available>=demands[index]['demand'] and i<len(journey[1])-1):
         #distance=nx.single_source_dijkstra(g,source=lorries[v]['location'],target=demands[index]['id'])[0]
           lorries[v]['loc'].append([demands[index]['id'],-demands[index]['demand']])
           available-=demands[index]['demand']
            #diff=lorries[v]['current']-demands[index]['demand']
           given_to_others+=demands[index]['demand']
           demands[index]['demand']=0

        
         #del custo_ids[custo_ids.index(demands[index]['id'])]
         
           lorries[v]['location']=demands[index]['id']
           lorries[v]['stops']+=1
         #lorries[v]['miles']+=distance
           del demands[index]
           del custo_ids[index]
        elif(lorries[v]['stops']<4 and available<demands[index]['demand'] and i<len(journey[1])-1 and available>0):
        #distance=nx.single_source_dijkstra(g,source=lorries[v]['location'],target=demands[index]['id'])[0]
           demands[index]['demand']-=available
           lorries[v]['loc'].append([demands[index]['id'],-available])
           given_to_others+=available
           available=0
           lorries[v]['stops']+=1
        #lorries[v]['miles']+=distance
           lorries[v]['location']=demands[index]['id']

    elif i==len(journey[1])-1:
       id=journey[1][i]
       index=custo_ids.index(id)

       lorries[v]['current']-=demands[index]['demand']
  #distance=nx.single_source_dijkstra(g,source=lorries[v]['location'],target=demands[c]['id'])[0]
       lorries[v]['loc'].append([demands[index]['id'],-demands[index]['demand']])
       demands[index]['demand']=0
       lorries[v]['location']=demands[index]['id']
       lorries[v]['stops']+=1
       lorries[v]['miles']+=journey[0]
       del demands[index]
       del custo_ids[index]
       
         
  lorries[v]['current']-=given_to_others
# If a lorry needs to charge, it has to go to a nearest depot.
def nearby_depot(location):
  closest=depots[0]['id']
  distance=nx.single_source_dijkstra(g,source=location,target=depots[0]['id'],weight='weight')[0]
  for i in range(len(depots)):
    
    current_distance=nx.single_source_dijkstra(g,source=location,target=depots[i]['id'],weight='weight')[0]
    if(current_distance<distance):
      closest=depots[i]['id']
      distance=current_distance
  return closest

def depot_and_deliver(lorries,v,c,end,demands,custo_ids,under_threshold,under_ids):
  
 
  depot=nearby_depot(lorries[v]['location'])
  journey_to_depot=journey=nx.single_source_dijkstra(g,source=lorries[v]['location'],target=depot,weight='weight')
  for i in range(1,len(journey_to_depot[1])):
    if(i<len(journey_to_depot[1])-1):
       if(journey_to_depot[1][i] in custo_ids):
         indice=custo_ids.index(journey_to_depot[1][i])
         if(lorries[v]['stops']>3 and lorries[v]['current']>=demands[indice]['demand']):
           lorries[v]['current']-=demands[indice]['demand']
           lorries[v]['loc'].append([demands[indice]['id'],-demands[indice]['demand']])
           demands[indice]['demand']=0
           lorries[v]['stops']+=1
           lorries[v]['location']=demands[indice]['id']
         elif( lorries[v]['stops']>3 and lorries[v]['current']>0 and lorries[v]['current']<demands[indice]['demand']):
           demands[indice]['demand']-=lorries[v]['current']
           lorries[v]['loc'].append([demands[indice]['id'],-lorries[v]['current']])
           lorries[v]['current']=0
           lorries[v]['stops']+=1
           lorries[v]['location']=demands[indice]['id']
  #This is once it gets to depot
    elif i==len(journey[1][i]-1):
       
      lorries[v]['location']=depot
      load=lorries[v]['capacity']-lorries[v]['current']
      lorries[v]['current']=lorries[v]['capacity']
      lorries[v]['loc'].append([depot,load])
      lorries[v]['stops']+=1
      lorries[v]['miles']+=journey_to_depot[0]
      lorries[v]['location']=depot
  
  journey=nx.single_source_djikstra(g,source=depot,target=end,weight='weight')
  #The path not satisfied.
  deliver(lorries,v,c,journey,demands,custo_ids,under_threshold,under_ids)
  
#depot_and_deliver()

def have_delivered(lorries):
  journeys=[]
  for i in range(len(lorries)):
    if(len(lorries[i]['loc'])>1):
      
      
      
      journeys.append({'lorry_id':lorries[i]['lorry_id'],'location':lorries[i]['location'],'loc':lorries[i]['loc'],'miles':lorries[i]['miles']})
      
  return journeys
# At the end, lorries who are not at the depot have to find a nearby depot. 
def back_to_depot(have_worked):
  for i in range (len(have_worked)):
    depot_end=nearby_depot(have_worked[i]['location'])
    distance=nx.single_source_dijkstra(g,source=have_worked[i]['location'],target=depot_end,weight='weight')[0]
    have_worked[i]['miles']+=distance
    have_worked[i]['loc'].append([depot_end,0])
    del have_worked[i]['location']
    del have_worked[i]['miles']
  return have_worked


  
  deliver1(lorries,v,c,customer_id,target,demands,custo_ids,under_threshold,under_ids)

def main():
  left=0
  
  custo_ids=[5, 8, 13, 14, 22, 27, 29, 31, 32, 36, 41, 44, 63, 64, 65, 70, 73, 77, 78, 80, 82, 86, 94, 100, 103, 105, 110, 113, 118, 130, 135, 136, 144, 146, 147, 160, 169, 171, 172, 175, 177, 180, 183, 190, 200, 202, 204, 205, 206, 210, 214, 216, 220, 225, 235, 243, 245, 254, 255, 257, 260, 264, 265, 270, 271, 274, 276, 294, 308, 324, 332, 337, 362, 364, 372, 374, 377, 378, 380, 387, 389, 391, 393, 397, 398, 400, 408, 411, 418, 431, 437, 446, 449, 453, 455, 459, 474, 476, 491, 497, 507, 511, 519, 520, 528, 531, 534, 539, 542, 543, 547, 550, 566, 569, 584, 585, 598, 603, 606, 621, 624, 632, 633]
  demands=[{'id': 5, 'demand': 0.09999999999999998}, {'id': 8, 'demand': 0.19999999999999996}, {'id': 13, 'demand': 0.19999999999999996}, {'id': 14, 'demand': 0.32999999999999996}, {'id': 22, 'demand': 1.68}, {'id': 27, 'demand': 1.02}, {'id': 29, 'demand': 0.54}, {'id': 31, 'demand': 0.56}, {'id': 32, 'demand': 0.92}, {'id': 36, 'demand': 0.81}, {'id': 41, 'demand': 1.03}, {'id': 44, 'demand': 0.71}, {'id': 63, 'demand': 0.47}, {'id': 64, 'demand': 0.96}, {'id': 65, 'demand': 0.72}, {'id': 70, 'demand': 1.46}, {'id': 73, 'demand': 0.22999999999999998}, {'id': 77, 'demand': 1.47}, {'id': 78, 'demand': 0.63}, {'id': 80, 'demand': 0.22999999999999998}, {'id': 82, 'demand': 0.6}, {'id': 86, 'demand': 1.03}, {'id': 94, 'demand': 1.52}, {'id': 100, 'demand': 1.02}, {'id': 103, 'demand': 0.43999999999999995}, {'id': 105, 'demand': 1.27}, {'id': 110, 'demand': 1.99}, {'id': 113, 'demand': 0.44999999999999996}, {'id': 118, 'demand': 0.71}, {'id': 130, 'demand': 1.19}, {'id': 135, 'demand': 1.33}, {'id': 136, 'demand': 0.33999999999999997}, {'id': 144, 'demand': 0.45999999999999996}, {'id': 146, 'demand': 1.45}, {'id': 147, 'demand': 0.8500000000000001}, {'id': 160, 'demand': 0.91}, {'id': 169, 'demand': 1.4}, {'id': 171, 'demand': 1.3199999999999998}, {'id': 172, 'demand': 0.91}, {'id': 175, 'demand': 1.63}, {'id': 177, 'demand': 1.23}, {'id': 180, 'demand': 0.76}, {'id': 183, 'demand': 0.3999999999999999}, {'id': 190, 'demand': 0.3600000000000001}, {'id': 200, 'demand': 0.27}, {'id': 202, 'demand': 0.17000000000000004}, {'id': 204, 'demand': 0.69}, {'id': 205, 'demand': 0.9099999999999999}, {'id': 206, 'demand': 0.88}, {'id': 210, 'demand': 0.47}, {'id': 214, 'demand': 1.6099999999999999}, {'id': 216, 'demand': 0.27}, {'id': 220, 'demand': 0.61}, {'id': 225, 'demand': 0.64}, {'id': 235, 'demand': 0.36}, {'id': 243, 'demand': 0.6699999999999999}, {'id': 245, 'demand': 0.15000000000000002}, {'id': 254, 'demand': 1.28}, {'id': 255, 'demand': 0.16999999999999998}, {'id': 257, 'demand': 0.19999999999999996}, {'id': 260, 'demand': 1.62}, {'id': 264, 'demand': 0.8600000000000001}, {'id': 265, 'demand': 0.48}, {'id': 270, 'demand': 0.21999999999999997}, {'id': 271, 'demand': 0.9}, {'id': 274, 'demand': 0.16999999999999993}, {'id': 276, 'demand': 0.9299999999999999}, {'id': 294, 'demand': 0.81}, {'id': 308, 'demand': 0.6799999999999999}, {'id': 324, 'demand': 0.42000000000000004}, {'id': 332, 'demand': 0.79}, {'id': 337, 'demand': 0.44999999999999996}, {'id': 362, 'demand': 0.75}, {'id': 364, 'demand': 0.89}, {'id': 372, 'demand': 1.75}, {'id': 374, 'demand': 0.5}, {'id': 377, 'demand': 0.95}, {'id': 378, 'demand': 0.54}, {'id': 380, 'demand': 0.15999999999999998}, {'id': 387, 'demand': 1.24}, {'id': 389, 'demand': 0.07}, {'id': 391, 'demand': 1.0}, {'id': 393, 'demand': 1.12}, {'id': 397, 'demand': 0.7}, {'id': 398, 'demand': 0.89}, {'id': 400, 'demand': 0.19}, {'id': 408, 'demand': 0.28}, {'id': 411, 'demand': 0.99}, {'id': 418, 'demand': 0.32999999999999996}, {'id': 431, 'demand': 0.39}, {'id': 437, 'demand': 0.94}, {'id': 446, 'demand': 0.94}, {'id': 449, 'demand': 1.74}, {'id': 453, 'demand': 0.61}, {'id': 455, 'demand': 0.3}, {'id': 459, 'demand': 1.98}, {'id': 474, 'demand': 0.3999999999999999}, {'id': 476, 'demand': 0.31000000000000005}, {'id': 491, 'demand': 0.33999999999999997}, {'id': 497, 'demand': 0.98}, {'id': 507, 'demand': 1.15}, {'id': 511, 'demand': 0.24}, {'id': 519, 'demand': 0.21000000000000002}, {'id': 520, 'demand': 0.44}, {'id': 528, 'demand': 0.12}, {'id': 531, 'demand': 0.10999999999999999}, {'id': 534, 'demand': 1.19}, {'id': 539, 'demand': 0.28}, {'id': 542, 'demand': 0.47}, {'id': 543, 'demand': 0.54}, {'id': 547, 'demand': 0.95}, {'id': 550, 'demand': 0.45999999999999996}, {'id': 566, 'demand': 0.26}, {'id': 569, 'demand': 0.13}, {'id': 584, 'demand': 0.21999999999999997}, {'id': 585, 'demand': 1.41}, {'id': 598, 'demand': 0.97}, {'id': 603, 'demand': 0.86}, {'id': 606, 'demand': 1.44}, {'id': 621, 'demand': 0.24}, {'id': 624, 'demand': 0.51}, {'id': 632, 'demand': 1.24}, {'id': 633, 'demand': 0.18000000000000005}]
  
  under_threshold=[{'id': 32, 'demand': 0.92}, {'id': 63, 'demand': 0.47}, {'id': 70, 'demand': 1.46}, {'id': 77, 'demand': 1.47}, {'id': 110, 'demand': 1.99}, {'id': 206, 'demand': 0.88}, {'id': 254, 'demand': 1.28}, {'id': 276, 'demand': 0.9299999999999999}, {'id': 364, 'demand': 0.89}, {'id': 372, 'demand': 1.75}, {'id': 377, 'demand': 0.95}, {'id': 391, 'demand': 1.0}, {'id': 398, 'demand': 0.89}, {'id': 449, 'demand': 1.74}, {'id': 459, 'demand': 1.98}, {'id': 497, 'demand': 0.98}, {'id': 520, 'demand': 0.44}, {'id': 542, 'demand': 0.47}, {'id': 585, 'demand': 1.41}, {'id': 598, 'demand': 0.97}, {'id': 603, 'demand': 0.86}, {'id': 606, 'demand': 1.44}]
  under_ids=[32, 63, 70, 77, 110, 206, 254, 276, 364, 372, 377, 391, 398, 449, 459, 497, 520, 542, 585, 598, 603, 606]
  
  lorries=[{'lorry_id': '523-0', 'capacity': 5, 'cpm': 1.0, 'cptm': 1.5, 'loc': [], 'location': 523, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '523-1', 'capacity': 5, 'cpm': 1.0, 'cptm': 1.5, 'loc': [], 'location': 523, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '523-2', 'capacity': 12, 'cpm': 1.5, 'cptm': 1.0, 'loc': [], 'location': 523, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '523-3', 'capacity': 12, 'cpm': 1.5, 'cptm': 1.0, 'loc': [], 'location': 523, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '523-4', 'capacity': 22, 'cpm': 2.0, 'cptm': 0.5, 'loc': [], 'location': 523, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '124-0', 'capacity': 5, 'cpm': 1.0, 'cptm': 1.5, 'loc': [], 'location': 124, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '124-1', 'capacity': 5, 'cpm': 1.0, 'cptm': 1.5, 'loc': [], 'location': 124, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '124-2', 'capacity': 5, 'cpm': 1.0, 'cptm': 1.5, 'loc': [], 'location': 124, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '124-3', 'capacity': 12, 'cpm': 1.5, 'cptm': 1.0, 'loc': [], 'location': 124, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '124-4', 'capacity': 12, 'cpm': 1.5, 'cptm': 1.0, 'loc': [], 'location': 124, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '124-5', 'capacity': 12, 'cpm': 1.5, 'cptm': 1.0, 'loc': [], 'location': 124, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '124-6', 'capacity': 22, 'cpm': 2.0, 'cptm': 0.5, 'loc': [], 'location': 124, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '124-7', 'capacity': 22, 'cpm': 2.0, 'cptm': 0.5, 'loc': [], 'location': 124, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '373-0', 'capacity': 5, 'cpm': 1.0, 'cptm': 1.5, 'loc': [], 'location': 373, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '373-1', 'capacity': 5, 'cpm': 1.0, 'cptm': 1.5, 'loc': [], 'location': 373, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '373-2', 'capacity': 5, 'cpm': 1.0, 'cptm': 1.5, 'loc': [], 'location': 373, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '373-3', 'capacity': 12, 'cpm': 1.5, 'cptm': 1.0, 'loc': [], 'location': 373, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '373-4', 'capacity': 12, 'cpm': 1.5, 'cptm': 1.0, 'loc': [], 'location': 373, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '373-5', 'capacity': 12, 'cpm': 1.5, 'cptm': 1.0, 'loc': [], 'location': 373, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '373-6', 'capacity': 12, 'cpm': 1.5, 'cptm': 1.0, 'loc': [], 'location': 373, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '373-7', 'capacity': 22, 'cpm': 2.0, 'cptm': 0.5, 'loc': [], 'location': 373, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '373-8', 'capacity': 22, 'cpm': 2.0, 'cptm': 0.5, 'loc': [], 'location': 373, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '373-9', 'capacity': 22, 'cpm': 2.0, 'cptm': 0.5, 'loc': [], 'location': 373, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '116-0', 'capacity': 5, 'cpm': 1.0, 'cptm': 1.5, 'loc': [], 'location': 116, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '116-1', 'capacity': 12, 'cpm': 1.5, 'cptm': 1.0, 'loc': [], 'location': 116, 'current': 0, 'stops': 0, 'miles': 0}]
 
  def pers1(lorries,demands,custo_ids,under_threshold,under_ids,left):
    answer=[[],[]]
    while len(under_threshold)>0:
      
      #c=random.randint(0,len(under_threshold)-1)
      c=0
      customer_id=under_threshold[c]['id']
      
      target=custo_ids.index(customer_id)
      options=possible_lorries(lorries,c,demands,custo_ids,under_threshold,under_ids)
      if(len(options)==0):
        left+=1
        del under_threshold[c]
        del under_ids[c]
        del demands[target]
        del custo_ids[target]
      else:
        
      # Firstly we deliver to those customers who tanks volume are less than 15%. However, the lorry can meet on its way if it encounters other customers; only if that doesn't violate the given constraints. 
        v=cheapest_provider(options,c,lorries,demands,custo_ids,under_threshold,under_ids)
        if(len(lorries[v]['loc'])==0):
          lorries[v]['current']=lorries[v]['capacity']
          lorries[v]['loc'].append([lorries[v]['location'],lorries[v]['capacity']])
        if(lorries[v]['current']>=under_threshold[c]['demand']):
          deliver1(lorries,v,c,customer_id,target,demands,custo_ids,under_threshold,under_ids)
        elif(lorries[v]['current']<under_threshold[c]['demand']):
          depot_and_deliver1(lorries,v,c,customer_id,target,demands,custo_ids,under_threshold,under_ids)
        
    while len(under_threshold)==0 and len(demands)>0:
    # When the number of customers of that threshold are finished or if visiting them would violate the underlined constraints, we moved to other customers  
      c=0
      target=c
      customer_id=demands[c]['id']
      options=possible_lorries(lorries,c,demands,custo_ids,under_threshold,under_ids)
      if len(options)==0:
        del demands[c]
        del custo_ids[c]
      else:
        #v=options[random.randint(0,len(options)-1)]
        v=cheapest_provider(options,c,lorries,demands,custo_ids,under_threshold,under_ids)
        if(len(lorries[v]['loc'])==0):
          lorries[v]['current']=lorries[v]['capacity']
          lorries[v]['loc'].append([lorries[v]['location'],lorries[v]['capacity']])
        if(lorries[v]['current']>=demands[c]['demand']):
          journey=nx.single_source_dijkstra(g,source=lorries[v]['location'],target=customer_id,weight='weight')
          deliver(lorries,v,c,journey,demands,custo_ids,under_threshold,under_ids)
        elif(lorries[v]['current']<demands[c]['demand']):
          depot_and_deliver(lorries,v,c,customer_id,demands,custo_ids,under_threshold,under_ids)
        
        #print(len(demands))
    have_worked=have_delivered(lorries)
    back_to_depot(have_worked)
   
    return have_worked
  return pers1(lorries,demands,custo_ids,under_threshold,under_ids,left)
 

solution=main2()
print(json.dumps(solution))


