import urllib.request
import json
import sqlite3

url = 'http://t.weather.sojson.com/api/weather/city/101160301'
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
    ymd_1 = data['yesterday']
    ymd_yesterday = ymd_1['ymd']
    yesterday_high = yesterday['high']
    yesterday_low = yesterday['low']
    yesterday_type = yesterday['type']
    # 今天
    forecast_today = data['forecast']
    forecast_1 = forecast_today[0]
    ymd_forecast = forecast_1['ymd']
    forecast_high = forecast_1['high']
    forecast_low = forecast_1['low']
    forecast_type = forecast_1['type']
    # 明天
    forecast_tomorrow  = data['forecast']
    forecast_2 = forecast_tomorrow[1]
    ymd_tomorrow = forecast_2['ymd']
    tomorrow_high = forecast_2['high']
    tomorrow_low = forecast_2['low']
    tomorrow_type = forecast_2['type']
    # 后天
    forecast_houtian = data['forecast']
    forecast_3 = forecast_houtian[2]
    ymd_houtian = forecast_3['ymd']
    houtian_high = forecast_3['high']
    houtian_low = forecast_3['low']
    houtian_type = forecast_3['type']
    # 星期一
    forecast_mon = data['forecast']
    forecast_4 = forecast_mon[3]
    ymd_mon = forecast_4['ymd']
    mon_high = forecast_4['high']
    mon_low = forecast_4['low']
    mon_type = forecast_4['type']
    # 星期二
    forecast_tue = data['forecast']
    forecast_5 = forecast_tue[4]
    ymd_tue = forecast_5['ymd']
    tue_high = forecast_5['high']
    tue_low = forecast_5['low']
    tue_type = forecast_5['type']
    print(f'{ymd_yesterday}:{yesterday_high}~{yesterday_low}, 天气:{yesterday_type}')
    print(f'{ymd_forecast}:{forecast_high}~{forecast_low}, 天气:{forecast_type}')
    print(f'{ymd_tomorrow}:{tomorrow_high}~{tomorrow_low}, 天气:{tomorrow_type}')
    print(f'{ymd_houtian}:{houtian_high}~{houtian_low}, 天气:{houtian_type}')
    print(f'{ymd_mon}:{mon_high}~{mon_low}, 天气:{mon_type}')
    print(f'{ymd_tue}:{tue_high}~{mon_low}, 天气:{tue_type}')
    connect = sqlite3.connect("weather.db")
    cursor = connect.cursor()
    # 添加天气信息
    # connect.execute("insert into weather(riqi, gaowen, diwen, tianqi) values(?,?,?,?)",(ymd_yesterday, yesterday_high, yesterday_low, yesterday_type))
    # connect.execute("insert into weather(riqi, gaowen, diwen, tianqi) values(?,?,?,?)",
    #                 (ymd_forecast, forecast_high, forecast_low, forecast_type))
    # connect.execute("insert into weather(riqi, gaowen, diwen, tianqi) values(?,?,?,?)",
    #                 (ymd_tomorrow, tomorrow_high, tomorrow_low, tomorrow_type))
    # connect.execute("insert into weather(riqi, gaowen, diwen, tianqi) values(?,?,?,?)",
    #                 (ymd_houtian, houtian_high, houtian_low, houtian_type))
    # connect.execute("insert into weather(riqi, gaowen, diwen, tianqi) values(?,?,?,?)",
    #                 (ymd_mon, mon_high, mon_low, mon_type))
    # connect.execute("insert into weather(riqi, gaowen, diwen, tianqi) values(?,?,?,?)",
    #                 (ymd_tue, tue_high, tue_low, tue_type))

    # 更新天气信息
    cursor.execute("update weather set riqi=?,gaowen=?,diwen=?,tianqi=? where id=1",(ymd_yesterday, yesterday_high, yesterday_low, yesterday_type))
    cursor.execute("update weather set riqi=?,gaowen=?,diwen=?,tianqi=? where id=2",
                   (ymd_forecast, forecast_high, forecast_low, forecast_type))
    cursor.execute("update weather set riqi=?,gaowen=?,diwen=?,tianqi=? where id=3",
                   (ymd_tomorrow, tomorrow_high, tomorrow_low, tomorrow_type))
    cursor.execute("update weather set riqi=?,gaowen=?,diwen=?,tianqi=? where id=4",
                   (ymd_houtian, houtian_high, houtian_low, houtian_type))
    cursor.execute("update weather set riqi=?,gaowen=?,diwen=?,tianqi=? where id=5",
                   (ymd_mon, mon_high, mon_low, mon_type))
    cursor.execute("update weather set riqi=?,gaowen=?,diwen=?,tianqi=? where id=6",
                   (ymd_tue, tue_high, tue_low, tue_type))




    print('成功')
    cursor.close()
    connect.commit()
    connect.close()



