"""
COMMON FILE FOR BRINGING ALL THE METHODS TOGETHER AND MAKING LIFE EASIER
"""

from flask_login import login_user, logout_user, current_user, login_required
from flask import current_app as app, render_template, request, redirect, flash


from application.models import *


from controllers.appfunc import *
from controllers.userops import *
from controllers.trackerops import *
from controllers.logops import *
from controllers.miscmethods import *