def add_item(item, item_list=[]):
    print(f"item_list의 id: {id(item_list)}")
    item_list.append(item)
    return item_list


a = add_item("apple")
print(a)

b = add_item("banana")
print(b)

c = add_item("cherry")
print(c)
