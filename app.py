from flask import Flask, render_template, redirect, url_for, flash, session, request
from lib.database_connection import get_flask_database_connection
from lib.project_repository import ProjectRepository
from lib.project_content_repository import ProjectContentRepository
from lib.sketchbook_repository import SketchbookRepository
from lib.auth_repository import AuthRepository
from lib.project_content import ProjectContent
from lib.project import Project
import os
from dotenv import load_dotenv

app = Flask(__name__)

app.secret_key = os.getenv("FLASK_SECRET_KEY")


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/projects", methods=["GET", "POST"])
def projects():
    connection = get_flask_database_connection(app)
    repo = ProjectRepository(connection)
    editing_id = request.args.get("edit", type=int)
    

    if(editing_id and request.method == "POST"):
        title = request.form["title"]
        cover_image_url = request.form["cover_image_url"]
        model = Project(id=editing_id, cover_image_url=cover_image_url, title=title)
        repo.update_project(model)
        return redirect(url_for('projects'))

    if(request.method == "POST"):
        # get form values
        title = request.form["title"]
        cover_image_url = request.form["cover_image_url"]
        # instantiate model
        model = Project(title=title, cover_image_url=cover_image_url)
        # insert new project
        repo.post_project(model)
        # redirect to project to prevent for resubmision
        return redirect(url_for("projects"))
    projects = repo.get_all_projects()
    return render_template("projects.html", projects=projects, editing_id = editing_id) 


@app.route("/projects/<int:project_id>", methods=["GET", "POST"])
def project_detail(project_id):
    connection = get_flask_database_connection(app)
    project_repo = ProjectRepository(connection)
    content_repo = ProjectContentRepository(connection)
    project = project_repo.get_project(project_id)

    editing_id = request.args.get("edit", type=int)

    if(request.method == "POST" and editing_id):
        caption = request.form["caption"]
        image_url = request.form["image_url"]
        model = ProjectContent(project_id=project.id, caption=caption, image_url=image_url, id=editing_id)
        content_repo.update_content(model)
        return redirect(url_for("project_detail", project_id = project.id))


    if(request.method == "POST"):
        # get form values
        caption = request.form["caption"]
        image_url = request.form["image_url"]
        # instantial content model
        model = ProjectContent(project_id=project.id, caption=caption, image_url=image_url)
        # insert content
        new_content = content_repo.post_content(model)
        # add new content to project content list
        project.add_content(new_content)
        # redirect to project detailt to prevent form resubmission
        return redirect(url_for("project_detail", project_id = project.id))
    
    contents = content_repo.get_project_contents(project.id)
    project.contents = contents
    return render_template("project_contents.html", project = project, editing_id = editing_id)


@app.route("/projects/<int:project_id>/delete/content_id/<int:content_id>", methods = ["POST"])
def delete_project_detail(project_id, content_id):
    connection = get_flask_database_connection(app)
    repo = ProjectContentRepository(connection)
    repo.delete_content(content_id)
    return redirect(url_for("project_detail", project_id = project_id ))

@app.route("/projects/<int:project_id>/delete", methods=["POST"])
def delete_project(project_id):
    connection = get_flask_database_connection(app)
    repo = ProjectRepository(connection)
    repo.delete_project(id=project_id)
    return redirect(url_for("projects"))





@app.route("/sketchbook", methods=["GET", "POST"])
def sketchbook():
    connection = get_flask_database_connection(app)
    repo = SketchbookRepository(connection)
    if (request.method == "POST"):
        image_url = request.form['image_url']
        repo.add_sketch(image_url=image_url) 
        return redirect(url_for("sketchbook"))

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
