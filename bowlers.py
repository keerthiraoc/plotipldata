import csv, re
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
results=[];runs=[]
with open('./ipl/matches.csv') as File: 
    reader = csv.DictReader(File)
    for row in reader:
        if row['season']=='2015':
            results.append((row['id']))
with open('./ipl/deliveries.csv') as File: 
    read = csv.DictReader(File)
    for row in read:
        if row['match_id'] in results:
            runs.append((row['bowler'],row['total_runs']))
totalruns={}
for i in runs:
    if i[0] in totalruns:
        totalruns[i[0]] = [totalruns[i[0]][0]+int(i[1]),totalruns[i[0]][1]+1]
    else:
        totalruns[i[0]] = [int(i[1]), 1]
for i,j in totalruns.items():
    totalruns[i] = j[0]/(j[1]/6)
min=sorted(totalruns.items(), key=lambda kv:kv[1])[:5]
x,y = zip(*min)
plt.bar(x,y,color=['yellow','green'], width=0.4)
plt.xlabel('Bowler Name')
plt.ylabel('Economy rate')
plt.title('Economy of Bowlers in 2015')
plt.show()