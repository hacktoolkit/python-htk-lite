# HTK Lite for Python

A set of convenience utils for Python requiring no external libs.


# Features

1. Debug via Slack using `slack_debug` and `slack_debug_json`. The best of `println` debugging, without the inconvenience of visually fishing for one message out of thousands of log lines.


# How To Use This Awesome?

1. Clone this repository into a directory named `htk` (preferred) or `htk_lite`  
    SSH: `git clone git@github.com:hacktoolkit/pyhtk-lite.git htk`  
    HTTPS: `git clone https://github.com/hacktoolkit/pyhtk-lite.git`
1. Create `local_settings.py` and add your [Slack incoming webhook](https://slack.com/apps/A0F7XDUAZ-incoming-webhooks) URL to `SLACK_WEBHOOK_URL`.
1. In your code do:
    ```
    from htk import slack_debug
    from htk import slack_debug_json

    slack_debug('This is a test!')
    ```
1. Check your Slack to verify that the message was posted. If not, perhaps your token was wrong, or the Slack integration was disabled.
1. Profit!

# Authors and Maintainers

[Hacktoolkit](https://github.com/hacktoolkit) and [Jonathan Tsai](https://github.com/jontsai)

# License

MIT. See `LICENSE.md`
