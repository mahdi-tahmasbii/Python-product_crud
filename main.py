from product import Products

p1 = Products('1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1')

p1.create_product(p1)
print(Products.read_product(p1))
