# Question: Optimizing the transportation cost.
#Data: 25 lorries with capacities: 5, 10, 15 and 20 tonnes, 123 customers and 4 depots. 
#Constraints: lorries capacity
# Importing the required libraries
import pandas as pd
import numpy as np
import math
import networkx as nx
import random
# Putting the data in python arrays with python
df=pd.read_csv('/locations)
df1=pd.read_csv('/links')
coordinates=np.array(df[['x', 'y']])
customers=np.array(df.loc[df['is_customer']==True])
custo_ids=[5, 8, 13, 14, 22, 27, 29, 31, 32, 36, 41, 44, 63, 64, 65, 70, 73, 77, 78, 80, 82, 86, 94, 100, 103, 105, 110, 113, 118, 130, 135, 136, 144, 146, 147, 160, 169, 171, 172, 175, 177, 180, 183, 190, 200, 202, 204, 205, 206, 210, 214, 216, 220, 225, 235, 243, 245, 254, 255, 257, 260, 264, 265, 270, 271, 274, 276, 294, 308, 324, 332, 337, 362, 364, 372, 374, 377, 378, 380, 387, 389, 391, 393, 397, 398, 400, 408, 411, 418, 431, 437, 446, 449, 453, 455, 459, 474, 476, 491, 497, 507, 511, 519, 520, 528, 531, 534, 539, 542, 543, 547, 550, 566, 569, 584, 585, 598, 603, 606, 621, 624, 632, 633]
demands=[{'id': 5, 'demand': 0.09999999999999998}, {'id': 8, 'demand': 0.19999999999999996}, {'id': 13, 'demand': 0.19999999999999996}, {'id': 14, 'demand': 0.32999999999999996}, {'id': 22, 'demand': 1.68}, {'id': 27, 'demand': 1.02}, {'id': 29, 'demand': 0.54}, {'id': 31, 'demand': 0.56}, {'id': 32, 'demand': 0.92}, {'id': 36, 'demand': 0.81}, {'id': 41, 'demand': 1.03}, {'id': 44, 'demand': 0.71}, {'id': 63, 'demand': 0.47}, {'id': 64, 'demand': 0.96}, {'id': 65, 'demand': 0.72}, {'id': 70, 'demand': 1.46}, {'id': 73, 'demand': 0.22999999999999998}, {'id': 77, 'demand': 1.47}, {'id': 78, 'demand': 0.63}, {'id': 80, 'demand': 0.22999999999999998}, {'id': 82, 'demand': 0.6}, {'id': 86, 'demand': 1.03}, {'id': 94, 'demand': 1.52}, {'id': 100, 'demand': 1.02}, {'id': 103, 'demand': 0.43999999999999995}, {'id': 105, 'demand': 1.27}, {'id': 110, 'demand': 1.99}, {'id': 113, 'demand': 0.44999999999999996}, {'id': 118, 'demand': 0.71}, {'id': 130, 'demand': 1.19}, {'id': 135, 'demand': 1.33}, {'id': 136, 'demand': 0.33999999999999997}, {'id': 144, 'demand': 0.45999999999999996}, {'id': 146, 'demand': 1.45}, {'id': 147, 'demand': 0.8500000000000001}, {'id': 160, 'demand': 0.91}, {'id': 169, 'demand': 1.4}, {'id': 171, 'demand': 1.3199999999999998}, {'id': 172, 'demand': 0.91}, {'id': 175, 'demand': 1.63}, {'id': 177, 'demand': 1.23}, {'id': 180, 'demand': 0.76}, {'id': 183, 'demand': 0.3999999999999999}, {'id': 190, 'demand': 0.3600000000000001}, {'id': 200, 'demand': 0.27}, {'id': 202, 'demand': 0.17000000000000004}, {'id': 204, 'demand': 0.69}, {'id': 205, 'demand': 0.9099999999999999}, {'id': 206, 'demand': 0.88}, {'id': 210, 'demand': 0.47}, {'id': 214, 'demand': 1.6099999999999999}, {'id': 216, 'demand': 0.27}, {'id': 220, 'demand': 0.61}, {'id': 225, 'demand': 0.64}, {'id': 235, 'demand': 0.36}, {'id': 243, 'demand': 0.6699999999999999}, {'id': 245, 'demand': 0.15000000000000002}, {'id': 254, 'demand': 1.28}, {'id': 255, 'demand': 0.16999999999999998}, {'id': 257, 'demand': 0.19999999999999996}, {'id': 260, 'demand': 1.62}, {'id': 264, 'demand': 0.8600000000000001}, {'id': 265, 'demand': 0.48}, {'id': 270, 'demand': 0.21999999999999997}, {'id': 271, 'demand': 0.9}, {'id': 274, 'demand': 0.16999999999999993}, {'id': 276, 'demand': 0.9299999999999999}, {'id': 294, 'demand': 0.81}, {'id': 308, 'demand': 0.6799999999999999}, {'id': 324, 'demand': 0.42000000000000004}, {'id': 332, 'demand': 0.79}, {'id': 337, 'demand': 0.44999999999999996}, {'id': 362, 'demand': 0.75}, {'id': 364, 'demand': 0.89}, {'id': 372, 'demand': 1.75}, {'id': 374, 'demand': 0.5}, {'id': 377, 'demand': 0.95}, {'id': 378, 'demand': 0.54}, {'id': 380, 'demand': 0.15999999999999998}, {'id': 387, 'demand': 1.24}, {'id': 389, 'demand': 0.07}, {'id': 391, 'demand': 1.0}, {'id': 393, 'demand': 1.12}, {'id': 397, 'demand': 0.7}, {'id': 398, 'demand': 0.89}, {'id': 400, 'demand': 0.19}, {'id': 408, 'demand': 0.28}, {'id': 411, 'demand': 0.99}, {'id': 418, 'demand': 0.32999999999999996}, {'id': 431, 'demand': 0.39}, {'id': 437, 'demand': 0.94}, {'id': 446, 'demand': 0.94}, {'id': 449, 'demand': 1.74}, {'id': 453, 'demand': 0.61}, {'id': 455, 'demand': 0.3}, {'id': 459, 'demand': 1.98}, {'id': 474, 'demand': 0.3999999999999999}, {'id': 476, 'demand': 0.31000000000000005}, {'id': 491, 'demand': 0.33999999999999997}, {'id': 497, 'demand': 0.98}, {'id': 507, 'demand': 1.15}, {'id': 511, 'demand': 0.24}, {'id': 519, 'demand': 0.21000000000000002}, {'id': 520, 'demand': 0.44}, {'id': 528, 'demand': 0.12}, {'id': 531, 'demand': 0.10999999999999999}, {'id': 534, 'demand': 1.19}, {'id': 539, 'demand': 0.28}, {'id': 542, 'demand': 0.47}, {'id': 543, 'demand': 0.54}, {'id': 547, 'demand': 0.95}, {'id': 550, 'demand': 0.45999999999999996}, {'id': 566, 'demand': 0.26}, {'id': 569, 'demand': 0.13}, {'id': 584, 'demand': 0.21999999999999997}, {'id': 585, 'demand': 1.41}, {'id': 598, 'demand': 0.97}, {'id': 603, 'demand': 0.86}, {'id': 606, 'demand': 1.44}, {'id': 621, 'demand': 0.24}, {'id': 624, 'demand': 0.51}, {'id': 632, 'demand': 1.24}, {'id': 633, 'demand': 0.18000000000000005}]
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

g = nx.Graph()
all_edges=[]
for i in range(len(edges)):
  links=edges[i]['links']
  key=edges[i]['key']
  for j in range(len(links)):
    
    one=links[j]
    g.add_edge(key,one,weight=distances[key][one])
    all_edges.append([key,one,distances[key][one]])



depots=[{'id':523},{'id':124},{'id':373},{'id':116}]
# lorries capacities, location and their associated costs
lorries=[{'lorry_id': '523-0', 'capacity': 5, 'cpm': 1.0, 'cptm': 1.5, 'loc': [], 'location': 523, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '523-1', 'capacity': 5, 'cpm': 1.0, 'cptm': 1.5, 'loc': [], 'location': 523, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '523-2', 'capacity': 12, 'cpm': 1.5, 'cptm': 1.0, 'loc': [], 'location': 523, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '523-3', 'capacity': 12, 'cpm': 1.5, 'cptm': 1.0, 'loc': [], 'location': 523, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '523-4', 'capacity': 22, 'cpm': 2.0, 'cptm': 0.5, 'loc': [], 'location': 523, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '124-0', 'capacity': 5, 'cpm': 1.0, 'cptm': 1.5, 'loc': [], 'location': 124, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '124-1', 'capacity': 5, 'cpm': 1.0, 'cptm': 1.5, 'loc': [], 'location': 124, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '124-2', 'capacity': 5, 'cpm': 1.0, 'cptm': 1.5, 'loc': [], 'location': 124, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '124-3', 'capacity': 12, 'cpm': 1.5, 'cptm': 1.0, 'loc': [], 'location': 124, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '124-4', 'capacity': 12, 'cpm': 1.5, 'cptm': 1.0, 'loc': [], 'location': 124, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '124-5', 'capacity': 12, 'cpm': 1.5, 'cptm': 1.0, 'loc': [], 'location': 124, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '124-6', 'capacity': 22, 'cpm': 2.0, 'cptm': 0.5, 'loc': [], 'location': 124, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '124-7', 'capacity': 22, 'cpm': 2.0, 'cptm': 0.5, 'loc': [], 'location': 124, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '373-0', 'capacity': 5, 'cpm': 1.0, 'cptm': 1.5, 'loc': [], 'location': 373, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '373-1', 'capacity': 5, 'cpm': 1.0, 'cptm': 1.5, 'loc': [], 'location': 373, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '373-2', 'capacity': 5, 'cpm': 1.0, 'cptm': 1.5, 'loc': [], 'location': 373, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '373-3', 'capacity': 12, 'cpm': 1.5, 'cptm': 1.0, 'loc': [], 'location': 373, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '373-4', 'capacity': 12, 'cpm': 1.5, 'cptm': 1.0, 'loc': [], 'location': 373, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '373-5', 'capacity': 12, 'cpm': 1.5, 'cptm': 1.0, 'loc': [], 'location': 373, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '373-6', 'capacity': 12, 'cpm': 1.5, 'cptm': 1.0, 'loc': [], 'location': 373, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '373-7', 'capacity': 22, 'cpm': 2.0, 'cptm': 0.5, 'loc': [], 'location': 373, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '373-8', 'capacity': 22, 'cpm': 2.0, 'cptm': 0.5, 'loc': [], 'location': 373, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '373-9', 'capacity': 22, 'cpm': 2.0, 'cptm': 0.5, 'loc': [], 'location': 373, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '116-0', 'capacity': 5, 'cpm': 1.0, 'cptm': 1.5, 'loc': [], 'location': 116, 'current': 0, 'stops': 0, 'miles': 0}, {'lorry_id': '116-1', 'capacity': 12, 'cpm': 1.5, 'cptm': 1.0, 'loc': [], 'location': 116, 'current': 0, 'stops': 0, 'miles': 0}]
costs={'523-0': [1.0, 1.5], '523-1': [1.0, 1.5], '523-2': [1.5, 1.0], '523-3': [1.5, 1.0], '523-4': [2.0, 0.5], '124-0': [1.0, 1.5], '124-1': [1.0, 1.5], '124-2': [1.0, 1.5], '124-3': [1.5, 1.0], '124-4': [1.5, 1.0], '124-5': [1.5, 1.0], '124-6': [2.0, 0.5], '124-7': [2.0, 0.5], '373-0': [1.0, 1.5], '373-1': [1.0, 1.5], '373-2': [1.0, 1.5], '373-3': [1.5, 1.0], '373-4': [1.5, 1.0], '373-5': [1.5, 1.0], '373-6': [1.5, 1.0], '373-7': [2.0, 0.5], '373-8': [2.0, 0.5], '373-9': [2.0, 0.5], '116-0': [1.0, 1.5], '116-1': [1.5, 1.0]}
for i in range(0,len(lorries)):
  lorries[i]['current']=lorries[i]['capacity']
# Callback function to compute the cost from a particular lorry to a customer
def delivery_cost(v,c,location,current_volume):
  
  total_cost=0
  lorry_id=lorries[v]['lorry_id']
  total_gas=0
  
  available=current_volume-demands[c]['demand']
  given_to_others=0
  target=demands[c]['id']
 
  
  journey=nx.single_source_dijkstra(g,source=location,target=target,weight='weight')
  
  for i in range(1,len(journey[1])):
      if(i<len(journey)-1 and available>0):

        if(journey[1][i] in custo_ids and available>=demands[c]['demand']):
          id=journey[1][i]
          indice=custo_ids.index(journey[1][i])

          distance=nx.single_source_dijkstra(g,source=location,target=id,weight='weight')[0]
          
          miles_cost=costs['lorry_id'][0]*distance
          tonnes_cost=costs['lorry_id'][1]*current_volume
          total_cost+=(miles_cost+tonnes_cost)
          current_volume-=demands[indice]['demand']
          available-=demands[indice]['demand']
          location=demands[indice]['id']
         
        elif(journey[1][i] in custo_ids and available<demands[indice]['demand'] and available>0):

          id=journey[1][i]
          indice=custo_ids.index(journey[1][i])
          distance=nx.single_source_dijkstra(g,source=lorries[v]['location'],target=id,weight='weight')[0]
          miles_cost=costs[lorry_id][0]*distance
          tonnes_cost=costs[lorry_id][1]*current_volume
          total_cost+=(miles_cost+tonnes_cost)
          current_volume-=available
          
          available=0
          location=lorries[indice]['id']
        
      elif(i==len(journey)-1):
        distance=nx.single_source_dijkstra(g,source=location,target=target,weight='weight')[0]
        miles_cost=costs[lorry_id][0]*distance
        tonnes_cost=costs[lorry_id][1]*current_volume
        total_cost+=(miles_cost+tonnes_cost)
        current_volume-=demands[c]['demand']
        location=demands[c]['id']
        
        
  
  return total_cost
  # Calculating the delivery cost by also taking into account the journey to the depot  
def depot_and_delivery_cost(v,c,location,current_volume):
  total_cost=0
  cost_to_depot=0
  
  depot=nearby_depot(location)
  lorry_id=lorries[v]['lorry_id']
  journey=nx.single_source_dijkstra(g,source=location,target=depot,weight='weight')[1]
  for i in range(1,len(journey)):

    if(i<len(journey)-1):
         id=journey[i]
         
         if(id in custo_ids and current_volume>=demands[custo_ids.index(id)]['demand']):
           indice=custo_ids.index(id)
           distance=nx.single_source_dijkstra(g,source=location,target=id,weight='weight')[0]
           miles_cost=costs[lorry_id][0]*distance
           tonnes_cost=costs[lorry_id][1]*current_volume
           cost_to_depot+=(miles_cost+tonnes_cost)
           current_volume-=demands[indice]['demand']
           location=id
          
           
         elif(id in custo_ids and current_volume>0 and current_volume<demands[custo_ids.index(id)]['demand']):
            distance=nx.single_source_dijkstra(g,source=location,target=id,weight='weight')[0]
            miles_cost=costs[lorry_id][0]*distance
            tonnes_cost=costs[lorry_id][1]*current_volume
            cost_to_depot+=(miles_cost+tonnes_cost)
            current_volume=0
            location=id
    elif i==len(journey)-1:

        
      distance=nx.single_source_dijkstra(g,source=location,target=depot,weight='weight')[0]
        
      miles_cost=costs[lorry_id][0]*distance
      tonnes_cost=costs[lorry_id][1]*current_volume
      cost_to_depot+=(miles_cost+tonnes_cost)
      current_volume=lorries[v]['capacity']
      location=depot
      
      total_cost=cost_to_depot+deliver_cost(v,c,location,current_volume)
  return total_cost
# Extracting the cheapest path by taking into account the lorries costs and their locations repesctive to the customers locations. 
def cheapest_path():
  path={}
 
  for i in range(0,len(lorries)):
    if lorries[i]['current']>=demands[0]['demand']:
      cheapest=deliver_cost(i,0,lorries[i]['location'],lorries[i]['current'])
      path['v']=i
      path['c']=0
      break
  for i in range(len(lorries)):
    for j in range(len(demands)):
      if(lorries[i]['current']>=demands[j]['demand']):
        cost=deliver_cost(i,j,lorries[i]['location'],lorries[i]['current'])
      else:
        cost=depot_and_deliver_cost(i,j,lorries[i]['location'],lorries[i]['current'])
      
      if(cost<cheapest):
        cheapest=cost
        path['v']=i
        path['c']=j
  
  return path
# After finding the cheapest path, the lorry deliver petroleum to the customer
def delivery(v,c,journey):
 
  given_to_others=0
  
  available=lorries[v]['current']-demands[c]['demand']
  for i in range(1,len(journey)):
    if(i<len(journey)-1 and available>0):


        if(journey[i] in custo_ids):
           id=journey[i]
           index=custo_ids.index(id)
   
           if(available>=demands[index]['demand'] and i<len(journey)-1):
              lorries[v]['loc'].append([demands[index]['id'],-demands[index]['demand']])
              available-=demands[index]['demand']
            
              given_to_others+=demands[index]['demand']
              demands[index]['demand']=0
        
         
         
              lorries[v]['location']=demands[index]['id']
              del demands[index]
              del custo_ids[index]
           elif(available<demands[index]['demand'] and i<len(journey)-1 and available>0 and demands[index]['id']==journey[i]):
              demands[index]['demand']-=available
              lorries[v]['loc'].append([demands[index]['id'],-available])
              given_to_others+=available
              available=0
        
              lorries[v]['location']=demands[index]['id']

    elif(i==len(journey)-1):
         id=journey[i]
         index=custo_ids.index(id)
         lorries[v]['current']-=demands[index]['demand']
         lorries[v]['loc'].append([demands[index]['id'],-demands[index]['demand']])
         demands[index]['demand']=0
         lorries[v]['location']=demands[index]['id']
         del demands[index]
         del custo_ids[index]
        #print('done')

  lorries[v]['current']-=given_to_others

def nearby_depot(location):
  closest=depots[0]['id']
  distance=nx.single_source_dijkstra(g,source=location,target=depots[0]['id'],weight='weight')[0]
  for i in range(len(depots)):
    
    current_distance=nx.single_source_dijkstra(g,source=location,target=depots[i]['id'],weight='weight')[0]
    if(current_distance<distance):
      closest=depots[i]['id']
      distance=current_distance
  return closest
# If the lorry doesn't have enough gas, it will first go to the depot and subsequently deliver to the customer. 
def depot_and_deliver(v,c,end):
  
  depot=nearby_depot(lorries[v]['location'])
  journey_to_depot=journey=nx.shortest_path(g,source=lorries[v]['location'],target=depot,weight='weight')
  for i in range(1,len(journey_to_depot)):
    if(i<len(journey_to_depot)-1):

         if(journey_to_depot[i] in custo_ids):
            indice=custo_ids.index(journey_to_depot[i])
            if(lorries[v]['current']>0 and lorries[v]['current']>=demands[indice]['demand']):
               lorries[v]['current']-=demands[indice]['demand']
               lorries[v]['loc'].append([demands[indice]['id'],-demands[indice]['demand']])
               demands[indice]['demand']=0
               lorries[v]['location']=demands[indice]['id']
               del demands[indice]
               del custo_ids[indice]
         elif(lorries[v]['current']>0 and lorries[v]['current']<demands[indice]['demand']):
               demands[indice]['demand']-=lorries[v]['current']
               lorries[v]['loc'].append([demands[indice]['id'],-lorries[v]['current']])
               lorries[v]['current']=0
               lorries[v]['location']=demands[indice]['id']
    elif i==len(journey_to_depot)-1:

  
          lorries[v]['location']=depot
          load=lorries[v]['capacity']-lorries[v]['current']
          lorries[v]['current']=lorries[v]['capacity']
          lorries[v]['loc'].append([depot,load])
          lorries[v]['location']=depot
  
  journey=nx.shortest_path(g,source=depot,target=end,weight='weight')
  
  deliver(v,c,journey)
 
# Finding the lorries which have at least made one journey
def have_delivered(lorries):
  journeys=[]
  for i in range(len(lorries)):
    if(len(lorries[i]['loc'])>1):
      
      journeys.append({'lorry_id':lorries[i]['lorry_id'],'loc':lorries[i]['loc']})
  return journeys
# ALl lorries go back to their depots
def back_to_depot(have_worked):
  for i in range (len(have_worked)):
    start=have_worked[i]['loc'][0][0]
    have_worked[i]['loc'].append([start,0])
  return have_worked

def main():
    
   
    def pers():
      
        
        while len(custo_ids)>0:
           
          
            
           
            path=cheapest_path()
            v=path['v']
            c=path['c']
            end=custo_ids[c]
            if(len(lorries[v]['loc'])==0):
              
              lorries[v]['current']=lorries[v]['capacity']
              lorries[v]['loc'].append([lorries[v]['location'],lorries[v]['current']])
            

       
            if lorries[v]['current']>0 and lorries[v]['current']>=demands[c]['demand']:
               journey=nx.shortest_path(g,source=lorries[v]['location'],target=end,weight='weight')
              
               deliver(v,c,journey)
            elif lorries [v]['current']<demands[c]['demand']:
              depot_and_deliver(v,c,end)
           
        have_worked=have_delivered(lorries)
        
        return have_worked
    
    return pers() 


solution=main()
print(json.dumps(solution))

