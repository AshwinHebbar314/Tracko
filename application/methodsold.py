"""
OLD METHODS FILE WITH ALL THE METHODS INTACT, USED AS A BACKUP,  DOES NOT AND SHOULD NOT PLAY AN ACTIVE ROLE IN THE FUNCTIONINF OF THE APP
"""

from flask_login import login_user, logout_user, current_user, login_required
from flask import current_app as app, render_template, request, redirect, flash
from application.models import *
from datetime import datetime
import matplotlib.pyplot as plt 
import numpy as np




    ################################################################
# User CRUD
    ################################################################

from controllers.appfunc import *
from controllers.userops import *
from controllers.trackerops import *
from controllers.logops import *
from controllers.miscmethods import *

# @app.route("/")
# def landing():
#     return render_template("index.html")

# @app.route("/login", methods=["GET", "POST"])
# def login():
#     if request.method == "GET":
#         return render_template("signin.html")
#     elif request.method == "POST":
#         user = request.form["user_name"]
#         passw = request.form["passw"]
#         loginu = User.query.filter_by(name=user).first()
#         if(passw == loginu.password):
#             try:
#                 login_user(loginu)
#             except:
#                 return f"User {user} does not exist, you can <a href = '/signup'> Create a new user by clicking here</a>"
#             return details()
#         else:
#             return f"Wrong Password, please <a href = '/login'> try again </a>"

# @app.route("/logout")
# @login_required
# def logout():
#     logout_user()
#     return redirect("/")




# @app.route("/signup", methods=["GET", "POST"])
# def signup():
#     if request.method == "GET":
#         return render_template("signup.html")
#     elif request.method == "POST":
#         fname = request.form["fname"]
#         lname = request.form["lname"]
#         passw = request.form["passw"]
#         con_passw = request.form["con_passw"]
            

#         user = request.form["user_name"]
#         email = request.form["email"]
#         current_users = User.query.with_entities(User.name).all()
#         for cuser in current_users:
#             if(cuser.name == user):
#                 return "<h1>User Already Exists!</h1> please <a href = '/login'>Sign in using your existing credentials</a>"
#         if(passw != con_passw):
#             return "<h1>Password Mismatch!</h1> please <a href = '/signup'>Sign up again</a>"
#         upd = User(fname = fname, lname = lname, name=user, password = passw, email=email)
#         db.session.add(upd)
#         db.session.commit()
#         return f"user {user} added!, please <a href = '/login'> login to access your dashboard </a>"

# @app.route("/dashboard")
# @login_required
# def details():
#     tlist = Tracker.query.filter_by(userid=current_user.id).all()
#     all_track = []
#     for tracker in tlist:
#         current_track = []
#         current_track.append(tracker.id)  # 0
#         current_track.append(tracker.name)  # 1
#         current_track.append(tracker_type(tracker.type))  # 2
#         l = Logs.query.filter_by(tid=tracker.id, userid=current_user.id).order_by(
#             Logs.time.desc()).first()
#         try:
#             current_track.append(l.time)  # 3
#         except:
#             current_track.append("Not Logged")
#         try:
#             current_track.append(l.value)  # 4
#         except:
#             current_track.append("Not Logged")
#         all_track.append(current_track)

#     all_track = sorted(all_track, key=lambda x: x[3], reverse=True)

#     return render_template("dashboard.html", userid = current_user.id,  username=current_user.name, all_track=all_track, uname = current_user.fname + " " + current_user.lname, userdet = current_user)


# @app.route("/<uid>/edit", methods=["GET", "POST"])
# @login_required
# def edituser(uid):
#     if request.method == "GET":
#         user = User.query.filter_by(id=uid).first()
#         return render_template("edituser.html", user=user)
#     else:
#         users = User.query.all()
#         user = User.query.filter_by(id=uid).first()
#         curr_names = [x.name for x in users]
#         for c in curr_names:
#             if c == request.form["user_name"]:
#                 return f"User Already Exist, please <a href = '/{user.id}/edit'>Choose another username</a>"
#         user.name = request.form["user_name"]
#         user.email = request.form["email"]
#         db.session.commit()
#         return redirect("/dashboard")

