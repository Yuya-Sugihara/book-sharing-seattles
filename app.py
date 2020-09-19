#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
import os

import Test.Sugihara.FlaskTest as TestSugihara

#-------------------------------------------------
app = Flask(__name__)


#-------------------------------------------------
#ディレクトリ定義

#  book-sharing-seattles/がリクエストされた時に返される
@app.route("/")
def hello():
    return "Hello, Heroku"

#   book-sharing-seattles/TestSugihara/がリクエストされた時に返される
@app.route("/TestSugihara")
def executeTestSugihara():
    return TestSugihara.execute()


#-------------------------------------------------
#  エントリポイント
if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    #app.run(host="0.0.0.0", port=port)
    app.run(port = port)
