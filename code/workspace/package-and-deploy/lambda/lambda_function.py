from datetime import datetime

from pytz import timezone, utc


def handler(event, context):
    payload = event["time_zone"]
    message = f"Current date/time in TimeZone *{payload}* is: {_timezone(payload)}"

    return {"message": message}


def _timezone(time_zone):
    utc_now = utc.localize(datetime.utcnow())
    compare_to_utc = utc_now.astimezone(timezone(time_zone))

    return compare_to_utc.strftime("%Y-%m-%d %H:%M")
