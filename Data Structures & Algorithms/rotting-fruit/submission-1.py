class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=deque()
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        time=0
        fresh=0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    q.append((r,c))

        while q and fresh>0:
            length=len(q)
            for i in range(length):
                r,c=q.popleft()

                for dr,dc in directions:
                    rows=r+dr
                    cols=c+dc

                    if(rows in range(len(grid)) and cols in range(len(grid[0])) and grid[rows][cols]==1):
                        grid[rows][cols]=2
                        q.append((rows,cols))
                        fresh-=1

            time+=1
        if fresh==0:
            return time
        else:
            return -1

        