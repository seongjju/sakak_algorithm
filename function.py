def sequence(n):
    if n==1:
        return "1"
    cur="1"
    for _ in range(2,n+1):
        i=0
        li=[]
        while i<len(cur):
            count=1
            while i+1<len(cur) and cur[i] == cur[i+1]:
                count+=1
                i+=1
            li.append(str(count))
            li.append(cur[i])
            i+=1
        cur=''.join(li)
    return cur
