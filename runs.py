import csv, re
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
results=[];runs=[]
with open('./ipl/matches.csv') as File: 
    reader = csv.DictReader(File)
    for row in reader:
        if row['season']=='2016':
            results.append((row['id']))
with open('./ipl/deliveries.csv') as File: 
    read = csv.DictReader(File)
    for row in read:
        if row['match_id'] in results:
            runs.append((row['batting_team'],row['extra_runs']))
totalruns={}
for i in runs:
    if i[0] in totalruns:
        totalruns[i[0]] += int(i[1])
    else:
        totalruns[i[0]] = int(i[1])
x,y = zip(*totalruns.items())
plt.bar(x,y,color=['yellow','green'])
plt.xticks(np.arange(len(totalruns.keys())),[''.join(re.findall(r'([A-Z])',s)) for s in totalruns.keys()])
plt.xlabel('Teams')
plt.ylabel('Runs')
plt.title('Runs Conceded in 2016')
plt.show()