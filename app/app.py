import argparse
from flask import Flask
from concentration import Concentration

# note: running this outside of the docker container will require the argument -c app/concentration.timeseries.csv or other location
parser = argparse.ArgumentParser()
parser.add_argument('-c', '--csv_file', type=str, help='The location of the csv file containing concentration data.', default='concentration.timeseries.csv')

app = Flask(__name__)

@app.route('/get-mean')
def mean():
	return concentration.mean

@app.route('/get-std-deviation')
def dev():
	return concentration.dev

@app.route('/get-sum')
def sum():
	return concentration.sum

@app.route('/get-image')
def image():
	# this might not be correct, might need to access a file.
	return concentration.image


# I want to calculate everything as it is initialized so I only need to store and return the data
if __name__ == '__main__':
	args = parser.parse_args()
	concentration = Concentration(args.csv_file)
	app.run(host='0.0.0.0', port=8000)
