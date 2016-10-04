# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from snownlp import SnowNLP
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/sentiment/<content>')
def sentiment(content):
    s = SnowNLP(unicode(content))
    return repr(s.sentiments) 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
