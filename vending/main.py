def run(input_file: str, output_file: str) -> None:
    with open(input_file) as operations:
        line = operations.readline()
        operation = line[:1]
        ## match case con las 4 operaciones
        if operation == 'M':
            money_sum()  ## cargar dinero
        if operation == 'P':
            change_price()  ## cambiar precio producto


maquina = {'balance': 0, 'products': {'': {'stock': 0, 'price': 0}}}


def money_sum(op_list: list):
    money_counter = 0
    if op_list[0] == 'M':
        money_counter += op_list[1]
        return money_counter


def change_price(op_list: list):
    if op_list[0] == 'P':
        product = op_list[1]
        maquina['products'][product]['price'] = op_list[2]


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
