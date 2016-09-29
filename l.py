def clear_bit():
	a=int(input("Enter the number \t"))
	n=int(input("\nwhich bit to clear\t"))
	m=~(1<<n)&a
	print("New number is %d"%m)
clear_bit()


