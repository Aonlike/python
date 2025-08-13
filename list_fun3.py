new_tuple = ()


new_tuple = tuple(range(1,21))
print("Tuple:", new_tuple)

sum_odd_positions = sum(new_tuple[i] for i in range(1, len(new_tuple), 2))
print("Sum at odd positions:", sum_odd_positions)


sum_even_positions = sum(new_tuple[i] for i in range(0, len(new_tuple), 2))
print("Sum at even positions:", sum_even_positions)

sum_smallest_highest = min(new_tuple) + max(new_tuple)
print("Sum of smallest and highest element:", sum_smallest_highest)