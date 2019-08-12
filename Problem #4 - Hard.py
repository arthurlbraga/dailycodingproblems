#Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
#For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
#You can modify the input array in-place.

# Constraints
# Must be O(n)
# Must be 0 < x < k(n)

def find_lowest(array_in):
    higher_than = 0
    lower_than = 0
    count = 0
    lowest = 1

    while(count < len(array_in)):
        current = array_in[count]

        if(current > lower_than):
            lower_than = current

        if(current < lower_than and current > higher_than):
            higher_than = current

        if(current == lowest):
            lowest = higher_than + 1

        print("HIGHER THAN: " + str(higher_than) + " | CURRENT: " + str(current) + " | LOWER THAN: " + str(lower_than) + " | LOWEST: " + str(lowest))
        count += 1

    if(lowest == lower_than):
        lowest += 1

    return lowest


array_in = [8,4,2,5,1,6,9,3,10,7]
result = find_lowest(array_in)
print(result)


# k(0) = 3
# k(1) = 4
# k(2) = -1
# k(3) = 1
#
#
# k(0) = 1 --
# k(1) =
# k(2) =
#
#
#
#
#
#
