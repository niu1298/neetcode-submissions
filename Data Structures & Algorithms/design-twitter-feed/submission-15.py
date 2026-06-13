class Twitter:

    def __init__(self):
        self.tweets = {}
        self.followMap = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.tweets:
            self.tweets[userId] += [(self.time,tweetId)]
        else:
            self.tweets[userId] = [(self.time,tweetId)]
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        ans = []
        if userId in self.tweets:
            ans += self.tweets[userId][:]
        if userId in self.followMap:
            for followeeId in self.followMap[userId]:
                if followeeId in self.tweets and followeeId != userId:
                    ans += self.tweets[followeeId]
        
        ans.sort(key = lambda p: p[0],reverse=True)
        li = []
        for i in range(min(len(ans),10)):
            li += [ans[i][1]]
        return li
        

    def follow(self, followerId: int, followeeId: int) -> None:

        if followerId in self.followMap and (followeeId not in self.followMap[followerId]):
            self.followMap[followerId].add(followeeId)
        else:
            self.followMap[followerId] = {followeeId}
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap:
            self.followMap[followerId].discard(followeeId)
        
