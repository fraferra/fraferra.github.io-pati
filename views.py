import os
import jinja2
from flask import render_template, request, session, redirect, url_for, escape, Flask
app = Flask(__name__)

if __name__ == '__main__':
    app.run()

@app.route('/', methods=['GET'])
def views():
    return render_template('index.html')
