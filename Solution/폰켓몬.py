def solution(nums):
    dict={}
    for num in nums:
        dict[num]=0
        
    for num in nums:
        dict[num]+=1
 
    if(len(dict)>len(nums)//2):
        return len(nums)//2
    else:
        return len(dict)
    

