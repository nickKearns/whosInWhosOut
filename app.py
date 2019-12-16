from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

client = MongoClient()
db = client.WhosInWhosOut
games = db.games

games = [
    {'title': 'test_title', 'players_out': 'player1, player2', 'league': 'nfl'},
    {'title': 'test_title2', 'players_out': 'player1, player2', 'league': 'nfl'}
]


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game')
def display_game():
    return render_template('game.html')


@app.route('/nba')
def display_NBA():
    return render_template('nba.html')

@app.route('/nfl')
def display_NFL():
    return render_template('nfl.html', games=games)

@app.route('/mlb')
def display_MLB():
    return render_template('mlb.html')

@app.route('/nhl')
def display_NHL():
    return render_template('nhl.html')


# @app.route('/nba')
# def new_nba_game():
