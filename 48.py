class Solution(object):
    def groupAnagrams(self, strs):
        dic={}

        for word in strs:
            sort_w=''.join(sorted(word))

            if sort_w not in dic:
                dic[sort_w]=[word]
            else:
                dic[sort_w].append(word)

        return list(dic.values())
