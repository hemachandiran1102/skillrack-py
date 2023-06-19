"""!An odd length string S of length L is passed as the input. The program must print the string S as two diagonals as shown in the example 


Input/Output= b


"""

I="TINKU"
def oddlengthofstring(I):
    
    for i in range(len(I)):
        
        for j in range (len(I)):
            if i==j :
                print(I[j],end=" ")       
            elif i==len(I)-j-1:
                print(I[j], end=" ")
           
            else:
                print(" ",end=" ")
        print()
#oddlengthofstring(I)

"""------------------------------------------------------------------------------------------------------------------------------------"""
"""-----------------P2------------------"""
"""A string S is passed as the input. 
The program must reverse the order of the words in the string and print them as the output.
 Input Format: The first line will contain S. 
 Output Format: The first line will contain the words in the string S in the reverse order. 
 Boundary Conditions: Length of S is from 5 to 100. 
 Example Input/Output 1: 
 Input: Today is Friday 
 Output: Friday is Today 
 Example 
 Input/Output 2: 
 Input: five six ten eleven 
 Output: eleven ten six five
 
 """
#A=list(map(str,input("enter the value: ").split()))
def reversestring(A):
    for I in reversed(range(len(A))):
        print(A[I],end=" ")
#reversestring(A)

#for(int i=0;i<n;i++):

#-------------------------------P3------------------------------------------------------#
"""Minimum Distance Between Words [AMAZON]"""
"""A string S is passed as the input. 

Two words W1 and W2 which are present in the string S are also passed as the input. 
The program must find the minimum distance D between W1 and W2 in S (in forward or reverse order) 
and print D as the output. 

Input Format: The first line will contain S. 
The second line will contain W1. 
The third line will contain W2. 

Output Format: The first line will contain D - the minimum distance between W1 and W2 in S. 

Boundary Conditions: Length of S is from 5 to 200. 
Example Input/Output 1: 

Input: the brown quick frog quick the the quick 
Output: 1 

Explanation: quick and the are adjacent as the last two words. Hence distance between them is 1. 

Example Input/Output 2: 

Input: the quick the brown quick brown the frog quick frog 

Output: 3

"""
#A=["the","brown",'quick','frog','quick','the','the','quick']
#A=['the','quick','the','brown','quick','brown','the','frog','quick','frog']
#w1="the"
#w2='quick'
##list1=[]
#list2=[]
def Minimum_Distance_Between_Words(A,w1,w2):
    for i in range(len(A)):
        if A[i]==w1:
            sum=0
            sum1=0
            for j in range(i,len(A)):
                sum+=1
                if A[j]==w2 :
                    list1.append(sum-1)
            for J in reversed(range(0,i)):
                sum1+=1
                if A[J]==w1:
                    list2.append(sum1-1)
    print(list1,list2)
#Minimum_Distance_Between_Words(A,w1,w2)                    

"""Pattern Printing - Floyd Triangle

 A number N indicating the number of rows in Floyd's triangle is passed as the input. 
 The program must print the Floyd's triangle pattern. 
 Input Format: The first line will contain N.
 Output Format: The first N lines will contain the Floyd's triangle pattern. 
 Boundary Conditions: 3 <= N <= 50 
 Example Input/Output 1: 7 
 Output: 
1 
2 3
4 5 6 
7 8 9 10
11 12 13 14 15 
16 17 18 19 20 21 
22 23 24 25 26 27 28

"""
def floydtriangle(A=int(input("enter-the-value: "))):
    sum=1
    for i in range(A+1):
        for j in range(A+1):
            if i==j:
                break
            else:
                print(sum,end=" ")
                sum+=1
        print()
#floydtriangle()

"""Tower Line of Sight Issue Four towers A, B, C, D are to be erected. 
Tower A is to communicate with tower C. 
Tower B is to communicate with tower D. 
Line of sight issue can occur under the following conditions - 
when tower B or D is in the straight line connecting A and C - 
when tower A or C is in the straight line connecting B and D 
The program must accept the co-ordinates of all four towers and print yes or no 
depending on whether Line of sight issue will occur or not. 
Input Format: The first line will contain X and Y co-ordinates of tower A separated by a space. 
The second line will contain X and Y co-ordinates of tower B separated by a space. 
The third line will contain X and Y co-ordinates of tower C separated by a space. 
The fourth line will contain X and Y co-ordinates of tower D separated by a space 
Output Format: The first line will contain yes or no (smaller case) 
Boundary Conditions: The value of the co-ordinates will be from -500 to 500. 
Example Input/Output 1: 
0 0 
0-2 
2 0 
0 2 

Output: yes 

Example Input/Output 2: 
Input: 
0 0
0 -2 
2 0 
0 -5 
Output: no

"""