# Concentration-Flask-Timeseries

## Text from assignment

You should have received the file “concentration.timeseries.csv” with this assignment.

This file is a CSV file and will be the foundation of this assignment.

The requirements for this assignment are as follows:

1.) Publicly hosted repository of your choice (GitHub, BitBucket, etc.)

2.) The use of FLASK Web Framework within Python

3.) Implementation of the following endpoints:

	a.) /get-mean, returns the mean of the concentration

	b.) /get-std-deviation, returns the standard deviation of the concentration

	c.) /get-sum, returns the sum of the concentration

	d.) /get-image, returns png visualization of concentration

4.) Docker container deployment

5.) Project README.md 

## Notes

1. Create repo
2. Initialize Docker and flask
* should be a preexisting flask docker project that I can clone
* https://github.com/docker/awesome-compose/tree/master/flask
* this project uses specific and unnecessary development options, I have modified the docker files to be as simple as possible
* create a test endpoint so that I can make sure docker is setup properly

* dockerfile and docker-compose.yaml are both successfully modified.
* test endpoint is / and returns hello world

* run project with docker compose up or docker compose up -d to skip the error message about production deployments that flask generates.
3. API endpoints
* what framework do I use for the timeseries? Pandas? I believe pandas can do data visualizations.
* read the csv file in with an argument in case they want to run it with a different csv.
* python has a csvreader, but look into other options

* set up the endpoints with stubs. Be sure to run docker compose up --build to see changes.

* created a Concentration class for simple data management. Currently stubbed.

* mean std and sum all appear to be working, need to manually check they are correct before submitting.

* For the image, I will need to research what library to use. Requirements just say to do a visualization.

* Could do a 3D plot and color each point depending on the concentration.

* I was told this was a timeseries, however my variables are x y z and concentration. I am not finding any examples of a 3D concentration timeseries online.

* This looks good https://matplotlib.org/stable/gallery/mplot3d/scatter3d.html

* Core functionality complete, code still needs some cleanup and need to write readme.md

* Might want to change the format of the numbers that get returned from E to digits.

4. Tests? 
5. Write a completed README.md

## API Endpoints

/get-sum, returns the sum of the concentration

I'll start with the sum, it should be the easiest to confirm as correct.

/get-mean, returns the mean of the concentration

/get-std-deviation, returns the standard deviation of the concentration

/get-image, returns png visualization of concentration

I'm not sure what the best way to make the image is, but I think I can use matplotlib.