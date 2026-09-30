lim_t = float(input())
n = int(input())
T = []
errors = 0
ol = 0

for i in range(n):
    t = input()
    if t == 'error':
        errors += 1
    elif float(t) > lim_t:
        ol += 1
        T.append(float(t))
    else:
        T.append(float(t))

print(n)
print(errors)
print(ol)
print(f'{max(T):.1f}')
print(f'{sum(T)/(n-errors):.1f}')
