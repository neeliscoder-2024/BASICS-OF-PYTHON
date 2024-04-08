# Removing duplicates character from the given string.
s=input("Enter the string:")
a=' '
for i in s:
	if i not in a:
		a+=i
print(a)

# Removing unique character from the given string.
def duplicates(s):
	element=0
	for char in s:
		element^=char
	return element
print(duplicates([1,2,1]))
