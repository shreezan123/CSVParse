import matplotlib.pyplot as plt
csv = open('radiation.csv','r')
rad_list = list()

#parse the radiation value (8760) of them and store them in an array: rad_list
for line in csv:
        currentLine = line.split(',')
        rad_list.append(int(currentLine[6]))
i = 0
j = 24
day_list = list()

while True:
    #if we are finished with the data
    if j == 8784:
        break
    #index the rad_list to create record for hourly record
    each_day = rad_list[i:j]
    day_list.append(each_day)
    #increment pointers to move forward
    i += 24
    j += 24

sum_list = list()
average_list = list()
#store sum per day in sum_list
for day in day_list:
    sum_list.append(sum(day))
#store average per day in average_list
for sums in sum_list:
    average_list.append(float(sums/24))
print '----------------Sums---------------------'
print (sum_list)
print '----------------Average---------------------'
print (average_list)
#Bonus: draw histogram
plt.xlabel("Radiation")
plt.ylabel("Occurences")
plt.title("Radiation v/s Time")
plt.hist(rad_list,histtype='bar')

plt.show()
