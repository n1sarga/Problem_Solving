a, b = map(int, input().split())

print(f'floor {a} / {b} = {int(a/b)}')
print(f'ceil {a} / {b} = {int(a/b + 1)}')
print(f'round {a} / {b} = {int(a/b)}')