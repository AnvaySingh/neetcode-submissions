class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        finaloutput={}

        for number in nums:

            if number in finaloutput:
                finaloutput[number]+=1
            else:
                finaloutput[number]=1

        sorted_hashmap=sorted(finaloutput, key=finaloutput.get, reverse=True)

        return sorted_hashmap[:k]



            


        