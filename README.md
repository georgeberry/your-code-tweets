
# your-code-tweets

Does your code send too few Tweets to you? Fix that problem right away.

1. Decorate any Python function to Tweet you on success or failure.
2. Easily suppress success Tweets and publish only a record of your failures.

## Example

Say you have a terrible, terrible function

    def failure():
        return 'not an integer'/42

You're using 70's hardware, so it could take days to complete.

Get notified on Twitter when it's done (or fails) by simply decorating the function with your username:

    from your_code_tweets import tweet_me

    @tweet_me('@myusername')
    def failure():
      return 'not an integer'/42

Ignore successful function calls with:

    @tweet_me('@myusername', tweet_success=False)
    def failure():
      return 'not an integer'/42

Use the decorator class just to send Tweets willy-nilly:
    
    tweet_result = tweet_me('@myusername')
    tweet_result.tweet('your message here')

## Output example

I called `failure` and sent it to my friend Chris. This is what he got:

> Hey @chrisjcameron, your function call failure failed with exception unsupported
> operand type(s) for /: 'str' and 'int'. Get it together!

Pretty nifty: you get the error right in the tweet. `your-code-tweets` automatically trims the message to 140 characters.

## The Catch

You need to create a `conf.yaml` file in the local directory that holds the Twitter API information for your account. [More information here](https://dev.twitter.com/overview/documentation).

Suggestions on more elegant ways to this are appreciated.

## Disclaimer

I'm not responsible for you sticking this decorator on a function in a triple-nested for loop and Twitter banning your API access. Use with care!

This works best for toplevel functions that are called once and have to run for a long time.

# License

[GPL 3.0](https://www.gnu.org/licenses/gpl-3.0.txt).
