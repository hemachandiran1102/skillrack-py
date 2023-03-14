#-----------------------------------------------------------------P1----------------------------------------------------------------

"""Identify correct operator. An expression E is passed as an input to the program. 
The expression will contain three numbers A, B and C, one equal symbol and one of the mathematical operators + - * / 
But the given mathematical operator is incorrect and hence the expression is not valid. 
Hence the program must identify the correct operator and print that as the output. 

Input Format: First line will contain the expression E 

Output Format: First line will contain the correct mathematical operator 

Sample Input/Output: 

Example 1: 

Input: 

5-4=20 
Output: * 

Explanation: Only 5 multiplied with 4 gives 20. Hence - must be replaced with *. 

Example 2: Input: 999+9=111 Output: / Explanation: Only 999 divided by 9 gives 111. Hence + must be replaced with /."""

#print(ord("*"),ord("/"),ord("+"),ord("-"))



def idfycrtop():
    E=["808-100","98"]
    
    A=""
    for I in range(len(E[0])):      
        if ord(E[0][I])==45 or ord(E[0][I])==42 or ord(E[0][I])==47 or ord(E[0][I])==43:
            A=E[0].split(E[0][I])
            
        
    if int(A[0])*int(A[1])==int(E[1]):
        print("*")
    elif int(A[0])/int(A[1])==int(E[1]):
        print("/") 
    elif int(A[0])+int(A[1])==int(E[1]):
        print("+")
    elif int(A[0])-int(A[1])==int(E[1]):
        print("-")   
    print(A)
        

#idfycrtop()


#-------------------------------------------------------------------------P2--------------------------------------------------------------------
"""Character B follows A Given a string S and two characters A, 
B the program must print the number of occurrences where A is followed by B. 

Boundary Conditions: Length of the string S is between 2 and 200. 

Input Format: First line will contain the string value S. 
Second line will contain the value of A. 
Third line will contain the value of B. 

Output Format: First line will contain the integer which represents the number of occurrences in sring S 

where A is followed by B Sample 

Input/Output: 

Example 1: 

Input: 
malayalam 
a 

l 

Output: 

2 

Explanation: The two occurrences where a is followed by l is as highlighted below. malayalam 

Example 2: 

Input: 

engine 

e 

n 

Output: 1


"""
def twochar():
    S="amapodumadam"
    A="a"
    B="m"
    count=0
    for I in range(len(S)):
        if S[I]==A and S[I+1]==B:
            count+=1
    print(count)
#twochar()


#---------------------------------------------------------------------------P2-------------------------------------------------------------

"""Arithmetic Progression - Nth Term The first three terms in an arithmetic progression are passed as input. 
A positive integer value N (where N > 3) is also passed as the input. 

The program must print Nth term in the arithmetic progression. 

Input Format: The first line will contain the first three terms separated by a space. 

The second line will contain N. 

Output Format: The integer value denoting the Nth term. 

Example 

Input/Output 1: 

Input: 
5 10 15 
6 

Output:
 30 
 
 Explanation: The progression is 5 10 15 20 25 30 35 and so on. 
 
 The 6th term is 30. 
 
 Example Input/Output 2: 
 
 Input: 1 4 7 
 5 
 
 Output: 13"""

def ArrProgres():
    #A=list(map(int,input().split()))
    #B=int(input())
    A=[1,4,7]
    B=5
    I=0
    D=A[1]-A[0]
    sum=A[0]
    while I < B-1:
        sum+=D
        I+=1
    print(sum)
#ArrProgres()

#--------------------------------------------------------P3-------------------------------------------------------------

"""Arrange Alphabets - Descending Order A string S (with only LOWER case alphabets and length from 3 to 100) will be passed as input. 
The program should print the alphabets in the string in descending order. 

Input Format: The first line will contain S. 
Output Format: The first line will contain the alphabets present in S in descending order. 

Example Input/Output 1: 

Input: cake 

Output: keca 

Example Input/Output 2: 

Input: innovation 

Output: vtonia

"""

def ArrAlpha():
    S="innovation"
    list=[]
    for i in range(len(S)):
        list.append(ord(S[i]))
    
    for I in range(len(list)):
        for J in range(I+1,len(list)):
            if list[I]>list[J]:
                list[I],list[J]= list[J],list[I]
            #if list[I] == list[J]:
    print(list)
#ArrAlpha()
#-------------------------------------------------P4----------------------------------------------
""" Square Matrix - Corner Elements Sum A square matrix of size N×N is passed as the input. 
 The program must calculate and print the sum of the elements in the corners. 
 
 Input Format: The first line will contain the value of N. 
 
 The next N lines will contain the N values separated by one or more spaces. 
 
 Output Format: The first line will contain the integer value denoting the sum of the elements
  in the corners. 
  
  Boundary Conditions: 2 <= N <= 20 
  
  Example 
  
  Input/Output 1: 
  Input: 
  3 
  10 90 1 
   4 22 5 
  32 8 66
  
  Output: 109 Explanation: The sum = 10+1+66+32 = 109
  
  
  
  """           

def sumOfMatrix():
    #N=int(input())
    list1=[[10, 90, 1], [4, 22, 5], [32, 8, 66]]
    #for I in range(3):
        #I = list(map(int,input().split()))
        #list1.append(I)
    print(list1[0][0]+list1[0][len(list1[0])-1]+list1[len(list1)-1][0]+list1[len(list1)-1][len(list1[0])-1  ])
#sumOfMatrix()

#----------------------------------------------------P5-------------------------------------------

"""Rotate String - N Positions A string S of length L is passed as the input. 
The program must rotate the string S by N position in forward direction and 
print the result as the output. 

Input Format: The first line will contain the value of S. The second line will contain N. 

Output Format: The first line will contain the rotated string value. 

Boundary Conditions: The length L of the string S is from 3 to 100. 
0 <= N <= L 

Example Input/Output 1: 

Input: 
    cricket 
    2 
Output: 
    etcrick 
Example Input/Output 2: 

Input: 
    truth 
    5 
Output:
    truth
"""

def RotateString():
    S="truth"
    N=4
    print(S[len(S)-N:len(S)+1])
#RotateString()

#-----------------------------------------------------------P6----------------------------------------
"""Next Prime Number A number N is passed as the input. 
The program must print the next immediate prime number. 
Input Format: The first line will contain N. 
Output Format: The first line will contain the integer value of next immediate prime number. 
Boundary Conditions: 1 <= N <= 999999 Example 
Input/Output 1: 
Input: 11 
Output: 13 

Example 
Input/Output 2:
Input: 2 
Output: 3
"""
N=3371
def checkprime(N):

    if N == 1:
        #print(N,"prime")
        return True
    if N == 0:
        #print (N,"not prime")
        return False
    for i in range(2,N):
       
        if N%i==0:
            #print(N,"not prime")           
            return False
            break
        
        else:
            #print(N,"prime")
            return True
            break
def findnextprime(N):
    
    while True:
        N=N+1
        if checkprime(N)==True:
            print(N)
            break
        
        
        
            
        
            
#checkprime(N)
findnextprime(N)
        