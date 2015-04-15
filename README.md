# your-code-tweets

Does your code send too few Tweets to you? Fix that problem right away.

1. Decorate any Python function to Tweet you on success or failure.
2. Easily suppress your successes and publish only a record of your failures.

## Example

Say you have a terrible, terrible function

    def failure():
        return 'not an integer'/42

You're using 70's hardware, so it could take days to complete.

Get notified on Twitter when it's done (or fails) by simply decorating the function with your username:

    from your_code_tweets import tweet_me

    @tweet_me('@myusername', credentials)
    def failure():
      return 'not an integer'/42

Ignore successful function calls with:

    @tweet_me('@myusername', credentials=credentials, tweet_success=False)
    def failure():
      return 'not an integer'/42


## Output example

I called `failure` and sent it to my friend Chris. This is what he got:

> Hey @chrisjcameron, your function call failure failed with exception unsupported
> operand type(s) for /: 'str' and 'int'. Get it together!

Pretty nifty: you get the error right in the tweet. `your-code-tweets` automatically trims the message to 140 characters.

## The Catch (Credentials)

You need to make a Twitter account for your code and pass Twitter credentials to the decorator. More about Twitter credentials [here](https://dev.twitter.com/overview/documentation) and [here](https://code.google.com/p/python-twitter/).

There are three ways to pass credentials:

1. A string containing the absolute path to a `.json` file with credentials
2. A list of ordered credentials
3. A dictionary of named credentials

These are auto-detected from the type of the passed object. See `your_code_tweets.py` for the exact format of these objects.

## Disclaimer

I'm not responsible for you sticking this decorator on a function in a triple-nested for loop and Twitter banning your API access. Use with care!

Right now, each calling class instance is limited to one tweet per 10 seconds, but this doesn't stop you from making multiple class instances.

This works best for toplevel functions that are called once and have to run for a long time.

# License

[GPL 3.0](https://www.gnu.org/licenses/gpl-3.0.txt)