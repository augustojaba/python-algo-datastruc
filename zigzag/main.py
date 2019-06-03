
class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        count = 0
        direction = 1
        result = list()

        for i in range(num_rows):
            result.append(str())

        print(count)
        for c in s:
            result[count] += c

            if direction == 1:
                if count < num_rows - 1:
                    count += 1
                else:
                    count -= 1
                    direction = 0
            else:
                if count > 0:
                    count -= 1
                else:
                    count += 1
                    direction = 1
        print(''.join(result))


Solution().convert('PAYPALISHIRING', 3)
# "PAYPALISHIRING"
# # 3