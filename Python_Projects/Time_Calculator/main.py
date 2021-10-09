import math

def add_time(start, duration, day=None):
	#declare
	time_start = start.split(":")
	hour_s = int(time_start[0])
	end = time_start[1].split(" ")
	minutes_s = int(end[0])
	end_s = end[1]
	day_s = ""
	text_days = ""

	duration = list(map(int, duration.split(":")))
	hour_d = duration[0]
	minutes_d = duration[1]

	day_incre = 0

	days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

	#search the minutes first to check if there minutes going to hour.
	m_now = (minutes_s + minutes_d)
	if m_now > 60 :
		m_now = m_now % 60
		hour_s += 1

	# check if hour increment is 24.
	if(hour_d == 24):
		h_now = hour_s
		day_incre = 1
		text_days = "(next day)"
		if(day!= None):
			day = day.lower().capitalize()
			days_now = days.index(day)
			day = days[days_now]
	else:
		#if not then proceed and set the day_increment.
		h_now = (hour_s + hour_d)
		if(hour_d>24):
			day_incre = math.floor((hour_s + hour_d) / 24)	
	# if the hour is more than 12 then convert the AM / PM and change the hour.	
	if h_now > 12 : 
		h_now = h_now % 12
		if end_s == "AM" : end_s = "PM"
		elif end_s == "PM" : 
			end_s = "AM"
			day_incre += 1

	# if the hour is 12 then only change the AM / PM.
	elif h_now == 12:
		if end_s == "AM" : end_s = "PM"
		elif end_s == "PM" : 
			end_s = "AM"
			day_incre += 1
	
	# Check the day and (next day) or ({} days later).
	if(day_incre > 1):
		text_days = "({} days later)".format(day_incre)
	elif(day_incre == 1):
		text_days = "(next day)"

	# Set the day.
	if(day!=None):
		day = day.lower().capitalize()
		day_now = days.index(day)
		if(day_incre > 6):
			day_incre = day_incre % 7
		day_now = day_now + day_incre
		if(day_now > 6):
			day_now = day_now % 7
		day = days[day_now]

	# Set the hour if 0 become 12 since it was  AM and PM.
	if h_now == 0:
		h_now = 12

	# Set all int to str.
	h_now = str(h_now)
	m_now = str(m_now)

	# Check if minutes is 1 digit, set to 2 digit.
	if(len(m_now)==1):
		m_now = "0" + str(m_now)

	# Insert the output.
	newtime = "{}:{} {}".format(h_now, m_now, end_s)

	# Set the day if exists.
	if(day != None):
		newtime += ", " + day.capitalize()

	# Set the text if day changed.
	if(len(text_days)>1):
		newtime += " " + text_days

	return newtime



	print(newtime)


# 5:42 PM
# 3:07 PM
# 2:45 AM (next day)
# 12:05 PM
# 2:59 AM (next day)
# 12:04 AM (2 days later)
# 6:18 AM (20 days later)
# 5:01 AM
# 5:42 PM, Monday
# 2:59 AM, Sunday (next day)
# 12:04 AM, Friday (2 days later)
# 6:18 AM, Monday (20 days later)
add_time("3:30 PM", "2:12")
add_time("11:55 AM", "3:12")
add_time("9:15 PM", "5:30")
add_time("11:40 AM", "0:25")
add_time("2:59 AM", "24:00")
add_time("11:59 PM", "24:05")
add_time("8:16 PM", "466:02")
add_time("5:01 AM", "0:00")
add_time("3:30 PM", "2:12", "Monday")
add_time("2:59 AM", "24:00", "saturDay")
add_time("11:59 PM", "24:05", "Wednesday")
add_time("8:16 PM", "466:02", "tuesday")