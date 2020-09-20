#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask,render_template

def execute():
    return render_template('test/sugihara/index.html')
    #return "Hello Test World"