# Transaction Category Classifier

Training a transaction category classifier based on the transactions that I've handcrafted since 2019.

Transaction labels are one of the following:
* Auto, Bank, Business, Development, Entertainment, Faith, Financial, Food, Gas, Gifts & Donations, Groceries, 
  Healthcare, Home Improvement, Housing, Loan, Medical, Other, Personal, Phone, Rent, Shopping, Sports, Tax, Travel,
  Utilities

Raw Features:
* Purchased_At (date): denoting when the purchase was made
* Amount (float, usd): denoting the amount of the purchase
* Description (str)  : denoting the description of the purchase

Label:
* Category (str): denoting the category of the expense. One of the above.