import numpy as np

def en_lang():
    arr_marks = list(np.array([4,4,4,4,4,5,4,5,4,3,4,5,5,5,4,4,5,5,5,3,3,3,4,5,5,4,0,4,4,4,4,3,5,5]))
    count_0 = arr_marks.count(0)
    count_2 = arr_marks.count(2)
    count_3 = arr_marks.count(3)
    count_4 = arr_marks.count(4)
    count_5 = arr_marks.count(5)
    arr_count = [count_0, count_2, count_3, count_4, count_5]
    marks = list(np.arange(0,6))
    del marks[1]

    return marks, arr_count
    
def phis_ed():
    arr_marks = list(np.array([5,3,5,4,5,3,4,5,4,4,5,0,5,5,0,4,4,5,4,5,4,5,5,4,5,4,0,5,4,5,4,3,4,3]))
    count_0 = arr_marks.count(0)
    count_2 = arr_marks.count(2)
    count_3 = arr_marks.count(3)
    count_4 = arr_marks.count(4)
    count_5 = arr_marks.count(5)
    arr_count = [count_0, count_2, count_3, count_4, count_5]
    marks = list(np.arange(0,6))
    del marks[1]

    return marks, arr_count

def ru_lang():
    arr_marks = list(np.array([4,4,4,4,4,5,4,4,5,4,5,4,5,5,3,4,4,4,5,3,3,5,4,5,5,4,4,4,4,4,4,4,5,4]))
    count_0 = arr_marks.count(0)
    count_2 = arr_marks.count(2)
    count_3 = arr_marks.count(3)
    count_4 = arr_marks.count(4)
    count_5 = arr_marks.count(5)
    arr_count = [count_0, count_2, count_3, count_4, count_5]
    marks = list(np.arange(0,6))
    del marks[1]

    return marks, arr_count

def math():
    arr_marks = list(np.array([3,3,2,3,3,3,2,3,3,3,2,3,4,4,3,2,3,3,5,2,3,2,3,2,4,3,2,3,2,3,2,2,3,3]))
    count_0 = arr_marks.count(0)
    count_2 = arr_marks.count(2)
    count_3 = arr_marks.count(3)
    count_4 = arr_marks.count(4)
    count_5 = arr_marks.count(5)
    arr_count = [count_0, count_2, count_3, count_4, count_5]
    marks = list(np.arange(0,6))
    del marks[1]

    return marks, arr_count

def OS():
    arr_marks = list(np.array([3,4,2,4,5,5,3,4,3,3,3,4,4,5,3,4,4,5,5,3,3,3,4,4,3,5,2,3,3,3,2,2,3,2]))
    count_0 = arr_marks.count(0)
    count_2 = arr_marks.count(2)
    count_3 = arr_marks.count(3)
    count_4 = arr_marks.count(4)
    count_5 = arr_marks.count(5)
    arr_count = [count_0, count_2, count_3, count_4, count_5]
    marks = list(np.arange(0,6))
    del marks[1]

    return marks, arr_count

def inf_tech():
    arr_marks = list(np.array([4,3,4,4,3,4,4,3,3,3,4,4,5,5,4,4,4,4,5,3,3,4,5,4,4,4,2,3,3,4,3,3,4,3]))
    count_0 = arr_marks.count(0)
    count_2 = arr_marks.count(2)
    count_3 = arr_marks.count(3)
    count_4 = arr_marks.count(4)
    count_5 = arr_marks.count(5)
    arr_count = [count_0, count_2, count_3, count_4, count_5]
    marks = list(np.arange(0,6))
    del marks[1]

    return marks, arr_count

def alg_and_prog():
    arr_marks = list(np.array([3,3,2,3,4,4,5,2,3,3,3,4,5,5,2,3,5,5,5,3,3,3,4,4,4,3,2,3,3,3,3,2,3,3]))
    count_0 = arr_marks.count(0)
    count_2 = arr_marks.count(2)
    count_3 = arr_marks.count(3)
    count_4 = arr_marks.count(4)
    count_5 = arr_marks.count(5)
    arr_count = [count_0, count_2, count_3, count_4, count_5]
    marks = list(np.arange(0,6))
    del marks[1]

    return marks, arr_count

def con_work():
    arr_marks = list(np.array([4,4,3,3,4,4,3,4,5,3,3,4,5,4,4,4,4,4,4,3,3,3,4,4,3,4,3,4,4,4,3,4,4,4]))
    count_0 = arr_marks.count(0)
    count_2 = arr_marks.count(2)
    count_3 = arr_marks.count(3)
    count_4 = arr_marks.count(4)
    count_5 = arr_marks.count(5)
    arr_count = [count_0, count_2, count_3, count_4, count_5]
    marks = list(np.arange(0,6))
    del marks[1]
    print('%.2f'%np.mean(arr_marks))
    return marks, arr_count

def con_work():
    arr_marks = list(np.array([4,4,3,3,4,4,3,4,5,3,3,4,5,4,4,4,4,4,4,3,3,3,4,4,3,4,3,4,4,4,3,4,4,4]))
    count_0 = arr_marks.count(0)
    count_2 = arr_marks.count(2)
    count_3 = arr_marks.count(3)
    count_4 = arr_marks.count(4)
    count_5 = arr_marks.count(5)
    arr_count = [count_0, count_2, count_3, count_4, count_5]
    marks = list(np.arange(0,6))
    del marks[1]

    return marks, arr_count

def MDK():
    arr_marks = list(np.array([3,3,3,3,4,4,3,4,3,3,3,4,4,5,3,2,4,4,5,3,3,3,4,4,4,3,2,3,4,2,2,2,3,4]))
    count_0 = arr_marks.count(0)
    count_2 = arr_marks.count(2)
    count_3 = arr_marks.count(3)
    count_4 = arr_marks.count(4)
    count_5 = arr_marks.count(5)
    arr_count = [count_0, count_2, count_3, count_4, count_5]
    marks = list(np.arange(0,6))
    del marks[1]

    return marks, arr_count