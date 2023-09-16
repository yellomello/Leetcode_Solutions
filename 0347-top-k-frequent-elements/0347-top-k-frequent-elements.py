class Solution(object):
    def topKFrequent(self, nums, k):
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return (res)



#My First solution that didn't work:
'''

d={}
for i in range(len(nums)):
  # if nums[i] not in d:
  #   d[nums[i]]=1
  # else: 
  #   d[nums[i]]+=1
  if nums[i] in d:
    d[nums[i]]+=1
  else: 
    d[nums[i]]=1
sorted_dict = dict(sorted(d.items(), key=lambda item: item[1],reverse=True))
first_two_keys = list(sorted_dict.keys())[:k]
return(first_two_keys)

'''
