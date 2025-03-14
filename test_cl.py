
from cloudant.client import Cloudant

#Cloudant credentials here 
# {
#   "apikey": "U6gkibgbshNn9notLjhUIoiULuASTckde0zI-onXSgX3",
#   "host": "d41c36bb-eaf3-4e85-a710-f4b654204838-bluemix.cloudantnosqldb.appdomain.cloud",
#   "iam_apikey_description": "Auto-generated for key crn:v1:bluemix:public:cloudantnosqldb:au-syd:a/cc16129c32434032a8f22d47936b97b6:ed2a5264-5eba-4f44-bbf4-e71f458773d5:resource-key:ddb37acd-39c2-4cc2-8822-ea8aa611b8aa",
#   "iam_apikey_id": "ApiKey-67cd5852-17f7-4338-93a1-086fbc0e2e86",
#   "iam_apikey_name": "to-do-List",
#   "iam_role_crn": "crn:v1:bluemix:public:iam::::serviceRole:Manager",
#   "iam_serviceid_crn": "crn:v1:bluemix:public:iam-identity::a/cc16129c32434032a8f22d47936b97b6::serviceid:ServiceId-07a46af0-6106-4c8e-bc54-2464913fe9b7",
#   "url": "https://d41c36bb-eaf3-4e85-a710-f4b654204838-bluemix.cloudantnosqldb.appdomain.cloud",
#   "username": "d41c36bb-eaf3-4e85-a710-f4b654204838-bluemix"
# }
cloudant_url="https://d41c36bb-eaf3-4e85-a710-f4b654204838-bluemix.cloudantnosqldb.appdomain.cloud"
cloudant_username="d41c36bb-eaf3-4e85-a710-f4b654204838-bluemix"
cloudant_apikey="U6gkibgbshNn9notLjhUIoiULuASTckde0zI-onXSgX3"

print(f"Username: {cloudant_username}")

#establishing a conneciton 
client = Cloudant.iam(cloudant_username, cloudant_apikey, connect = True)
database = client["todo_list"]

test_doc = {"task": "Test Cloudant Connection"}
doc = database.create_document(test_doc)

print(f"Document inserted: {doc['_id']} - {doc['task']}")
