import pandas as pd
from collections import defaultdict
hashmap = defaultdict(list)
hashdirectors = defaultdict(list)
fields = ["director_name", "actor_1_name", "actor_2_name", "actor_3_name", "plot_keywords", "gross"]
dataset = pd.read_csv("new_data.csv", usecols=fields)
act_1 = []
act_2 = []
act_3 = []
dir_names = []
gross = []
plot_keywords = []
countedactors = []
counteddirectors = []

for n in dataset.plot_keywords:
    plot_keywords.append(n)
for n in dataset.director_name:
    dir_names.append(n)
for n in dataset.gross:
    gross.append(str(n))
for n in dataset.actor_1_name:
    act_1.append(n)
for n in dataset.actor_2_name:
    act_2.append(n)
for n in dataset.actor_3_name:
    act_3.append(n)

for director in dir_names:
    count = 0
    if director not in counteddirectors:
        for col in dir_names:
            if director == col:
                count += 1
        hashdirectors[count].append(director)
        counteddirectors.append(director)
for actor in act_1:
    count = 0
    if actor not in countedactors:
        for col in act_1:
            if actor == col:
                count += 1
        for col in act_2:
            if actor == col:
                count += 1
        for col in act_3:
            if actor == col:
                count += 1
        hashmap[count].append(actor)
        countedactors.append(actor)
for actor in act_2:
    count = 0
    if actor not in countedactors:
        for col in act_1:
            if actor == col:
                count += 1
        for col in act_2:
            if actor == col:
                count += 1
        for col in act_3:
            if actor == col:
                count += 1
        hashmap[count].append(actor)
        countedactors.append(actor)
for actor in act_3:
    count = 0
    if actor not in countedactors:
        for col in act_1:
            if actor == col:
                count += 1
        for col in act_2:
            if actor == col:
                count += 1
        for col in act_3:
            if actor == col:
                count += 1
        hashmap[count].append(actor)
        countedactors.append(actor)

for n in range(len(dir_names)):
    count = 0
    for key, value in hashdirectors.iteritems():
        if dir_names[n] in value:
            count = key
            break
    dir_names[n] = count
for n in range(len(act_1)):
    count = 0
    for key, value in hashmap.iteritems():
        if act_1[n] in value:
            count = key
            break
    act_1[n] = count
for n in range(len(act_2)):
    count = 0
    for key, value in hashmap.iteritems():
        if act_2[n] in value:
            count = key
            break
    act_2[n] = count
for n in range(len(act_3)):
    count = 0
    for key, value in hashmap.iteritems():
        if act_3[n] in value:
            count = key
            break
    act_3[n] = count
data = []
print(act_1)
for i in range(len(plot_keywords)):
    row = (dir_names[i], act_1[i], act_2[i], act_3[i], plot_keywords[i], str(gross[i]))
    data.append(row)
df = pd.DataFrame(data)
df.columns = ["director_name", "actor_1_name", "actor_2_name", "actor_3_name", "plot_keywords", "gross"]
df.to_csv("sorted_data.csv")

print("hello")
print(hashmap)


