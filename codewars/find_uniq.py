'''There is an array with some numbers. All numbers are equal except for one. Try to find it!

findUniq([ 1, 1, 1, 2, 1, 1 ]) === 2
findUniq([ 0, 0, 0.55, 0, 0 ]) === 0.55
It’s guaranteed that array contains more than 3 numbers.

The tests contain some very huge arrays, so think about performance.

This is the first kata in series:
'''


def find_uniq(arr):
    unique = 0
    dict = {}
    dict[arr[0]] = arr[0]
    for i in range(len(arr)):
        left = arr[0] 
        middle = arr[len(arr)//2]
        right = arr[len(arr) - 1]
        if arr[i] not in dict:
            if arr[i] == middle and arr[i] == right:
                unique = arr[0]
            else:
                unique = arr[i]
            break
    return unique  

    find_uniq([ 1, 1, 1, 2, 1, 1 ])
    #find_uniq([ 0, 0, 0.55, 0, 0 ])
    #find_uniq([ 3, 10, 3, 3, 3 ])

'''
def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b


def find_uniq(arr):
    s = set(arr)
    for e in s:
        if arr.count(e) == 1:
            return e


def find_uniq(arr):
    a = sorted(arr)
    return a[0] if a[0] != a[1] else a[-1]
'''