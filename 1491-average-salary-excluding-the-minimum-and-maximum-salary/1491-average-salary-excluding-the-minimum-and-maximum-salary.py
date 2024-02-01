class Solution:
    def average(self, salary: List[int]) -> float:
        sum=0
        avg=0
        l=len(salary)-2
        salary.sort()
        for i in range(1,len(salary)-1):
            sum+=salary[i]
        avg=sum/l
        return avg
        