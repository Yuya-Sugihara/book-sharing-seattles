#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
import sys
import os
import python_script.test.sugihara.flask_test as test_sugihara

#Flaskの初期化
#templateを探索するルートフォルダーは html/templates
app = Flask(__name__,template_folder='html/templates')

#-------------------------------------------------
#ルーティング処理

#   book-sharing-seattles/がリクエストされた時に返される
@app.route('/')
def hello():
    return "Hello, Heroku"

#   book-sharing-seattles/test_sugihara/がリクエストされた時に返される
@app.route('/test_sugihara')
def execute_test_sugihara():
    return test_sugihara.execute()


#-------------------------------------------------
#  エントリポイント
if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    #app.run(host="0.0.0.0", port=port)
    app.run(port = port)
