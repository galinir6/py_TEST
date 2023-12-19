
# sums all digits of the number(num)
def sumofdigits(num):
        num_string = str(num)
        sum=0
        for x in num_string:
         sum +=int(x)
        return sum
    

# checks if a number(num) is a palindrome
def ispal(num):
#    turn number to a string
     num_string = str(num)
# check if number = number in reverse
     return num_string == num_string[::-1]
# return true/false
   
   
   