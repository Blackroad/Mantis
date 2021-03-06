from Model.projectmodel import Project
from generator.name_gen import random_string



def test_add_new_project(app,db):
    project_data = Project(name=random_string('name', 8, symbols=1), description='not')
    current_project_list = db.get_project_list()
    app.project.add_new_project(project_data)
    new_project_list = db.get_project_list()
    current_project_list.append(project_data)
    assert app.soap.soap_project_list()
    assert sorted(current_project_list, key=Project.id_or_max) == sorted(new_project_list, key=Project.id_or_max)


