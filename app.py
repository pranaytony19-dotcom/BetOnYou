from flask import Flask, render_template, request, redirect

app = Flask(__name__)

goals = []

@app.route("/")
def home():
    return render_template("index.html", goals=goals)

@app.route("/add_goal", methods=["POST"])
def add_goal():
    name = request.form["name"]
    duration = request.form["duration"]
    money = request.form["money"]

    goal = {
        "name": name,
        "duration": duration,
        "money": money,
        "completed": False,
        "streak": 0,
        "status": "In Progress"
    }

    goals.append(goal)   # FIXED (was appeneed)
    return redirect("/")

@app.route("/complete/<int:index>")   # keep route name simple
def complete(index):
    goals[index]["completed"] = True
    goals[index]["streak"] += 1
    goals[index]["status"] = "Success (Money Returned)"
    return redirect("/")

@app.route("/fail/<int:index>")   # FIXED (removed space)
def fail(index):
    goals[index]["completed"] = False
    goals[index]["streak"] = 0
    goals[index]["status"] = "Failed (Money Donated)"
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)