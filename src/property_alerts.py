```python
import json
from pymongo import MongoClient

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['real_estate_db']
alert_collection = db['property_alerts']

# Alert Schema
AlertSchema = {
    'user_id': '',
    'property_id': '',
    'alert_type': '',
    'alert_message': ''
}

def set_property_alert(user_id, property_id, alert_type):
    alertData = AlertSchema.copy()
    alertData['user_id'] = user_id
    alertData['property_id'] = property_id
    alertData['alert_type'] = alert_type

    if alert_type == 'new_listing':
        alertData['alert_message'] = 'A new property matching your preferences has been listed.'
    elif alert_type == 'price_change':
        alertData['alert_message'] = 'A property you are interested in has changed its price.'

    alert_collection.insert_one(alertData)

def get_property_alerts(user_id):
    user_alerts = alert_collection.find({'user_id': user_id})
    return list(user_alerts)

def delete_property_alert(alert_id):
    alert_collection.delete_one({'_id': alert_id})
```