# Function integerDecision 
#     INPUT PARAMETERS
#        number : an integer number which is the number to be tested 
#     returns None
def integerDecision(number): # DO NOT MODIFY THIS STATEMENT!!!
    if number < 0:
        print("Input number is not positive.")  
    elif number < 50:
        print("Input number is less than 50")
    elif (number >= 50) and (number <= 100):
        if not(number == 60):
            print("Input number " + str(number) + " is >= 50 and <=100")
        else:
            print("I FOUND 60.")
    elif (number > 100):
        print("Input number is greater than 100")

# Function multipleThree 
#     INPUT PARAMETERS
#        range1 : an integer number
#     returns number of multiples between 1 and range1
def multipleThree(range1): # DO NOT MODIFY THIS STATEMENT!
    x = 1
    count = 0
    if range1 <= 0:
        print("Input number is not positive.")  
    elif range1 > 0:
        while x <= range1:
            if x % 3 == 0:
                count = count + 1
                print("The number " + str(x) + " is a multiple of 3!")
            x = x + 1
    #print(str(count))
    return count

# function multipleThreeFive
#     INPUT PARAMETERS
#        range2 : an integer number 
#     returns None 
def multipleThreeFive(range2): # DO NOT MODIFY THIS STATEMENT!
    if range2 <= 0:
        print("Input number is not positive.")  
    elif range2 > 0:
        for i in range(1,range2 + 1):
            if (i % 3 == 0 or i % 5 == 0) and not (i % 3 == 0 and i % 5 == 0):
                print(str(i))
            i = i + 1

def main(): # DO NOT MODIFY THIS STATEMENT!
   text1 = input("integerDecision: ")
   text2 = input("multiple3: ")
   text3 = input("multiple35: ")
   integerDecision(int(text1))
   count = multipleThree(int(text2))
   print("The count of multiples of 3 is: " + str(count))
   multipleThreeFive(int(text3))
main()
