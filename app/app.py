import argparse
import os
from flask import Flask, send_file
from concentration import Concentration

app = Flask(__name__)

@app.route('/get-mean')
def get_mean():
    return concentration.mean()

@app.route('/get-std-deviation')
def get_std_deviation():
    return concentration.std_dev()

@app.route('/get-sum')
def get_sum():
    return concentration.sum()

@app.route('/get-image')
def get_image():
    return send_file(concentration.img_location, mimetype='image/png')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--csv_file', type=str, help='The location of the csv file containing concentration data.', default='concentration.timeseries.csv')
    args = parser.parse_args()

    if not os.path.isfile(args.csv_file):
        raise FileNotFoundError(f"File '{args.csv_file}' does not exist.")

    concentration = Concentration(args.csv_file)
    app.run(host='0.0.0.0', port=8000)