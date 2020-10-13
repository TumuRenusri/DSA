def reverse(s,stop,start):
    if start<stop:
        return s
    else:
        s[start],s[stop]=s[stop],s[start]
        return reverse(s,start+1,stop)
x=input()
y=list(map(int,x.split()))
print(reverse(y,0,len(y)-1))