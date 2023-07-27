```python
import json
from src.property_recommendations import userPreferences
from src.property_data import PropertySchema

leadData = []

def getLeadGeneration():
    global leadData
    leadData = []
    for user in userPreferences:
        for property in PropertySchema:
            if user['budget'] >= property['price']:
                lead = {
                    'userId': user['id'],
                    'propertyId': property['id'],
                    'agentId': property['agentId']
                }
                leadData.append(lead)
    return leadData

def saveLeadData():
    with open('leadData.json', 'w') as outfile:
        json.dump(leadData, outfile)

def loadLeadData():
    global leadData
    with open('leadData.json') as json_file:
        leadData = json.load(json_file)
    return leadData
```