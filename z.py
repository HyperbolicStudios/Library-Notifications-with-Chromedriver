import time
import datetime

from datetime import datetime
from pytz import timezone
import pytz


date_format='%m/%d/%Y %H:%M:%S %Z'
date = datetime.now(tz=pytz.utc)
date = date.astimezone(timezone('US/Pacific'))
date  = (date.strftime(date_format))

print(date)
