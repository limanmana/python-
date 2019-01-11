# 免费的天气接口 https://www.sojson.com/blog/305.html


import urllib.request
import json


url = 'http://t.weather.sojson.com/api/weather/city/101200901'
resp = urllib.request.urlopen(url)

if resp.code == 200:
    weather_json = resp.read().decode('utf-8')
    print(type(weather_json), weather_json)
    weather_data = json.loads(weather_json)
    data = weather_data['data']
    print('\n\n\n\n\n\n', data, '\n\n')
    today_humidity= data['shidu']
    # 昨天
    yesterday = data['yesterday']
    yesterday_high = yesterday['high']
    yesterday_low = yesterday['low']
    yesterday_type = yesterday['type']
    # 今天
    forecast_today = data['forecast']
    forecast_1 = forecast_today[0]
    forecast_high = forecast_1['high']
    forecast_low = forecast_1['low']
    forecast_type = forecast_1['type']
    # 明天
    forecast_tomorrow  = data['forecast']
    forecast_2 = forecast_tomorrow[1]
    tomorrow_high = forecast_2['high']
    tomorrow_low = forecast_2['low']
    tomorrow_type = forecast_2['type']
    # 后天
    forecast_houtian = data['forecast']
    forecast_3 = forecast_houtian[2]
    houtian_high = forecast_3['high']
    houtian_low = forecast_3['low']
    houtian_type = forecast_3['type']
    # 星期一
    forecast_mon = data['forecast']
    forecast_4 = forecast_mon[3]
    mon_high = forecast_4['high']
    mon_low = forecast_4['low']
    mon_type = forecast_4['type']
    # 星期二
    forecast_tue = data['forecast']
    forecast_5 = forecast_tue[4]
    tue_high = forecast_5['high']
    tue_low = forecast_5['low']
    tue_type = forecast_5['type']





    today_pm25 = data['pm25']
    today_temperature = data['wendu']
    print(f'昨天温度:{yesterday_high}~{yesterday_low}, 天气:{yesterday_type}')
    print(f'今天温度:{forecast_high}~{forecast_low}, 天气:{forecast_type}')
    print(f'明天温度:{tomorrow_high}~{tomorrow_low}, 天气:{tomorrow_type}')
    print(f'后天温度:{houtian_high}~{houtian_low}, 天气:{houtian_type}')
    print(f'星期一温度:{mon_high}~{mon_low}, 天气:{mon_type}')
    print(f'星期二温度:{tue_high}~{mon_low}, 天气:{tue_type}')
