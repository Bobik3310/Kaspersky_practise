
print(''.join([[chr(i) for i in range(ord('a'), ord('z') + 1)][i - 1] for count, i in enumerate(list(map(int, '23|8|1|20|4|15|25|15|21|11|14|15|23|1|2|15|21|20|1|2|3'.split('|'))),start=0)]))
