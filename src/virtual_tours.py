```python
import os
from ARVR import ARVR

class VirtualTour:
    def __init__(self):
        self.arvr = ARVR()
        self.virtualTourData = {}

    def getVirtualTour(self, propertyId):
        # Fetch the virtual tour data for the given propertyId
        self.virtualTourData = self.arvr.fetchVirtualTour(propertyId)
        return self.virtualTourData

    def displayVirtualTour(self, propertyId):
        # Display the virtual tour for the given propertyId
        virtualTourData = self.getVirtualTour(propertyId)
        self.arvr.displayVirtualTour(virtualTourData)

    def saveVirtualTour(self, propertyId):
        # Save the virtual tour data for the given propertyId
        virtualTourData = self.getVirtualTour(propertyId)
        with open(os.path.join('virtual_tours', f'{propertyId}.json'), 'w') as file:
            json.dump(virtualTourData, file)

if __name__ == "__main__":
    virtualTour = VirtualTour()
    propertyId = '12345'
    virtualTour.displayVirtualTour(propertyId)
    virtualTour.saveVirtualTour(propertyId)
```