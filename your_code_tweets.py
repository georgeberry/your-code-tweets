import twitter, yaml, time


class tweet_me(object):
    '''

    ===
    
    DECORATE your functions with this

    give the DECORATOR arguments (next lvl, rite?)

    make a TWITTER ACCOUNT for your CODE

    (super fly)

    ===

    make a conf.yaml file of the following format:
        consumer_key : <>
        consumer_secret : <>
        access_token_key : <>
        access_token_secret : <>

    requires you to have python-twitter and pyyaml installed

    ===
    
    '''
    def __init__(self, recipient, tweet_success=True):

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
        
        if recipient[0] != '@':
            self.recipient = '@' + recipient
        else:
            self.recipient = recipient
        self.tweet_success = tweet_success
        self.last_tweet_time = 0


    def tweet(self, message):
        if len(message) > 140:
            message = message[:139] #clipped

        if time.time() - self.last_tweet_time > 10:
            self.last_tweet_time = time.time()
            self.t.PostUpdate(message)
        else:
            print('Slow your roll')
            raise


    def __call__(self, f):
        '''
        replace f with wrapped_f, yo
        '''
        def wrapped_f(*args):
            try:
                f(*args)
                if self.tweet_success:
                    msg = 'Hey {}, your function {} completed successfully!! :3'.format(self.recipient, f.__name__)
                    self.tweet(msg)

            except Exception as e:
                msg = 'Hey {}, your function call {} failed with exception {}. Get it together!'.format(self.recipient, f.__name__, e)
                self.tweet(msg)
                raise e

        return wrapped_f
