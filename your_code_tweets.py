import twitter, json, time


class tweet_me(object):
    '''
    decorate your functions with this

    give the decorator arguments (the arguments that __init__ takes)
    '''
    def __init__(self, recipient, credentials=None, tweet_success=True):
        '''
        can specify credentials in 3 ways:
            1) absolute path to json file
            2) list of keys, in order
            3) dict of keys, by name

        if reading credentials from disk,
        make a conf.json file of the following format:
            {consumer_key : value
            consumer_secret : value
            access_token_key : value
            access_token_secret : value}
        '''

        if type(credentials) == str: #absolute path
            with open(credentials, 'r') as f:
                conf = json.load(f)
                consumer_key = conf['consumer_key']
                consumer_secret = conf['consumer_secret']
                access_token_key = conf['access_token_key']
                access_token_secret = conf['access_token_secret']
        elif type(credentials) == list: #list of keys
            consumer_key, consumer_secret, access_token_key, access_token_secret = credentials
        elif type(credentials) == dict: #dict of keys
            consumer_key = credentials['consumer_key']
            consumer_secret = credentials['consumer_secret']
            access_token_key = credentials['access_token_key']
            access_token_secret = credentials['access_token_secret']
        else:
            raise Exception('No valid credentials')

        self.t = twitter.Api(consumer_key=consumer_key,
                             consumer_secret=consumer_secret,
                             access_token_key=access_token_key,
                             access_token_secret=access_token_secret)
        
        #automatically add an @ if you don't have it
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
            raise Exception('Slow your roll')


    def __call__(self, f):
        '''
        replace f with wrapped_f
        '''
        def wrapped_f(*args):
            try:
                res = f(*args)
                if self.tweet_success:
                    msg = 'Hey {}, your function "{}" completed at {}!! :3'.format(self.recipient, f.__name__, time.time())
                    self.tweet(msg)
                return res


            except Exception as e:
                msg = 'Hey {}, function "{}" failed with exception "{}" at {}. :('.format(self.recipient, f.__name__, e, time.time())
                self.tweet(msg)
                raise e

        return wrapped_f
