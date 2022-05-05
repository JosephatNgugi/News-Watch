from flask import render_template

from app.requests import get_news
from . import main


@main.route("/")
def index():
    """Root page view function returning the index page and its data"""
    general_news = get_news("general")
    sports_news = get_news("sports")
    # bbc_news = get_news('bbc')
    title = "Home - Be on Loop with the Latest News"
    
    return render_template("index.html",general_news=general_news ,sports_news=sports_news, title=title)