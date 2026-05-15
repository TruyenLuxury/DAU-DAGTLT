class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        record = []
        for op in operations:
            if op == 'C':
                record.pop()                        # Xóa điểm trước đó
            elif op == 'D':
                record.append(record[-1] * 2)       # Gấp đôi điểm trước đó
            elif op == '+':
                record.append(record[-1] + record[-2])  # Tổng 2 điểm trước
            else:
                record.append(int(op))              # Thêm điểm mới
        return sum(record)