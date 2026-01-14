from flask import Flask
import random

app = Flask(__name__)

quotes = [
    "The best way to predict the future is not to wait for it, but to actively build it through consistent effort, learning, and perseverance.",

    "Success does not come from what you do occasionally, but from what you do consistently, even on the days when motivation is low.",

    "Knowledge is not just about collecting information; it is about understanding, applying, and transforming that information into wisdom.",

    "Dream big, start small, and act now. Every great achievement begins with a simple decision to try.",

    "Failure is not the opposite of success; it is a part of success that teaches you lessons no textbook ever can.",

    "Discipline is choosing between what you want now and what you want most, and that choice defines your future.",

    "Do not wait for opportunities to come your way. Build your skills so well that opportunities start looking for you.",

    "Growth begins at the end of your comfort zone. Every challenge you face is shaping you into something stronger.",

    "Your time is limited, so do not waste it living someone else’s life or chasing someone else’s definition of success.",

    "Small progress every day may seem insignificant, but over time it creates results that once felt impossible."
]

@app.route("/")
def quote():
    return random.choice(quotes)

