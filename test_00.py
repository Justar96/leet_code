
word1 = "hbkhl"
word2 = "asdwe"

val1 = len(word1)
val2 = len(word2)
val3 = val1+val2


temp2 = 0
temp3 = []
check = False
if val1 == val2:
    for i in range(len(word1)):
        temp0 = word2[-1]
        merged0 = word2[i].join(word1[i:i+2])
        temp3.append(merged0[0:2])
    str_convert = map(str, temp3)
    str_list = ''.join(str_convert)
    result = str_list+temp0
else:
    if val1 < val2:
        for i in range(len(word1)):
            temp0 = val2-val1
            temp1 = word2[0:val1]
            temp2 = word2[(val2-temp0)-1:]
            merged0 = word2[i].join(word1[i:i+2])
            temp3.append(merged0[0:2])
        str_convert = map(str, temp3)
        str_list = ''.join(str_convert)
        result = str_list+temp2
    else:
        for i in range(len(word2)):
            temp0 = val1-val2
            temp1 = word1[0:val1]
            temp2 = word1[val1-temp0:]
            merged0 = word2[i].join(word1[i:i+2])
            temp3.append(merged0[0:2])
        str_convert = map(str, temp3)
        str_list = ''.join(str_convert)
        result = str_list+temp2
    
    


if val3 == len(result):
    check = True





        # merged0 = word2[0].join(word1[0:2])
        # merged1 = word2[1].join(word1[1:3])
        # merged2 = word2[2].join(word1[2:4])
        # merged3 = word2[3].join(word1[3:5])
        # merged4 = word2[4].join(word1[4:6])
        # result = f"{merged0[0:2]+merged1[0:2]+merged2[0:2]+merged3[0:2]+merged4[0:2]+temp2}"
print(val1)
print(val2)
print(val3)
# print(temp0)
# print(temp1)
# print(temp2)
print(result)
print(check)
