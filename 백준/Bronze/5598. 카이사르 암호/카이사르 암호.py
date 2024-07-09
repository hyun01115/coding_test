word = input()
for n in word:
    if ord(n)<=67:
        print(chr(ord(n) - 3 +26), end='')
    else:
        print(chr(ord(n)-3), end='')