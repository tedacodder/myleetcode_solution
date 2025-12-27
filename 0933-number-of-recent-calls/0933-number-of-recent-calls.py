class RecentCounter:

    def __init__(self):
        counter=0
        self.request=deque()

    def ping(self, t: int) -> int:
        a,b=t-3000,t
        if not self.request:
            self.request.append(t)
            return 1
        else:
            while self.request and self.request[0]<a:
                self.request.popleft()
            self.request.append(t)
        return len(self.request)

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)