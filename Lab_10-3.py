# Author: Caleb Moura

# define input list double, set parameters and returns.
def double_stuff(input_list):
   
    for i in range(len(input_list)):
        input_list[i] *= 2

# test case 1: List containing only integers.
int_list = [1, 2, 3, 4]
double_stuff(int_list)
print("Test case 1:", int_list)

# test case 2: List containing a combination of integer, string, and float values.
mixed_types_list = [1, 'two', 3.5, 'four']
double_stuff(mixed_types_list)  
print("Test case 3:", mixed_types_list)