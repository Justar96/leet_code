class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        val1 = len(word1)
        val2 = len(word2)
        val3 = val1+val2
        
        temp3 = []

        if val1 == val2:
            temp0 = word2[-1]
            for i in range(len(word1)):
                merged0 = word2[i].join(word1[i:i+2])
                temp3.append(merged0[0:2])
            str_convert = map(str, temp3)
            str_list = ''.join(str_convert)
            result = str_list+temp0
        else:
            if val1 < val2:
                temp0 = val2-val1
                temp1 = word2[0:val1]
                temp2 = word2[(val2-temp0)-1:]
                for i in range(len(word1)):
                    merged0 = word2[i].join(word1[i:i+2])
                    temp3.append(merged0[0:2])
                str_convert = map(str, temp3)
                str_list = ''.join(str_convert)
                result = str_list+temp2
            else:
                temp0 = val1-val2
                temp1 = word1[0:val1]
                temp2 = word1[val1-temp0:]
                for i in range(len(word2)):
                    merged0 = word2[i].join(word1[i:i+2])
                    temp3.append(merged0[0:2])
                str_convert = map(str, temp3)
                str_list = ''.join(str_convert)
                result = str_list+temp2
        return result