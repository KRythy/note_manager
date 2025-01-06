title = []

title1 = input("Введите первый заголовок: ")
title2 = input("Введите второй заголовок: ")
title3 = input("Введите третий заголовок: ")

title.append(title1)
title.append(title2)
title.append(title3)

print("Заголовки заметок:")
for title in title:
    print(title)