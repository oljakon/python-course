a = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р',\
     'с','т','у','ф','х','ц','ч','щ','ш','ъ','ы','ь','э','ю','я']
A = ['А','Б','В','Г','Д','Е','Ё','Ж','З','И','Й','К','Л','М','Н','О','П','Р',\
     'С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я']
l = ['.',',',';',':','/','\','|']

c = ''
b = input('Введите строку: ')
k = len(b)
for j in range(len(b)):
    if b[j] in a or b[j] in A:
        c += b[j]
    elif b[j] not in a and b[j] not in A:
        c += ' '
    else:
        c += ''

d = ''
n = []
for i in range(len(c)):
    if c[i] != ' ':
        d += c[i]
    else:
        n.append(d)
        d = ''
        
for i in range(len(n) - 1):
    for j in range(len(n) - 2, i - 1, -1):
        if len(n[j]) > len(n[j+1]):
            n[j], n[j+1] = n[j+1], n[j]

f = ''      
for i in range(len(n)):
    f += n[i]
    f += ' '
print(f)
