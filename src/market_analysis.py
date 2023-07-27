```python
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

class MarketAnalysis:
    def __init__(self, market_data):
        self.market_data = market_data
        self.marketData = pd.DataFrame()

    def load_data(self):
        self.marketData = pd.read_csv(self.market_data)

    def preprocess_data(self):
        scaler = StandardScaler()
        self.marketData = scaler.fit_transform(self.marketData)

    def analyze_market(self):
        kmeans = KMeans(n_clusters=5, random_state=0)
        self.marketData['Cluster'] = kmeans.fit_predict(self.marketData)

    def get_market_analysis(self):
        self.load_data()
        self.preprocess_data()
        self.analyze_market()
        return self.marketData

if __name__ == "__main__":
    market_analysis = MarketAnalysis('market_data.csv')
    marketData = market_analysis.get_market_analysis()
    print(marketData)
```