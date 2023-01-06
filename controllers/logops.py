"""
LOG CRUD OPERATIONS
"""


from flask_login import current_user, login_required
from flask import current_app as app, render_template, request, redirect
from application.models import *
from datetime import datetime
from controllers.miscmethods import *


@app.route("/dashboard/<trackerid>/log", methods=["GET", "POST"])
@login_required
def addlog(trackerid):
    tdet = Tracker.query.filter_by(id=trackerid).first()
    if tdet.type == 1 or tdet.type == 3:

        if request.method == "GET":
            timenow = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
            return render_template("addlog_type_1_3.html", timenow=timenow, tname=tdet.name)
        elif request.method == "POST":
            time = request.form["time"]
            value = request.form["tval"]
            details = request.form["tdet"]

            upd = Logs(userid=current_user.id, tid=trackerid,
                       value=value, data=details, time=time)
            db.session.add(upd)
            db.session.commit()
            return redirect(f"/dashboard/{trackerid}/details")

    elif tdet.type == 2 or tdet.type == 4:
        if request.method == "GET":
            timenow = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
            print("\n\n\n", tdet.choices)
            if tdet.type == 2:
                return render_template("addlog_type_2_4.html", timenow=timenow, tname=tdet.name, choices=eval(tdet.choices))
            else:
                return render_template("addlog_type_2_4.html", timenow=timenow, tname=tdet.name, choices=eval("['True', 'False']"))
        elif request.method == "POST":
            time = request.form["time"]
            value = request.form["tval"]
            details = request.form["tdet"]

            upd = Logs(userid=current_user.id, tid=trackerid,
                       value=value, data=details, time=time)
            db.session.add(upd)
            db.session.commit()
            return redirect(f"/dashboard/{trackerid}/details")

    elif tdet.type == 5:
        if request.method == "GET":
            timenow = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
            return render_template("addlog_type_5.html", timenow=timenow, tname=tdet.name)
        elif request.method == "POST":
            time = request.form["time"]
            value = request.form["tval"]
            details = request.form["tdet"]

            upd = Logs(userid=current_user.id, tid=trackerid,
                       value=value, data=details, time=time)
            db.session.add(upd)
            db.session.commit()
            return redirect(f"/dashboard/{trackerid}/details")


@app.route("/dashboard/<trackerid>/logs/<logid>/delete", methods=["GET"])
@login_required
def delete_logs(trackerid, logid):
    Logs.query.filter_by(id=logid, tid=trackerid).delete()
    db.session.commit()
    return redirect(f"/dashboard/{trackerid}/details")


@app.route("/dashboard/<trackerid>/logs/<logid>/edit", methods=["GET", "POST"])
def edit_logs(trackerid, logid):
    tdet = Tracker.query.filter_by(id=trackerid).first()
    log = Logs.query.filter_by(id=logid, tid=trackerid).first()
    if tdet.type == 1 or tdet.type == 3:
        if request.method == "GET":
            timenow = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
            return render_template("editlog_type_1_3.html", log=log, timenow=timenow, name=tdet.name)
        elif request.method == "POST":
            log.time = request.form["time"]
            log.value = request.form["tval"]
            log.data = request.form["tdet"]
            db.session.commit()
            return redirect(f"/dashboard/{trackerid}/details")

    elif tdet.type == 2 or tdet.type == 4:
        if request.method == "GET":
            timenow = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
            print("\n\n\n", tdet.choices)
            if tdet.type == 2:
                return render_template("editlog_type_2_4.html", timenow=timenow, tname=tdet.name, choices=eval(tdet.choices), log=log)
            else:
                return render_template("editlog_type_2_4.html", timenow=timenow, tname=tdet.name, choices=eval("['True', 'False']"), log=log)
        elif request.method == "POST":
            log.time = request.form["time"]
            log.value = request.form["tval"]
            log.data = request.form["tdet"]
            db.session.commit()
            return redirect(f"/dashboard/{trackerid}/details")

    elif tdet.type == 5:
        if request.method == "GET":
            timenow = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
            return render_template("editlog_type_5.html", timenow=timenow, tname=tdet.name, log=log)
        elif request.method == "POST":
            log.time = request.form["time"]
            log.value = request.form["tval"]
            log.data = request.form["tdet"]
            db.session.commit()
            return redirect(f"/dashboard/{trackerid}/details")

@app.route("/dashboard/<trackerid>/logs/<logid>", methods=["GET"])
@login_required
def view_log(trackerid, logid):
    tdet = Tracker.query.filter_by(id=trackerid).first()
    log = Logs.query.filter_by(id=logid, tid=trackerid).first()
    return render_template("view_log.html", log=log, tracker = tdet)