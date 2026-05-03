class Investment:
    def calculate_roi(self):
        pass
    
class Stock(Investment):
    def __init__(self, investment_amount, returns):
        self.investment_amount = investment_amount
        self.returns = returns
    def calculate_roi(self):
        return (self.returns - self.investment_amount) / self.investment_amount * 100

class Bond(Investment):
    def __init__(self, investment_amount, returns):
        self.investment_amount = investment_amount
        self.returns = returns
    def calculate_roi(self):
        return (self.returns - self.investment_amount) / self.investment_amount * 100

#creating instances of Stock and Bond
stock = Stock(1000,1200)
bond = Bond(1000,1100)

#put the in List
investments = [stock, bond]

#calculate and print ROI for each investment
for investment in investments:
    print(f"ROI: ",investment.calculate_roi())