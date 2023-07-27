```python
import os
import json
from ARVRSchema import ARVRSchema

class ARVR:
    def __init__(self):
        self.arVrData = {}
        self.schema = ARVRSchema()

    def load_data(self, filepath):
        if os.path.exists(filepath):
            with open(filepath, 'r') as file:
                self.arVrData = json.load(file)
        else:
            print("File not found")

    def get_virtual_tours(self, property_id):
        if property_id in self.arVrData:
            return self.arVrData[property_id]
        else:
            return "No virtual tour available for this property"

    def validate_data(self, data):
        errors = self.schema.validate(data)
        if errors:
            return False, errors
        else:
            return True, "Data is valid"

    def add_virtual_tour(self, property_id, data):
        is_valid, message = self.validate_data(data)
        if is_valid:
            self.arVrData[property_id] = data
            return "Virtual tour added successfully"
        else:
            return message

    def save_data(self, filepath):
        with open(filepath, 'w') as file:
            json.dump(self.arVrData, file)

arvr = ARVR()
arvr.load_data('ar_vr_data.json')
print(arvr.get_virtual_tours('property123'))
arvr.add_virtual_tour('property456', {'tour_link': 'www.example.com', 'images': ['img1.jpg', 'img2.jpg']})
arvr.save_data('ar_vr_data.json')
```