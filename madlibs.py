def main():
	# write your code here

	time = input("Enter a Time:  ")
	items = input("Enter an Item:  ")
	name = input("Enter a Name:  ")
	scream = input("Enter any Sentence:  ")
	action = input("Enter an Action:  ")

	print("It was " + time + " o'clock when I heard a knock at the door.")
	print('I opened the door and there was a box of ' + items + ' with a note saying \"From Mr. ' + name.title() + '."')
	print('Just as I closed the door I heard a scream" ' + scream.upper()+ '."')
	print("I froze in place and all I could do was " + action + ".")


if __name__ == '__main__':
	main()
