# this is age-checker project using python
import time


if __name__ == '__main__':

	useryear = int(input("Enter your birth year: "))
	year = time.strftime("%Y")
	currentyear = int(year)

	if  useryear > currentyear:
		print(f"sorry {useryear} this year not come yet")

	elif useryear == currentyear:
		print("you are a new born baby")
	
	else:
		for i in range(currentyear,currentyear+100):
			print(f"your age in {i} is {i-useryear}")



