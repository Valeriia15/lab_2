def esc(code):
    return f'\u001b[{code}m'

def flag_cz():
    for i in range(4):
        print(GREEN + '   ' * 5 + YELLOW + '   ' * 10 + GRAY)
    for i in range(4):
        print(GREEN + '   ' * 5 + RED + '   ' * 10 + GRAY)

def yzor():
    for j in range(9):
        if j < 2:
            i = 3 * j
            print(GRAY + ' ' * (12 - i) + WHITE + ' ' * (2 * i + 3) + GRAY + ' ' * (15 - 2 * i) + WHITE + (2 * i + 3) * ' ' + GRAY + (12 - i) * ' ')
        if 1 < j < 4:
            i = 3 * j
            print(GRAY + ' ' * (12 - i) + WHITE + ' ' * (2 * i + 3) + GRAY + ' ' * (9 - i) + WHITE + (i + 9) * ' ' + GRAY + (12 - i) * ' ')
        if j==4:
            i = 3 * j
            print(WHITE + 45 * ' ' + GRAY)
        if 4 < j < 7:
            i = 3 * j
            print(GRAY + ' ' * (i - 12) + WHITE + ' ' * (51 - 2 * i) + GRAY + ' ' * (i - 15) + WHITE + (33 - i) * ' ' + GRAY + (i - 12) * ' ')
        if j > 6:
            i = 3 * j
            print(GRAY + ' ' * (i - 12) + WHITE + ' ' * (51 - 2 * i) + GRAY + ' ' * (2 * i - 33) + WHITE + (51 - 2 * i) * ' ' + GRAY + (i - 12) * ' ')

def diagram(x, y):
    a = max(x, y)
    b = x + y - max(x, y)
    c = a - b
    for i in range(c):
        print(GRAY + 3 * ' ' + RED + 3 * ' ' + GRAY + 3 * ' ')
    for i in range(b):
        print(GRAY + 3 * ' ' + RED + 3 * ' ' + GRAY + 3 * ' ' + GREEN + 3 * ' ' + GRAY + 3 * ' ')
    print(GRAY + 3 * ' ' + str(a) + '%' + GRAY + 3 * ' ' + str(b) + '%' + GRAY + 3 * ' ')

def function():
    for i in range(9, 0, -1):
        if i >= 2:
            print(i, WHITE + '   ' * (i - 2) + RED + '   ' + WHITE + '   ' * (10 - i) + GRAY)
        else:
            print(i, WHITE + '   ' * 9 + GRAY)
    print('0  1  2  3  4  5  6  7  8  9')

RED = esc(41)
GREEN = esc(42)
YELLOW = esc(103)
GRAY = esc(0)
WHITE = esc(107)

flag_cz()
print(' ')

yzor()
print(' ')

function()
print(' ')

f = open('books.csv')
more = 0
less = 0
all = 0
dlina = 0
s = f.readline()
cp = ''
for s in f:
    s = f.readline()
    tz1 = s.find(';')
    tz2 = s.find(';', tz1 + 1)
    tz3 = s.find(';', tz2 + 1)
    tz4 = s.find(';', tz3 + 1)
    tz5 = s.find(';', tz4 + 1)
    tz6 = s.find(';', tz5 + 1)
    tz7 = s.find(';', tz6 + 1)
    tz8 = s.find(';', tz7 + 1)
    tchk = s.find('.', tz7 + 1)
    cp = s[tz7 + 1:tz8]
    dlina = tz8 - tz7
    dlina_t = tchk - tz7-1
    if dlina_t < dlina:
        cp = cp[0:dlina_t]
    if cp != '':
        all += 1
        if int(cp) < 150:
            less += 1
        if int(cp) >= 150:
            more += 1
more_di = round(more/(all/100))
less_di = 100-more_di
diagram(less_di, more_di)
if more >= less:
    print('до 150  от 150')
else:
    print('до 150  от 150')