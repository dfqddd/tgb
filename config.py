# 配置文件：config.py

# 基础URL模板（使用格式化占位符）
BASE_URL_TEMPLATE = "https://www.tgb.cn/user/blog/moreReplyMod?time={time}&userID={user_id}&pageNo={page}"

# 请求头配置
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    'Referer': 'https://www.tgb.cn/user/blog/',
}

# Cookie 配置
COOKIES_STR = "acw_tc=0a09669617434252426165392e87c16a3c8dfc2d07ec1b140c6faa7931df67; JSESSIONID=NDA3NWQwNTctNGZhYS00ODE1LTg5MTMtYzA5MmQ1ZDQ2NzY1; gdp_user_id=gioenc-8g0106c8%2C8c72%2C538d%2Ca6a0%2Cd7c91g2571bb; 893eedf422617c96_gdp_session_id=a1601808-d3c8-41c1-8909-1357be7fd9b0; tgbuser=8896779; tgbpwd=d4a3ead9770a13114f85d86b6215cdac99f0450787fe384512fa4e453996b39bs1q3p7pxwaz33th; loginStatus=phone; 893eedf422617c96_gdp_gio_id=gioenc-9987668; 893eedf422617c96_gdp_cs1=gioenc-9987668; Hm_lvt_cc6a63a887a7d811c92b7cc41c441837=1743425279; Hm_lpvt_cc6a63a887a7d811c92b7cc41c441837=1743425279; HMACCOUNT=A4C037CFB47B69AF; creatorStatus8896779=true; wsStatus=true; showStatus8896779=true; tfstk=gCMSCbfPu2Hqqq_mqUK4cVlAL72IF29NRMZKjDBPv8eRJwnTu9uytDUIOr3qaaloYk6Iqr0Qt34UJygEvb-2QdooqJ2LdFJwQKpWAa0Q2uERkHELYuK4w0kzUqep7FJql4-AHJ3rb-wBGmU0AwULp2QYHl4Y26F-JrFYXl78pJ3pc-EuA6C8y_QYMkUYJJeKJmKbxf0D9k17P0t8kW58RIYiVr6dpxZv-Pn7boqqhyP8WSUfpkMbV7atVYzyWHrI6ANoWE5zyfGi5luyHTgs24GT6YQvlJmq12ZsehC_R4mxUSHJY1q0KbhTevT1ymuSrYct2E5bcjnrhSk959NoM4cgOv82I8lZbvVteL_gu5qI58hXkTgO4FWa5Wn5OiNGdoawcn1ht9i4QJXbbZW8woqSqntfPWV8motWcn1ht7E00QKXcaNh.; 893eedf422617c96_gdp_sequence_ids=%7B%22globalKey%22%3A3%2C%22PAGE%22%3A3%7D; 893eedf422617c96_gdp_session_id_a1601808-d3c8-41c1-8909-1357be7fd9b0=true"

COOKIES_DICT = {}
for item in COOKIES_STR.split(';'):
    key, value = item.strip().split('=')
    COOKIES_DICT[key] = value

COOKIES = COOKIES_DICT

# 去抓一下淘股吧不同人对应的userId 放到这里
USER_IDS = [8934153]  # 将 USER_ID 改为 USER_IDS 列表
TIME_PARAM = "2025-03-30"

# 分页配置（独立配置块）这里需要手动去抓 tgb没做区分
PAGINATION = {
    "start_page": 1,
    "end_page": 6
}

# 网络请求配置
TIMEOUT = 10
SLEEP_SECONDS = 1  # 请求间隔时间

# 文件存储配置
ENCODING = 'utf-8'
