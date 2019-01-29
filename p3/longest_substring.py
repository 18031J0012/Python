def main():
    s = input()
    # the input string is in s
    # remove pass and start your code here
    maxlen=0
    current=s[0]
    long=s[0]
    
    for i in range(len(s)-1):
        if s[i+1]>=s[i]:
            current+=s[i+1]
            if len(current)>maxlen:
                maxlen=len(current)
                long=current
        else:
            current=s[i+1]
    i+=1
    print(long)
    
if __name__== "__main__":
    main()

