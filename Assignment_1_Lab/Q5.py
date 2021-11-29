str = "abccdddefgggg"
i = 0
k = int(input("Enter a Positive Integer for repetitive Count:"))
while (k < 0):
    k = int(input("Please enter a Positive Integer for repetitive Count:"))
count = 1
flag = True
while i < len(str):
    if(i+1 < len(str)):
        if(str[i] == str[i+1]):
            count += 1
        else:
            count = 1
    if(count == k):
        flag = False
        break
    i += 1

if flag:
    print(f"Nothing found for the string {str}!")
else:
    print(f"The first substring of length {count} is {str[i]*k}!")
