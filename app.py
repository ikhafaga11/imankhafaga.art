from flask import Flask, render_template, redirect, url_for, flash, request
from lib.database_connection import get_flask_database_connection
from lib.project_repository import ProjectRepository
from lib.project_image_repository import ProjectImageRepository
from lib.sketchbook_repository import SketchbookRepository
import os

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/projects", methods=["GET"])
def projects():
    connection = get_flask_database_connection(app)
    repo = ProjectRepository(connection)
    projects = repo.get_all_projects()
    return render_template("projects.html", projects=projects)

@app.route('/projects/<int:project_id>', methods=["GET"])
def project(project_id):
    connection = get_flask_database_connection(app)
    repo = ProjectImageRepository(connection)
    project_images = repo.get_all_project_images(project_id)
    return render_template('project_images.html', project_images = project_images)

@app.route("/sketchbook", methods=["GET"])
def sketchbook():
    connection = get_flask_database_connection(app)
    repo  = SketchbookRepository(connection)
    sketches = repo.get_all_sketches()
    return render_template("sketchbook.html", sketches = sketches)


@app.route("/links", methods=["GET"])
def links():
    return render_template("links.html")


@app.route("/contact", methods=["GET"])
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5000)))
