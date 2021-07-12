#reverseList - Write a function that reverses the values in the list (without creating a temporary array).
def reverseList(numbers):
    for i in range(int((len(numbers)-1)/2)):
        numbers[i],numbers[len(numbers)-1-i]=numbers[len(numbers)-1-i],numbers[i]
    print(numbers)

reverseList([5,3,1,4])

#isPalindrome - Write a function that checks whether the given word is a palindrome (a word that spells the same backward)
word = "Madam"

word_lower = word.lower().replace(" ", "")

if word_lower == word_lower[::-1]:
    print("It's a palindrome")
else:
    print("This is not a palindrome")

#coins - Write a function that determines how many quarters, dimes, nickels, and pennies to give to a customer for a change where you minimize the number of coins you give out.
def Coins(coin):
    change=[]
    change.append(coin//25)
    change.append((coin%25)//10)
    change.append(((coin%25)%10)//5)
    change.append(((coin%25)%10)%5)
    print(change)

Coins(102)



