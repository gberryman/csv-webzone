from flask import render_template, request, redirect, url_for, safe_join, send_file
from werkzeug.utils import secure_filename
import csv
import math
from matplotlib.figure import Figure
from app import app

app.uploads = {}

@app.route('/')
@app.route('/index')
@app.route('/index/<path:selected_file>')
def index(selected_file=''):
	if selected_file != '' and selected_file in app.uploads:
		return render_template(
			'index.html', 
			uploads=list(app.uploads.keys()), 
			selected=True,
			selected_file=selected_file,
			plot=selected_file+'_plot.png',
			stats=app.uploads[selected_file]
			)
	else:
		return render_template('index.html', selected=False, uploads=list(app.uploads.keys()))


@app.route('/upload', methods = ['GET','POST'])
def upload():
	if request.method=='POST':        
		if 'file' not in request.files:
			return redirect(request.url)

		file = request.files['file']
		filename = secure_filename(file.filename)

		file.save(safe_join(app.config['UPLOAD_FOLDER'], filename))
		app.uploads[filename]=calculate_stats(filename)
		file.close()
		return redirect(url_for('index'))

	return render_template('upload.html')

@app.route('/display/<path:filename>')
def display(filename):
	filename = safe_join(app.config['UPLOAD_FOLDER'], filename)
	datafile = open(filename)
	dictreader = csv.DictReader(datafile)
	cleaned_reader = clean_reader(dictreader)
	template = render_template('display.html', reader=cleaned_reader, fieldnames=dictreader.fieldnames)
	datafile.close()
	return template

@app.route('/get_plot/<path:plot>')
def get_plot(plot):
	return send_file(safe_join(app.config['PLOT_FOLDER'], plot))

def calculate_stats(filename):
	file = open(safe_join(app.config['UPLOAD_FOLDER'], filename))
	datareader = csv.DictReader(file)
	stats = {}
	for row in datareader:
		year = int(row['date'].split('/')[2])
		stats[year] = stats.get(year, 0) + 1
	average = round(sum(stats.values())/len(stats), 2)
	ordered = sorted(stats.items(), key=lambda s:s[1])
	min_item = str(ordered[0][0]) + ' with ' + str(ordered[0][1]) + ' people'
	max_item = str(ordered[-1][0]) + ' with ' + str(ordered[-1][1]) + ' people'
	plot_filename=filename+'_plot.png'
	render_plot(stats, plot_filename)
	return {
		'average':average, 
		'min': min_item, 
		'max': max_item
	}

def render_plot(stats, plot_filename):
    fig = Figure()
    ax = fig.subplots()
    sorted_stats = sorted(stats.items(), key=lambda s:s[0])
    year = [e[0] for e in sorted_stats]
    data = [e[1] for e in sorted_stats]
    line = ax.plot(year, data, color='blue')
    ax.set_ylabel('Number of people')
    ax.set_xlabel('year')
    ax.set_xticks(range(math.floor((min(year)-1)/10)*10, math.ceil((max(year))/10)*10 + 1, 10))
    for tick in ax.get_xticklabels():
        tick.set_rotation(90)
    fig.align_xlabels
    fig.savefig(safe_join(app.config['PLOT_FOLDER'], plot_filename))

def clean_reader(reader):
    for row in reader:
        if row['state']=='':
            newrow = row.copy()
            newrow['state']='BLANK'
            yield newrow
        else:
            yield row