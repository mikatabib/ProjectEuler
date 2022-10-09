LIM = 100
sum_of_squares = sum(map(lambda x: x**2, range(1, LIM + 1)))
square_of_sum = (LIM * (LIM + 1) / 2) ** 2

print(sum_of_squares)
print(square_of_sum)

result = square_of_sum - sum_of_squares
print(result)
