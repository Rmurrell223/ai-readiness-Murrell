print("Hello, I am Ramon Murrell , and my student ID is R02418971.")

def calculate_stats(numbers):
    if not numbers:
        return 0, 0
    mean_val = sum(numbers) / len(numbers)
    max_val = max(numbers)
    return mean_val, max_val

my_list = [10, 25, 42, 7, 19]
mean_result, max_result = calculate_stats(my_list)

print(f"For the list {my_list}:")
print(f"Mean: {mean_result}")
print(f"Maximum: {max_result}")
