def run(input_file: str, output_file: str) -> None:
    vending_machine = {
        'balance': 0,
        'products': {
            '': {'stock': 0, 'price': 0},
        },
    }
    with open(input_file, 'r') as orders_data:
        product_info = orders_data.readline().split()
        order_code = product_info[0]
        match order_code:
            case 'O':
                product = product_info[1]
                quantity_requested = int(product_info[2])
                money_to_pay = int(product_info[3])
                vending_machine['products'][product]['stock'] -= quantity_requested
                vending_machine['balance'] += money_to_pay
                vending_machine['balance'] -= money_to_pay % (
                    (vending_machine['products'][product]['price']) * (quantity_requested)
                )

            case 'R':
                product = product_info[1]
                product_stock = int(product_info[2])
                if product not in vending_machine['products']:
                    vending_machine['products'] = product
                    vending_machine['products'][product_stock]['stock'] = product_stock
                    vending_machine['products'][product]['price'] = 1
                else:
                    vending_machine['products'][product_stock]['stock'] += product_stock

            case 'P':
                product = product_info[1]
                price = product_info[2]
                vending_machine['products'][product] = int(price)
            case 'M':
                money_to_restore = product_info[1]
                vending_machine['balance'] += money_to_restore
    with open(output_file, 'w') as after_orders:
        after_orders.write(f'{vending_machine["balance"]}')


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
