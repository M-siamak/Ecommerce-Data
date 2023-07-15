
class Buyer:
    def __init__(self, name, budget):
        self.name = name
self.budget = budget
def buy_product(self, sellers, products, prices, quantities):
    product = random.choice(products)
price = prices[product]
quantity = quantities[product]
if price <= self.budget and quantity > 0:
    transaction = {'buyer': self.name, 'seller': None, 'product': 
product}
sellers_with_product = [seller for seller, seller_products in
quantities.items() if product in seller_products and seller_products[product] 
> 0]
if sellers_with_product:
    seller = random.choice(sellers_with_product)
transaction['seller'] = seller
quantities[seller][product] -= 1
return transaction
return None
class Seller:
    def __init__(self, name):
        self.name = name
def restock_products(self, quantities):
    sold_out_products = [product for product, seller_products in
quantities.items() if all(quantity == 0 for quantity in
seller_products.values())]
for product in sold_out_products:
    quantities[self.name][product] = random.randint(1, 10)
def calculate_total_sales(self, transactions, prices):
    total_sales = sum([prices[transaction['product']] for transaction in
transactions if transaction['seller'] == self.name])
    return total_sales
# Initialization
buyers = [Buyer('b1', 50), Buyer('b2', 30), Buyer('b3', 40)]
sellers = [Seller('s1'), Seller('s2'), Seller('s3')]
products = ['p1', 'p2', 'p3']
prices = {'p1': 10, 'p2': 20, 'p3': 30}
quantities = {'s1': {'p1': 5, 'p2': 3, 'p3': 7}, 's2': {'p1': 4, 'p2': 6, 
'p3': 2}, 's3': {'p1': 2, 'p2': 8, 'p3': 4}}
transactions = []
# Buyer Behavior
for buyer in buyers:
    transaction = buyer.buy_product(sellers, products, prices, quantities)
if transaction:
    transactions.append(transaction)
# Seller Behavior
for seller in sellers:
    seller.restock_products(quantities)
total_sales = seller.calculate_total_sales(transactions, prices)
print(f"{seller.name} total sales: {total_sales}")
# Termination
if all(all(quantity == 0 for quantity in seller_products.values()) for
seller_products in quantities.values()):
    print("All products sold out!")