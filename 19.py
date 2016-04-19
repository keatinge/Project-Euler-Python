monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
monthNames = {0:"January", 1:"February", 2:"March", 3:"April", 4:"May", 5:"June",
	6:"July", 7:"August", 8:"September", 9:"October", 10:"November", 11:"December"}
	
daysOfWeek = [0,1,2,3,4,5,6]
daysOfWeekNames = {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"}


#problem gives us Jan 1 1990 is a monday
#note that everything here is zero indexed
weekDayIndex = 1
monthIndex = 0 


#we are forced to start at 1900
years = range(1900, 2001)


totalDays = 0 #number of times the first day of month is Sunday in 20th century

for year in years:
	#deal with leap years
	if year % 4 == 0:
		monthDays[1] = 29
		if year % 100 == 0:
			monthDays[1] = 28
			if year % 400 == 0:
				monthDays[1] = 29
	else:
		monthDays[1] = 28 #not leap year
		
	for monthIndex,month in enumerate(monthDays):
		for i in range(month):
			#but we only want to count Sundays if the year is after 1900
			if year > 1900 and weekDayIndex == 0 and i == 0: #if it's sunday and the first day of the month
				print(year, monthNames[monthIndex], str(i+1), daysOfWeekNames[weekDayIndex])
				totalDays += 1
			
			weekDayIndex += 1	
			#end of the week, start over again at 0
			if weekDayIndex == 7:
				weekDayIndex = 0
				
print(totalDays)