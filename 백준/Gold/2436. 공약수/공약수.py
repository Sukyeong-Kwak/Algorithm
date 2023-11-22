a, b = map(int, input().split())
c = b // a; e = 0; f = 0; GCD = 10;

for i in range(int(c**(0.5)), 0, -1):
    if c % i == 0:
        e = i; f = c//e; GCD = 1;
        for j in range(min(e,f), 1, -1):
            if (e%j == 0 and f%j == 0): GCD *= j;
    if (GCD == 1): break;
print(e*a, f*a)
