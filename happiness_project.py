import csv
filename = "ACME-HappinessSurvey2020.csv"  # File name
fields = []  # Column names
rows = []    # Data rows

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)  # Reader object

    fields = next(csvreader)  # Read header
    #print('fields is: ', fields)
    for row in csvreader:     # Read rows
        #print('row is ', row, '\n')
        rows.append(row)
        #print('row: ', row)

    print("Total no. of rows: %d" % csvreader.line_num)  # Row count
row = [3,4]
print('Field names are: ' + ', '.join(fields))

#print('rows is: ', rows)

'''print('\nFirst 5 rows are:\n')
for row in rows[:5]:
    for col in row:
        print("%10s" % col, end=" ")
    print('\n')'''

#print(rows[125])

Y = []
X1 = []
X2 = []
X3 = []
X4 = []
X5 = []
X6 = []
satisfaction = []

i = 0;
while i < len(rows):
    #print('index is ', i, '\n')
    #print('the ith row is: ', rows[i], '\n')
    #print('the Y value for the row is ', rows[i][0], '\n')
    Y.append(int(rows[i][0]))
    X1.append(int(rows[i][1]))
    X2.append(int(rows[i][2]))
    X3.append(int(rows[i][3]))
    X4.append(int(rows[i][4]))
    X5.append(int(rows[i][5]))
    X6.append(int(rows[i][6]))
    #satisfaction.append(X1[i]+X2[i]+X3[i]+X4[i]+X5[i]+X6[i])
    i = i+1
    
cutoff = 4
#print('X5 > ', cutoff)

# x1 gives 65% cutoff 5
# x2 gives 47% cutoff 5
# x3 gives 58% cutoff 4
# x4 gives 56% cutoff 3
# x5 gives 60% cutoff 4
# x6 gives 61% cutoff 4
i=0
value = 0
while i < len(rows):
    #satisfaction.append(0*X1[i] + 0*X2[i] + 3*X3[i] + 0*X4[i] + 3*X5[i] + 0*X6[i])
    #satisfaction.append(X5[i])
    value = 0
    if (X1[i] >= 5): value = value + 1
    #if (X2[i] >= 5): value = value + 1
    if (X3[i] >= 4): value = value + 1
    if (X4[i] >= 3): value = value + 1
    if (X5[i] >= 4): value = value + 1
    if (X6[i] >= 4): value = value + 1
    satisfaction.append(value)
    i = i + 1


i=0
#print(Y)
TP = 0
FP = 0
TN = 0
FN = 0
while i < len(rows):
#    print('hello')
    #print('Happiness is ', Y[i], '\n')
    if (satisfaction[i] >= cutoff and Y[i] == 1): TP = TP+1
    elif (satisfaction[i] >= cutoff and Y[i] == 0): FP = FP+1
    elif (satisfaction[i] < cutoff and Y[i] == 0): TN = TN+1
    elif (satisfaction[i] < cutoff and Y[i] == 1): FN = FN+1
    else: print('failure')
    #print('satisfaction is ', X1[i] + X2[i] + X3[i] + X4[i] + X5[i] + X6[i], '\n\n')
    i = i + 1

print('number of true positives: ', TP)
print('number of true negatives: ', TN)
print('number of false positives: ', FP)
print('number of false negatives: ', FN)

accuracy = (TP + TN) / (FP + FN + TP + TN)
positivity = TP / (TP + FP)
negativity = TN / (TN + FN)

print('accuracy is ', accuracy)
print('positivity is ', positivity)
print('negativity is ', negativity)
'''
i=0
TP = 0
FP = 0
TN = 0
FN = 0
while i < len(rows):
#    print('hello')
    #print('Happiness is ', Y[i], '\n')
    if (X5[i] >= 4 and Y[i] == 1): TP = TP+1
    elif (X5[i] >= 4 and Y[i] == 0): FP = FP+1
    elif (X5[i] < 4 and Y[i] == 0): TN = TN+1
    elif (X5[i] < 4 and Y[i] == 1): FN = FN+1
    else: print('failure')
    #print('satisfaction is ', X1[i] + X2[i] + X3[i] + X4[i] + X5[i] + X6[i], '\n\n')
    i = i + 1

print('number of true positives: ', TP)
print('number of true negatives: ', TN)
print('number of false positives: ', FP)
print('number of false negatives: ', FN)

accuracy = (TP + TN) / (FP + FN + TP + TN)
print('accuracy is ', accuracy)
'''
#X3 and X5, each at 4 or higher

#exploratory data analysis with numpy and statistical visualization