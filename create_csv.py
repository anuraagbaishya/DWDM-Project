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


fields = ["director_name", "actor_1_name", "actor_2_name", "actor_3_name", "plot_keywords", "gross"]
dataset = pd.read_csv("movie_metadata.csv", usecols=fields)
dataset = dataset.dropna(subset=["plot_keywords"])
dataset = dataset.dropna(subset=["gross"])
plot_keywords = dataset.plot_keywords
unique_plot_keywords = dict()

dir_names = getfromfile(dataset.director_name)
act_1 = getfromfile(dataset.actor_1_name)
act_2 = getfromfile(dataset.actor_2_name)
act_3 = getfromfile(dataset.actor_3_name)
gross = []
for n in dataset.gross:
    gross.append(str(n))
data = []

filter ='with at from into during including until against among throughout despite towards upon concerning of\
          to in for on by about like through over before between after since without under within along \
following across behind beyond plus except but up out around down up out around down off above near'

filter_words = filter.split(' ')
index = 0

for i in plot_keywords:
    plot_kword_final = []
    keywords = i.split("|")
    for w in keywords:
        if len(w.split()) > 1:
            ws = w.split(" ")
            for x in ws:
                if x not in plot_kword_final and x not in filter_words:
                    plot_kword_final.append(x)
        elif w not in plot_keywords:
            plot_kword_final.append(w)
    unique_plot_keywords[str(index)] = plot_kword_final
    index += 1

for i in range(len(unique_plot_keywords)):
    wlist = unique_plot_keywords[str(i)]
    for w in wlist:
        row = (dir_names[i], act_1[i], act_2[i], act_3[i], w, str(gross[i]))
        data.append(row)

df = pd.DataFrame(data)
df.columns = ["director_name", "actor_1_name", "actor_2_name", "actor_3_name", "plot_keywords", "gross"]
df.to_csv("new_data1.csv")

new_df = pd.read_csv("new_data.csv")
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
    cluster_data.append((dir_cluster[n], act1_cluster[n], act2_cluster[n], act3_cluster[n], df.plot_keywords[n], df.gross[n]))
df = pd.DataFrame(cluster_data)
df.columns = ["director_name", "actor_1", "actor_2", "actor_3", "plot_keywords", "gross"]
df.to_csv("cluster_data1.csv")