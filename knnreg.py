import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from numpy import array, mean, sum, absolute, ravel

def get_num(name, name_list, num_list):
    for i in range(len(name_list)):
        if name_list[i] == name:
            return num_list[i]

in_genre = input("Genre: ")

data_with_genre = pd.read_csv("frequency_genre.csv")
data.drop(data.columns[1], axis=1)

no_genre_data = pd.read_csv("frequency_nogenre.csv")

genre_data = data.loc[data['genres'] == in_genre]
x = genre_data.iloc[:, :-2]
y = genre_data.iloc[:, 5:6]

X_train, X_test, y_train, y_test = train_test_split(x, y, train_size=0.75) 

x_no_genre = no_genre_data.iloc[:, 1:5]
y_no_genre = no_genre_data.iloc[:, 6:7]

X_train_no_genre, X_test_no_genre, y_train_no_genre, y_test_no_genre = train_test_split(x_no_genre, y_no_genre) 

regressor = LinearRegression()
knn_regressor = KNeighborsRegressor(n_neighbors=1, weights='distance')

print("---------Without Genre Based Clustering---------")

regressor.fit(X_train_no_genre, y_train_no_genre)
y_pred_no_genre = regressor.predict(X_test_no_genre)
print("Multiple Linear Regression:")
print("Mean Absolute Percentage Error", float(sum(absolute(y_pred_no_genre-y_test_no_genre)/y_test_no_genre)/len(y_test_no_genre)))

knn_regressor.fit(X_train_no_genre, y_train_no_genre)
y_pred_no_genre = knn_regressor.predict(X_test_no_genre)
print("KNN Regression:")
print("Mean Absolute Percentage Error", float(sum(absolute(y_pred_no_genre-y_test_no_genre)/y_test_no_genre)/len(y_test_no_genre)))

print("---------With Genre Based Clustering---------")

regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
print("Multiple Linear Regression:")
print("Mean Absolute Percentage Error", float(sum(absolute(y_pred-y_test)/y_test)/len(y_test)))

knn_regressor.fit(X_train, y_train)
y_pred = knn_regressor.predict(X_test)
print("KNN Regression:")
print("Mean Absolute Percentage Error", float(sum(absolute(y_pred-y_test)/y_test)/len(y_test)))
