"""
    @author: common
    @describe: 公共函数文件
    @date: 2020/3/20
"""
import time



def datetime_to_unixtime(dtime):
    """
    将datetime转换为unix时间戳
    create by: yu bin
    :param dtime: datetime
    :return: Unix时间戳的str表示
    """
    ans_time = time.mktime(dtime.timetuple())
    return str(ans_time)