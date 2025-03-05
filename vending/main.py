# en vez de con funciones externas los podemos hacer con funciones interiores
# cuando salgan por pantalla hay que imprimirlas
def run(input_file: str, output_file: str) -> None:
    vending_machine = {'balance': 0, 'products': {}}

    def order_product(product, quantity, money):
        # hay que cambiar esto porque hay que tener en cuenta más cosas
        vending_machine['products'][product]['stock'] -= quantity
        vending_machine['balance'] += money
        vending_machine['balance'] -= money % (
            (vending_machine['products'][product]['price']) * (quantity)
        )

    def replace_product(product, pro_stock):
        if product not in vending_machine['products']:
            vending_machine['products'][product] = {'stock': pro_stock, 'price': 1}
        else:
            vending_machine['products'][product]['stock'] += pro_stock

    def change_price(index_op, product, price):
        if product in vending_machine['products']:
            vending_machine['products'][product]['price'] = int(price)
        else:
            print(f'OP{index}: PRODUCT NOT FOUND')

    def push_money(money):
        vending_machine['balance'] += money

    def error_unknown_operation():
        return 'UNKNOWN OPERATION'

    def error_product_not_found():
        return 'PRODUCT NOT FOUND'

    def error_out_of_stock():
        return 'OUT OF STOCK'

    def error_not_enough_user_money():
        return print('NOT ENOUGH USER MONEY')

    with open(input_file, 'r') as orders_data:
        POSSIBLE_ORDER_CODES = 'ORPM'
        for index, line in enumerate(orders_data, start=1):
            product_info = orders_data.readline().split()
            order_code = product_info[0]
            if order_code in POSSIBLE_ORDER_CODES:
                match order_code:
                    case 'O':
                        continue
                        # order_product(product_info[1], int(product_info[2]), int(product_info[3]))
                    case 'R':
                        replace_product(product_info[1], int(product_info[2]))
                    case 'P':
                        change_price(index, product_info[1], int(product_info[2]))
                    case 'M':
                        push_money(int(product_info[1]))
            else:
                # esto no tiene sentido porque si entra por la O, entra por la O de arriba
                if order_code not in POSSIBLE_ORDER_CODES:
                    error_unknown_operation()
                if order_code == 'O':
                    if product_info[1] not in vending_machine:
                        error_product_not_found()
                    elif vending_machine['products'][product_info[1]]['stock'] < (product_info[2]):
                        error_out_of_stock()
                    elif (
                        int(product_info[3])
                        < int(product_info[2])
                        * vending_machine['products'][product_info[1]]['price']
                    ):
                        error_not_enough_user_money()

    with open(output_file, 'w') as after_orders:
        after_orders.write(f'{vending_machine["balance"]}\n')
        products = list(vending_machine['products'].keys())
        for product in products:
            stock = vending_machine['products'][product]['stock']
            price = vending_machine['products'][product]['price']
            after_orders.write(f'{product} {stock} {price}\n')


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
