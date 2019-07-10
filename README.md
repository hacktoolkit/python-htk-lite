# HTK Lite for Python

A set of convenience utils for Python requiring no external libs.


# Features

1. Debug via Slack using `slack_debug` and `slack_debug_json`


# How To Use This Awesome?

1. Clone this repository
1. Create `local_settings.py` and add your Slack incoming webhook url to `SLACK_WEBHOOK_URL`.
1. In your code do:
    ```
    from htk_lite import slack_debug
    from htk_lite import slack_debug_json

    slack_debug('This is a test!')
    ```
1. Check your Slack that the message was posted.
1. Now, you no longer have to watch lines scroll by in a terminal!

# Authors and Maintainers

[Hacktoolkit](https://github.com/hacktoolkit) and [Jonathan Tsai](https://github.com/jontsai)

# License

MIT. See `LICENSE.md`
