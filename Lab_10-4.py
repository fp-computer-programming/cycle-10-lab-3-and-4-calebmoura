# Author: Caleb Moura

# define index list and set restrictions to names and returns.
def indexed_names(names):
    
    indexed_list = [f"{index}: {name}" for index, name in enumerate(names)]
    return indexed_list

# test case 1: List with only integers.
integers_list = [5, 10, 15, 20]
result_integers = indexed_names(integers_list)
print("Test Case 1:")
print(result_integers)

# test case 2: List with a combination of integer, string, and float values.
mixed_values_list = [1, "apple", 3.14, "blue", 5]
result_mixed_values = indexed_names(mixed_values_list)
print("\nTest Case 3:")
print(result_mixed_values)