class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        sorted_d=sorted(zip(heights,names), reverse=True)
        sorted_n=[]
        for _,names in sorted_d:
            sorted_n.append(names)
        return sorted_n