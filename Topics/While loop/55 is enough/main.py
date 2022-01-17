number = int(input())
s = 0
f = 0
end_num = 55
while number != end_num:
    s += number
    f += 1
    number = int(input())
print(f)
print(s)
print(round(s / f))