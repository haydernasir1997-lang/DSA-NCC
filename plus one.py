class Solution:
    def plusOne(self, d: List[int]) -> List[int]:
        s=""
        for i in range(len(d)):
            s +=str(d[i])
        t = int(s)    
        t+=1
        x=str(t)
        d2=[]
        for j in x:
            d2.append(int(j))

        d= d2
        return d     


