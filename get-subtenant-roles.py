import requests
import json
import time
from jsonpath_ng import jsonpath
from jsonpath_ng.ext import parse
import warnings 

warnings.filterwarnings("ignore")

url = "https://{MORPHEUS-APPLIANCE-URL}/api/roles?max=25&offset=0&sort=name&direction=asc&roleType=account"

headers = {
    "accept": "application/json",
    "authorization": "Bearer {MORPHEUS-API-KEY}"
}

response = requests.get(url, headers=headers, verify=False)
data = response.json()

subtenantRolesQuery = parse("$.roles[?(@.ownerId[*] != 1)]")       # only retrieve subtenant roles
subtenantRoles = [match.value for match in subtenantRolesQuery.find(data)]

print(json.dumps(subtenantRoles, indent=2))
