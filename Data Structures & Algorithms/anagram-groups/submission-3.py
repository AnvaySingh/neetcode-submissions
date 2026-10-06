class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}

        for word in strs:
            intialsort="".join(sorted(word))

            if intialsort in hashmap:
                hashmap[intialsort].append(word)
            else:
                hashmap[intialsort]=[word]

        return list(hashmap.values())


        