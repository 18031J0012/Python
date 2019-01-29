'''Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2'''

def main():
        s=input()
        s1=s.lower()
        count=0
        for i in range(len(s1)-2):
                if(s1[i]=='b' and s1[i+1]=='o' and s1[i+2]=='b'):
                        count = count + 1
        print(count)
	

if __name__== "__main__":
	main()