# @app.route("/<uid>/delete", methods=["GET"])
# @login_required
# def deleteuser(uid):
#     Logs.query.filter_by(userid=uid).delete()
#     db.session.commit()
#     Tracker.query.filter_by(userid=uid).delete()
#     db.session.commit()
#     User.query.filter_by(id=uid).delete()
#     db.session.commit()
#     return redirect("/")


#     ###############################################################
# TRACKER
#     ###############################################################



# @app.route("/dashboard/create_tracker", methods=["GET", "POST"])
# @login_required
# def create_tracker():
#     if request.method == "GET":
#         return render_template("create_tracker.html")
#     elif request.method == "POST":
#         name = request.form["tname"]
#         details = request.form["tdet"]
#         type = request.form["ttype"]
#         choices = request.form["mulcho"]
#         choices = str(choices.split(' '))
#         print(choices)

#         upd = Tracker(userid=current_user.id, name=name,  type=type, choices=choices,
#                       details=details, time=datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
#         db.session.add(upd)
#         db.session.commit()
#         return redirect("/dashboard")


# @app.route("/dashboard/<tid>/details", methods=["GET"])
# @login_required
# def tracker_details(tid):
#     create_plot(tid)
#     tracker = Tracker.query.filter_by(id=tid).first()
#     logs = Logs.query.filter_by(tid=tid, userid=current_user.id).all()
#     return render_template("tracker_details.html", tracker=tracker, logs=logs)




# @app.route("/dashboard/<tid>/delete", methods=["GET"])
# @login_required
# def delete_tracker(tid):
#     logs = Logs.query.filter_by(tid=tid).delete()
#     db.session.commit()
#     tracker = Tracker.query.filter_by(id=tid).delete()
#     db.session.commit()
#     return redirect("/dashboard")

#     ###############################################################
# LOGGING
#     ###############################################################

# @app.route("/dashboard/<trackerid>/log", methods=["GET", "POST"])
# @login_required
# def addlog(trackerid):
#     tdet = Tracker.query.filter_by(id=trackerid).first()
#     if tdet.type == 1 or tdet.type == 3:

#         if request.method == "GET":
#             timenow = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
#             return render_template("addlog_type_1_3.html", timenow=timenow, tname=tdet.name)
#         elif request.method == "POST":
#             time = request.form["time"]
#             value = request.form["tval"]
#             details = request.form["tdet"]

#             upd = Logs(userid=current_user.id, tid=trackerid,
#                        value=value, data=details, time=time)
#             db.session.add(upd)
#             db.session.commit()
#             return redirect("/dashboard")

#     elif tdet.type == 2 or tdet.type == 4:
#         if request.method == "GET":
#             timenow = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
#             print("\n\n\n", tdet.choices)
#             if tdet.type == 2:
#                 return render_template("addlog_type_2_4.html", timenow=timenow, tname=tdet.name, choices=eval(tdet.choices))
#             else:
#                 return render_template("addlog_type_2_4.html", timenow=timenow, tname=tdet.name, choices=eval("['True', 'False']"))
#         elif request.method == "POST":
#             time = request.form["time"]
#             value = request.form["tval"]
#             details = request.form["tdet"]

#             upd = Logs(userid=current_user.id, tid=trackerid,
#                        value=value, data=details, time=time)
#             db.session.add(upd)
#             db.session.commit()
#             return redirect("/dashboard")

#     elif tdet.type == 5:
#         if request.method == "GET":
#             timenow = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
#             return render_template("addlog_type_5.html", timenow=timenow, tname=tdet.name)
#         elif request.method == "POST":
#             time = request.form["time"]
#             value = request.form["tval"]
#             details = request.form["tdet"]

#             upd = Logs(userid=current_user.id, tid=trackerid,
#                        value=value, data=details, time=time)
#             db.session.add(upd)
#             db.session.commit()
#             return redirect("/dashboard")


