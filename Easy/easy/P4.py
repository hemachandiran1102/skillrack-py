#----------------------------------------------------P1--------------------------------------

""" A single line L with a set of space separated values indicating distance travelled and time taken is passed as the input. The program must calculate the average speed S (with precision upto 2 decimal places) and print S as the output.
Note: The distance and time taken will follow the format DISTANCE@TIMETAKEN. DISTANCE will be in kilometers and TIMETAKEN will be in hours.
Input Format:
The first line contains L.
Output Format:
The first line contains the average speed S.
Boundary Conditions:
Length of L will be from 3 to 100.
Example Input/Output 1:
Input:
60@2 120@3
Output:
36.00 kmph
Explanation:
Total distance = 60+120 = 180 km.
Total time taken = 2+3 = 5 hours.
Hence average speed = 180/5 = 36.00 kmph """









from calendar import month


def avgspeed():
    L="60@2 120@3"
    list=["60@2",'120@3']
    totald=0
    timet=0
    
    for I in list:
        totaldistance,timetaken=I.split("@")
        totald+=int(totaldistance)
        timet+=int(timetaken)
    print(totald//timet)

#avgspeed()
#-------------------------------------------------P2-------------------------------------------------- 
"""
INPUT:
abcdefgxyzlmnoopqi
5
OUTPUT:
ezo
"""

def chx():

    string="abcdexyzwqpoolj"
    
    x=5
    for i in range(1,len(string)):
        if (i+1)%x==0:
            print(string[i],end="")
#chx()

#------------------------------------------------P3------------------------------------------

"""First Repeating Character A string S is passed as the input. 
S has at least one repeating character. The program must print the first repeating character"""

"""Example Input/Output 1: 
Input: abcdexyzbwqpoolj 
Output: b"""

def reptchar():
    A="abcdexyzbwqpoolj"
    b=''
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if A[i] == A[j]:
                b+=A[j]
                break
    print(b[0])
        
#reptchar()

""" A string S is passed as the input. S has at least one repeating character. 
The program must print the first repeating character C from the last. 

Example Input/Output 1: 
Input: abcdexyzbwqpoolj 
Output: p"""

def reversereptchar():
    #A="abcdexyzbwqpooplj"
    A="mnadsh2327 237$$!#"
    B=A[::-1]
    b=''
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if B[i] == B[j]:
                b+=B[j]
                break
    
    print(b[0])
#reversereptchar()

#-----------------------------------------------------P4--------------------------------------------
"""Common part in string values 
Two string values S1 and S2 are passed as input. 
The last portion of S1 will be the first portion of S2. 
The program must print this common part in S1 and S2.
Input: 

mayday 
daybreak 

Output: 

day

"""
def matchstring():
    #S1="Georgeflee"
    #S2="fleeceblanket"
    #S1="mayday"
    #S2="daybreak"
    S1="redfish"
    S2="fishtank"
    #S1="aaaamm"
    #S2="aaamm"
    #A=min(len(S1),len(S2))
    #B=max(len(S1),len(S2))
    string1=""
    string2=""
    for i in range(len(S1)):        
        for j in range(i,len(S1)):
            string1+=S1[j]            
        string1+=" "        
    for I in reversed(range(0,(len(S2)+1))):
        for J in range(I):
            string2+=S2[J]
        string2+=" "
    A=string1.split()
    B=string2.split()
    print(A,B)
    for I1 in range(len(A)):
        for I2 in range(len(B)):
            if A[I1]==B[I2]:
                print(B[I2])
     
#matchstring()

###-----------------------------------------------------------------------P5---------------------------------------------------------------------------
"""Odd Length String - Middle Three Letters An odd length string S is passed as the input. 
 The middle three letters of S must be printed as the output. 
 
 Input Format: First line will contain the string value S 
 Output Format: First line will contain the middle three letters of S. 
 
 Boundary Conditions: Length of S is from 5 to 100 
 
 Example Input/Output 1: 
 Input: 
        level 
Output: 
        eve 
        
Example Input/Output 2: 

Input: manager 

Output: nag

"""
def oddlenofS():
    S="manager"
    print(S[(len(S)//2)-1:2+(len(S)//2)])
#oddlenofS()

##-----------------------------------------------------------------------P6---------------------------------------------------------------------

"""String Word Count The program must accept a string S and print the count of words in S. 

Boundary Condition(s): 1 <= Length of S <= 1000 

Input Format: The first line contains S. 

Output Format: The first line contains the integer value representing the word count. 

Example Input/Output 1: 

Input: I like tea 

Output: 3 

Example Input/Output 2: 

Input: I like coffee very much 

Output: 5

"""
def StringWrdCount():
    S=input().split(" ")
    print(len(S))


#--------------------------------------------------------------------P7----------------------------------------------------------------------------
"""First Letter In Word - Uppercase A string value S is passed as the input. 
The program must print the first letter of each word in S in upper case. 
Input Format: First line will contain the string value S 
Output Format: First line will contain the string value with the first letter of each word in S in upper case. 
Boundary Conditions: Length of S is from 5 to 500 
Example Input/Output 1: 
Input: She is happy. 
Output: She Is Happy. 
Example Input/Output 2: 
Input: joIN tHE ParTY 
Output: JoIN THE ParTY"""
#print(ord("A"),ord("Z"))
def FirstLetterInWord():
    S=['she', 'is', '', '', '', '', '', '', '', '', '', '', '', 'happy.']
    print(S)

    for I in S:
        if len(I)==0:
            print(" ",end="")
        
        elif ord(I[0])>=97 and ord(I[0])<=122:
            
            print(chr(ord(I[0])-32),end="")
            print(I[1:],end=" ")
        else:
            print(I,end=" ")
        
           
#FirstLetterInWord()


#-----------------------------------------------------------P9----------------------------------------------
"""Alen and Tim both own a tennis grass court and they decide to mow the lawn in and around the court
 which will cost them Rs.5 per square feet. 
 Given the amount they spent to mow the lawn and the width of the court, 
 find the difference between the length of the courts. 
 
 Input Format: First line will contain the amount spent (in Rs) by Alen and Tim separated by space. 
 Second line will contain the width (in feet) of the courts of Alen and Tim separated by space. 
 
 Output Format: The value (in feet) which is the difference between the length of the courts 
 rounded off upto two decimal points.
 
 Input Format: First line will contain the amount spent (in Rs) by Alen and Tim separated by space. 
 Second line will contain the width (in feet) of the courts of Alen and Tim separated by space. 
 Output Format: The value (in feet) which is the difference between the length of the courts 
 rounded off upto two decimal points. 
 
 Example Input/Output 1: 
 Input: 
    100000 80000 
    100 80 
Output: 
    0.00 
    
Explanation: 
    Area of Alen's court = 100000/5 = 20000 sq.ft. 
    Length = 20000/100 = 200 
    Hence the difference = 200-200 = 0 
    Area of Tim's court = 80000/5 = 16000 sq.ft. 
    Length = 16000/80 = 200 
    which when rounded off to decimal places is 0.00 
    
Example 
Input/Output 2: 
Input: 
    17500 40000 
    50 80 
Length = 8000/80 = 100 
    
Output: 
    30.00
Explanation: 
Area of Alen's court = 17500/5 = 3500 sq.ft. 
Length = 3500/50 = 70 
Area of Tim's court = 40000/5 = 8000 sq.ft. 
Hence the difference = 100-70 = 30.00            
 """

def DiffBetLengthRectangles():
    A=["17500","40000"]

    B=["50","80"]
    diff=[]
    for I in range(len(A)):
        diff.append((int(A[I])/5)/int(B[I]))
    sorted(diff)    
    if diff[1]>diff[0]:
        print("%.2f" %(diff[1]-diff[0]))
    else:
        print("%.2f" %( diff[0]-diff[1]))
#DiffBetLengthRectangles()   

#--------------------------------------P10------------------------------------------------

"""A date in DD-MM-YYYY format is passed as the input. 
The program must print the calendar month. 01 - January, 02 - February and so on till 12 - December. 
Input Format: First line will contain the date in DD-MM-YYYY format. 
Output Format: The string value denoting the month. 
Example Input/Output 1: Input: 23-12-2016 Output: December"""

def date_month():
    #A=input().split("-")
    A=["30","12","1998"]
    months=["January","February","March","April","May","June","July","August","September","October","November","December"]
    for I in range(0,len(months)):
        print(months[I],I+1,A[1])
        #if int(A[1])==I+1:
            #print(months[I])
date_month()