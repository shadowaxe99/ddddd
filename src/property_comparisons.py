```python
import pandas as pd

class PropertyComparisons:
    def __init__(self, comparisonData):
        self.comparisonData = comparisonData

    def compare_properties(self, property1_id, property2_id):
        property1 = self.comparisonData.loc[self.comparisonData['id'] == property1_id]
        property2 = self.comparisonData.loc[self.comparisonData['id'] == property2_id]

        comparison_result = pd.concat([property1, property2]).T
        return comparison_result

    def get_comparison_data(self):
        return self.comparisonData

if __name__ == "__main__":
    comparisonData = pd.read_csv('comparisonData.csv')
    propertyComparisons = PropertyComparisons(comparisonData)
    print(propertyComparisons.compare_properties('P123', 'P456'))
```