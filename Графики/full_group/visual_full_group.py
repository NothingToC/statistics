import matplotlib.pyplot as plt
import data_full_group

colors = ['#b3b3b3','#ff7518','#edff21','#c0ff61','#66ff00']

plt.figure()

plt.subplot(3,3,1)
plt.tight_layout()
plt.title('График оценок по Английскому языку')
plt.ylabel('Количество оценок')
plt.xlabel('Оценки')
plt.bar(data_full_group.en_lang()[0], data_full_group.en_lang()[1], color=colors)

plt.subplot(3,3,2)
plt.title('График оценок по Физической культуре')
plt.ylabel('Количество оценок')
plt.xlabel('Оценки')
plt.bar(data_full_group.phis_ed()[0], data_full_group.phis_ed()[1], color=colors)

plt.subplot(3,3,3)
plt.title('График оценок по Русскому языку')
plt.ylabel('Количество оценок')
plt.xlabel('Оценки')
plt.bar(data_full_group.ru_lang()[0], data_full_group.ru_lang()[1], color=colors)

plt.subplot(3,3,4)
plt.title('График оценок по Высшей математике')
plt.ylabel('Количество оценок')
plt.xlabel('Оценки')
plt.bar(data_full_group.math()[0], data_full_group.math()[1], color=colors)

plt.subplot(3,3,5)
plt.title('График оценок по ОС и средам')
plt.ylabel('Количество оценок')
plt.xlabel('Оценки')
plt.bar(data_full_group.OS()[0], data_full_group.OS()[1], color=colors)

plt.subplot(3,3,6)
plt.title('График оценок по Информационным технологиям')
plt.ylabel('Количество оценок')
plt.xlabel('Оценки')
plt.bar(data_full_group.inf_tech()[0], data_full_group.inf_tech()[1], color=colors)

plt.subplot(3,3,7)
plt.title('График оценок по Основом алгоритмизации')
plt.ylabel('Количество оценок')
plt.xlabel('Оценки')
plt.bar(data_full_group.alg_and_prog()[0], data_full_group.alg_and_prog()[1], color=colors)

plt.subplot(3,3,8)
plt.title('График оценок по Конструктору карьеры')
plt.ylabel('Количество оценок')
plt.xlabel('Оценки')
plt.bar(data_full_group.con_work()[0], data_full_group.con_work()[1], color=colors)


plt.subplot(3,3,9)
plt.title('График оценок по Технологии разработки')
plt.ylabel('Количество оценок')
plt.xlabel('Оценки')
plt.bar(data_full_group.MDK()[0], data_full_group.MDK()[1], color=colors)
plt.show()