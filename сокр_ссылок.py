import pyshorteners


link = input('Введите ссылку: ')

s = pyshorteners.Shortener()
short = s.tinyurl.short(link)

print(short)

save = int(input("Вы хотите сохронить файл с ссылкой, то нажмите 1 "))

if save == 1:
    fin = open('shorteners.txt', 'wt')
    fin.write(short)
    fin.close()
else:
    print("Хорошо не сохраняю")
