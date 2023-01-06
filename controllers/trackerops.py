"""
TRACKER CRUD OPERATIONS, TRACKER DETAILS DOWNLOAD
"""

from flask_login import current_user, login_required
from flask import current_app as app, render_template, request, redirect, send_file
from application.models import *
from datetime import datetime
from controllers.miscmethods import *
import os


@app.route("/dashboard/create_tracker", methods=["GET", "POST"])
@login_required
def create_tracker():
    if request.method == "GET":
        return render_template("create_tracker.html")
    elif request.method == "POST":
        name = request.form["tname"]
        details = request.form["tdet"]
        type = request.form["ttype"]
        choices = request.form["mulcho"]
        choices = str(choices.split(' '))
        print(choices)

        upd = Tracker(userid=current_user.id, name=name,  type=type, choices=choices,
                      details=details, time=datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
        db.session.add(upd)
        db.session.commit()
        return redirect("/dashboard")


@app.route("/dashboard/<tid>/details", methods=["GET"])
@login_required
def tracker_details(tid):
    create_plot(tid)
    tracker = Tracker.query.filter_by(id=tid).first()
    logs = Logs.query.filter_by(tid=tid, userid=current_user.id).all()
    return render_template("tracker_details.html", tracker=tracker, logs=logs)


@app.route("/dashboard/<tid>/delete", methods=["GET"])
@login_required
def delete_tracker(tid):
    logs = Logs.query.filter_by(tid=tid).delete()
    db.session.commit()
    tracker = Tracker.query.filter_by(id=tid).delete()
    db.session.commit()
    return redirect("/dashboard")



@app.route("/dashboard/<tid>/edit", methods=["GET", "POST"])
@login_required
def edit_tracker(tid):
    tracker = Tracker.query.filter_by(id=tid).first()
    if request.method == "GET":
        return render_template("edit_tracker.html", tracker=tracker, type = tracker_type(tracker.type))
    elif request.method == "POST":
        name = request.form["tname"]
        details = request.form["tdet"]
        choices = request.form["mulcho"]
        choices = str(choices.split(' '))
        upd = Tracker.query.filter_by(id=tid).first()
        upd.name = name
        upd.details = details
        if(tracker.type in [5, '5']):
            upd.choices = choices
        db.session.commit()
        return redirect(f"/dashboard/{tracker.id}/details")


@app.route("/dashboard/<tid>/download", methods=["GET"])
@login_required
def download_tracker_data(tid):
    t = Tracker.query.filter_by(id=tid).first()
    os.makedirs(os.path.dirname(f"download/{t.name}.csv"), exist_ok=True)
    f = open(f"download/{t.name}.csv", "w")
    logs = Logs.query.filter_by(tid=t.id).all()
    f.write("value,time,date\n")
    for l in logs:
        f.write(f"{l.value},{l.time},{l.data}\n")
    f.close()
    return send_file(f"download/{t.name}.csv", as_attachment=True)

