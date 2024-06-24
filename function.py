def sequence(n, dic={1: "1"}):
    if n in dic:
        return dic[n]
    
    cur = sequence(n - 1, dic)
    i = 0
    li = []

    while i<len(cur):
        count=1
        while i+1<len(cur) and cur[i] == cur[i+1]:
            count+=1
            i+=1
        li.append(str(count))
        li.append(cur[i])
        i+=1
    dic[n] = ''.join(li)
    return dic[n]


def print_middle(n):
    answer = sequence(n)
    index = len(answer) // 2
    result1 = answer[index-1]
    result2 = answer[index]
    result = result1+result2
    return int(result)



