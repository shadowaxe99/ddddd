```python
import pandas as pd
from sklearn.neighbors import NearestNeighbors

class NeighborhoodInsights:
    def __init__(self, neighborhood_data):
        self.neighborhood_data = neighborhood_data
        self.model = NearestNeighbors(n_neighbors=5, algorithm='ball_tree')
        self.model.fit(self.neighborhood_data[['latitude', 'longitude']])

    def get_neighborhood_insights(self, property_location):
        distances, indices = self.model.kneighbors([property_location])
        neighborhood_indices = indices[0]
        neighborhood_insights = self.neighborhood_data.iloc[neighborhood_indices]
        return neighborhood_insights.to_dict()

if __name__ == "__main__":
    neighborhood_data = pd.read_csv('neighborhood_data.csv')
    neighborhood_insights = NeighborhoodInsights(neighborhood_data)
    property_location = [40.7128, -74.0060]  # Example property location (latitude, longitude)
    neighborhood_insights = neighborhood_insights.get_neighborhood_insights(property_location)
    print(neighborhood_insights)
```