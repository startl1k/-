def find_thing(a, b):
    '''
    Находим индексы нужную строку в строке
    :param a: строка с фамилией, именем, датой и препаратом, и составом
    :param b: искомая строка
    :return: список индексов под которыми находятся нужная нам строка
    '''
    count = []
    for i in range(len(a)):
        if a[i] == b:
            count.append(i)
    return count
def fio_short(n):
    '''
    Сокращает ФИО до фамилии и инициалов
    :param n: фамилия имю отчество в виде строки
    :return: фамилия, инициалы
    '''
    a = list(n.split())
    return a[0] + ' ' + a[1][0] + '. ' + a[2][0] + '.'


Names = [] #фио ученых
preparations = [] # название препарата
dates = [] #дата создания препарата

f = open('scientist.txt', encoding = 'utf8')
top = f.readline()
scientists = [x.strip().split(',') for x in f]
f.close()


for i in range(len(scientists)):
    for j in scientists[i]:
        s1 = str(scientists[i])
        x = find_thing(s1, '#')
        #print(x)
        if x[0] < 32:
            Name = s1[:x[0]]
            Names.append(Name[2:])
            #print(Names)
        if x[1] > 32:
            preparation = s1[:x[1]]
            preparations.append(preparation[x[1]-(x[1]-x[0])+1:])
            #print(preparations)
        if x[2] >= 42:
            date = s1[:x[2]]
            dates.append(date[x[2]-(x[2]-x[1])+1:])
            #print(dates)
req_date = input()
while  req_date != 'эксперимент':
    req_date = req_date[6:] + '-' + req_date[3] + req_date[4] + '-' + req_date[0] + req_date[1]
    if req_date in dates:
        inde = find_thing(dates, req_date)[0]
        print(f'Ученый {fio_short(Names[inde])} создал препарат {preparations[inde]}-{dates[inde]}')
    else:
        print("В этот день ученые отдыхали")
    req_date = input()