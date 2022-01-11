import csv
import matplotlib.pyplot as plt
import numpy as np

GMK=0
SA=0
ePBT=0
MW=0
Infinikey=0
KK=0
DSS=0
DSA=0
DMK=0
others=0
with open('2021keebinfo.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] == "GMK":
            GMK=GMK+1
        elif row[0] == "SA":
            SA=SA+1
        elif row[0] == "ePBT" or row[0] == "EPBT" or row[0] == "epbt":
            ePBT = ePBT +1
        elif row[0] == "MW":
            MW=MW+1
        elif row[0] == "Infinikey":
            Infinikey=Infinikey+1
        elif row[0] == "KAT" or row[0] == "KAM":
            KK=KK+1
        elif row[0] == "DSS":
            SA=SA+1
        elif row[0] == "DSA":
            SA=SA+1
        else: 
            others= others +1
print(DSA)
y = np.array([GMK, SA, ePBT, KK, MW, Infinikey, others])
brandLabels = ["GMK", "SP",  "ePBT", "Keyreative", "MW", "IFK", "Others"]
myexplode = [0, 0, 0, 0.24 , 0.24, 0.24, 0]
plt.title("Proportion of keycap groupbuys in 2021 by manufacturer")
plt.pie(y, labels = brandLabels, explode = myexplode, shadow = True)
plt.show()
