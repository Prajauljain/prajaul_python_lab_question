def max_two(x,y,z):
    l.append(x)
    l.append(y)
    l.append(z)
    return max(l)
a,b,c=map(int,input().split())
l=[]
print(max_two(a,b,c))
