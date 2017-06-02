import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from numpy import array, mean, sum, absolute, ravel

def get_num(name, name_list, num_list):
    for i in range(len(name_list)):
        if name_list[i] == name:
            return num_list[i]

in_genre = input("Genre: ")

data = pd.read_csv("sorted_data2.csv")
data_text = pd.read_csv("new_data2.csv")
data.drop(data.columns[1], axis=1)

old_data = pd.read_csv("sorted_data1.csv")
old_data_text = pd.read_csv("new_data1.csv") 

reg_set = data.loc[data['genres'] == in_genre]
x = reg_set.iloc[:, :-2]
y = reg_set.iloc[:, 5:6]

X_train, X_test, y_train, y_test = train_test_split(x, y, train_size=0.75) 

x_old = old_data.iloc[:, 1:5]
y_old = old_data.iloc[:, 6:7]

X_train_old, X_test_old, y_train_old, y_test_old = train_test_split(x_old, y_old) 

regressor = LinearRegression()
knn_regressor = KNeighborsRegressor(n_neighbors=1, weights='distance')
dt_regressor_2 = DecisionTreeRegressor(max_depth=2)
dt_regressor_5 = DecisionTreeRegressor(max_depth=5)

print("---------Without Genre Based Clustering---------")

regressor.fit(X_train_old, y_train_old)
y_pred_old = regressor.predict(X_test_old)
print("Multiple Linear Regression:")
print("Mean Absolute Percentage Error", float(sum(absolute(y_pred_old-y_test_old)/y_test_old)/len(y_test_old)))

knn_regressor.fit(X_train_old, y_train_old)
y_pred_old = knn_regressor.predict(X_test_old)
print("KNN Regression:")
print("Mean Absolute Percentage Error", float(sum(absolute(y_pred_old-y_test_old)/y_test_old)/len(y_test_old)))

print("---------With Genre Based Clustering---------")

regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
print("Multiple Linear Regression:")
print("Mean Absolute Percentage Error", float(sum(absolute(y_pred-y_test)/y_test)/len(y_test)))

knn_regressor.fit(X_train, y_train)
y_pred = knn_regressor.predict(X_test)
print("KNN Regression:")
print("Mean Absolute Percentage Error", float(sum(absolute(y_pred-y_test)/y_test)/len(y_test)))