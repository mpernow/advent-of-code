f = open('report.dat', 'r')
report = f.readlines()
f.close()

report = [int(entry) for entry in report]

# print(report)

i = 0
j = 0

for i in range(len(report)):
    for j in range(i, len(report)):
        if report[i] + report[j] == 2020:
            print(i, j, report[i], report[j], report[i]*report[j])

i = 0
j = 0
k = 0

for i in range(len(report)):
    for j in range(i, len(report)):
        for k in range(j, len(report)):
            if report[i] + report[j] + report[k] == 2020:
                print(i, j, k, report[i], report[j], report[k], report[i]*report[j]*report[k])
