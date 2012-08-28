from setuptools import setup

setup(
    name = "tweetnevada_updates",
    version = "0.1",
    description = "A munin plugin to show number of tweets from TweetNevada.com",
    author = "Eric Davis",
    author_email = "ed@npri.org",
    py_modules = ["tweetnevada_updates"],
    install_requires = ["pymongo"],
    entry_points = {
        "console_scripts": [
            "tweetnevada_updates=tweetnevada_updates:main",
        ],
    }
)
