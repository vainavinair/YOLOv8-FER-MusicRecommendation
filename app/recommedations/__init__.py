from flask import Blueprint

bp = Blueprint('recommendations', __name__)

from app.recommedations import routes