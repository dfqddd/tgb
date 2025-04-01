# 配置文件：config.py

# 基础URL模板（使用格式化占位符）
BASE_URL_TEMPLATE = "https://www.tgb.cn/user/blog/moreReplyMod?time={time}&userID={user_id}&pageNo={page}"

# 请求头配置
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    'Referer': 'https://www.tgb.cn/user/blog/',
}

# Cookie 配置
COOKIES_STR = "gdp_user_id=gioenc-58a096d5%2C1786%2C537e%2C991g%2Cdd9cbe4ebg82; Hm_lvt_cc6a63a887a7d811c92b7cc41c441837=1743255942; HMACCOUNT=365CEF6FF7B24572; agree=enter; creatorStatus8896779=true; loginStatus=account; tgbuser=8896779; tgbpwd=d4a3ead9770a13114f85d86b6215cdac99f0450787fe384512fa4e453996b39bs1q3p7pxwaz33th; 893eedf422617c96_gdp_gio_id=gioenc-9987668; 893eedf422617c96_gdp_cs1=gioenc-9987668; dvNgbOperaTime=1743420640184; 893eedf422617c96_gdp_sequence_ids=%7B%22globalKey%22%3A81%2C%22VISIT%22%3A10%2C%22PAGE%22%3A56%2C%22CUSTOM%22%3A17%7D; Hm_lpvt_cc6a63a887a7d811c92b7cc41c441837=1743424898; tfstk=gh-ZjG97eiAIVGxZi9j48ggqaqIOmGc5nn1fnKvcC1fgflND8Ld-HZc9hBSVttaGiEsxpwK6MraGjl43-tBcnl4i_W4hUtfcn14gBedWEltsWiZVXiImNbiSVApODiX944nA6pvdnv6GTsRt8iImNXOEbvARDQpWJtOMKvWfQtVDiNf3tOChIrqDi6bhETNGmiAmL6Xces4cnZbnxO1hiijDipDFHfPG8aoFENDqrMduOu4TWspGToqDxmQNad4bmoxFQN-DI67VuHWN7_7LfOkH4LvM2t-xEr52eFA1pIorTMxw_hbF0mrdfL8H_w8Zgk7p-LKc8ehzyLpM_UbkjDkC8hp5j6-xHoCM5Kxfuhcuh1x91H7JD5lCGU9BjwRoOkRAuFYljnlrxgk0M90DvnLair7Gp95SLvWslsQ1ILyWZrUA-I6FNApTkrQii95SLvzYkNnVL_M9B"

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
