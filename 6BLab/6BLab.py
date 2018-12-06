monthsOfTheYear = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
weekends = {monthsOfTheYear[0]: [6,7,13,14,20,21,27,28],
monthsOfTheYear[1]: [3,4,10,11,17,18,24,25],
monthsOfTheYear[2]: [3,4,10,11,17,18,24,25,31],
monthsOfTheYear[3]: [1,7,8,14,15,21,22,28,29],
monthsOfTheYear[4]: [5,6,12,13,19,20,26,27],
monthsOfTheYear[5]: [2,3,9,10,16,17,23,24,30],
monthsOfTheYear[6]: [1,7,8,14,15,21,22,28,29],
monthsOfTheYear[7]: [4,5,11,12,18,19,25,26],
monthsOfTheYear[8]: [1,2,8,9,15,16,22,23,29,30],
monthsOfTheYear[9]: [6,7,13,14,20,21,27,28],
monthsOfTheYear[10]: [3,4,10,11,17,18,24,25],
monthsOfTheYear[11]: [1,2,8,9,15,16,22,23,29,30]}

print("What day is your birthday on?")
month = input("Month(3 letter abbreviation) - ").lower()
day = int(input("Day(DD) - "))
z = 0
y = 0

for a in range(len(monthsOfTheYear)):
    if(monthsOfTheYear[a] == month):
        if a < 9:
            m1 = 0
            m2 = a + 1
        else:
            m1 = 1
            m2 = a - 9

for i in weekends:
    if i == month:
        for j in weekends[i]:
            if j == day:
                print(str(m1) + str(m2) + "/" + str(day) + "/18: " + "Your birthday is on a weekend.")
                y = j
if y == z:
    print(str(m1) + str(m2) + "/" + str(day) + "/18: Your birthday is not on a weekend.")
