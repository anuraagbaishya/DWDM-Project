import pandas as pd
import word_sim

dataset = pd.read_csv("new_data.csv")
words = []
for d in dataset.plot_keywords:
    if d not in words:
        words.append(d)

word_pairs = []
sim_words = []
sim_words_all, sim_words_list = [],[]
for w in range(0, 1):
    print(words[w])
    for x in words:
        if words[w] == x:
            continue
        if word_sim.word_similarity(words[w], x) > 0.7:
            sim_words.append([words[w], x])
            words.remove(x)

    sim_words_all.append(sim_words)
    sim_words = []


for w in sim_words_all:
    for x in w:
        sim_words_list.append(x)

print(sim_words_list)
# df = pd.DataFrame(sim_words_list)
# df.columns = ["root", "synonyms"]
# with open('word_cluster.csv', 'a') as f:
#     df.to_csv(f, header=False)
