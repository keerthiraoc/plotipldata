import csv, re
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
results=[]
with open('./ipl/matches.csv') as File: 
    reader = csv.DictReader(File)
    for row in reader:
        results.append((row['season'],row['winner']))
    res = [i[0]+i[1]+str(j) for i,j in Counter(results).items()]
    res.sort()
    a = [re.findall(r'(\d+)([a-zA-Z ]*)(\d+)',i) for i in res]
    years = [i for i in range(2008,2018)]
    teams = list(set(
        [i[0][1] for i in a]))
    arr = np.zeros((len(teams),len(years)), dtype = int)
    for i in a:
        arr[teams.index(i[0][1])][int(i[0][0])%2008] = i[0][2]
    print(arr)
    x = np.arange(arr.shape[0])
    fig, ax = plt.subplots()
    for i in range(arr.shape[1]):
        bottom = np.sum(arr[:,0:i], axis = 1)
        ax.bar(x, arr[:,i], bottom=bottom, label='Year {}'.format(i+2008))
    plt.ylabel("Matches")
    plt.xlabel("Teams")
    plt.xticks(np.arange(len(teams)),[''.join(re.findall(r'([A-Z])',s)) for s in teams], fontSize=8)
    plt.legend(framealpha=1).draggable()
    plt.show()