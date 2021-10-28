def cut_cake(parts):
	try:
		return 1 / int(parts)
	except(ZeroDivisionError, TypeError, ValueError):
		return "What it this?!"


cake = cut_cake([1, 2, 5])


def do_somthing(x):
	try:
		print(x)
	except:
		print('Bye!')

x = 0
while x < 10:
	do_somthing(x)
x += 1