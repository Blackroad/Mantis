from suds.client import Client
from suds import WebFault

class SoapHelper:
    def __init__(self, app):
        self.app = app



    def can_login(self,username,password):
        client = Client("http://localhost/mantisbt-1.3.0/api/soap/mantisconnect.wsdl")
        try:
            client.service.mc_login(username,password)
            return True
        except WebFault:
            return False


    def added_project(self,project_name):
        credentials = self.app.config['webadmin']
        client = Client("http://localhost/mantisbt-1.3.0/api/soap/mantisconnect.php?wsdl")
        try:
            project= client.factory.create('ProjectData')
            project.name = project_name
            client.service.mc_project_add(credentials['username'], credentials['password'], project)
            client.service.mc_project_get_id_from_name(credentials['username'], credentials['password'],
                                                            project_name)
            return True
        except WebFault:
            return False

    def deleted_project(self, project_id):
        credentials = self.app.config['webadmin']
        client = Client("http://localhost/mantisbt-1.3.0/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_project_delete(credentials['username'], credentials['password'], int(project_id))
            return True
        except WebFault:
            return False