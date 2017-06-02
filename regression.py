import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from numpy import array,ravel


def get_num(name, name_list, num_list):
    for i in range(len(name_list)):
        if name_list[i] == name:
            return num_list[i]

data = pd.read_csv("sorted_data2.csv")
data_text = pd.read_csv("new_data2.csv")
data.drop(data.columns[1], axis=1)

old_data = pd.read_csv("sorted_data1.csv")
old_data_text = pd.read_csv("new_data1.csv")

in_dir = input("Enter Director: ")
in_act = input("Enter Actor: ")
in_act2 = input("Enter Actor 2: ")
in_act3 = input("Enter Actor 3: ")
in_genre = input("Genre: ")

old_in_list = [get_num(in_dir, old_data_text.director_name, old_data.director_name),
               get_num(in_act, old_data_text.actor_1_name, old_data.actor_1_name),
               get_num(in_act2, old_data_text.actor_2_name, old_data.actor_2_name),
               get_num(in_act3, old_data_text.actor_3_name, old_data.actor_3_name)]
print(old_in_list)
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

x_old = old_data.iloc[:, 1:5]
y_old = old_data.iloc[:, 6:7]

regressor = LinearRegression()
poly_regressor = SVR(kernel='poly')
rbf_regressor = SVR(kernel='rbf', C=1, gamma=1)
sig_regressor = SVR(kernel='sigmoid')
knn_regressor = KNeighborsRegressor(n_neighbors=1, weights='distance')

print("---------Without Genre Based Clustering---------")

regressor.fit(x_old, y_old)
np_list = array(old_in_list).reshape(1,-1)
print("With Multiple Linear Regression", float(regressor.predict(np_list)))

# poly_regressor.fit(x_old, ravel(y_old))
# print("With Polynomial SVR", float(poly_regressor.predict(np_list)))
#
rbf_regressor.fit(x_old, ravel(y_old))
print("With RBF SVR", float(rbf_regressor.predict(np_list)))

sig_regressor.fit(x_old, ravel(y_old))
print("With Sigmoid SVR", float(sig_regressor.predict(np_list)))

knn_regressor.fit(x_old, y_old)
np_list = array(old_in_list).reshape(1,-1)
print("With KNN Regression", float(knn_regressor.predict(np_list)))

print("---------With Genre Based Clustering---------")

regressor.fit(x, y)
np_list = array(in_list).reshape(1,-1)
print("With Multiple Linear Regression", float(regressor.predict(np_list)))


poly_regressor.fit(x, ravel(y))
print("With Polynomial SVR", float(poly_regressor.predict(np_list).reshape(1, -1)))


rbf_regressor.fit(x, ravel(y))
print("With RBF SVR", float(rbf_regressor.predict(np_list).reshape(1, -1)))

sig_regressor.fit(x, ravel(y))
print("With Sigmoid SVR", float(sig_regressor.predict(np_list).reshape(1, -1)))

knn_regressor.fit(x, y)
print("With KNN Regression", float(knn_regressor.predict(np_list)))