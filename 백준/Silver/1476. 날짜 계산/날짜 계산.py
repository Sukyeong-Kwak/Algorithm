a, b, c = map(int, input().split())

n = b

a %= 15;b %= 28;c %= 19;


while(1):
    if n%15 == a and n%19 == c:
        break;
    n += 28

print(n)