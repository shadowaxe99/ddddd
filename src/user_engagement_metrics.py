```python
import pandas as pd
from datetime import datetime

class UserEngagementMetrics:
    def __init__(self, engagement_data):
        self.engagement_data = engagement_data

    def calculate_time_spent(self):
        self.engagement_data['duration'] = self.engagement_data['end_time'] - self.engagement_data['start_time']
        return self.engagement_data['duration'].mean()

    def calculate_property_views(self):
        return self.engagement_data['property_views'].sum()

    def calculate_ai_interactions(self):
        return self.engagement_data['ai_interactions'].sum()

def load_engagement_data(file_path):
    engagement_data = pd.read_csv(file_path)
    engagement_data['start_time'] = pd.to_datetime(engagement_data['start_time'])
    engagement_data['end_time'] = pd.to_datetime(engagement_data['end_time'])
    return engagement_data

def main():
    engagement_data = load_engagement_data('engagement_data.csv')
    user_engagement = UserEngagementMetrics(engagement_data)
    avg_time_spent = user_engagement.calculate_time_spent()
    total_property_views = user_engagement.calculate_property_views()
    total_ai_interactions = user_engagement.calculate_ai_interactions()

    engagementMetrics = {
        'avg_time_spent': avg_time_spent,
        'total_property_views': total_property_views,
        'total_ai_interactions': total_ai_interactions
    }

    return engagementMetrics

if __name__ == "__main__":
    print(main())
```