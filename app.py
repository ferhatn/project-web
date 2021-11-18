from flask import Flask
from flask import render_template
import os 
import sqlite3


app = Flask(__name__)

@app.route("/")
def movie():
    with sqlite3.connect("db/movie.db") as c:
        return render_template('index.html', 
           api_url="http://127.0.0.1:8000", 
           suggests=c.execute("""
            SELECT ItemID, MovieTitle, ROUND(Rating, 1) FROM movies 
            ORDER BY Rating DESC
            LIMIT 10 
        """))
@app.route("/sample")
def movie_sample():
    return render_template('index.html', suggests=[(1, "Transformers",3.2), (2, "Toy Story",2.5)])
