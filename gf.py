p1=input()
q2=''
r3='0ABCDEFGHIJKLMNOPQRSTUVWXYZABC'
for i in p1:
    if i in r3:
        t=r3.index(i)
        t=t+3
        q2=q2+r3[t]
print(q2)
