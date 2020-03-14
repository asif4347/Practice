import time

# YYYY-DD-MM HH:MM:SS	2020-02-03 02:40:45
epoch = '1490157520.05'
t = time.strftime("%Y-%d-%m %H:%M:%S", time.localtime(float(epoch)))
# print(t)
validated_data = {
    'timestamp': '1583121333'
}

# updated_on = time.strftime("%Y-%d-%m %H:%M:%S", time.localtime(float(validated_data['timestamp'])))
# print(updated_on)
# t = time.localtime(float(validated_data['timestamp']))
# print(t)
# # utc = pytz.UTC
# # print(utc.localize(t))


from datetime import datetime, timezone
import pytz
from datetime import datetime, timedelta
from datetime import timezone as time_timezone

# updated_on = str(pytz.UTC.localize(datetime.fromtimestamp(float(validated_data['timestamp']))))
# print(updated_on)
#
# updated_on = str(
#     (datetime.strptime(validated_data['timestamp'], '%Y-%m-%d %H:%M:%S').replace(tzinfo=timezone.utc) - timedelta(
#         hours=1)).timestamp())
#
# print(updated_on)
utc_datetime = datetime.fromtimestamp(float(validated_data['timestamp'])).replace(tzinfo=timezone.utc) - timedelta(
    hours=1)
# utc_epoch = str(datetime.strptime(utc_datetime, '%Y-%m-%d %H:%M:%S').replace(tzinfo=timezone.utc) - timedelta(
#     hours=1))
print(str(utc_datetime))
#
# def validate_epoch_timestamp(self, value):
#     try:
#         utc_datetime = datetime.fromtimestamp(float(value))
#         utc_epoch = (utc_datetime.replace(tzinfo=timezone.utc) - timedelta(hours=tdelta)).timestamp()
#         return str(utc_epoch)
#     except Exception as e:
#         raise serializers.ValidationError(f'{value}:{e}')
#
#
# print(validate_epoch_timestamp(validated_data['timestamp']))
