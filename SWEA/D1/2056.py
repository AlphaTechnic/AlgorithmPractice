N = int(input())
data = []


for i in range(N):
    yearmonthday = input()
    data.append(yearmonthday)


daytype1 = ['01', '02', '03', '04', '05', '06', '07', '08', '09',
            '10', '11', '12', '13', '14', '15', '16', '17', '18',
            '19', '20', '21', '22', '23', '24', '25', '26', '27',
            '28', '29', '30', '31']
daytype2 = ['01', '02', '03', '04', '05', '06', '07', '08', '09',
            '10', '11', '12', '13', '14', '15', '16', '17', '18',
            '19', '20', '21', '22', '23', '24', '25', '26', '27',
            '28', '29', '30']
daytype3 = ['01', '02', '03', '04', '05', '06', '07', '08', '09',
            '10', '11', '12', '13', '14', '15', '16', '17', '18',
            '19', '20', '21', '22', '23', '24', '25', '26', '27',
            '28']

monthtype1 = ['01', '03', '05', '07', '08', '10', '12']
monthtype2 = ['04', '06', '09', '11']
monthtype3 = ['02']


for num, m in enumerate(data):
    if m[4:6] in monthtype1 and m[6:9] in daytype1:
        print("#%s" % (num + 1), m[:4] + '/' + m[4:6] + '/' + m[6:])
    elif m[4:6] in monthtype2 and m[6:9] in daytype2:
        print("#%s" % (num + 1), m[:4] + '/' + m[4:6] + '/' + m[6:])
    elif m[4:6] in monthtype3 and m[6:9] in daytype3:
        print("#%s" % (num + 1), m[:4] + '/' + m[4:6] + '/' + m[6:])
    else:
        print("#%s" % (num+1), "-1")
