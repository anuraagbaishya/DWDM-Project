import pandas as pd
from collections import defaultdict


def getfromfile(a):
    returnvalue = []
    for n in a:
        returnvalue.append(n)
    return returnvalue


def getcount(a):
    hashcollection = defaultdict(list)
    counted = []
    for i in a:
        count = 0
        if i not in counted:
            for col in a:
                if i == col:
                    count += 1
            hashcollection[count].append(i)
            counteddirectors.append(i)
    return hashcollection


def getcountactors(hashcollection, counted, a, act1, act2, act3):
    for actor in a:
        count = 0
        if actor not in counted:
            for col in act1:
                if actor == col:
                    count += 1
            for col in act2:
                if actor == col:
                    count += 1
            for col in act3:
                if actor == col:
                    count += 1
            hashcollection[count].append(actor)
            counted.append(actor)
    return counted, hashcollection


def putfrequency(hashmap1, col):
    for n in range(len(col)):
        count = 0
        for key, value in hashmap1.iteritems():
            if col[n] in value:
                count = key
                break
        col[n] = count
    return col

hashmap = defaultdict(list)
hashdirectors = defaultdict(list)
fields = ["director_name", "actor_1_name", "actor_2_name", "actor_3_name", "plot_keywords", "gross"]
dataset = pd.read_csv("new_data.csv", usecols=fields)
act_1 = getfromfile(dataset.actor_1_name)
act_2 = getfromfile(dataset.actor_2_name)
act_3 = getfromfile(dataset.actor_3_name)
dir_names = getfromfile(dataset.director_name)
gross = []
plot_keywords = getfromfile(dataset.plot_keywords)
countedactors = []
counteddirectors = []

for n in dataset.gross:
    gross.append(str(n))

hashdirectors = getcount(dir_names)
countedactors, hashmap=getcountactors(hashmap, countedactors, act_1, act_1, act_2, act_3)
countedactors, hashmap=getcountactors(hashmap, countedactors, act_2, act_1, act_2, act_3)
countedactors, hashmap=getcountactors(hashmap, countedactors, act_3, act_1, act_2, act_3)

dir_names = putfrequency(hashdirectors, dir_names)
act_1 = putfrequency(hashmap, act_1)
act_2 = putfrequency(hashmap, act_2)
act_3 = putfrequency(hashmap, act_3)
data = []
print(act_1)
for i in range(len(plot_keywords)):
    row = (dir_names[i], act_1[i], act_2[i], act_3[i], plot_keywords[i], str(gross[i]))
    data.append(row)
df = pd.DataFrame(data)
df.columns = ["director_name", "actor_1_name", "actor_2_name", "actor_3_name", "plot_keywords", "gross"]
df.to_csv("sorted_data1.csv")

print("hello")
print(hashmap)


