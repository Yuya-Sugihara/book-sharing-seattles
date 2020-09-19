#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
import os

import Test.Sugihara.FlaskTest as TestSugihara

#-------------------------------------------------
app = Flask(__name__)


#-------------------------------------------------
#�f�B���N�g����`

#  book-sharing-seattles/�����N�G�X�g���ꂽ���ɕԂ����
@app.route("/")
def hello():
    return "Hello, Heroku"

#   book-sharing-seattles/TestSugihara/�����N�G�X�g���ꂽ���ɕԂ����
@app.route("/TestSugihara")
def executeTestSugihara():
    return TestSugihara.execute()


#-------------------------------------------------
#  �G���g���|�C���g
if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    #app.run(host="0.0.0.0", port=port)
    app.run(port = port)
