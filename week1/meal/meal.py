def main():
	time = input("What time is it? ");

	# call the convert function
	whatTime(convert(time));


def convert(time):
	# get hours and minutes
	hours, minutes = time.split(":");

	# get the total hour in float (7:30 == 7.5)
	totalTime = ((float(hours) * 60) + float(minutes)) / 60;
	return(totalTime);


def whatTime(time):
	# conditionals to validate the time of meals
	if time >= 7.0 and time <= 8.0:
		print("breakfast time");
	elif time >= 12.0 and time <= 13.0:
		print("lunch time");
	elif time >= 18.0 and time <= 19.0:
		print("dinner time");


# If you are failing the checks but are sure your program
# behaves correctly, make sure that you haven’t removed the
# line from the code structure you were given. That allows
# check50 to test your convert function separately. You’ll
# learn more about this in later weeks.
if __name__ == "__main__":
	main()


# def main():
#     # Get time from user
#     answer = input("What time is it? ")

#     time = convert(answer)

#     if time >= 7 and time <= 8:
#         print("breakfast time")
#     elif time >= 12 and time <= 13:
#         print("lunch time")
#     elif time >= 18 and time <= 19:
#         print("dinner time")

# def convert(time):
#     hours, minutes = time.split(":")

#     # convert time into a float number
#     new_minute = float(minutes) / 60
#     # return the result to main function
#     return float(hours) + new_minute
