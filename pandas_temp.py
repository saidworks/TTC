import pandas as pd
import csv

titles = ['date','temperaturemin','temperaturemax','precipitation','swfall','swdepth','avgwindspeed','fastest2minwinddir','fastest2minwindspeed','fastest5secwinddir','fastest5secwindspeed']
with open('rdu-weather-history.csv','r',newline='') as file:
    reader = csv.reader(file)
    new_data = []
    prepared_data = []
    data_dic = {}
    for row in reader:
        for entry in row:
            entry.replace(';','_')
            new_data.append(entry)

    for entry in new_data:
        entry = entry.replace(';',',')
        prepared_data.append(entry)
        data_dic[entry[0:10]] = entry
    print(data_dic)
    # prepared_data = {entry.replace(';',',') for entry in new_data}
    # print(prepared_data)



datas = pd.read_csv('rdu-weather-history.csv',sep='\t',header=None,names=titles)
datas_df = pd.DataFrame(datas)

