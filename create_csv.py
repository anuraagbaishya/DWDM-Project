import pandas as pd


def getfromfile(a):
    returnvalue = []
    for n in a:
        returnvalue.append(n)
    return returnvalue


def uniquefn(uniquekey, col):
    for n in col:
        if n not in uniquekey:
            uniquekey.append(n)
    return uniquekey


def process(uniquekey, col):
    clusterfinal = []
    for n in range(len(col)):
        for x in range(len(uniquekey)):
            if col[n] is uniquekey[x]:
                clusterfinal.insert(n, x)
    return clusterfinal


fields = ["director_name", "actor_1_name", "actor_2_name", "actor_3_name", "gross", "genres"]
dataset = pd.read_csv("movie_metadata.csv", usecols=fields)
dataset = dataset.dropna(subset=["gross"])
dataset = dataset.dropna(subset=["genres"])
genres_keywords = dict()

genres = getfromfile(dataset.genres)
dir_names = getfromfile(dataset.director_name)
act_1 = getfromfile(dataset.actor_1_name)
act_2 = getfromfile(dataset.actor_2_name)
act_3 = getfromfile(dataset.actor_3_name)
gross = []
for n in dataset.gross:
    gross.append(str(n))
data = []
print (genres)

index = 0

for i in genres:
    genres_final = []
    keywords = i.split("|")
    for w in keywords:
        if len(w.split()) > 1:
            ws = w.split(" ")
            for x in ws:
                    genres_final.append(x)
    genres_keywords[str(index)] = genres_final
    index += 1

for i in range(len(genres_keywords)):
    wlist = genres_keywords[str(i)]
    for w in wlist:
        row = (dir_names[i], act_1[i], act_2[i], act_3[i], w, str(gross[i]))
        data.append(row)

df = pd.DataFrame(data)
df.columns = ["director_name", "actor_1_name", "actor_2_name", "actor_3_name", "genres", "gross"]
df.to_csv("new_data2.csv")

new_df = pd.read_csv("new_data2.csv")
dirs = getfromfile(new_df.director_name)
act1 = getfromfile(new_df.actor_1_name)
act2 = getfromfile(new_df.actor_2_name)
act3 = getfromfile(new_df.actor_3_name)

unique_dirs, dir_cluster = [], []
unique_act1, act1_cluster = [], []
unique_act2, act2_cluster = [], []
unique_act3, act3_cluster = [], []
cluster_data = []
unique_dirs = uniquefn(unique_dirs, dirs)
unique_act1 = uniquefn(unique_act1, act1)
unique_act2 = uniquefn(unique_act2, act2)
unique_act3 = uniquefn(unique_act3, act3)

dir_cluster = process(unique_dirs, dirs)
act1_cluster = process(unique_act1, act1)
act2_cluster = process(unique_act2, act2)
act3_cluster = process(unique_act3, act3)

print(dir_cluster)
print(act1_cluster)

for n in range(len(dir_cluster)):
    cluster_data.append((dir_cluster[n], act1_cluster[n], act2_cluster[n], act3_cluster[n], df.genres[n], df.gross[n]))
df = pd.DataFrame(cluster_data)
df.columns = ["director_name", "actor_1", "actor_2", "actor_3", "genres", "gross"]
df.to_csv("cluster_data1.csv")