# @app.route("/dashboard/<trackerid>/logs/<logid>/delete", methods=["GET"])
# @login_required
# def delete_logs(trackerid, logid):
#     Logs.query.filter_by(id=logid, tid=trackerid).delete()
#     db.session.commit()
#     return redirect("/dashboard")


# @app.route("/dashboard/<trackerid>/logs/<logid>/edit", methods=["GET", "POST"])
# def edit_logs(trackerid, logid):
#     # if request.method == "GET":
#     #   log = Logs.query.filter_by(id = logid, tid = trackerid).first()
#     #   return render_template("edit_logs.html", log = log)
#     # elif request.method == "POST":
#     #   log = Logs.query.filter_by(id = logid, tid = trackerid).first()
#     #   log.value = request.form["tval"]
#     #   log.data = request.form["tdet"]
#     #   db.session.commit()
#     #   return redirect("/dashboard")
#     tdet = Tracker.query.filter_by(id=trackerid).first()
#     log = Logs.query.filter_by(id=logid, tid=trackerid).first()
#     if tdet.type == 1 or tdet.type == 3:
#         if request.method == "GET":
#             timenow = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
#             return render_template("editlog_type_1_3.html", log=log, timenow=timenow, name=tdet.name)
#         elif request.method == "POST":
#             log.time = request.form["time"]
#             log.value = request.form["tval"]
#             log.data = request.form["tdet"]
#             db.session.commit()
#             return redirect("/dashboard")

#     elif tdet.type == 2 or tdet.type == 4:
#         if request.method == "GET":
#             timenow = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
#             print("\n\n\n", tdet.choices)
#             if tdet.type == 2:
#                 return render_template("editlog_type_2_4.html", timenow=timenow, tname=tdet.name, choices=eval(tdet.choices), log=log)
#             else:
#                 return render_template("editlog_type_2_4.html", timenow=timenow, tname=tdet.name, choices=eval("['True', 'False']"), log=log)
#         elif request.method == "POST":
#             log.time = request.form["time"]
#             log.value = request.form["tval"]
#             log.data = request.form["tdet"]
#             db.session.commit()
#             return redirect("/dashboard")

#     elif tdet.type == 5:
#         if request.method == "GET":
#             timenow = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
#             return render_template("editlog_type_5.html", timenow=timenow, tname=tdet.name, log=log)
#         elif request.method == "POST":
#             log.time = request.form["time"]
#             log.value = request.form["tval"]
#             log.data = request.form["tdet"]
#             db.session.commit()
#             return redirect("/dashboard")

# @app.route("/dashboard/<trackerid>/logs/<logid>", methods=["GET"])
# @login_required
# def view_log(trackerid, logid):
#     tdet = Tracker.query.filter_by(id=trackerid).first()
#     log = Logs.query.filter_by(id=logid, tid=trackerid).first()
#     return render_template("view_log.html", log=log, tracker = tdet)


# ###############################################################

# @login_required
# def create_plot(trackerid):
#     tdet = Tracker.query.filter_by(id=trackerid).first()
#     if(tdet.type == 1 or tdet.type == 3):
#         log = Logs.query.filter_by(tid=trackerid).all()
#         x = [int(l.value) for l in log]
#         y = [str(i) for i in range(1,len(x)+1)]
#         print(x,y)
#         plt.ylabel(tdet.name)
#         plt.xlabel("Logs")
#         plt.title(f"Graph for {tdet.name} Tracker")
#         plt.bar(y,x)
#         # plt.plot(y,x)
#         plt.savefig("static/graph.png")
#         plt.close()

#     else:
#         d = dict()
#         log = Logs.query.filter_by(tid=trackerid).all()
#         for i in log:
#             try:
#                 d[i.value] += 1
#             except:
#                 d[i.value] = 1

#         y,labels = d.values(), d.keys()
#         plt.pie(y, labels = labels)
#         plt.savefig("static/graph.png")
#         plt.close()



