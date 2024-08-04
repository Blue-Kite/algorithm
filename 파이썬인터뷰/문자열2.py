class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        numlog = []
        strlog = []
        for log in logs:
            if log.split()[1].isdigit():
                numlog.append(log)
            else:
                strlog.append(log)
        strlog.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return strlog + numlog