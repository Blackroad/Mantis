from Model.projectmodel import Project
from generator.name_gen import random_string



def test_add_new_project(app,db):
    project_data = Project(name=random_string('name', 8, symbols=1), description='not')
    assert app.soap.added_project(project_data.name)

