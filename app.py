from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Store goals in memory (simple for hackathon)
goals = []

# Home route
@app.route("/")
def home():
    total = sum(goal["money"] for goal in goals)
    return render_template("index.html", goals=goals, total=total)

# Add Goal
@app.route("/add_goal", methods=["POST"])
def add_goal():
    name = request.form["name"]
    duration = request.form["duration"]
    
    # FIX: convert to int
    money = int(request.form["money"])

    goals.append({
        "name": name,
        "duration": duration,
        "money": money,
        "status": "In Progress",
        "completed": False,
        "failed": False,
        "streak": 0
    })

    return redirect("/")

# Complete Goal
@app.route("/complete/<int:index>")
def complete(index):
    if 0 <= index < len(goals):
        goals[index]["status"] = "Completed"
        goals[index]["completed"] = True
        goals[index]["failed"] = False

        #Increase streak
        goals[index]["streak"] += 1

    return redirect("/")

# Fail Goal
@app.route("/fail/<int:index>")
def fail(index):
    if 0 <= index < len(goals):
        goals[index]["status"] = "Failed"
        goals[index]["failed"] = True
        goals[index]["completed"] = False

        #Reset streak
        goals[index]["streak"] = 0

    return redirect("/")

# Delete Goal
@app.route("/delete/<int:index>")
def delete(index):
    if 0 <= index < len(goals):
        goals.pop(index)
    return redirect("/")

# Run app
if __name__ == "__main__":
    app.run(debug=True)