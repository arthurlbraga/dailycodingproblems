# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

def addUp(arr, k):
    for x in arr:
        if(x < k):
            if (k-x) in arr[1:]:
                return [x, (k-x)]

    return []

arr = [10, 15, 3, 7]
k = 17
result = addUp(arr, k)

if(len(result) > 0):
    print("True since " + str(" + ".join(str(x) for x in result)) + " is " + str(k))
