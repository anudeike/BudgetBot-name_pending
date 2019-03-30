from faker import Faker

fake = Faker()

"""
0 - Retail
1 - Groceries
2 - Transportation
3 - Entertainment
"""
#template for a purchase

acct_holder_name = fake.name()
print(acct_holder_name)

purchase = {
    "merchant_name": "",
    "amount": 0,
    "category": 0,
    "description" : ""
}

purchases = []

# n = 150
# for x in range(150):
#     purchase["amount"] =
