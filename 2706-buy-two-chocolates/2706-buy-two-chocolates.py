class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        m1 = math.inf
        m2 = math.inf

        for p in prices:
            if p <= m1:
                m2 = m1
                m1 = p
            elif p < m2:
                m2 = p

        minCost = m1 + m2
        return money if minCost > money else money - minCost