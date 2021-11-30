from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import requests
import csv

from werkzeug.utils import redirect

data_timeTable = "./export/Timetable.csv"

data_Course = "./data/Course.csv"
data_Instructor = "./data/Instructor.csv"
data_MeetingTime = "./data/MeetingTime.csv"
data_Department = "./data/Department.csv"
data_Rooms = "./data/Room.csv"

app = Flask(__name__)
Bootstrap(app)



@app.route('/')
def index():
    with open(data_timeTable) as csv_file:
        data = csv.reader(csv_file, delimiter=',')
        first_line = True
        data_timeTables = []
        for row in data:
            if not first_line:
                data_timeTables.append({
                    "Shift":row[1],
                    "Day":row[2],
                    "Room":row[3],
                    "Course":row[4],
                    "Instructor":row[5],
                    "Department":row[6]
                })
            else:
                first_line = False
        return render_template("index.html", timeTables = data_timeTables)

@app.route('/listRoom', methods=['GET'])
def listRoom():
    with open(data_Rooms) as csv_file:
        data_rooms = csv.reader(csv_file, delimiter=',')
        first_line = True
        data_Room = []
        for row in data_rooms:
            if not first_line:
                data_Room.append({
                    "name":row[1],
                    "seat_capacity":row[2]
                })
            else:
                first_line = False
        return render_template("Room/listRoom.html", Rooms = data_Room)

@app.route('/addRoom', methods=["GET", "POST"])
def addRoom():
    if request.method == "GET":
        return render_template("Room/addRoom.html")
    elif request.method == "POST":
        roomdata = dict(request.form)
        name = roomdata["name"]
        seat_capacity = int(roomdata["seat_capacity"])
        
        with open(data_Rooms, "r+", newline='') as csv_file:
            data_rooms = csv.reader(csv_file, delimiter=',')
            id_room = len(list(data_rooms)) - 2
            List_room=[id_room, name,seat_capacity]
            # csv_file.write("\n")
            data = csv.writer(csv_file)
            data.writerow(List_room)
            csv_file.close()
        # return render_template("Room/test.html",id_room = id_room, name = name, seat_capacity = seat_capacity)
        return redirect("/listRoom")




if __name__ == '__main__':
	app.run(debug=True)