def log_machine_status(output_file, machine):
    with open(output_file, 'w') as after_orders:
        after_orders.write(f'{machine["balance"]}')
        products = dict(sorted(machine['products'].items()))
        last_line = '\n'
        for product_name, product_data in products.items():
            stock = product_data['stock']
            price = product_data['price']
            after_orders.write(f'\n{product_name} {price} {stock}')
        after_orders.write(f'{last_line}')


def record_of_operations(operation_number: int, message: str):
    print(f'OP{operation_number}: {message}')


def error_unknown_operation(operation_number: int):
    record_of_operations(operation_number, 'UNKNOWN OPERATION')


def error_product_not_found(operation_number: int):
    record_of_operations(operation_number, 'PRODUCT NOT FOUND')


def error_out_of_stock(operation_number: int):
    record_of_operations(operation_number, 'OUT OF STOCK')


def error_not_enough_user_money(operation_number: int):
    record_of_operations(operation_number, 'NOT ENOUGH USER MONEY')


def operation_success(operation_number: int):
    record_of_operations(operation_number, 'OK')


def order_product(machine: dict, product, quantity, money, n_line):
    quantity = int(quantity)
    money = int(money)

    if product not in machine['products']:
        error_product_not_found(n_line)
    else:
        product_data = machine['products'][product]

        if product_data['stock'] < quantity:
            error_out_of_stock(n_line)
        else:
            final_price = product_data['price'] * quantity

            if final_price > money:
                error_not_enough_user_money(n_line)
            else:
                machine['products'][product]['stock'] -= quantity
                machine['balance'] += final_price
                operation_success(n_line)


def refill_product(machine: dict, product_name, product_stock, n_line):
    product_stock = int(product_stock)

    if product_name not in machine['products']:
        machine['products'][product_name] = {'stock': product_stock, 'price': 1}
        operation_success(n_line)
    else:
        product_data = machine['products'][product_name]
        product_data['stock'] += int(product_stock)
        operation_success(n_line)


def change_price(machine: dict, product_name, price, n_line: int):
    if product_name not in machine['products']:
        error_product_not_found(n_line)
    else:
        product_data = machine['products'][product_name]
        product_data['price'] = int(price)
        operation_success(n_line)


def push_money(machine: dict, money: str, n_line: int):
    machine['balance'] += int(money)
    operation_success(n_line)


def run(input_file: str, output_file: str) -> None:
    vending_machine = {'balance': 0, 'products': {}}
    POSSIBLE_ORDER_CODES = 'ORPM'

    with open(input_file, 'r') as orders_data:
        for n_line, line in enumerate(orders_data, start=1):
            product_info = line.strip().split()
            order_code = product_info[0]
            if order_code in POSSIBLE_ORDER_CODES:
                match order_code:
                    case 'O':
                        order_product(
                            vending_machine,
                            product_info[1],
                            product_info[2],
                            product_info[3],
                            n_line,
                        )
                    case 'R':
                        refill_product(vending_machine, product_info[1], product_info[2], n_line)
                    case 'P':
                        change_price(vending_machine, product_info[1], product_info[2], n_line)
                    case 'M':
                        push_money(vending_machine, product_info[1], n_line)
            else:
                error_unknown_operation(n_line)
            log_machine_status(output_file, vending_machine)


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
