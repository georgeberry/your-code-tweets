# decorative-tweets

Decorate any Python function to Tweet you on success or failure. Easily suppress success Tweets.

# Example

Say you have a terrible, terrible function

    def failure():
      return 'not an integer'/42

You're running this function, and you're using 70's hardware, so it could take days to complete.

Get notified on Twitter when it's done (or fails) by simply decorating the function with your username:

    from decorative-tweets import tweet_me
    @tweet_me('@myusername')
    def failure():
      return 'not an integer'/42

