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


from ast import Num


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
#print(ord("0"))

def exalpha():
    S= "1vedha2giri4dhara5hema"
    num=""
    name=""    
    for i in S:
        if ord(i) <=57 and ord (i) >= 48:
            num+=i
            name+=" "
        else:
            num+=" "
            name+=i    
    listnum=num.split(" ")
    listname=name.split(" ")
    count=0
    count1=0
    for j in range(len(listnum)):
        if listnum[j-count] != "":            
            continue
        else:
            listnum.pop(j-count)
            count+=1
    for J in range(len(listname)):
        if listname[J-count1] != "":
            continue
        else:
            listname.pop(J-count1)
            count1+=1

    for no1 in range(len(listnum)):
        for numpat in range(int(listnum[no1])):
            print(listname[no1],end="")  
    
#exalpha()


#------------------------------------------------------P6-----------------------------------------
#A string S is passed as input. 
# S will contain two integer values separated by one of these alphabets - A, S, M, D 
# where - A or a is for addition  
# - S or s is for subtraction  
# - M or m is for multiplication 
# - D or d is for division 
# The program must perform the necessary operation and print the result
# (Ignore any floating point values just print the integer result.)
# Input Format: The first line contains S. 
# Output Format: The first line contains the resulting integer value. 
# Boundary Conditions: Length of S is from 3 to 100
# Example Input/Output 1: 
# Input: 5A11 
# Output: 16 
# Explanation: As the alphabet is A, 5 and 11 are added giving 16.

#print(ord("-"),ord("a"),ord("S"),ord("s"),ord("M"),ord("m"),ord("D"),ord("d"))
def calc():
    S="-90s-109"
    num=""
    
    for I in range(len(S)):
        if ord(S[I])>=48 and ord(S[I])<=57 :
            num+=S[I]
        elif ord(S[I])==45:
            num+=S[I]    
        else:
            num+=" "
            num+=S[I]
            num+=" "
            
    NUM=num.split(' ')
    print(NUM)
    for J in range(len(NUM)):
        print(NUM[J])
        if NUM[J] == "A" or NUM[J] == "a":
                output=int(NUM[J-1])+int(NUM[J+1])
        elif NUM[J] == "S" or NUM[J] == "s":
                output=int(NUM[J-1])-int(NUM[J+1])
        elif NUM[J] == "M" or NUM[J] == "m":
                output=int(NUM[J-1])*int(NUM[J+1])
        elif NUM[J] == "D" or NUM[J] == "d":
                output=int(NUM[J-1])/int(NUM[J+1])            

    print(output)
#calc()

#-----------------------------------------------------------------------------------------------------P7-----------------------------------------------------------------------------
#A floating point value F indicating the amount in rupees is passed as input.
# The program must print the corresponding value in paise. 
# Note: 1 rupee = 100 paise. 
# Input Format: The first line contains F. 
# Output Format: The first line contains the integer value denoting the paise. 
# Boundary Conditions: 0.00 <= F <= 999999.99 Example 
# Input/Output 1: Input: 11.30 
# Output: 1130 
# Example Input/Output 2: 
# Input: 0.80 
# Output: 80 
# Example Input/Output 3:
# Input: 0.0 
# Output: 0

def paisacal():
    F="0.30"
    valstr=""
    val=[]
    for i in range(len(F)):
        if F[i] == ".":
            
            val.append(valstr)
            valstr=""
        elif i == len(F)-1:
            valstr+=F[i]
            val.append(valstr)
        else:
            valstr+=F[i]
    output=0
    for j in range(len(val)):
        if j == 0:
            output+=int(val[j])*100
            
        else:
            output+=int(val[j])
    print(output)
#paisacal()
#-------------------------------------------------------------------------------------------P8-------------------------------------------------------------------------------
#In a zoo there are some birds and animals.
#  All birds have two legs and all animals have four legs. 
# GIven the head count and leg count of both birds and animals taken together, 
# the program must print the head count of birds and animals separated by a space as output. 
# Input Format:
# First line will contain the integer value H representing the head count of both birds and animals taken together. 
# Second line will contain the integer value L representing the leg count of both birds and animals taken together. 
# Output Format: First line will contain the integer values of the head count of birds and animals separated by a space. 
# Constraints: 0 < H < 1000 1 < L < 2000 
# Sample Input/Output: Example 1: 
# Input: 27 84 
# Output: 12 15 
# Explanation: There are 12 birds and 15 animals. 
# Example 2: Input: 114 256 
# Output: 100 14 
# Explanation: There are 100 birds and 14 animals.
def anbirdcount():
    head=int(input())
    legs=int(input())
    animals=int(legs/2)-head
    birds=head-animals
    print(birds,animals)
#anbirdcount()

#--------------------------------------------------------------------------------------P9--------------------------------------------------------------------------------------
#Count of common factors Given a set of numbers where all other numbers are multiple of the smallest number,
#  the program must find the count of the common factors C excluding 1. 
# Input Format: First line will contain the integer value N representing how many numbers are passed as input. 
# Next N lines will have the numbers. 
# Output Format: First line will contain the count of common factors C. 
# Constraints: N will be from 2 to 20. 
# Sample Input/Output: 
# Example 1: 
# Input: 
# 2 
# 100 
# 75 
# Output: 2 
# Explanation: The common factors excluding 1 are 5,25. Hence output is 2 
# 
# Example 2: 
# Input: 
# 3 
# 10 
# 20 
# 30 
# Output: 3 
# Explanation: 
# The common factors excluding 1 are 2,5,10. Hence output is 3.


def countcommonfactor():
    #N = int(input())
    no=[10,20,30]
    #for num in range(N):
       # no.append(int(input()))
    
    for i in range(len(no)):
        for j in range(len(no)):
            if no[i] > no[j]:
                no[i] , no[j] = no[j] , no [i]
    count=0
    for I in range(2,no[0]):
        c=0
        for J in no:
            
            if J%I==0:
                c+=1
                print(J,c)
        if(c==len(no)):
            count+=1
    print(count)
#countcommonfactor()

#---------------------------------------------------------------------------------------------------P10----------------------------------------------------------------------------
#Reverse Number Sign An integer value N is passed as the input. 
# The program must reverse the sign of N and print -N as the output. 
# Input Format: The first line contains N. 
# Output Format: The first line contains -N. 
# Boundary Conditions: -999999 <= N <= 999999 
# Example Input/Output 1: 
# Input: 125 
# Output: -125 
# Example Input/Output 2: 
# Input: -346 
# Output: 346 
# Example Input/Output 3: 
# Input: 0 
# Output: 0

def ReverseNumberSign():
    N="345"
    if N[0] == "-":
        print(N[1:])
    elif N=="0":
        print(N)
    elif N[0] != "-" or N[0]=="+":
        print("-"+N)
ReverseNumberSign()