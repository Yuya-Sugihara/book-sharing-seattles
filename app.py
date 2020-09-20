#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
import sys
import os
import python_script.test.sugihara.flask_test as test_sugihara

#Flask�̏�����
#template��T�����郋�[�g�t�H���_�[�� html/templates
app = Flask(__name__,template_folder='html/templates')

#-------------------------------------------------
#���[�e�B���O����

#   book-sharing-seattles/�����N�G�X�g���ꂽ���ɕԂ����
@app.route('/')
def hello():
    return "Hello, Heroku"

#   book-sharing-seattles/test_sugihara/�����N�G�X�g���ꂽ���ɕԂ����
@app.route('/test_sugihara')
def execute_test_sugihara():
    return test_sugihara.execute()


#-------------------------------------------------
#  �G���g���|�C���g
if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    #app.run(host="0.0.0.0", port=port)
    app.run(port = port)
