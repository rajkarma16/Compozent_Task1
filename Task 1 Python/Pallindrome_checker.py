a = input("Enter a String to Check Pallindrome: ")

if (a.lower() == a.lower()[::-1]):
    print(f"String {a} is pallindrome")
else:
    print(f"String {a} is not a pallindrome")