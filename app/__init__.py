from flask import Flask
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER']='uploads'
if not os.path.isdir('uploads'):
	os.mkdir('uploads')
app.config['PLOT_FOLDER']='plots'
if not os.path.isdir('plots'):
	os.mkdir('plots')

from app import routes

if __name__ == "__main__":
	app.run()