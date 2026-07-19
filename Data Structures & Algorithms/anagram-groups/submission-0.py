class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import Counter
        counter_dict = {}
        position = 0
        res = []
        for i in range(len(strs)):
            key = "".join(sorted(strs[i]))
            if counter_dict.get(key) == None:
                res.append([strs[i]])
                counter_dict[key] = position
                position += 1
            else:
                res[counter_dict[key]].append(strs[i])
        
        return res