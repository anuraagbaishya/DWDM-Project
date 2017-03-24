import pandas as pd

fields = ["director_name", "actor_1_name", "actor_2_name", "actor_3_name", "plot_keywords", "gross"]
dataset = pd.read_csv("movie_metadata.csv", usecols=fields)
dataset = dataset.dropna(subset=["plot_keywords"])
dataset = dataset.dropna(subset=["gross"])
plot_keywords = dataset.plot_keywords
unique_plot_keywords = dict()

dir_names = []
act_1 = []
act_2 = []
act_3 = []
gross = []
for n in dataset.director_name:
    dir_names.append(n)
for n in dataset.actor_1_name:
    act_1.append(n)
for n in dataset.actor_2_name:
    act_2.append(n)
for n in dataset.actor_3_name:
    act_3.append(n)
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
df.to_csv("new_data.csv")

dirs, act1 = [], []
act2, act3 = [], []

new_df = pd.read_csv("new_data.csv")
for n in new_df.director_name:
    dirs.append(n)

for n in new_df.actor_1_name:
    act1.append(n)

for n in new_df.actor_2_name:
    act2.append(n)

for n in new_df.actor_3_name:
    act3.append(n)

unique_dirs, dir_cluster = [], []
unique_act1, act1_cluster = [], []
unique_act2, act2_cluster = [], []
unique_act3, act3_cluster = [], []
cluster_data = []
for n in dirs:
    if n not in unique_dirs:
        unique_dirs.append(n)

for n in act1:
    if n not in unique_act1:
        unique_act1.append(n)

for n in act3:
    if n not in unique_act3:
        unique_act3.append(n)

for n in act2:
    if n not in unique_act2:
        unique_act2.append(n)

print("Processing Dirs", len(dirs))

for n in range(len(dirs)):
    for x in range(len(unique_dirs)):
        if dirs[n] is unique_dirs[x]:
            dir_cluster.insert(n, x)


print("Processing Act1", len(act1))

for n in range(len(act1)):
    for x in range(len(unique_act1)):
        if act1[n] is unique_act1[x]:
            act1_cluster.insert(n, x)

print("Processing Act2", len(act2))

for n in range(len(act2)):
    for x in range(len(unique_act2)):
        if act2[n] is unique_act2[x]:
            act2_cluster.insert(n, x)

print("Processing Act3", len(act3))

for n in range(len(act3)):
    for x in range(len(unique_act3)):
        if act3[n] is unique_act3[x]:
            act3_cluster.insert(n, x)

for n in range(len(dir_cluster)):
    cluster_data.append((dir_cluster[n], act1_cluster[n], act2_cluster[n], act3_cluster[n], df.plot_keywords[n], df.gross[n]))
df = pd.DataFrame(cluster_data)
df.columns = ["director_name", "actor_1", "actor_2", "actor_3", "plot_keywords", "gross"]
df.to_csv("cluster_data.csv")