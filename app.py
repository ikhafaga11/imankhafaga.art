from flask import Flask, render_template, redirect, url_for, flash, session, request
from lib.database_connection import get_flask_database_connection
from lib.project_repository import ProjectRepository
from lib.project_content_repository import ProjectContentRepository
from lib.sketchbook_repository import SketchbookRepository
from lib.auth_repository import AuthRepository
import os
from dotenv import load_dotenv

app = Flask(__name__)

app.secret_key = os.getenv("FLASK_SECRET_KEY")


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/projects", methods=["GET"])
def projects():
    connection = get_flask_database_connection(app)
    repo = ProjectRepository(connection)
    projects = repo.get_all_projects()
    return render_template("projects.html", projects=projects) 


@app.route("/projects/<int:project_id>", methods=["GET"])
def project_detail(project_id):
    connection = get_flask_database_connection(app)
    project_repo = ProjectRepository(connection)
    content_repo = ProjectContentRepository(connection)
    project = project_repo.get_project(project_id)
    contents = content_repo.get_project_contents(project.id)
    project.contents = contents
    return render_template("project_contents.html", project = project)


@app.route("/sketchbook", methods=["GET"])
def sketchbook():
    connection = get_flask_database_connection(app)
    repo = SketchbookRepository(connection)
    sketches = repo.get_all_sketches()
    return render_template("sketchbook.html", sketches=sketches)


@app.route("/links", methods=["GET"])
def links():
    return render_template("links.html")


@app.route("/contact", methods=["GET"])
def contact():
    return render_template("contact.html")

@app.route("/auth/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        connection = get_flask_database_connection(app)
        repo = AuthRepository(connection)
        user = repo.get_user(username, password)
        session.clear()
        session['user_id'] = user.id
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/auth/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5000)))
