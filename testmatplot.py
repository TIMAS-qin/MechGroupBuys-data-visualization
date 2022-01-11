import csv
import matplotlib.pyplot as plt
import numpy as np

GMKup=0
SAup=0
ePBTup=0
MWup=0
Infinikeyup=0
KKup=0
othersup=0
GMK=0
SA=0
ePBT=0
MW=0
Infinikey=0
KK=0
others=0
GMKc=0
SAc=0
ePBTc=0
MWc=0
Infinikeyc=0
KKc=0
othersc=0

with open('2021keebinfo.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] == "GMK":
            GMKup=GMKup + int(row[1])
            GMKc=GMKc + int(row[2])
            GMK=GMK+1
        elif row[0] == "SA" or row[0] == "DSS" or row[0] == "DSA":
            SAup=SAup+int(row[1])
            SAc=SAc + int(row[2])
            SA=SA+1
        elif row[0] == "ePBT" or row[0] == "EPBT" or row[0] == "epbt":
            ePBTup = ePBTup +int(row[1])
            ePBTc=ePBTc + int(row[2])
            ePBT = ePBT +1
        elif row[0] == "MW":
            MWup=MWup+int(row[1])
            MWc=MWc + int(row[2])
            MW=MW+1
        elif row[0] == "Infinikey":
            Infinikeyup=Infinikeyup+int(row[1])
            Infinikeyc=Infinikeyc + int(row[2])
            Infinikey=Infinikey+1
        elif row[0] == "KAT" or row[0] == "KAM":
            KKup=KKup+int(row[1])
            KKc=KKc + int(row[2])
            KK=KK+1
        elif row[0] == "brand":
            pass
        else: 
            othersup= othersup +int(row[1])
            othersc=othersc + int(row[2])
            others= others +1

def avg(upvotes, num):
    avg = upvotes/num
    return(avg)
"""
========
Barchart
========

A bar plot with errorbars and height labels on individual bars
"""
brands = ["GMK", "SA", "KAT/KAM", "ePBT", "MW", "IFK", "Others"]
avgup = [avg(GMKup, GMK),avg(SAup, SA),avg(KKup, KK),avg(ePBTup, ePBT),avg(MWup, MW), avg(Infinikeyup, Infinikey), avg(othersup, others)]
avgc = [avg(GMKc, GMK),avg(SAc, SA),avg(KKc, KK),avg(ePBTc, ePBT),avg(MWc, MW), avg(Infinikeyc, Infinikey), avg(othersc, others)]


N = 7

men_std = (64, 45, 92, 45, 38, 46, 49)

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, avgup, width, color='r' )

women_std = (17, 9, 22, 8, 8, 8, 15)
rects2 = ax.bar(ind + width, avgc, width, color='b')

# add some text for labels, title and axes ticks
ax.set_ylabel('Number of upvotes/comments')
ax.set_title('Average number of upvotes/comments by keycap manufacturer')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(("GMK", "SP", "Keyreative", "ePBT", "MW", "IFK", "Others"))

ax.legend((rects1[0], rects2[0]), ('upvotes', 'comments'))


def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.0*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.show()