"""
Routes and views for the bottle application.
"""

from bottle import route, view
from datetime import datetime

@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year
    )

@route('/contact')
@view('contact')
def contact():
    """Renders the contact page."""
    return dict(
        title='Gosha',
        message='Gosha sdelai shto nibud pojaluista!',
        year=datetime.now().year
    )

@route('/about')
@view('about')
def about():
    """Renders the about page."""
    return dict(
        title='History',
        message='The history of skateboarding',
        year=datetime.now().year
    )
# Обработка роута на страницу с отзывами
@route('/reviews')
@view('reviews')
def reviews():
    return dict(
        title='Reviews',
        message='Here you can see reviews',
        year=datetime.now().year
    )
