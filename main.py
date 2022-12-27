from product import Products


def main():
    p1 = Products(1, 'lenovo idea pad 3', 'gaming laptop', 'gaming model', 'lenovo-idea-pad-3', 'asda', True, '42', 420,
                  56,
                  75, 5, 5, True,
                  '2021/2/4',
                  '2021/2/4')
    p2 = Products(2, 'lenovo think pad', 'gaming laptop', 'gaming model', 'lenovo-idea-pad-3', 'asda', True, '42', 420,
                  56,
                  75, 5, 5, True,
                  '2021/2/4',
                  '2021/2/4')

    p1.create_product()
    p1.read_product()
    p1.update_product(p1, p2)
    p1.delete_product(p1)
    print(f'Product ({p1.title}) is Deleted')
    p1.list_all()

    print(isinstance(p1, Products))


if __name__ == "__main__":
    main()
