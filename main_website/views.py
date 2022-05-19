from crypt import methods
from flask import Blueprint, redirect, render_template, request, jsonify, url_for
from lib.encrypt import Encrypt
from lib.util import *
from lib.emailController import emailController
from . import DB # for using the sql alchemy ORM
from models import UserContact
from config import Config
# import json
# from flask_login import login_required, current_user  # may not need this time

views = Blueprint('views', __name__)

@views.route('/') # url for when browsing or when linking using <a> or api
def home():
    try:
        return render_template("index.html")

    except Exception as e:
        return jsonify(
            {
                "error": str(e)
            }
        )
