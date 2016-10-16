from Model.projectmodel import Project
from generator.name_gen import random_string
import random


def test_add_new_project(app,db):
    if len(db.get_project_list())==0:
        app.project.add_new_project(Project(name=random_string('name', 7, symbols=1),description='not'))
    current_project_list = db.get_project_list()
    project_id = random.choice(current_project_list)
    app.project.delete_project(project_id.id)
    current_project_list.remove(project_id)
    new_project_list = db.get_project_list()
    assert current_project_list == new_project_list
