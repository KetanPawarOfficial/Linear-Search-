
pos = -1

def search(list, n):
    i = 0

    while i < len(list):
        if list[i] == n:

            globals()['pos'] = i
            return True
        i = i + 1

    return False

list = [4,7,2,1,9,5]
n = 7

if search(list, n):
    print("Element Found at posotion no", pos)
else:
    print("Element Not Found")