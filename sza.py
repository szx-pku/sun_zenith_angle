import numpy as np
import datetime

def cal_sza(date, time, lat, lon):
    """
    this function calculate the sun zenith angle for a given situation at a specific time
    :param date: the date of the observation, in class "datetime.date"
    :param time: the UTC time of the observation, in class "datetime.time"
    :param lat: the latitude of the location, positive for north
    :param lon: the longitude of the location, positive for east
    :return: the cosine of the sun zenith angle
    """

    # 计算太阳赤纬
    date1 = date
    date2 = datetime.date(2000, 1, 1)
    N = (date1 - date2).days
    print(N)
    b = 2 * np.pi * (N - 1) / 365.25
    delta = 0.006918 - 0.399912 * np.cos(b) + 0.070257 * np.sin(b) - 0.006758 * np.cos(2*b) + 0.000907 * np.sin(2*b) - 0.002697 * np.cos(3*b) + 0.00148 * np.sin(3*b)
    print(delta)
    # 计算时角
    true_time = time.hour + time.minute / 60 + time.second / 3600 + lon / 15   #真太阳时，以小时为单位
    t = (true_time - 12) * 15

    # calulate the cosine of sza
    result = np.sin(lat * np.pi / 180) * np.sin(delta) + np.cos(lat * np.pi / 180) * np.cos(delta) * np.cos(t * np.pi / 180)
    return result