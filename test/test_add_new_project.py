from Model.projectmodel import Project

def test_add_new_project(app):
    app.project.add_new_project(Project(name='new',description='not'))