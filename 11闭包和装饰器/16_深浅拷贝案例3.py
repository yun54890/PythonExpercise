

def add_item_to_cart(item,cart_list=[]):
    cart_list.append(item)
    return cart_list

print(add_item_to_cart("apple"))
print(add_item_to_cart("orange"))
print(add_item_to_cart("banana"))