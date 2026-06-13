class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}

        for task in tasks:
            if task in count:
                count[task] += 1
            else:
                count[task] = 1

        max_freq = 0
        
        for task in count:
            if count[task] > max_freq:
                max_freq = count[task]
        
        max_freq_count = 0

        for task in count:
            if count[task] == max_freq:
                max_freq_count += 1

        return max((max_freq-1)*(n+1) + max_freq_count, len(tasks))