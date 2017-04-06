import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from numpy import array,ravel

data = pd.read_csv("sorted_data2.csv")
data_text = pd.read_csv("new_data2.csv")
data.drop(data.columns[1], axis=1)

in_dir = input("Enter Director: ")
in_act = input("Enter Actor: ")
in_act2 = input("Enter Actor 2: ")
in_act3 = input("Enter Actor 3: ")
in_genre = input("Genre: ")

in_list = []

dir_found = False
act_found = False
act2_found = False
act3_found = False

count = 0
for i in range(len(data_text)):

    if data_text.ix[i].director_name == in_dir and data_text.ix[i].genres == in_genre and not dir_found:
        in_list.append(data.ix[count].director_name)
        dir_found = True

    if data_text.ix[i].actor_1_name == in_act and data_text.ix[i].genres == in_genre and not act_found:
        in_list.append(data.ix[count].actor_1_name)
        act_found = True

    if data_text.ix[i].actor_2_name == in_act2 and data_text.ix[i].genres == in_genre and not act2_found:
        in_list.append(data.ix[count].actor_2_name)
        act2_found = True

    if data_text.ix[i].actor_3_name == in_act3 and data_text.ix[i].genres == in_genre and not act3_found:
        in_list.append(data.ix[count].actor_3_name)
        act3_found = True

    if dir_found and act3_found and act2_found and act_found:
        break
    count += 1

reg_set = data.loc[data['genres'] == in_genre]
x = reg_set.iloc[:, :-2]
y = reg_set.iloc[:, 5:6]

regressor = LinearRegression()
regressor.fit(x, y)
np_list = array(in_list).reshape(1,-1)
print("With Multiple Linear Regression", float(regressor.predict(np_list)))

regressor = SVR(kernel='poly')
regressor.fit(x, ravel(y))
print("With Polynomial SVR", float(regressor.predict(np_list).reshape(1, -1)))

regressor = SVR(kernel='rbf')
regressor.fit(x, ravel(y))
print("With RBF SVR", float(regressor.predict(np_list).reshape(1, -1)))

regressor = SVR(kernel='sigmoid')
regressor.fit(x, ravel(y))
print("With Sigmoid SVR", float(regressor.predict(np_list).reshape(1, -1)))