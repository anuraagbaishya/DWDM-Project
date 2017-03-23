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
        print(row)
        data.append(row)

df = pd.DataFrame(data)
df.columns = ["director_name", "actor_1_name", "actor_2_name", "actor_3_name", "plot_keywords", "gross"]
df.to_csv("new_data.csv")



