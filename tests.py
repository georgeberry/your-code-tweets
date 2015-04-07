from your_code_tweets import tweet_me


if __name__ == '__main__':

    #as a decorator
    @tweet_me('usernamehere', 'conf.yaml')
    def failure():
        return 'not an integer'/42

    failure()
