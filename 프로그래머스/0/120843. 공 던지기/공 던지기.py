def solution(numbers, k):
    #0->2->4->6->8->10
    
    idx = 2 * (k-1)
    idx= idx % (len(numbers))
    
    return numbers[idx] 