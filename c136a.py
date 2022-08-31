import pandas as pd
df = pd.read_csv('starWithGravity.csv')
print(df.head())
df.drop(['Unnamed: 0'], axis = 1, inplace = True)
name = df['Star_name'].to_list()
mass = df['Mass'].to_list()
radius = df['Radius'].to_list()
dist = df['Distance'].to_list()
gravity = df['Gravity'].to_list()
finalStarList = []
tempDict = {}
for i in range(0, len(name)):
    tempDict['name'] = name[i]
    tempDict['mass'] = mass[i]
    tempDict['radius'] = radius[i]
    tempDict['distance'] = dist[i]
    tempDict['gravity'] = gravity[i]
    finalStarList.append(tempDict)
    tempDict = {}
print(finalStarList)