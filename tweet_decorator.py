'''
tweets at you when shit goes wrong (or right)

make an info.yaml file of the following format:
    consumer_key : <>
    consumer_secret : <>
    access_token_key : <>
    access_token_secret : <>

requires you to have python-twitter and pyyaml installed
'''

import twitter, yaml

class tweet_me(object):
    '''
    DECORATE your functions with this

    super fly

    give the DECORATOR arguments (next lvl, rite?)

    make a TWITTER ACCOUNT for your CODE
    '''
    def __init__(self, tweet_atcha, tweet_success=True):
        '''
        email_to and email_from have to be email addresses
        '''
        with open('conf.yaml', 'r') as f:
            conf = yaml.load(f)
            consumer_key = conf['consumer_key']
            consumer_secret = conf['consumer_secret']
            access_token_key = conf['access_token_key']
            access_token_secret = conf['access_token_secret']

        self.t = twitter.Api(consumer_key=consumer_key,
                             consumer_secret=consumer_secret,
                             access_token_key=access_token_key,
                             access_token_secret=access_token_secret)
        
        self.tweet_atcha = tweet_atcha
        self.tweet_success = tweet_success


    def tweet(self, message):
        if len(message) > 140:
            message = message[:139] #clipped

        self.t.PostUpdate(message)


    def __call__(self, f):
        '''
        replace f with wrapped_f, yo
        '''
        def wrapped_f(*args):
            try:
                f(*args)
                if self.tweet_success:
                    msg = 'Hey {}, your function {} completed successfully!! :3'.format(self.tweet_atcha, f.__name__)
                    self.tweet_msg

            except Exception as e:
                msg = 'Hey {}, your function call {} failed with exception {}. Get it together!'.format(self.tweet_atcha, f.__name__, e)
                self.tweet(msg)

        return wrapped_f


