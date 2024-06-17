# config/config.py
import os
import yaml
import pytz

def load_config(config_path):
    if os.path.exists(config_path):
        with open(config_path, 'r') as file:
            config_vars = yaml.safe_load(file)
    else:
        config_vars = {}

    # Function to get the value from config.yml or environment variable
    def get_config(key, default=None):
        return config_vars.get(key, os.getenv(key, default))

    config = {
        'TZ': get_config('TZ', 'Etc/UTC'),
        'DISCORD_TOKEN': get_config('DISCORD_TOKEN', 'your_discord_bot_token'),
        'CHANNEL_ID': int(get_config('CHANNEL_ID', 'your_channel_id')),
        'UPDATE_DAYS': int(get_config('UPDATE_DAYS', 7)),
        'IMG_FOLDER': get_config('IMG_FOLDER', 'img'),
        'KEEP_DAYS': int(get_config('KEEP_DAYS', 7)),
        'TIME_RANGE_DAYS': int(get_config('TIME_RANGE_DAYS', 30)),
        'TAUTULLI_API_KEY': get_config('TAUTULLI_API_KEY', 'your_tautulli_api_key'),
        'TAUTULLI_URL': get_config('TAUTULLI_URL', 'http://your_tautulli_ip:port/api/v2'),
        'LANGUAGE': get_config('LANGUAGE', 'en'),
        'DAILY_PLAY_COUNT': bool(get_config('DAILY_PLAY_COUNT', True)),
        'PLAY_COUNT_BY_DAYOFWEEK': bool(get_config('PLAY_COUNT_BY_DAYOFWEEK', True)),
        'PLAY_COUNT_BY_HOUROFDAY': bool(get_config('PLAY_COUNT_BY_HOUROFDAY', True)),
        'TOP_10_PLATFORMS': bool(get_config('TOP_10_PLATFORMS', True)),
        'TOP_10_USERS': bool(get_config('TOP_10_USERS', True)),
        'PLAY_COUNT_BY_MONTH': bool(get_config('PLAY_COUNT_BY_MONTH', True))
    }

    config['timezone'] = pytz.timezone(config['TZ'])

    return config
