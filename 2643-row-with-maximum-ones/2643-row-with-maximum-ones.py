class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        res=[0,0]
        for i, row in enumerate(mat):
            cnt_o=sum(row)
            if res[1]<cnt_o:
                res=[i,cnt_o]
        return res