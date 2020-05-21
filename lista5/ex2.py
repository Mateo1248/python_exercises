import numpy as np
np.seterr(divide='ignore', invalid='ignore')


data_ratings = np.genfromtxt('ml-latest-small/ratings.csv', delimiter=',', skip_header=1)
data_movies = np.genfromtxt('ml-latest-small/movies.csv',dtype=str, delimiter=',', skip_header=1, usecols=(0,1))

users = np.unique(np.array([[row[0]] for row in data_ratings]))
movies = np.array([int(row[0]) for row in data_movies if int(row[0]) < 10000])

usr_mid_rat = np.array([[row[0], row[1], row[2]] for row in data_ratings if row[0] in users and row[1] < 10000])

x = np.zeros((len(users)+1, int(movies[-1])+1), dtype=float)
for row in usr_mid_rat:
    x[int(row[0])][int(row[1])] = row[2]




y = np.zeros((9019, 1))
y[2571] = 5
y[32] = 4
y[260] = 5
y[1097] = 4

z = np.dot(np.nan_to_num(x / np.linalg.norm(x, axis=0)), np.nan_to_num(np.array(y) / np.linalg.norm(y)))
X = np.nan_to_num(x / np.linalg.norm(x, axis=0))
Z = z / np.linalg.norm(z)
cos = np.dot(X.T, Z)
results = []
for i in range(len(movies)):
    results.append((cos[i][0], i))

results = sorted(results, key=lambda l: l[0])

print("(cos(θ) \t movies_id \t title)")
i = 0
while i < len(results):
    if results[i][0] > 0.0:
        print(results[i][0], '\t', results[i][1], '\t', data_movies[results[i][1]][1])
    i += 1