import pandas as pd
from collections import defaultdict


def getfromfile(a):
    returnvalue = []
    for n in a:
        returnvalue.append(n)
    return returnvalue


def getcount(a, genres):
    hashcollection = defaultdict(list)
    counted = []
    for i in range(len(a)):
        avalue = a[i]
        genrevalue = genres[i]
        count = 0
        checkvalue = (str(avalue) + "," + str(genrevalue))
        if checkvalue not in counted:
            for x in range(len(a)):
                if avalue == a[x] and genrevalue == genres[x]:
                    count += 1
            hashcollection[count].append(checkvalue)
            counteddirectors.append(checkvalue)
    return hashcollection


def getcountactors(hashcollection, counted, a, act1, act2, act3, genres):
    for i in range(len(a)):
        count = 0
        actor = a[i]
        genre = genres[i]
        checkvalue = str(actor) + "," + str(genre)
        if checkvalue not in counted:
            for x in range(len(act1)):
                if actor == act1[x] and genre == genres[x]:
                    count += 1
            for x in range(len(act2)):
                if actor == act2[x] and genre == genres[x]:
                    count += 1
            for x in range(len(act1)):
                if actor == act3[x] and genre == genres[x]:
                    count += 1
            hashcollection[count].append(checkvalue)
            counted.append(checkvalue)
    return counted, hashcollection


def putfrequency(hashmap1, col, genres):
    for n in range(len(col)):
        count = 0
        for key, value in hashmap1.iteritems():
            cvalue = col[n]
            genre = genres[n]
            checkvalue = str(cvalue) + "," + str(genre)
            if checkvalue in value:
                count = key
                break
        col[n] = count
    return col

hashmap = defaultdict(list)
hashdirectors = defaultdict(list)
fields = ["director_name", "actor_1_name", "actor_2_name", "actor_3_name", "genres", "gross"]
dataset = pd.read_csv("new_data2.csv", usecols=fields)
act_1 = getfromfile(dataset.actor_1_name)
act_2 = getfromfile(dataset.actor_2_name)
act_3 = getfromfile(dataset.actor_3_name)
dir_names = getfromfile(dataset.director_name)
gross = []
genres = getfromfile(dataset.genres)
countedactors = []
counteddirectors = []

for n in dataset.gross:
    gross.append(str(n))

hashdirectors = getcount(dir_names, genres)
countedactors, hashmap = getcountactors(hashmap, countedactors, act_1, act_1, act_2, act_3, genres)
countedactors, hashmap = getcountactors(hashmap, countedactors, act_2, act_1, act_2, act_3, genres)
countedactors, hashmap = getcountactors(hashmap, countedactors, act_3, act_1, act_2, act_3, genres)

dir_names = putfrequency(hashdirectors, dir_names, genres)
act_1 = putfrequency(hashmap, act_1, genres)
act_2 = putfrequency(hashmap, act_2, genres)
act_3 = putfrequency(hashmap, act_3, genres)
data = []
print(act_1)
for i in range(len(genres)):
    row = (dir_names[i], act_1[i], act_2[i], act_3[i], genres[i], str(gross[i]))
    data.append(row)
df = pd.DataFrame(data)
df.columns = ["director_name", "actor_1_name", "actor_2_name", "actor_3_name", "genres", "gross"]
df.to_csv("sorted_data2.csv")

print("hello")
print(hashmap)
