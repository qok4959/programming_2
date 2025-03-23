def average(numbers: list) -> float:
    return sum(numbers) / len(numbers)


result:float=average([1.4, 2.5, 3.6, 4.7, 5.8, 6.9])  # 3.0
print("result:", result)