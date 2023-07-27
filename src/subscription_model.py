```python
from src.user_engagement_metrics import engagementMetrics
from src.conversion_rate_metrics import conversionMetrics
from src.customer_satisfaction_metrics import satisfactionMetrics

class SubscriptionModel:
    def __init__(self):
        self.subscriptionData = {}

    def add_subscription(self, user_id, subscription_type):
        self.subscriptionData[user_id] = subscription_type

    def remove_subscription(self, user_id):
        if user_id in self.subscriptionData:
            del self.subscriptionData[user_id]

    def get_subscription(self, user_id):
        return self.subscriptionData.get(user_id, None)

    def get_all_subscriptions(self):
        return self.subscriptionData

    def calculate_revenue(self):
        premium_subscriptions = list(self.subscriptionData.values()).count('premium')
        basic_subscriptions = list(self.subscriptionData.values()).count('basic')
        return premium_subscriptions * 20 + basic_subscriptions * 10

    def calculate_conversion_rate(self):
        total_users = len(engagementMetrics)
        subscribed_users = len(self.subscriptionData)
        return conversionMetrics.calculate_conversion_rate(subscribed_users, total_users)

    def calculate_satisfaction_rate(self):
        satisfied_users = satisfactionMetrics.get_satisfied_users()
        subscribed_users = len(self.subscriptionData)
        return satisfactionMetrics.calculate_satisfaction_rate(satisfied_users, subscribed_users)

subscriptionModel = SubscriptionModel()
```