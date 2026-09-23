from collections import defaultdict

class Twitter:

    def __init__(self):
        self.followees = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        sources = set(self.followees[userId])
        sources.add(userId)
        h = []

        for uid in sources:
            if self.tweets[uid]:
                idx = len(self.tweets[uid]) - 1
                t, tid = self.tweets[uid][idx]
                # Store negative time for max-heap behavior
                heapq.heappush(h, (-t, tid, uid, idx))

        while h and len(res) < 10:
            neg_t, tid, uid, idx = heapq.heappop(h)
            res.append(tid)

            idx -= 1
            if idx >= 0:
                t, tid2 = self.tweets[uid][idx]
                heapq.heappush(h, (-t, tid2, uid, idx))
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followees[followerId]:
            self.followees[followerId].remove(followeeId)