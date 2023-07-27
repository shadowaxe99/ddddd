```python
import pandas as pd
from sklearn.linear_model import LinearRegression

# Define the InvestmentSchema
class InvestmentSchema:
    def __init__(self, property_price, rental_income, operating_expenses, mortgage_rate, loan_term):
        self.property_price = property_price
        self.rental_income = rental_income
        self.operating_expenses = operating_expenses
        self.mortgage_rate = mortgage_rate
        self.loan_term = loan_term

# Function to calculate ROI
def calculate_roi(investmentData):
    roi = (investmentData.rental_income - investmentData.operating_expenses) / investmentData.property_price
    return roi

# Function to calculate financial projections
def financial_projections(investmentData):
    # Calculate monthly mortgage payment
    monthly_rate = investmentData.mortgage_rate / 12 / 100
    n_payments = investmentData.loan_term * 12
    monthly_payment = investmentData.property_price * monthly_rate * (1 + monthly_rate)**n_payments / ((1 + monthly_rate)**n_payments - 1)
    
    # Calculate net cash flow
    net_cash_flow = investmentData.rental_income - monthly_payment - investmentData.operating_expenses
    
    # Calculate cash on cash return
    cash_on_cash_return = net_cash_flow / investmentData.property_price
    
    return monthly_payment, net_cash_flow, cash_on_cash_return

# Function to get investment analysis
def getInvestmentAnalysis(investmentData):
    roi = calculate_roi(investmentData)
    monthly_payment, net_cash_flow, cash_on_cash_return = financial_projections(investmentData)
    
    investment_analysis_message = {
        'roi': roi,
        'monthly_payment': monthly_payment,
        'net_cash_flow': net_cash_flow,
        'cash_on_cash_return': cash_on_cash_return
    }
    
    return investment_analysis_message
```