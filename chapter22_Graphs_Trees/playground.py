# #nodes and edges
# class node:
#     def __init__(self, name, population=0):
#         self._name = name
#         self._pop = population
#     def getName(self):
#         return self._name
#     def getPopulation(self):
#         return self._pop
# class edge:
#     def __init__(self, name1, name2, weight=0):
#         self._city1 = name1
#         self._city2 = name2
#         self._distance = weight
#     def getName1(self):
#         return self._city1
#     def getName2(self):
#         return self._city2
#     def getNames(self):
#         return (self._city1, self._city2)
#     def getWeight(self):
#         return self._distance
#
# #set up nodes list
# cities = []
# roads = []
# city = node('Rivertown', 1000)
# cities.append(city)
# city = node('Brookside', 1500)
# cities.append(city)
# city = node('Hillsview', 500)
# cities.append(city)
# city = node('Forrest City', 800)
# cities.append(city)
# city = node('Lakeside', 1100)
# cities.append(city)
# road = edge('Rivertown', 'Brookside', 100)
# roads.append(road)
# road = edge('Rivertown', 'Hillsview', 50)
# roads.append(road)
# road = edge('Hillsview', 'Brookside', 130)
# roads.append(road)
# road = edge('Hillsview', 'Forrest City', 40)
# roads.append(road)
# road = edge('Forrest City', 'Lakeside', 80)
# roads.append(road)
# #example of calculation of people living in the first edge (road)
# road = roads[0]
# pop1 = 0
# pop2 = 0
# for city in cities:
#     if city.getName() == road.getName1():
#         pop1 = city.getPopulation()
#     if city.getName() == road.getName2():
#         pop2 = city.getPopulation()
# total_population = pop2 + pop1

# class node:
#     def __init__(self, name, population=0):
#         self._name = name
#         self._pop = population
#     def getName(self):
#         return self._name
#     def getPopulation(self):
#         return self._pop
# class edge:
#     def __init__(self, index1, index2, weight=0):
#         self._city1 = index1
#         self._city2 = index2
#         self._distance = weight
#     def getIndex1(self):
#         return self._city1
#     def getIndex2(self):
#         return self._city2
#     def getIndices(self):
#         return (self._city1, self._city2)
#     def getWeight(self):
#         return self._distance
#
# #set up nodes list
# cities = []
# roads = []
# city = node('Rivertown', 1000)
# cities.append(city)
# city = node('Brookside', 1500)
# cities.append(city)
# city = node('Hillsview', 500)
# cities.append(city)
# city = node('Forrest City', 800)
# cities.append(city)
# city = node('Lakeside', 1100)
# cities.append(city)
# road = edge(1, 2, 100)
# roads.append(road)
# road = edge(2, 3, 50)
# roads.append(road)
# road = edge(3, 2, 130)
# roads.append(road)
# road = edge(3, 4, 40)
# roads.append(road)
# road = edge(4, 5, 80)
# roads.append(road)
# #example of calculation of people living in the first edge (road)
# road = roads[1]
# pop1 = cities[road.getIndex1()].getPopulation()
# pop2 = cities[road.getIndex2()].getPopulation()
# total_population = pop2 + pop1
# print(total_population)

# edges inside node class

class node:
    #variable intended for internal use => like private property
    def __init__(self, name,edges, population=0):
        self._name = name
        self._pop = population
        self._edges = edges
    def getName(self):
        return self._name
    def getPopulation(self):
        return self._pop
    def getEdge(self):
        return self.edge

cities = []
city = node('Rivertown',[['Rivertown', 'Brookside', 100],['Rivertown', 'Hillsview', 50]] ,1000)
cities.append(city)
# city = node('Brookside', 1500)
# cities.append(city)
# city = node('Hillsview', 500)
# cities.append(city)
# city = node('Forrest City', 800)
# cities.append(city)
# city = node('Lakeside', 1100)
# cities.append(city)
# road = edge('Rivertown', 'Brookside', 100)
# roads.append(road)
# road = edge('Rivertown', 'Hillsview', 50)
# roads.append(road)
# road = edge('Hillsview', 'Brookside', 130)
# roads.append(road)
# road = edge('Hillsview', 'Forrest City', 40)
# roads.append(road)
# road = edge('Forrest City', 'Lakeside', 80)
# roads.append(road)