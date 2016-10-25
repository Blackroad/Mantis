from suds.client import Client
from suds import WebFault

url = 'http://localhost/mantisbt-1.3.2/api/soap/mantisconnect.php?wsdl'
client = Client(url)
list = client.service.mc_projects_get_user_accessible('administrator','1234')
print (list)









