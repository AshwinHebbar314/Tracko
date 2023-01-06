"""
USER CRUD OPERATIONS, USER DATA DOWNLOAD
"""


from flask_login import current_user, login_required
from flask import current_app as app, render_template, request, redirect, send_file
from application.models import *
from controllers.miscmethods import *
from controllers.logops import *
import shutil, os

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    elif request.method == "POST":
        fname = request.form["fname"]
        lname = request.form["lname"]
        passw = request.form["passw"]
        con_passw = request.form["con_passw"]
            

        user = request.form["user_name"]
        email = request.form["email"]
        current_users = User.query.with_entities(User.name).all()
        for cuser in current_users:
            if(cuser.name == user):
                return "<h1>User Already Exists!</h1> please <a href = '/login'>Sign in using your existing credentials</a>"
        if(passw != con_passw):
            return "<h1>Password Mismatch!</h1> please <a href = '/signup'>Sign up again</a>"
        upd = User(fname = fname, lname = lname, name=user, password = passw, email=email)
        db.session.add(upd)
        db.session.commit()
        return f"user {user} added!, please <a href = '/login'> login to access your dashboard </a>"


@app.route("/dashboard")
@login_required
def details():
    tlist = Tracker.query.filter_by(userid=current_user.id).all()
    all_track = []
    for tracker in tlist:
        current_track = []
        current_track.append(tracker.id)  # 0
        current_track.append(tracker.name)  # 1
        current_track.append(tracker_type(tracker.type))  # 2
        l = Logs.query.filter_by(tid=tracker.id, userid=current_user.id).order_by(
            Logs.time.desc()).first()
        try:
            current_track.append(l.time)  # 3
        except:
            current_track.append("Not Logged")
        try:
            current_track.append(l.value)  # 4
        except:
            current_track.append("Not Logged")
        all_track.append(current_track)

    all_track = sorted(all_track, key=lambda x: x[3], reverse=True)

    return render_template("dashboard.html", userid = current_user.id,  username=current_user.name, all_track=all_track, uname = current_user.fname + " " + current_user.lname, userdet = current_user)


@app.route("/<uid>/edit", methods=["GET", "POST"])
@login_required
def edituser(uid):
    if request.method == "GET":
        user = User.query.filter_by(id=uid).first()
        return render_template("edituser.html", user=user)
    else:
        users = User.query.all()
        user = User.query.filter_by(id=uid).first()
        curr_names = [x.name for x in users]
        if user.name != request.form["user_name"]:
            for c in curr_names:
                if c == request.form["user_name"]:
                    return f"User Already Exist, please <a href = '/{user.id}/edit'>Choose another username</a>"
        user.name = request.form["user_name"]
        user.email = request.form["email"]
        user.fname = request.form["fname"]
        user.lname = request.form["lname"]
        user.password = request.form["passw"]
        db.session.commit()
        return redirect("/dashboard")

@app.route("/<uid>/delete", methods=["GET"])
@login_required
def deleteuser(uid):
    Logs.query.filter_by(userid=uid).delete()
    db.session.commit()
    Tracker.query.filter_by(userid=uid).delete()
    db.session.commit()
    User.query.filter_by(id=uid).delete()
    db.session.commit()
    return redirect("/")

@app.route("/dashboard/download", methods=["GET"])
@login_required
def download_user_data():
    try:
        shutil.rmtree('download')
        return redirect("/dashboard/download")
    except:
        trackers = Tracker.query.filter_by(userid=current_user.id).all()
        for t in trackers:
            os.makedirs(os.path.dirname(f"download/{t.name}.csv"), exist_ok=True)
            f = open(f"download/{t.name}.csv", "w")
            logs = Logs.query.filter_by(tid=t.id).all()
            f.write("value,time,date\n")
            for l in logs:
                f.write(f"{l.value},{l.time},{l.data}\n")
            f.close()
        shutil.make_archive(f"{current_user.name}", 'zip', root_dir = 'download')
        return send_file(f"{current_user.name}.zip", as_attachment=True)