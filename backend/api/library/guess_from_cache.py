from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.conf import settings
import json


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

CACHE_HISTORY_KEY = 'guess_history'
CACHE_GUESS_MIN_KEY = 'guess_min'
CACHE_GUESS_MAX_KEY = 'guess_max'

GUESS_MIN = 1
GUESS_MAX = 100

   
def make_guess(cache, action):
    if action == "start":
        cache.clear()
        cache.set(CACHE_GUESS_MIN_KEY, GUESS_MIN, timeout=CACHE_TTL)
        cache.set(CACHE_GUESS_MAX_KEY, GUESS_MAX, timeout=CACHE_TTL)
        cache.set(CACHE_HISTORY_KEY, json.dumps([]), timeout=CACHE_TTL)

    guess_min = cache.get(CACHE_GUESS_MIN_KEY, GUESS_MIN)
    guess_max = cache.get(CACHE_GUESS_MAX_KEY, GUESS_MAX)
    guess_history_cache = cache.get(CACHE_HISTORY_KEY, json.dumps([]))

    history = json.loads(guess_history_cache)

    if len(history) > 0:
        if action == ">":
            guess_min = history[-1] + 1

        elif action == "<":
            guess_max = history[-1]


    guessed_number = (guess_min+guess_max)//2
    history.append(guessed_number)
    attempt = len(history)

    cache.set(CACHE_GUESS_MIN_KEY, guess_min, timeout=CACHE_TTL)
    cache.set(CACHE_GUESS_MAX_KEY, guess_max, timeout=CACHE_TTL)
    cache.set(CACHE_HISTORY_KEY, json.dumps(history), timeout=CACHE_TTL)

    return {
        'guessed_number' : guessed_number,
        'attempt': attempt,
    }
   

def get_summary(cache):
    guess_history_cache = cache.get(CACHE_HISTORY_KEY, json.dumps([]))
    history = json.loads(guess_history_cache)

    if len(history) > 0:
        attempt = len(history) 
        guessed_number = history[-1]
        message = "Number is predicted successfully! Your selected number is {}".format(guessed_number)
     
        return {
            'message' : message,
            'attempt': attempt,
        }

    else:
        return {
            'message' : "cache history timout",
            'attempt': '',
        }
