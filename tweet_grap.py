import got

def call_o():
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('pepsi').setSince('2017-03-01').setUntil('2017-05-06').setMaxTweets(10)
    # tweetCriteria = got.manager.TweetCriteria().setUsername("barackobama").setSince("2015-09-10").setUntil("2015-09-12").setMaxTweets(1)
    # tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]
    ret = got.manager.TweetManager.getTweets(tweetCriteria)
    print len(ret)
    for i in ret:
        print {'id': i.id, 'username': i.username, 'date':i.date, 'text': i.text}
        print

    # print tweet.text

call_o()
