from flask import render_template

from app.requests import get_news, get_sources
from . import main


@main.route("/")
def index():
    """Root page view function returning the index page and its data"""
    # sources = get_sources("sources")
    general_news = get_news("general")
    sports_news = get_news("sports")
    # sources = get_sources("en")
    # bbc_news = get_news('bbc')
    title = "Home - Be on Loop with the Latest News"
    
    return render_template("index.html",general=general_news ,sports=sports_news, title=title)