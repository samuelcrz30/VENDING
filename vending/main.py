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

def error_unknown_operation():
    return 'UNKNOWN OPERATION'

def error_product_not_found():
    return 'PRODUCT NOT FOUND'

def error_out_of_stock():
    return 'OUT OF STOCK'

def error_not_enough_user_money():
    return 'NOT ENOUGH USER MONEY'

def run(input_file: str, output_file: str) -> None:
    vending_machine = {'balance': 0, 'products': {'': {'stock': 0, 'price': 0}}}
    with open(input_file, 'r') as orders_data:
        product_info = orders_data.readline().split()
        order_code = product_info[0]
        POSSIBLE_ORDER_CODES = 'ORPM'
        if order_code in POSSIBLE_ORDER_CODES:
            match order_code:
                case 'O':
                    order_product(vending_machine, product_info[1], product_info[2], product_info[3])
                case 'R':
                    replace_product(vending_machine, product_info[1], product_info[2])
                case 'P':
                    change_price(vending_machine, product_info[1], product_info[2])
                case 'M':
                    push_money(vending_machine, product_info[1])
        else:
            if order_code not in POSSIBLE_ORDER_CODES:
                error_unknown_operation()
            if order_code == 'O':
                if product_info[1] not in vending_machine:
                    error_product_not_found()
                elif vending_machine['products'][product_info[1]]['stock'] < int(product_info[2]):
                    error_out_of_stock()
                elif int(product_info[3]) < int(product_info[2]) * vending_machine['products'][product_info[1]]['price']:
                    error_not_enough_user_money()
       
    with open(output_file, 'w') as after_orders:
        after_orders.write(f'{vending_machine["balance"]}')
