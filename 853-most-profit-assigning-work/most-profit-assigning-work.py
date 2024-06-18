from typing import List

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # Step 1: Combine difficulty and profit and sort by difficulty
        jobs = sorted(zip(difficulty, profit))
        
        # Step 2: Sort the worker abilities
        worker.sort()
        
        max_profit = 0
        total_profit = 0
        job_index = 0
        n = len(jobs)
        
        # Step 3: Iterate through each worker
        for ability in worker:
            # Find the most profitable job the worker can do
            while job_index < n and jobs[job_index][0] <= ability:
                max_profit = max(max_profit, jobs[job_index][1])
                job_index += 1
            total_profit += max_profit
        
        return total_profit