numbers = [10, 25, 7, 45, 30, 18]

largest = None
second_largest = None

for number in numbers:

    if largest is None or number > largest:
        second_largest = largest
        largest = number

    elif number != largest and (
        second_largest is None or number > second_largest
    ):
        second_largest = number

print("Largest number:", largest)
print("Second-largest number:", second_largest)