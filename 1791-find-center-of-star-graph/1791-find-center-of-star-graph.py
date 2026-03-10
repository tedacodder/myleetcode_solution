class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        #convert to adjecency list
        addlist=defaultdict(list)
        for e in edges:
            u,v=e
            addlist[u].append(v)
            addlist[v].append(u)
        for i in addlist:
            if len(addlist[i])==len(edges):
                return i
