def order_product(machine: dict, product, quantity, money):
    machine['products'][product]['stock'] -= quantity
    machine['balance'] += money
    machine['balance'] -= money % ((machine['products'][product]['price']) * (quantity))


def replace_product(machine: dict, product, pro_stock):
    if product not in machine['products']:
        machine['products'] = product
        machine['products'][pro_stock]['stock'] = pro_stock
        machine['products'][product]['price'] = 1
    else:
        machine['products'][pro_stock]['stock'] += pro_stock


def change_price(machine: dict, product, price):
    machine['products'][product] = int(price)


def push_money(machine: dict, money: str):
    machine['balance'] += money


def run(input_file: str, output_file: str) -> None:
    vending_machine = {'balance': 0, 'products': {'': {'stock': 0, 'price': 0}}}
    with open(input_file, 'r') as orders_data:
        product_info = orders_data.readline().split()
        order_code = product_info[0]
        match order_code:
            case 'O':
                order_product(vending_machine, product_info[1], product_info[2], product_info[3])
            case 'R':
                replace_product(vending_machine, product_info[1], product_info[2])
            case 'P':
                change_price(vending_machine, product_info[1], product_info[2])
            case 'M':
                push_money(vending_machine, product_info[1])
    with open(output_file, 'w') as after_orders:
        after_orders.write(f'{vending_machine["balance"]}')


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
