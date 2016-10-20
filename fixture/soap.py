from suds.client import Client
from suds import WebFault

class SoapHelper:
    def __init__(self, app):
        self.app = app



    def can_login(self,username,password):
        client = Client("http://localhost/mantisbt-1.3.2/api/soap/mantisconnect.wsdl")
        try:
            client.service.mc_login(username,password)
        except WebFault:
            return False


    def added_project(self, username, password, project):
        client = Client("http://localhost/mantisbt-1.3.2/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_project_add(username, password, project)
        except WebFault:
            return False