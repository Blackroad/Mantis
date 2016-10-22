from suds.client import Client
from suds import WebFault

url = 'http://localhost/mantisbt-1.3.0/api/soap/mantisconnect.php?wsdl'
client = Client(url)
client.service.mc_project_delete('administrator','1234', 1)









