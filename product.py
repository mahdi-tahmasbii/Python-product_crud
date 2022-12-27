class Products:
    _products = []

    def __init__(self, id: int, title: str, short_description: str, description: str, slug: str, permalink: str,
                 is_available: bool, sku: str, price: float, regular_price: float, sale_price: float, manage_stock: int,
                 stock_quantity: int, is_visible: bool, date_created_gmt, date_modified_gmt):
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
        self.sale_price = sale_price
        self.manage_stock = manage_stock
        self.stock_quantity = stock_quantity
        self.is_visible = is_visible
        self.date_created_gmt = date_created_gmt
        self.date_modified_gmt = date_modified_gmt

    def __repr__(self):
        return f'Product({self.id},{self.title},{self.short_description},{self.description},{self.slug}' \
               f'{self.sku},{self.permalink},{self.is_available},{self.price},{self.regular_price},{self.sale_price}' \
               f'{self.manage_stock},{self.stock_quantity},{self.is_visible},{self.date_created_gmt},{self.date_modified_gmt}) '

    def create_product(self):
        self._products.append(self)

    def read_product(self):
        products = [print(product) for product in self._products]
        return products

    def update_product(self, old_product, new_product):
        for product in self._products:
            if product == old_product:
                old_product = new_product
                print(f'Product updated: {old_product}')
            else:
                print('Product is not in the list')

    def delete_product(self, product):
        print('List is empty') if self._products == [] else self._products.remove(product)
