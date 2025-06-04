class Solution(object):
    def decrypt(self, code, k):
        n = len(code)
        output = []
        for i in range(n):
            total = 0

            if k>0:
                for j in range(1,k+1):
                    index = (i+j) % n
                    total+=code[index]
            elif k<0:
                for j in range(1,-k+1):
                    index = (i-j) % n
                    total+=code[index]
            else:
                pass
            output.append(total)
        return output