from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int: 
        i, j = 0 
        length = len(chars)
        count = 1
        
        now_char = chars[i]
        
        while True:
            if now_char == chars[j]:
                count = count + 1
            else:
                
                if count > 1:
                    
                if count > 9: 
            
        
    # def compress(self, chars: List[str]) -> int:
    #     group_by = {}

    #     for char in chars:
    #         key = group_by.keys()

    #         if char in key:
    #             group_by[char] = group_by[char] + 1
    #         else:
    #             group_by[char] = 1

    #     result = []
    #     for k, v in group_by.items():
    #         result.append(k)
    #         print("v:", v)
    #         if v > 1 and v < 10:
    #             result.append(str(v))
    #         elif v >= 10:
    #             result.extend(list(str(v)))
    #     l = len(result)

    #     print(result)


chars = [
    ["a", "a", "b", "b", "c", "c", "c"],
    ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"],
]
s = Solution()

for c in chars:
    s.compress(c)
