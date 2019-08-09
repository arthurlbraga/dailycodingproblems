# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
# Follow-up: what if you can't use division?


def product(numbers):
    old = 1
    result = []
    count = len(numbers)
    last = 1
    if(count > 0):
        if(count == 1):
            return [numbers[0]]
        else:
            for x in range(count):
                if(x > 0):
                    last = last * numbers[x]

                if(x == 0):
                    result.append(numbers[x])
                else:
                    old = result[0]
                    for y in range(len(result)):
                        result[y] = result[y] * numbers[x]

                    result.append(old)
                    if(x == count - 1):
                        result[0] = last

    return result


numbers = [3, 2, 1]
result = product(numbers)
print(result)
