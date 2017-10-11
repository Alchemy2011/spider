# coding:utf8
import urllib2
# 这个脚本，没有实现自动化，因为是手动登录，手动获取的cookie。
# 而且cookie每次登录后都需要这样操作，没有实现自动化。
# 利用模拟登录已经实现了获取cookie的功能，所以没必要再细看了。

url = 'http://example.webscraping.com/places/default/index'
headers = {
    "Host": 'example.webscraping.com',
    "Proxy-Connection": 'keep-alive',
    # "Upgrade-Insecure-Requests": '1',
    "User-Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    "Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    "Referer": 'http://example.webscraping.com/places/default/view/Afghanistan-1',
    # "Accept-Encoding": 'gzip, deflate',
    "Accept-Language": 'zh-CN,zh;q=0.8',
    "Cookie": 'session_data_places="8a2f6af6d0e87e70d36e048d3df046c2:sZzWJZobUQUF8in_E-3XLdPQt1bxVQ0WOW8E7Vj-v5DONazovc3oZpMgWHSiVTHR9fApGdGV_A-5eN4usxeWUEbAQG594WY_H-IEvxhs3cCASETZml7D-_S5iynd0qaTDXProsLHwZpph2vdI8_gUUr__zkIYIyREfOzZyu5y9_v6yGQLP-KZ5YskpLX2EcK5OzkXtv8qkh6hGr0j-SEQHJG4TKkOwcnlU8Ys2npbK6ws58wb-PHeh5oaqPit3J0vl03QerNZWsUfFbuHkRnqHHuY8nY-M3XWQawCryZ3BiMuV5V3TB8Iu9_FbgyM6FCXWSYmuOAuSb6W-HLvN0-US8qCMwaV4plxkdHFiTC4-AW3qjZlZnw_462chTjj0uj9X1cb-xjBg7HqP5QqSEe4DZfjvkTiSVvYIk9QoqaM4b694MOsCbwko5noG6hi5paQgfvhD4IAECWmgRHwsySU6rgJQZxb1JvThV6X9xKytgEuPjZ19ixnOtlE0xH8hsn6foUpd-i_NTmTPXxHtO3UVMc29VevTm-6kl2nxDTpK3PWXFSU-EKGqAKT-ITMnnkIdT7bCmd6-me8JGlXm3lmmcznRF1vYhmzQuyWafRvw93THvrOK9vDgn-BWGvEreW76uLlRz0Q8fW-JkYW1gGDHic4GkXAV0mp7LdcvMDQbc1DklZqzoQicyF9WPl07CJkL_VM--wZiVFRoXWFGEYIk_ZHRsVOvkJdEmxNPxllf66iEzEao42xCv9M86AqRNhf_CbIVgbCgL4lJ6r_gkcnNCuts-Wc6t93njbJjoOTXffi-Q_ZwoGQ4RZ2LlHtCRgcOCumOQcX9hP5BCtBDCXFQhMaWANypJOlhuIKe2inviznRFhYM460BBdAD_lk70utKUMT1FY1U7kz4Hm5kPRww=="; session_id_places=True',
}

request = urllib2.Request(url, headers=headers)
response = urllib2.urlopen(request)
print response.read()