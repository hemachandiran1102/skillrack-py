#-----------------------------------------------------------------------------------------------p1----------------------------------------------------------------------
#Check leap year A year Y will be passed as input.
# The program must find if the given year is a leap year or not. - If it is leap year, 
#the program must print yes else it should print no Note: A year is a leap year if it is divisible by 4. 
#If it is a century then it should be divisible by 400. 
#The pseudocode is as given below. 
#if year is divisible by 400 then is_leap_year 
#else if year is divisible by 100 then not_leap_year
# else if year is divisible by 4 then is_leap_year 
#else not_leap_year 

#Example Input/Output:
# If 2000 is the input,
# the program must print yes
# If 2100 is the input, 
#the program must print no 
#If 2013 is the input, 
#the program must print no 
#Input Format: A year as a number is passed to the standard input. Output Format: The string value as per the conditions above printed to the standard output. 
#Boundary Conditions: 0 < Y <= 8000

def leapyear():
    Y= int(input())
    if Y%400==0 :
        print("yes")
    elif Y%100==0:
        print("no")
    elif Y%4==0:
        print("yes")
    else:
        print('no')
#leapyear()


#------------------------------------------------------------------------------------------p2-------------------------------------------------------------------------------------------------
# In a betting game involving the roll of a dice, 
# Sandeep gains Rs.X if an odd number turns up
#  and he loses Rs.Y is an even number turns up.
#  The numbers shown on the face of the dice in a certain number of games is passed as input. 
# The values of X and Y are also passed as input.
#  The program must print the net gain or loss as the output. 
# Input Format: First line will contain the numbers shown on the face of the dice separated by one or more spaces.
#  Second line will contain the value of X Third line will contain the value of Y 
# Output Format: The net gain or loss (loss will be a negative value) 
# Sample Input/Output: 
# Example 1: 
# Input: 1 4 3 
# 10 
# 30 
# 
# Output: -10 
# Explanation: He gains 20 rupees for 1 and 3 and loses 30 rupees for 4. Hence there is a net loss of 20-30 = -10 
# 
# Example 2: 
# Input: 
# 4 6 1 2 1
# 50 25 
# Output: 
# 25 
# He gains 100 rupees for 1,1 and loses 75 rupees for 4,6,2. Hence there is a net gain of 100-75 = 25


def rod():
    D=list(map(int,input().split(" ")))
    X=int(input())
    Y=int(input())
    p=0
    l=0
    for i in D:
        if i%2==0:
            l+=Y
        else:
            p+=X
    print(p-l)
#rod()

#---------------------------------------------------------------------------------p3-------------------------------------------------------------------------------------
#Count of common characters in two strings Two string values S1 and S2 are passed as input. 
# The program must print the count of common characters in the strings S1 and S2.
#  Assume the alphabets in S1 and S2 will be in lower case. 
# Input Format: First line will contain the value of string S1 Second line will contain the value of string S2 
# Output Format: First line will contain the count of common alphabets. 
# Boundary Conditions: Length of S1 and S2 will be from 3 to 100. 
# Sample Input/Output: 
# Example 1: 
# Input: 
#       china
#       india 
# Output: 3 
# Explanation: The common characters are i,n,a 
# Example 2: 
# Input: 
#           energy 
#           every 
#   Output: 3 
# Explanation: The common characters are e,r,y

def commonlet():
    S1=str(input())
    S2=str(input())
    letters=[]
    count=0
    for i in S1:
        for j in S2:
            if i == j and i not in letters:
                letters.append(i)
                count+=1
                break
    print(count)
#commonlet()


#---------------------------------------------------------------------------------------P4--------------------------------------------------------------------------------
#Reverse String Till Underscore String S is passed as the input to the program. 
# S may or may not have a single underscore embedded in it. 
# The program must reverse the String S till the first underscore and print it as the output. 
# Input Format: The first line contains S. 
# Output Format: The first line contains the string S modified based on the given conditions. 
# Boundary Conditions: Length of S is from 3 to 100. 
# Example Input/Output 1: 
# Input: abcd_pqrs 
# Output: dcba_pqrs 
# 
# Example 
# Input/Output 2: 
# Input: _kilo 
# Output: _kilo 
# 
# Example 
# Input/Output 3: 
# Input: nounderscore 
# Output: erocsrednuon
def untilunderscore():
    S=str(input())
    count=0
    for i in S:
        if i == "_":
            break
        else:
            count+=1
    print(S[0:count][::-1]+S[count:])

#untilunderscore()

#------------------------------------------------------------------------------------P5----------------------------------------------------------------------------------------------
# A string S is passed as input. 
# S will contain multiple integer values with each integer value followed by an alphabet. 
# The program must expand the alphabets based on the related integer value. 
# Input Format: The first line contains S. 
# Output Format: The first line contains the expanded string value. 
# Boundary Conditions: Length of S is from 2 to 100. 
# Example Input/Output 1: 
# Input: 4a5h 
# Output: aaaahhhhh 
# 
# Explanation: As it is 4a and 5h, four a's are printed followed by 5 h's 
# Example Input/Output 2: 
# Input: 1k2b4k 
# Output: kbbkkkk 
# Max Execution Time Limit: 5000 millisecs
#print(ord("9"))
def expandalphabets():
    S=input()
    
    for i in range(len(S)):
        nstr=""
        count=1
        if ord(S[i])>=48 and ord(S[i])<57:
            nstr+=S[i]
            if ord(S[i+count])>=48 and ord(S[i+count])<57:
                nstr+=S[i+count]
                
        print(nstr)
expandalphabets()