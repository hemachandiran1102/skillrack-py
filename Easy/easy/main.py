import sys
#--------------------------------------------------------------------------SET-01-EASY-challenges---------------------------------------------------------------------------------
#--------P1--------------------
def primenumber(N=7):
    if N>=2 and N<= 9999999:
        for i in range(2,N):
            if N%i==0:
                print("NO")
                break   
            else:
                print("Yes")
                break
#primenumber(11)

#USING RECURSSION
sys.setrecursionlimit(1000000)
def rec_primenumber(N=7,i=2):
    if N==i:
        print("prime")
    elif N%2==0:
        print("Not prime")
    else:
        return rec_primenumber(N,i+1)
#rec_primenumber(189210)

#--------P2-----------------------
#Fibbonaci sequence
def Fibbonacci_seq(N=10):
    n1=0
    n2=1
    for i in range(0,N):
        print(n1)
        n=n1+n2
        n1=n2
        n2=n
#Fibbonacci_seq(10)
def Fibbonacci_rec(N=10):
    if N==0 or N==1:
        return N
    else:
        print(N)
        return (Fibbonacci_rec(N-1)+Fibbonacci_rec(N-2))
#Fibbonacci_rec(10)
#---------------------------------------p3-----------------------
#Second Largest Value among N integers
#N=5
#A=N
def secondlargest(A):
    n = [121,3134,543,535,5454]
    #for i in range(A):
       # print(i)
        #N=int(input())
        #n.append(N)
    #print(n)
    for I in range(len(n)):
        for J in range(I+1,len(n)):
            if n[J] > n[I]:
                n[I],n[J] = n[J],n[I]
                
    print(n[1])

        

#secondlargest(A)

#-------------------------------------------p4------------------------------
#remove first and last character
def rmfirstlast():
    S="tinku"
    print(S[1:-1])
#rmfirstlast()
#------------------------------------p5-------------------------------------------
#The program must accept two numbers X and Y and then print their HCF/GCD.
#Input Format: The first line denotes the value of X. The second line denotes the value of Y. 
# Output Format: The first line contains the HCF of X and Y. 
# Boundary Conditions: 1 <= X <= 999999 1 <= Y <= 999999 
# Example Input/Output 1: 
# Input: 30 40 
# Output: 10 
# Example Input/Output 2: 
# Input: 15 10 
# Output: 5

def HCF():
    inputNumber_1 = 30
    # input number 2
    inputNumber_2 = 40
    # checking whether the first number is greater than
    # the second one
    if inputNumber_1 > inputNumber_2:
    # assigning the second number as a smaller number
        small_num = inputNumber_2
    else:
    # else assigning the first number as a smaller number
        small_num = inputNumber_1
    # traversing from 1 to the small number range
    for i in range(1, small_num+1):
    # checking whether both the first and second numbers divide exactly by index (i)
        if((inputNumber_1 % i == 0) and (inputNumber_2 % i == 0)):
        # assigning the index(i) value as HCF if the condition is true
            resultHcf = i
    # printing the HCF of input number 1 & input number 2
    print("The H.C.F of", inputNumber_1, "and", inputNumber_2, "=", resultHcf)

#----------------------------------------------------------------------------------P6-------------------------------------------------------
#String Reverse
#The program must accept a string value S and print the reverse of S. 
# Input Format: The first line denotes the value of S. 
# Output Format: The first line contains reversed value of S. 
# Boundary Conditions: Length of string S is from 2 to 100. 
# Example 
# Input/Output 1: 
# Input: abcde 
# Output: edcba 
# 
# Example
#  Input/Output 2: 
# Input: look 
# Output: kool

def string_reverse():
    S=str(input())
    print(S[::-1])
# string_reverse()

#--------------------------------------------------------------------------------------------------P7-------------------------------------------------------------------------
# The program must accept a number N and print the sum of tenth and unit digits. 
# Input Format: The first line denotes the value of N. 
# Output Format: The first line contains the sum of tenth and unit digits. 
# Boundary Conditions: 10 <= N <= 9999999 Example Input/Output 1: 
# Input: 231 
# Output: 4 
# Example Input/Output 2: 
# Input: 100 
# Output: 0 
# Example
# Input/Output 3: 
# Input: 192 
# Output: 11

def sot():
    N=int(input())
    u=N%10
    t=(N/10)%10
    print (round(u+t))
sot()