from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []


@app.route("/")
def home():
    return ("<a href='/tasks'>Tasks</a> <br>"
            "<a href='/about'>About</a> <br>")


@app.route("/about")
def about():
    return "<h1>Todo app</h1>"


@app.route("/tasks", methods=["GET", "POST"])
def tasks_page():
    if request.method == "POST":
        task = request.form.get("task")
        if task:
            tasks.append({"task": task, "done": False})
        return redirect(url_for("tasks_page"))
    return render_template("tasks.html", tasks=tasks)


@app.route("/done/<int:task_id>")
def mark_done(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]["done"] = True
    return redirect(url_for("tasks_page"))


@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for("tasks_page"))


if __name__ == "__main__":
    app.run(debug=True)
