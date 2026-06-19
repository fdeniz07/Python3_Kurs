#1)
print('\n1.Lösung')
print('Hauptdatentypen (Zahl, Kollektion, bool, None)')

#2)
print('\n2.Lösung')
i = 10
f = 2.3
c = 2+1j
s = 'Wort'
t = (1,'2','a',9.99)
l = [1,2,3]
s = {4,5}
d = {'1':'a','2':'b','3':'c'}

print('\n','integer werte : ', type(i),
      '\n','float werte : ', type(f),
      '\n','complex werte : ', type(c),
      '\n','string werte : ', type(s),
      '\n','tuple werte : ', type(t),
      '\n','list werte : ', type(l),
      '\n','set werte : ', type(s),
      '\n','dictionary werte : ', type(d))

for element in t:
    print('\n',type(element))
          
#3)
print('\n3.Lösung')
i = 1
f = 2.3
print (float(i))
print (int(f))

#4)
print('\n4.Lösung')
l.append(4)
print(l)

print(t.index(9.99))

#5)
print('\n5.Lösung')
z = input('Geben Sie ein Text ein! :')
g = int(input('Geben Sie ein Ganzezahl ein! :'))
print('Zeichenkette : ',z + str(g))      
