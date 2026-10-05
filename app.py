from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return """
    <h1>Cloud & DevOps Capstone Project</h1>
    <p>Task Management API is running!</p>
    <p>Database: SQLite</p>
    """


@app.route("/health")
def health():
    return {"status": "healthy"}


@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()

    return jsonify([
        {
            "id": task.id,
            "title": task.title,
            "completed": task.completed
        }
        for task in tasks
    ])


@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    if not data or "title" not in data:
        return {"error": "Title is required"}, 400

    task = Task(title=data["title"])

    db.session.add(task)
    db.session.commit()

    return {
        "message": "Task created successfully",
        "task": {
            "id": task.id,
            "title": task.title,
            "completed": task.completed
        }
    }, 201


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = db.session.get(Task, task_id)

    if not task:
        return {"error": "Task not found"}, 404

    db.session.delete(task)
    db.session.commit()

    return {"message": "Task deleted successfully"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)