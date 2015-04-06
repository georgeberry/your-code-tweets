from tweet_decorator import tweet_me


@tweet_me('')
def failure():
    return 'not an integer'/42

if __name__ == '__main__':
    failure()