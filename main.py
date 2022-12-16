class Products:
    products = []

    def create(self, id, title, short_description, description, slug, permalink, isAvailable, sku, price, regular_price,
               manage_stock, stock_quantity, isVisible, date_created_gmt, date_modified_gmt):
        product = id, title + short_description + description + slug + permalink + isAvailable + sku + price + regular_price + manage_stock + stock_quantity + isVisible + date_created_gmt + date_modified_gmt
        return self.products.append(product)

    def show_products(self):
        products = [print(product) for product in self.products]
        return products

    def update_product(self, old_product, new_product):
        for product in self.products:
            if product == old_product:
                old_product = new_product
            else:
                print('Product is not in the list')


p = Products()
p.create(1, 't', 's', 'd', 's', 'p', 'i', 'sk', 'p', 'r', 'm', 'st', 'isv', 'dc', 'dm')
p.show_products()
p.update_product((1, 'tsdspiskprmstisvdcdm'), (2, 'wsdspiskprmstisvdcdm'))
p.show_products()
