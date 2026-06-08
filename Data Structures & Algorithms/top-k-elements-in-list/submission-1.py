import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        
        topk=heapq.nlargest(k,freq.items(),key=lambda item:item[1])
        res=[]
        for i in topk:
            num=i[0]
            res.append(num)
        return res