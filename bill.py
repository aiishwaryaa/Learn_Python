class BlackShirt():
    color = "brown"
    size = "L"
    price = 3500

class WhiteShirt():
    color = "brown"
    size = "M"
    price = 1500

a = BlackShirt()
b = WhiteShirt()

print("Total Bill: "+str(a.price + b.price))