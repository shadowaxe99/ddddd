```python
import pandas as pd
from src.lead_generation import leadData
from src.property_alerts import alertData

conversionMetrics = {}

def calculateConversionRate():
    totalLeads = len(leadData)
    totalAlerts = len(alertData)
    
    if totalAlerts == 0:
        conversionMetrics['conversionRate'] = 0
    else:
        conversionMetrics['conversionRate'] = totalLeads / totalAlerts

def getConversionRateMetrics():
    calculateConversionRate()
    return conversionMetrics
```