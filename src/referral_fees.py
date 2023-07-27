```python
import json

# Load referral data
with open('referralData.json', 'r') as file:
    referralData = json.load(file)

class ReferralFees:
    def __init__(self, referralData):
        self.referralData = referralData

    def calculateReferralFees(self, transactionValue):
        referralFeePercentage = self.referralData['referralFeePercentage']
        referralFee = transactionValue * (referralFeePercentage / 100)
        return referralFee

    def updateReferralData(self, newReferralData):
        self.referralData = newReferralData
        with open('referralData.json', 'w') as file:
            json.dump(self.referralData, file)

# Create an instance of ReferralFees
referralFees = ReferralFees(referralData)

# Calculate referral fees for a transaction of value $500,000
transactionValue = 500000
print(f"The referral fee for a transaction of value ${transactionValue} is ${referralFees.calculateReferralFees(transactionValue)}")

# Update referral data
newReferralData = {
    "referralFeePercentage": 2.5
}
referralFees.updateReferralData(newReferralData)
```