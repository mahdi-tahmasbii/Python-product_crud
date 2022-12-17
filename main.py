class Products:
    _products = []

    def __init__(self, id, title, short_description, description, slug, permalink, is_available, sku, price,
                 regular_price,
                 manage_stock, stock_quantity, is_visible, date_created_gmt, date_modified_gmt, _products):
        self.id = id
        self.title = title
        self.short_description = short_description
        self.description = description
        self.slug = slug
        self.permalink = permalink
        self.is_available = is_available
        self.sku = sku
        self.price = price
        self.regular_price = regular_price
        self.manage_stock = manage_stock
        self.stock_quantity = stock_quantity
        self.is_visible = is_visible
        self.date_created_gmt = date_created_gmt
        self.date_modified_gmt = date_modified_gmt

    def create_product(self, products):
        return self._products.append(products)

    def read_product(self):
        products = [print(product) for product in self._products]
        return products

    def update_product(self, old_product, new_product):
        for product in self._products:
            if product == old_product:
                old_product = new_product
                print('1')
            else:
                print('Product is not in the list')

    def delete_product(self, product):
        print('List is empty') if self._products == [] else self._products.remove(product)
