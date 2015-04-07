from your_code_tweets import tweet_me

#tweets success or failure
@tweet_me('@georgeberry', 'conf.yaml')
def failure():
    return 'not an integer'/42

#don't tweet on success
@tweet_me('@georgeberry', credentials='conf.yaml', tweet_success=False)
def success():
    return 42/42


if __name__ == '__main__':


    failure()

    success()

