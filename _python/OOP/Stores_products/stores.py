import products
class stores:
    def __init__(self,name):
        self.name=name
        self.products=[]

    def add_product(self, new_product):
        self.products.append(new_product)
    def sell_product(self, id):
        del self.products[id]
    def inflation(self, percent_increase):
        products.update_price(percent_increase,True)
    def set_clearance(self, category, percent_discount):
        products.update_price(percent_discount,False)




