# Для заданного ряда вычислить сумму элементов с точностью e и построить
# таблицу значений с заданным шагом, если за n операций ряд не сошелся -
# вывести информацию об этом.
# Кондрашова
# x - переменная
# eps - эпсилон
# nmax - максимальное число шагов
# step - шаг
# s - сумма
# t - текущий член ряда

x = float(input('Введите значение x: '))
eps = float(input('Введите значение eps: '))
nmax = int(input('Введите максимальное число шагов: '))
step = int(input('Введите шаг: '))

l = 65
print('\u250C', 15 * '\u2500', '\u252C', 15 * '\u2500', '\u252C',\
      16 * '\u2500', '\u252C', 16 * '\u2500','\u2510', sep = '')
print('\u2502\t№\t\u2502\tX\t\u2502\tt\t',\
      '\u2502', '       Y      ','\u2502')
print('\u251C', 15 * '\u2500', '\u253C', 15 * '\u2500', '\u253C',\
      16 * '\u2500', '\u253C', 16 * '\u2500','\u2524', sep = '')

i = 1
n = m = 1
t = x / 2
s = 1 + t
print('\u2502\t', i, '\t\u2502  ','{:9.3f}'.format(x), '  \u2502  ',\
      '{:9.3f}'.format(t), '   \u2502   ', '{:9.3f}'.format(s), '  \u2502')

while i < (nmax + 1):
     i += 1
     n += 1
     t = -t * x * m / 2 / n
     m += 2
     s += t
     
     if (i == 1 or (i - 1) % step == 0) and i <= nmax:
          tabs = abs(t)
          if len(str(tabs)) > 8:
               tpr = '{:1.3e}'.format(tabs)
          else:
               tpr = '{:9.7f}'.format(tabs)
          if len(str(s)) > 8:
               spr = '{:1.3e}'.format(s)
               sl = str(spr)
               if sl[3:] == '00e+00':
                    spr = '{:9.1f}'.format(s)
                    print('\u2502\t', i, '\t\u2502  ','{:9.3f}'.format(x),\
                          '  \u2502  ', tpr,'   \u2502   ', spr, '  \u2502')
               elif sl[6:] == '+00':
                    spr = sl[:-3]
                    print('\u2502\t', i, '\t\u2502  ','{:9.3f}'.format(x),\
                          '  \u2502  ', tpr,'   \u2502   ', spr, 2 * ' ',\
                          '  \u2502')
          else:
               spr = '{:9.7f}'.format(s)
               print('\u2502\t', i, '\t\u2502  ','{:9.3f}'.format(x),\
                     '  \u2502  ',tpr,'   \u2502   ', spr, '  \u2502')
          
     if i < nmax and abs(t) < eps:
          print('\u2514', 15 * '\u2500', '\u2534', 15 * '\u2500', '\u2534',\
                16 * '\u2500', '\u2534', 16 * '\u2500','\u2518', sep = '')
          print('Ряд сошелся за {:1.0f} операций\n'.format(i), \
                'Сумма: ', spr)
          break
     if i > nmax and abs(t) >= eps:
          print('\u2514', 15 * '\u2500', '\u2534', 15 * '\u2500', '\u2534',\
                16 * '\u2500', '\u2534', 16 * '\u2500','\u2518', sep = '')
          print('Ряд не сошелся за', nmax, 'операций\n',\
                'Сумма: ', spr)
     

      
     
