import matplotlib.pyplot as plt
import data_Selutin_Danil as data

plt.figure()
plt.tight_layout()

plt.title("Статистика всех оценок")
plt.pie(data.count_marks(), labels=data.labels(), colors=data.colors, autopct='%.0f%%', explode=data.explode())
plt.show()