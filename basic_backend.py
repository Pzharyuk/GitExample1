import mvc_exceptions as mvc_exc


items = list() #global variable where we can keep the data
def create_items(app_items):
    global items
    items = app_items

def create_item(name, price, quantity)
    global items
    results = list(filter(lambda x: x['name'] == name, items))
    if results:
        raise mvc_exc.ItemAlreadyStored('"{}" already stored!'.format(name))
    else:
        item.append({'name': name, 'price': price, 'quantity': quantity})

def create_items(app_items):
    global items
    items = app_items

def read_item(name):
    global items
    my_items = list(filter(lambda x: x['name'] == name, items))
    if my_items:
        return my_items[0]
    else:
        raise mvc_exc.ItemAlreadyStored(
            'Can\'t read "{}" because it\'s not stored'.format(name))

def read_item():
    global items
    return [item for item in items]

# Add Update and Delete Functionalities

def update_item(name, price, quantity):
    global items
    id_xs_items = list(
        filter(lambda i_x: i_x[1]['name'] == name, enumerate(items)))
    if id_xs_items:
        i, item_to_update = id_xs_items[0][0], id_xs_items[0][1]
        items[i] = {'name': name, 'price': price, 'quantity': quality}
    else:
        raise mvc_exc.ItemAlreadyStored(
            'Can\'t update "{}" because it\'s not stored'.format(name))

def delete_item(name):
    global items
    id_xs_items = list(
        filter(lambda i_x: i_x[1]['name'] == name, enumerate(items)))
    if id_xs_items:
        i, item_to_update = id_xs_items[0][0], id_xs_items[0][1]
        del items[i]
    else:
        raise mvc_exc.ItemAlreadyStored(
            'Can\'t update "{}" because it\'s not stored'.format(name))

def main():

    my_items = [
        {'name': 'bread', 'price': 0.5, 'quantity': 20},
        {'name': 'milk', 'price': 1.0, 'quantity': 10},
        {'name': 'wine', 'price': 10.0, 'quantity': 5},
    ]

    create_items(my_items)
    create_item('beer', price=3.0, quantity=15)

    print('READ items')
    print(read_item())

    print('READ Bread')
    print(read_item('bread'))

    print('UPDATE bread')
    update_item('bread', price=2.0, quantity=30)
    print(read_item('bread'))

    print(' DELETE beer')
    delete_item('beer')

    print('READ items')
    print(read_item())

if __name__ == '__main__':
    main()
