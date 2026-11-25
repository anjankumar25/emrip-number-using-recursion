def aa(a,v=0):
    if a==0:
        return v
    e=a%10
    v=(v*10)+e
    return aa(a//10,v)
n=int(input("enter ;"))
vn=aa(n)
print(vn)
def ai(j,k):
    if k == 1:
        return 1
    if j % k ==0:
        return 0
    return ai(j,k-1 )
vl=ai(n,n-1)
vp=ai(vn,vn-1)
if vl == 1 and vp == 1:
    print(f"{n} and {vn} are the emrip numers")
else:
    print(f"{n} and {vn} not are the emrip numers")