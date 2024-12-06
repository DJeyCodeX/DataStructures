# Create a function that takes two tuples and returns a tuple containing the element-wise sum of the input tuples.
#
# Example
#
# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)

# print(output_tuple)  # Expected output: (5, 7, 9)

def tuple_elementwise_sum(tuple1, tuple2):
    return tuple(map(sum, zip(tuple1, tuple2)))


tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print(tuple_elementwise_sum(tuple1, tuple2))