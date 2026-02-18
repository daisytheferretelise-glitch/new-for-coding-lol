
def palind(r):
    e=len(r)-1
    s=0
    while(s<e):
        if (r[s]!=r[s]):
            return False
        s+=1
        e-=1
    return True

r=("Bob")
if(palind(r)):
    print("Jeff complainns how he was wrong since 'he' was wrong and Bob was so sigma for getting that right because it was flip-flop")
else:
    print("Jeff complainns how he was wrong since 'he' was wrong and Bob was so sigma for getting that right because it was not flip-flop")