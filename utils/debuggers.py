from __future__ import absolute_import

# Python Standard Library Imports
import json

# Third Party / PIP Imports
import requests

# HTKLite Imports
from ..encoders import DecimalEncoder
from ..settings import SLACK_WEBHOOK_URL


def slack_debug(text):
    payload = {
        'text' : text,
    }
    response = requests.post(
        SLACK_WEBHOOK_URL,
        json=payload
    )
    return response


def slack_debug_json(obj, label='JSON'):
    slack_debug(
        '%s: ```%s```' % (
            label,
            json.dumps(obj, indent=2, cls=DecimalEncoder),
        )
    )


__all__ = [
    'slack_debug',
    'slack_debug_json',
]
