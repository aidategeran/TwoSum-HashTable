#Two Sum Hash table 
nums=[2,7,11,15]
target=9


pair_idx={}
for i,num in enumerate(nums):
    if target-num in pair_idx:
         print ([i,pair_idx[target-num]])
    pair_idx[num]=i
    
       
     
        
