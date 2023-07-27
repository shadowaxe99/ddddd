```python
import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';

import PropertyRecommendations from './property_recommendations';
import MarketAnalysis from './market_analysis';
import InvestmentAnalysis from './investment_analysis';
import PropertyComparisons from './property_comparisons';
import NeighborhoodInsights from './neighborhood_insights';
import PropertyAlerts from './property_alerts';
import VirtualTours from './virtual_tours';
import FinancingOptions from './financing_options';
import SubscriptionModel from './subscription_model';
import LeadGeneration from './lead_generation';
import ReferralFees from './referral_fees';

const Stack = createStackNavigator();

function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Home">
        <Stack.Screen name="Property Recommendations" component={PropertyRecommendations} />
        <Stack.Screen name="Market Analysis" component={MarketAnalysis} />
        <Stack.Screen name="Investment Analysis" component={InvestmentAnalysis} />
        <Stack.Screen name="Property Comparisons" component={PropertyComparisons} />
        <Stack.Screen name="Neighborhood Insights" component={NeighborhoodInsights} />
        <Stack.Screen name="Property Alerts" component={PropertyAlerts} />
        <Stack.Screen name="Virtual Tours" component={VirtualTours} />
        <Stack.Screen name="Financing Options" component={FinancingOptions} />
        <Stack.Screen name="Subscription Model" component={SubscriptionModel} />
        <Stack.Screen name="Lead Generation" component={LeadGeneration} />
        <Stack.Screen name="Referral Fees" component={ReferralFees} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

export default App;
```