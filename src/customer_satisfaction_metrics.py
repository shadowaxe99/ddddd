```python
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error

class CustomerSatisfactionMetrics:
    def __init__(self, satisfactionData):
        self.satisfactionData = satisfactionData

    def calculate_satisfaction_score(self):
        # Assume satisfaction score is on a scale of 1-10
        total_score = sum([data['score'] for data in self.satisfactionData])
        total_users = len(self.satisfactionData)
        return total_score / total_users

    def calculate_satisfaction_rate(self):
        # Assume satisfaction rate is the percentage of users who rated above 7
        satisfied_users = len([data for data in self.satisfactionData if data['score'] > 7])
        total_users = len(self.satisfactionData)
        return (satisfied_users / total_users) * 100

    def calculate_rmse(self):
        # Assume we have predicted scores and actual scores for comparison
        actual_scores = [data['actual_score'] for data in self.satisfactionData]
        predicted_scores = [data['predicted_score'] for data in self.satisfactionData]
        return mean_squared_error(actual_scores, predicted_scores, squared=False)

    def calculate_mae(self):
        # Assume we have predicted scores and actual scores for comparison
        actual_scores = [data['actual_score'] for data in self.satisfactionData]
        predicted_scores = [data['predicted_score'] for data in self.satisfactionData]
        return mean_absolute_error(actual_scores, predicted_scores)

if __name__ == "__main__":
    # Assume we have some satisfaction data
    satisfactionData = [
        {'user_id': 1, 'score': 8, 'actual_score': 7, 'predicted_score': 7.5},
        {'user_id': 2, 'score': 9, 'actual_score': 8, 'predicted_score': 8.5},
        {'user_id': 3, 'score': 7, 'actual_score': 7, 'predicted_score': 7.2},
        # More data...
    ]

    metrics = CustomerSatisfactionMetrics(satisfactionData)
    print("Satisfaction Score:", metrics.calculate_satisfaction_score())
    print("Satisfaction Rate:", metrics.calculate_satisfaction_rate())
    print("RMSE:", metrics.calculate_rmse())
    print("MAE:", metrics.calculate_mae())
```