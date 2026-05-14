class Twitter:

    def __init__(self):
        self.following = {}
        self.posts = {}
        self.timestamp = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        if userId in self.posts:
            self.posts[userId].append((tweetId, self.timestamp))
        else:
            self.posts[userId] = [(tweetId, self.timestamp)]

    def getNewsFeed(self, userId: int) -> List[int]:
        
        tweets = self.posts.get(userId, []).copy()

        for followee in self.following.get(userId, []):
            tweets += self.posts.get(followee, [])

        tweets.sort(key=lambda x: x[1], reverse=True)
        return [x[0] for x in tweets[:10]]

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId: return
        if followerId in self.following:
            if followeeId not in self.following[followerId]:
                self.following[followerId].append(followeeId)
        else:
            self.following[followerId] = [followeeId]
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            if followeeId in self.following[followerId]:
                self.following[followerId].remove(followeeId)
        
