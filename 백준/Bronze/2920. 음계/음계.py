my_str = "".join(input().split(" "))
my_dict = {"12345678": "ascending", "87654321": "descending"}
print(my_dict.get(my_str, "mixed"))
