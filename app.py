#!/usr/bin/env python3

from flask import Flask, request, render_template_string
# import requests
from stars import get_stars


'''
Celeste is a local star gazing app 
'''

app = Flask('celeste')

## ip allowlisting

@app.route('/')
def main():
	timezone = request.get('timezone')
	if not timezone:
		timezone = 'UTC'
	#local users only
	if '192.168.' in request.remote_addr or request.remote_addr.startswith('172.16') or request.remote_addr.startswith('10.') or request.remote_addr.startswith('127.0.'):
		render_template_string('''
			<style>
			* {
			background-color: #ce1e57;
			}
			</style>
			<h2>Stars in '''+timezone+'</h2>'+'''
			<img src=data:image/png;base64,{{img}}>
			''', img=get_stars(timezone))
	else:
		return "Permission denied", 401


