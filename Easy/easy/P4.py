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



from itertools import count
from re import S
from markupsafe import string


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
    S1="mayday"
    S2="daybreak"
    
    string=""
    
    for I in range(min(len(S1),len(S2))):
    
        if S1[-I:] == S2[:I]:
            string+=S2[:I]

                    
            
    print(string)


        
                
            
                
                
    #print(string,list11)
matchstring()

