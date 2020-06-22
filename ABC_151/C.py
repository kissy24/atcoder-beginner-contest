N, M = list(map(int, input().split()))
a = []

for i in range(M):
    a.append(map(str, input().split()))

p_sum = 0
s_sum = 0

s_dict = {}
p_dict = {}
for k in range(M):
    ps = list(a[k])

    if (ps[0] in p_dict) == True:
        if p_dict[ps[0]] == True:
            continue
    if ps[1] == "WA":  
        if (ps[0] in s_dict) == True:
            s_dict[ps[0]] += 1
        else:
            s_dict[ps[0]] = 1
    else:
        p_dict[ps[0]] = True
        p_sum += 1
        if (ps[0] in s_dict) == True:
            s_sum += s_dict[ps[0]]
        pre_s_sum = 0

print(str(p_sum) + " " + str(s_sum))

# 考慮できていなかった点
# 過去番号のwaまたはacが後にくる場合