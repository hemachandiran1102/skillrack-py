#----------------------------------------------------------------P1-----------------------------------------------------------------------------------
#The runs scored by N batsmen of a cricket team is passed as the input to the program.
# The program must print the name of the batsman who scored the highest runs. (You can assume that no two batsmen will be the top scorers). 
#Input Format: The first line denotes the value of N. Next N lines will contain the name of the batsman and the runs score (both separated by a comma)
#Example Input/Output 1: Input: 
#5 BatsmanA,45 BatsmanB,52 
#  BatsmanD,9 BatsmanE,78 
#Output: BatsmanE

#N = int(input())
def maxruns(N):
    name=[]
    scorecard=[]
    for i in range(N):
        n,score=input().split(",")
        name.append(n)
        scorecard.append(int(score))
    for I in range(N):
        for j in range(N):
            if scorecard[I] < scorecard[j]:
                scorecard[I],scorecard[j] = scorecard[j],scorecard[I]
                name[I],name[j] = name[j],name[I] 
    print(name[N-1],scorecard[N-1])
#maxruns(N)


#--------------------------------------------------------------------P2-------------------------------------------------------------------------------------
#Names of N students and the marks scored by them in Maths, Physics and Chemistry are passed as the input. 
# The program must print the name of the student who has scored the maximum marks in these three subjects. (Assume only one student will be the top scorer). 
# Input Format: The first line denotes the value of N. 
# Next N lines will contain the name of the student and the marks in three subjects separated by colon. 
# Output Format: The first line contains the name of the students with the highest marks. 
# Boundary Conditions: 2 <= N <= 50 The length of the names will be from 3 to 100. 
# The value of the marks will be from 0 to 100.
#  Example Input/Output 1: 
# Input: 
# 4 
# Sasikumar:50:60:70 
# Arun:60:40:90 
# Manoj:50:50:60 
# Rekha:60:35:45 
# Output: Arun


#N=int(input())
def highestmarks(N):
    arr=[]
    names=[]
    for i in range (N) :   
        name,p,q,r=input().split(":")
        total=int(p)+int(q)+int(r)
        arr.append(total)
        names.append(name) 
    for I in range(N):
        for J in range(N):
            if arr[I] > arr[J]:
                arr[I] , arr[J] = arr[J] , arr[I]
                names[I] , names[J] = names[J] , names[I]
    print(names[0])

#highestmarks(N)

#------------------------------------------------------------------------------P3-------------------------------------------------------------------------------

#The runs scored by a cricket team in the first and second innings of N test cricket matches are passed as input. 
# The program must print the average of first and second innings (with precision upto two decimal places). 
# Input Format: The first line denotes the value of N. 
# Next N lines will contain the first and second innings score separated by a space. 
# Output Format: The first line contains the average of first innings score. 
# The second line contains the average of second innings score. 
# Boundary Conditions: 2 <= N <= 20 
# The value of the runs will be from 0 to 1000. 
# 
# Example Input/Output 1: 
# Input: 
# 3 
# 250 200 
# 450 300 
# 200 250 
# 
# Output:
# 
#  300.00 250.00

#N = int(input())
def averageinn(N):
    firstinn=0
    secondinn=0
    for i in range(N):
        first,second= input().split(" ")
        firstinn+=int(first)
        secondinn+=int(second)
    average1=(firstinn/N)
    average2=(secondinn/N)
    print("%.2f" %average1,"%.2f" %average2)

#averageinn(N)

#--------------------------------------------------------------------P4----------------------------------------------------------------
#Space Separated Integers Sum A single line consisting of a set of integers, each separated by space is passed as input to the program. 
# The program must print the sum of all the integers present. 
# Input Format: The first line contains the integer values (Each separated by a space) 
# Output Format: The first line contains the sum of all the integers. 
# Boundary Conditions: The length of the input string is between 3 to 10000 The value of the integer values will be from -99999 to 99999 
# 
# Example Input/Output 1: 
# Input: 100 -99 98 5 
# Output: 104 
# 
# Example Input/Output 2: 
# Input: 100 200 -300 500 -450 -50 
# Output: 0

#N=list(map(int,input().split(" ")))
def sumofall(N):
    n=0
    for I in N:
        n+=I
    print(n)
#sumofall(N)
#------------------------------------------------------------------------------------P5--------------------------------------------------------------------
#A certain number of people attended a meeting which was to begin at 10:00 am on a given day.
#  The arrival time in HH:MM format of those who attended the meeting is passed as the input in a single line, with each arrival time by a space. 
# The program must print the count of people who came late (after 10:00 am) to the meeting. 
# Input Format: The first line contains the arrival time separated by a space.
#  Output Format: The first line contains the count of late comers. 
# Boundary Conditions: The length of the input string is between 4 to 10000. 
# The time HH:MM will be in 24 hour format (HH is hours and MM is minutes).
#  Example Input/Output 1:
#  Input: 10:00 9:55 10:02 9:45 11:00 
# Output: 2 
# Explanation: The 2 people were those who came at 10:02 and 11:00
#A=list(map(str,input().split(" ")))
def meetinglatecomers(A):
    arr=[]
    count=0
    for I in range(len(A)):
        x,y=A[I].split(":")
        h,m=int(x),int(y)
        if ((h>=10) and m>0) or h>10:
            count +=1  

    print(count)

