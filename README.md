# KalderinoBot

## Installation

Create a .env file with the following variables and format:

```
# .env
ACCESS_TOKEN=abcd1234 
BOT_PREFIX=!
INITIAL_CHANNELS=kalderinofeross, anotherchannel1, anotherchannel2, ...
```

To generate an acces token, go to the twitch [token generator](https://twitchtokengenerator.com/), login as your bot account and select "bot chat token".


I recommend making a virtual environment using python 3.9.x or above:

```
pipenv --python 3.9
pipenv install -r requirements.txt
```

## Usage

```
(pipenv run) python bot.py
```

A Procfile is included for heroku deployment.

Use ctrl-C to stop the bot.
