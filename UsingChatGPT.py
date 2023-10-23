# 리스트 (List) 생성
my_list = [1, 2, 3, 4, 5]

# 튜플 (Tuple) 생성
my_tuple = (1, 2, 3, 4, 5)

# 딕셔너리 (Dict) 생성
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# 세트 (Set) 생성
my_set = {1, 2, 3, 4, 5}

# List 출력
print("List:")
print(my_list)

# Tuple 출력
print("\nTuple:")
print(my_tuple)

# Dict 출력
print("\nDict:")
print(my_dict)

# Set 출력
print("\nSet:")
print(my_set)

# List vs Tuple 비교
print("\nList vs Tuple:")
if my_list == list(my_tuple):
    print("List and Tuple are equal.")
else:
    print("List and Tuple are not equal.")

# List vs Dict 비교
print("\nList vs Dict:")
if set(my_list) == set(my_dict.keys()) and all(my_list[i] == my_dict[chr(ord('a') + i)] for i in range(len(my_list))):
    print("List and Dict are equal.")
else:
    print("List and Dict are not equal.")

# List vs Set 비교
print("\nList vs Set:")
if set(my_list) == my_set:
    print("List and Set are equal.")
else:
    print("List and Set are not equal.")

# Tuple vs Dict 비교
print("\nTuple vs Dict:")
if set(my_tuple) == set(my_dict.keys()) and all(my_tuple[i] == my_dict[chr(ord('a') + i)] for i in range(len(my_tuple))):
    print("Tuple and Dict are equal.")
else:
    print("Tuple and Dict are not equal.")

# Tuple vs Set 비교
print("\nTuple vs Set:")
if set(my_tuple) == my_set:
    print("Tuple and Set are equal.")
else:
    print("Tuple and Set are not equal.")

# Dict vs Set 비교
print("\nDict vs Set:")
if set(my_dict.keys()) == my_set:
    print("Dict and Set are equal.")
else:
    print("Dict and Set are not equal.")
