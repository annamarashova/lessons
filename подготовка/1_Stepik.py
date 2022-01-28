a = input().lower()
b = input().lower()
a_1 = [num for num in a]
b_1 = [num for num in b]
if a[0] == 'a' or a[0] == 'c' or a[0] == 'e' or a[0]=='g':
    if int(a[1])%2 == 0:
        res_a = 1#белые
    else:
        res_a = 0#черные
else:
    if int(a[1])%2 == 0:
        res_a = 0#белые
    else:
        res_a = 1#черные
if b[0] == 'b' or b[0] == 'd' or b[0] == 'f' or b[0] == 'h':
    if int(b[1])%2 == 0:
        res = 0#черные
    else:
        res = 1#белые
else:
    if int(a[1])%2 == 0:
        res = 1#белые
    else:
        res = 0#черные
if res == res_a:
    print("YES")
else:
    print('NO')