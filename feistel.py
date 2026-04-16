

l = 23
r = 6
key = 1

def function(num, key):
    return (num % 5)*key

def round_n(key):
    global l, r
    r_ = r
    r = function(r, key) ^ l
    l = r_


for i in range(1, 8, 1):
    print(l, r)
    round_n(key)
    key = key + 1

print(l, r)
tmp = r
r = l
l = tmp
print(l, r)
print()


for i in range(7, 0, -1):
    key = key - 1
    print(l, r)
    round_n(key)

print(l, r)
tmp = r
r = l
l = tmp
print(l, r)
