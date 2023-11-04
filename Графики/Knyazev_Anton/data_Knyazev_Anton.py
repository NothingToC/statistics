import numpy as np
from scipy import stats

colors = []
#colors = ['#66ff00','#c0ff61','#edff21','#ff7518','#b3b3b3']

def all_marks():
    marks = np.array([5,5,4,3,5,4,5,4,4])

    return marks

def count_marks():
    count_0 = list(all_marks()).count(0)
    count_2 = list(all_marks()).count(2)
    count_3 = list(all_marks()).count(3)
    count_4 = list(all_marks()).count(4)
    count_5 = list(all_marks()).count(5)
    arr_count = np.array([count_5, count_4, count_3, count_2, count_0])
    removed_arr_count = list(np.array([]))

    for i in range(len(arr_count)):
        if arr_count[i] == 0:
            continue
        
        else:
            removed_arr_count.append(arr_count[i])

    if arr_count[0] > 0:
            colors.append('#66ff00')

    if arr_count[1] > 0:
        colors.append('#c0ff61')

    if arr_count[2] > 0:
        colors.append('#edff21')

    if arr_count[3] > 0:
        colors.append('#ff7518')

    if arr_count[4] > 0:
        colors.append('#b3b3b3')

    return removed_arr_count

def len_count_marks():
    return len(count_marks())

def labels():
    arr_labels_marks = list(set(all_marks()))
    arr_labels_marks.sort(reverse=True)
    return arr_labels_marks

def explode():
    min_mark = min(all_marks())
    arr_marks = list(set(all_marks()))
    arr_marks.reverse()
    index = arr_marks.index(min_mark)
    arr_explode = []

    for i in range(len(arr_marks)):
        if i == index:
            arr_explode.append(0.1)

        else:
            arr_explode.append(0.0)

    return arr_explode

def midle_count():
    return np.mean(all_marks())

def moda():
    return stats.mode(all_marks())

print("График оценок Князева Антона:")
print(f"Наиболее частая оценка: {moda()}")
print(f"Средний бал: {midle_count()}")