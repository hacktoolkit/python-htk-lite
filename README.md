# HTK Lite for Python

A set of convenience utils for Python requiring no external libs. Some of the best tricks from [`django-htk`](https://github.com/hacktoolkit/django-htk), without the bloat and Django dependency.


# Features

1. Debug via Slack using `slack_debug` and `slack_debug_json`. The best of `println` debugging, without the inconvenience of visually fishing for one message out of thousands of log lines.


# How To Use This Awesome?

1. Clone this repository into a directory named `htk` (preferred) or `htk_lite`  
    SSH: `git clone git@github.com:hacktoolkit/pyhtk-lite.git htk`  
    HTTPS: `git clone https://github.com/hacktoolkit/pyhtk-lite.git`
1. Create `local_settings.py` and add your [Slack incoming webhook](https://slack.com/apps/A0F7XDUAZ-incoming-webhooks) URL to `SLACK_WEBHOOK_URL`.
1. Example usage in Python Shell
    ```
    In [1]: from htk import slack_debug

    In [2]: from htk import slack_debug_json

    In [3]: slack_debug('This is seriously awesome!')
    Out[3]: <Response [200]>

    In [4]: slack_debug('Yeah, no kidding.')
    Out[4]: <Response [200]>

    In [5]: slack_debug_json({'A':1,'B':2,'C':3,'X':['foo','bar','baz'],'Z':{'nested_key':'nested_val
       ...: ue'}}),
    Out[5]: (None,)
    ```
1. Check your Slack to verify that the message was posted. If not, perhaps your token was wrong, or the Slack integration was disabled.
    ![image](https://user-images.githubusercontent.com/422501/61012949-7d29db00-a335-11e9-941f-6c0d851179e9.png)
1. Profit!

# Authors and Maintainers

[Hacktoolkit](https://github.com/hacktoolkit) and [Jonathan Tsai](https://github.com/jontsai)

# License

MIT. See `LICENSE.md`
