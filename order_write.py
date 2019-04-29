def write_my_order_from_string(file_name,order):
    try:
        with open (file_name, "a") as file:
                file.write(order_string + "\n")

    except FileNotFoundError as errmsg:
        print("No file to write on. Check naming.")
        raise

def write_my_order_from_list(file_name, order):
    try:
        with open(file_name, "a") as file:
            for food_item in order:
                file.write(food_item + "\n")

    except FileNotFoundError as errmsg:
        print("No file to write on. Check naming.")
        raise

def write_my_order_from_dictionary(file_name,order_dictionary):
    try:
        with open (file_name, "a") as file:
            for value in order_dictionary.values():
                file.write(str(value)+ "\n")

    except FileNotFoundError as errmsg:
        print("No file to write on. Check naming.")
        raise


order_list = ["fries", "Big Mac", "Lamb Chops", "Steak" ]
write_my_order_from_list("order.txt",order_list)

order_string = "banana shake"
write_my_order_from_string("order.txt", order_string)

order_dictionary = {"item": "apples",
                    "price": 14}

write_my_order_from_dictionary("order.txt",order_dictionary)