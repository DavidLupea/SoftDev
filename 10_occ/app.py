#Peihua Huang, David Lupea
#SoftDev1 pd2
#K10 -- Occupations Flask app
#2019-09-19

import csv, random
# import modules
from flask import Flask, render_template
app = Flask(__name__)
#create instance of class Flask

@app.route("/")
def hello_world():
    print(__name__)
    return "Please go to /occupyflaskst"

@app.route("/occupyflaskst")
def template():
    dict = {}
    with open('data/occupations.csv') as file:
    # read in file
        csv_reader = csv.reader(file, delimiter = ',')
        # split each line based on commas
        next(csv_reader, None)
        # skip the first line, so heading is not added to dictionary
        for row in csv_reader:
            dict[row[0]] = float(row[1])
            # for every row in the file, add job and percentage to dictionary as a key and value pair
    del(dict["Total"])
    # delete the last row that sums up the percentage
    job = random.choices(list(dict.keys()), weights = list(dict.values()))
    # the built-in function random.choices takes in the list of keys (job) and the value (percentages of the job) in the same order,
    # and randomly chooses one job based on the given weights of the jobs.
    return render_template('template.html', title = "Occupation Data", heading = "Occupations and their Statistics", head2 = "We used python to convert the csv file into a dictionary and choose a random job, and used Flask, html, and jinja to display the random job and the jobs and their percentages as a table on a webpage", jobs = "Job Class", percent = "Percentage", team = " Team Cereal Before Milk: Peihua Huang, David Lupea", dict = dict.items(), rand_job = job[0])
    # render template and insert the title, heading, dictionary, and random job in accordingly

if __name__ == "__main__":
    app.debug = True
    app.run()
