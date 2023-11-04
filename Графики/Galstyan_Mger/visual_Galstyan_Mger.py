import matplotlib.pyplot as plt
import data_Galstyan_Mger as data

colors = ['#66ff00','#c0ff61','#edff21','#ff7518','#b3b3b3']

plt.figure()
plt.tight_layout()

plt.title("Статистика всех оценок")
plt.pie(data.count_marks(), labels=data.labels(), colors=colors, autopct='%.0f%%', explode=data.explode())
plt.show()