class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mindiff=arr[-1]-arr[0]
        num=[]
        
        for i in range(len(arr)-1):
            mindiff=min(mindiff,arr[i+1]-arr[i])
            
        for i in range(len(arr)):
            if (arr[i]-arr[i-1]==mindiff):
                num.append([arr[i-1],arr[i]])
        return num