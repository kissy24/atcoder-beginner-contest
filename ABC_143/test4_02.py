N = int(input())
dlist = list(map(int, input().split()))
dlist.sort(reverse=True)
sum = 0
N_2 = 2 ** N
for i in range(N_2):
    if bin(i).count('1') == 3:
        bin_i = bin(i)
        i_2 = bin_i.split('0b')[1]
        if len(i_2) < N:
            N_i = (N - len(i_2))
            N_0 = '0' * N_i
            i_2 = N_0 + i_2
        a_find = i_2.find('1')
        b_find = i_2.find('1',a_find + 1)
        c_find = i_2.find('1',b_find + 1)
        a = dlist[a_find]
        b = dlist[b_find]
        c = dlist[c_find]
        if a < b + c:
            sum += 1
print(sum)