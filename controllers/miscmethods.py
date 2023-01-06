"""
MISCLLEANOUS METHODS THAT PLAY A PART IN THE OVERALL APP (GRAPHING, TRACKERTYPE)
"""

from flask_login import login_required
from application.models import *
import matplotlib.pyplot as plt


def tracker_type(n):
    n = int(n)
    if(n == 1):
        return "Numerical"
    elif(n == 2):
        return "Multiple Choice"
    elif(n == 3):
        return "Time Duration"
    elif(n == 4):
        return "Boolean"
    elif(n == 5):
        return "Nominal/Text"


@login_required
def create_plot(trackerid):
    tdet = Tracker.query.filter_by(id=trackerid).first()
    if(tdet.type == 1 or tdet.type == 3):
        log = Logs.query.filter_by(tid=trackerid).all()
        x = [int(l.value) for l in log]
        y = [str(i) for i in range(1,len(x)+1)]
        print(x,y)
        plt.ylabel(tdet.name)
        plt.xlabel("Logs")
        plt.title(f"Graph for {tdet.name} Tracker")
        plt.plot(y,x)
        # plt.plot(y,x)
        plt.savefig("static/graph.png")
        plt.close()

    else:
        d = dict()
        log = Logs.query.filter_by(tid=trackerid).all()
        for i in log:
            try:
                d[i.value] += 1
            except:
                d[i.value] = 1

        y,labels = d.values(), d.keys()
        plt.pie(y, labels = labels)
        plt.savefig("static/graph.png")
        plt.close()
