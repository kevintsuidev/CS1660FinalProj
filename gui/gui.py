from flask import Flask, render_template, request, session, flash, redirect, url_for
from socket import socket, AF_INET, SOCK_STREAM

app = Flask(__name__)


@app.route("/")
def home():
	return render_template("index.html")

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)