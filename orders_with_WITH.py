# def open_using_with_then_print(file_name):
#
#     try:
#         with open(file_name,"r") as file:
#             for line in file.readlines():
#                 print(line.rstrip("\n"))
#
#
#     except FileNotFoundError as errmsg:
#
#         print("There has been an error!")
#         print(errmsg)
#         raise
#     finally:
#         print("\nDone. Execution completed!")
#
# open_using_with_then_print("order.txt")
#
#
