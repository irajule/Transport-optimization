# Question: optimizing the transportation cost
# #Data: 25 lorries with capacities: 5, 10, 15 and 20 tonnes, 123 customers and 4 depots. 
#Constraints:
#a. lorries capacity
#b. Each lorry can't travel more than 250 miles
#c. Each lorry can't make more than 5 stops.
#d. Each lorry has to end its journey in one of the depots.
import pandas as pd
import numpy as np
import math
import networkx as nx

# Data loading
df = pd.read_csv('/locations.csv')
df1 = pd.read_csv('/links.csv')

# Extracting coordinates and customer data
coordinates = df[['x', 'y']].to_numpy()
custo_ids = [5, 8, 13, 14, 22, 27, 29, 31, 32, 36, 41, 44, 63, 64, 65, 70, 73, 77, 78, 80, 82, 86, 94, 100, 103, 105, 110, 113, 118, 130, 135, 136, 144, 146, 147, 160, 169, 171, 172, 175, 177, 180, 183, 190, 200, 202, 204, 205, 206, 210, 214, 216, 220, 225, 235, 243, 245, 254, 255, 257, 260, 264, 265, 270, 271, 274, 276, 294, 308, 324, 332, 337, 362, 364, 372, 374, 377, 378, 380, 387, 389, 391, 393, 397, 398, 400, 408, 411, 418, 431, 437, 446, 449, 453, 455, 459, 474, 476, 491, 497, 507, 511, 519, 520, 528, 531, 534, 539, 542, 543, 547, 550, 566, 569, 584, 585, 598, 603, 606, 621, 624, 632, 633]
demands = [{'id': i, 'demand': d} for i, d in enumerate([0.1, 0.2, ...])]  # Ensure this list matches your data

# Construct the graph
g = nx.Graph()
for _, row in df1.iterrows():
    id1, id2 = int(row['id1']), int(row['id2'])
    dist = np.linalg.norm(coordinates[id1] - coordinates[id2])
    g.add_edge(id1, id2, weight=dist)

# Define lorries
lorries = [{'lorry_id': '523-0', 'capacity': 5, 'cpm': 1.0, 'cptm': 1.5, 'location': 523}, ...]

# Initialize lorries
for lorry in lorries:
    lorry['current'] = lorry['capacity']

# Cost functions
def calculate_delivery_cost(start, end, lorry):
    path_length = nx.shortest_path_length(g, source=start, target=end, weight='weight')
    return lorry['cpm'] * path_length + lorry['cptm'] * lorry['capacity']

def get_nearest_depot(location):
    # Returns the nearest depot from a given location
    distances = {d: nx.shortest_path_length(g, source=location, target=d, weight='weight') for d in [l['location'] for l in lorries]}
    return min(distances, key=distances.get)

def calculate_total_cost(lorry, depot, customer):
    # Calculates the total cost including depot to customer delivery
    cost_to_depot = nx.shortest_path_length(g, source=lorry['location'], target=depot, weight='weight') * lorry['cpm']
    cost_delivery = calculate_delivery_cost(depot, customer['id'], lorry)
    return cost_to_depot + cost_delivery

# Optimization function
def optimize_delivery():
    best_cost = float('inf')
    best_assignment = None

    for lorry in lorries:
        depot = get_nearest_depot(lorry['location'])
        for customer in demands:
            cost = calculate_total_cost(lorry, depot, customer)
            if cost < best_cost:
                best_cost = cost
                best_assignment = {'lorry': lorry['lorry_id'], 'customer': customer['id'], 'depot': depot, 'cost': best_cost}
    
    return best_assignment

# Run optimization
best_assignment = optimize_delivery()
print(f"Best assignment: {best_assignment}")