#meetinglatecomers(A)

#A string S is passed as the input. S can contain alphabets, numbers and special characters. 
# The program must print only the alphabets in S. 
# Input Format: The first line contains S.
# Output Format: The first line contains only the alphabets in S. 
# Boundary Conditions: The length of the input string is between 1 to 1000. 
# 
# Example Input/Output 1: 
# Input: abcd_5ef8!xyz 
# Output: abcdefxyz 
# 
# Example Input/Output 2: 
# Input: 1239_-87 
# Output: 
# Explanation: As there are no alphabets in the input value nothing is printed as output.

def findalpha():
    S="Abcd_5ef8!xyZ"
    for i in S:
        if ((ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 65 and ord(i) <= 90)):
            print(i,end="") 
#findalpha()

#---------------------------------------------P6----------------------------------------------------------------------------------
#The number of rows N is passed as the input. 
# The program must print the half pyramid using asterisk *. 
# Input Format: The first line contains N. 
# Output Format: N lines representing the half pyramid pattern using * (A single space is used to separate the *) 
# Boundary Conditions: 2 <= N <= 100 Example Input/Output 1:
#  Input: 5
#  Output:
# * 
# * *
# * * * 
# * * * * 
# * * * * * 
# 
# Example 
# 
# Input/Output 2:
# Input: 3 
# Output: 
# * 
# * * 
# * * *

def halfprymid():
    a=int(input())
    for i in range(a):
        for j in range(i+1):
            print("*",end="")
        print()
#halfprymid()

#----------------------------------------------------P7----------------------------------------------------------------------------------
#Lowest Mileage Car The name and mileage of certain cars is passed as the input. 
#The format is CARNAME@MILEAGE and the input is as a single line, with each car information separated by a space. 
# The program must print the car with the lowest mileage. (Assume no two cars will have the lowest mileage) 
# Input Format: The first line contains the 
# CARNAME@MILEAGE separated by a space. 
# Output Format: 
# The first line contains the name of the car with the lowest mileage. 
# Boundary Conditions: The length of the input string is between 4 to 10000. 
# The length of the car name is from 1 to 50.
# Example Input/Output 1: 
# Input: Zantro@16.15 Zity@12.5 Gamry@9.8 
# Output: Gamry
def lcm():
    A=list(map(str,input().split(" ")))
    C=[]
    M=[]
    for I in A :
        car,milage=I.split("@")
        C.append(car)
        M.append(float(milage))
    for J in range(len(M)):
        for j in range(len(M)):
            if M[J] > M[j] :
                M[J],M[j] = M[j],M[J]
                C[J],C[j] = C[j],M[J]     
    print(C,M)   
    print(C[len(A)-1])
#lcm()

#------------------------------------------------------------------------------------------P8----------------------------------------------------------
#Palindrome Missing Alphabet String S which is a palindrome is passed as the input.
#But just one alphabet A is missing in S. 
#The program must print the missing alphabet A.
# Note: The FIRST alphabet of S will always be present. 
# Input Format: The first line contains S.
#Output Format: The first line contains the missing alphabet A. 
#Boundary Conditions: The length of the input string S is between 3 to 100.
#The FIRST alphabet of S will always be present.
#Example Input/Output 1: 
# Input: malayaam 
# Output l
# Example Input/Output 2:
# Input: abcddcb 
# Output: a
def MissingPal():
    s=input()
    n=len(s)
    for i in range(n):
        if s.count(s[i])&1==1:
            if n&1==0 and i!=n//2 or n&1==1:
                print(s[i])
                break


    

#MissingPal()
###########--------------------------------------------------------------------P10-----------------------------------------------------------------------------------
#Pattern Printing - Half Pyramid Numbers The number of rows N is passed as the input.
#  The program must print the half pyramid using the numbers from 1 to N. 
# Input Format: The first line contains N. 
# Output Format: N lines representing the half pyramid pattern using the numbers from 1 to N. (A single space is used to separate the numbers) 
# Boundary Conditions: 2 <= N <= 100 
# Example Input/Output 1:
# Input: 5 
# Output:
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 
# 
# Example 
# Input/Output 2:
#  Input: 3 
# Output:
# 1 
# 1 2 
# 1 2 3

def numpattern():
    N =int(input())
    for i in range(N):
        for j in range(0,i+1):
            print(j+1,end=" ")
        print()
numpattern()