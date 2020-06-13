import numpy as np
import csv
from sklearn import datasets, linear_model
import matplotlib.pyplot as plt


file_path = 'ml-latest-small/ratings.csv'

with open(file_path, "r") as file:
    csv_reader = list(csv.DictReader(file))

    usr_ids = [int(row['userId']) for row in csv_reader if int(row['movieId']) == 1]
    
    fig, axes = plt.subplots(3, 3)

    #part 1
    i = 0
    for m in [10, 1000, 10000]:
        x = np.zeros((215,m))
        y = np.zeros((215))

        for row in csv_reader:
            if int(row['userId']) in usr_ids and int(row['movieId']) <= m+1:
                if int(row['movieId']) == 1:
                    y[ usr_ids.index(int(row['userId'])) ] = float(row['rating'])
                else:
                    x[ usr_ids.index(int(row['userId'])), int(row['movieId'])-2 ] = float(row['rating'])


        regr = linear_model.LinearRegression()
        model = regr.fit(x, y)
        predict = model.predict(x)
        
        axes[0,i].plot(np.array(usr_ids), y-predict, 'g', linewidth = 1)
        axes[0,i].set_title(f"part: 1, M: {m}")
        i += 1

    #part2
    i = 0
    j = 1
    for m in [10, 100, 200, 500, 1000, 10000]:
        x = np.zeros((215,m))
        y = np.zeros((215))

        for row in csv_reader:
            if int(row['userId']) in usr_ids and int(row['movieId']) <= m+1:
                if int(row['movieId']) == 1:
                    y[ usr_ids.index(int(row['userId'])) ] = float(row['rating'])
                else:
                    x[ usr_ids.index(int(row['userId'])), int(row['movieId'])-2 ] = float(row['rating'])

        y_tr = y[:200]
        y_pr = y[200:]

        x_tr = x[:200]
        x_pr = x[200:]
        
        regr = linear_model.LinearRegression()
        model = regr.fit(x_tr, y_tr)
        predict = model.predict(x_pr)
        
        axes[j,i].plot(np.array(usr_ids[200:]), y_pr, 'g', linewidth = 1, label="real")
        axes[j,i].plot(np.array(usr_ids[200:]), predict, 'r--', linewidth = 1, label="predicted")
        axes[j,i].set_title(f"part: 2, M: {m}")
        i += 1
        if i > 2:
            i = 0
            j = 2
            
    handles, labels = axes[2,2].get_legend_handles_labels()
    fig.legend(handles, labels, loc='upper center')
    plt.show()