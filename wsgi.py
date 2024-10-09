# pylint: disable=missing-docstring
from flask import Flask, render_template, redirect, request, session
from flask_session import Session
from longest_word.game import Game

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/')
def home():
    if not session.get("score"):
        session["score"] = 0
    game = Game()
    return render_template('home.html', grid=game.grid, score = session['score'])

@app.route('/check', methods=["POST"])
def check():
    game = Game()
    game.grid = list(request.form['grid'])
    word = request.form['word']
    is_valid = game.is_valid(word)
    if not session.get("score"):
        session["score"] = 0
    if is_valid:
        session["score"] += 1
    return render_template('check.html', is_valid=is_valid, grid=game.grid, word=word, score = session['score'])

@app.route('/reset')
def reset():
    session["score"] = 0
    return redirect("/")
