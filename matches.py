import csv
from collections import Counter
import matplotlib.pyplot as plt

results=[]
with open('./ipl/matches.csv') as File:
    reader = csv.DictReader(File)
    for row in reader:
        results.append(row['season'])
    x,y = zip(*sorted(Counter(results).items()))
    plt.bar(x,y,color=['green','red'])
    plt.xlabel('years')
    plt.ylabel('matches')
    plt.title('matches played in a year')
    plt.show()