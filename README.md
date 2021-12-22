# KalderinoBot

## Instalation

Create a .env file with the following variables and format:

```
# .env
ACCESS_TOKEN=abcd1234
BOT_PREFIX=!
INITIAL_CHANNELS=kalderinofeross, anotherchannel1, anotherchannel2, ...
```

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
