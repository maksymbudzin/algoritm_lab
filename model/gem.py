class Gem:
    def __init__(self, name='gem', price=0, carats_amount=0):
        self.name = name
        self.price = price
        self.carats_amount = carats_amount

    def __str__(self):
        return '\nName: "' + str(self.name) + \
               '"\nPrice: ' + str(self.price) + \
               '\nCarat amount is: ' + str(self.carats_amount) + "\n"
