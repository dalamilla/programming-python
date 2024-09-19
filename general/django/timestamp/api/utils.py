from datetime import datetime, timezone


def parsing_date(str_date: str):

    for valid_fmt in ("%Y-%m-%d", "%d %B %Y", "%d %B %Y, %Z"):
        try:
            pars_date = datetime.strptime(str_date, valid_fmt)
            return pars_date.replace(tzinfo=timezone.utc)
        except ValueError:
            pass

    raise ValueError("invalid date format")
