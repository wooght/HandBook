# -- coding: utf-8 -
"""
@project    :HandBook
@file       :tmp_test.py
@Author     :wooght
@Date       :2024/9/18 16:02
@Content    :
"""
import re
request_form = '''{"tryRequest":"false","address":"河北省 保定市 涞水县 108国道 靠近东河山村 ","globalLbs":"{\"globalAreaCode\":\"510104\",\"globalCityCode\":\"510100\",\"globalLat\":\"30.633133\",\"globalLng\":\"104.110722\",\"globalProvinceCode\":\"510000\",\"globalTownCode\":\"510104030\"}","cityCode":"130600","provinceCode":"130000","utdid":"Zs7Pnkn0r40DAKSy/CBlF7cX","latitude":"39.633542","edition":"{\"actualLanguageCode\":\"zh-CN\",\"countryId\":\"CN\",\"countryNumCode\":\"156\",\"currencyCode\":\"CNY\"}","containerParams":"{\"recommend_multi_channel\":{\"baseCacheTime\":0,\"bizParams\":{\"currentExposureItemID\":\"\",\"currentRequestType\":\"pullRefresh\",\"deviceLevel\":\"m\",\"firstPagePVID\":\"442a30c4-c408-415d-8ca5-b92061f547ac\",\"guessChannelId\":\"pindao_0001\",\"hundredClickItemId\":\"\",\"isComplexTexture\":false,\"isNeedSubSelectionData\":false,\"isPullRefresh\":true,\"latestHundredItem\":\"819489454988,628848984810,720823469990,784985838634,739438886168,808926323503,668089936192,725495594327,739156501668,661990790349,795844175004,623226477792\",\"new2021UIEnable\":true,\"tb_homepage_clientCache_lbs\":{}},\"clientReqOffsetTime\":0,\"clientReqTime\":0,\"deltaCacheTime\":0,\"pageParams\":{\"firstRequestInAdvance\":-1,\"lastPage\":false,\"pageNum\":0,\"requestInAdvance\":10,\"virtualPageNum\":0},\"passParams\":{\"firstPagePVID\":\"442a30c4-c408-415d-8ca5-b92061f547ac\",\"lastVersion\":\"v7\"},\"realBaseCacheTime\":0,\"requestType\":\"pullRefresh\"}}","userId":"4060247732","nick":"tb793426967","areaCode":"130623","poiRefreshTime":"1726644520","cityName":"保定","areaName":"涞水县","countryCode":"CN","countryName":"中国","provinceName":"河北省","gatewayVersion":"2.0","longitude":"115.109334","commonBizParams":"{\"deviceInfo\":\"{\\\"deviceModel\\\":\\\"phone\\\"}\"}"}'''
request_form_no_slash = request_form.replace('\\', '')
request_form_code = '''data=%7B%22tryRequest%22%3A%22false%22%2C%22address%22%3A%22%E6%B2%B3%E5%8C%97%E7%9C%81+%E4%BF%9D%E5%AE%9A%E5%B8%82+%E6%B6%9E%E6%B0%B4%E5%8E%BF+108%E5%9B%BD%E9%81%93+%E9%9D%A0%E8%BF%91%E4%B8%9C%E6%B2%B3%E5%B1%B1%E6%9D%91+%22%2C%22globalLbs%22%3A%22%7B%5C%22globalAreaCode%5C%22%3A%5C%22510104%5C%22%2C%5C%22globalCityCode%5C%22%3A%5C%22510100%5C%22%2C%5C%22globalLat%5C%22%3A%5C%2230.633133%5C%22%2C%5C%22globalLng%5C%22%3A%5C%22104.110722%5C%22%2C%5C%22globalProvinceCode%5C%22%3A%5C%22510000%5C%22%2C%5C%22globalTownCode%5C%22%3A%5C%22510104030%5C%22%7D%22%2C%22cityCode%22%3A%22130600%22%2C%22provinceCode%22%3A%22130000%22%2C%22utdid%22%3A%22Zs7Pnkn0r40DAKSy%2FCBlF7cX%22%2C%22latitude%22%3A%2239.633542%22%2C%22edition%22%3A%22%7B%5C%22actualLanguageCode%5C%22%3A%5C%22zh-CN%5C%22%2C%5C%22countryId%5C%22%3A%5C%22CN%5C%22%2C%5C%22countryNumCode%5C%22%3A%5C%22156%5C%22%2C%5C%22currencyCode%5C%22%3A%5C%22CNY%5C%22%7D%22%2C%22containerParams%22%3A%22%7B%5C%22recommend_multi_channel%5C%22%3A%7B%5C%22baseCacheTime%5C%22%3A0%2C%5C%22bizParams%5C%22%3A%7B%5C%22currentExposureItemID%5C%22%3A%5C%22%5C%22%2C%5C%22currentRequestType%5C%22%3A%5C%22pullRefresh%5C%22%2C%5C%22deviceLevel%5C%22%3A%5C%22m%5C%22%2C%5C%22firstPagePVID%5C%22%3A%5C%22442a30c4-c408-415d-8ca5-b92061f547ac%5C%22%2C%5C%22guessChannelId%5C%22%3A%5C%22pindao_0001%5C%22%2C%5C%22hundredClickItemId%5C%22%3A%5C%22%5C%22%2C%5C%22isComplexTexture%5C%22%3Afalse%2C%5C%22isNeedSubSelectionData%5C%22%3Afalse%2C%5C%22isPullRefresh%5C%22%3Atrue%2C%5C%22latestHundredItem%5C%22%3A%5C%22819489454988%2C628848984810%2C720823469990%2C784985838634%2C739438886168%2C808926323503%2C668089936192%2C725495594327%2C739156501668%2C661990790349%2C795844175004%2C623226477792%5C%22%2C%5C%22new2021UIEnable%5C%22%3Atrue%2C%5C%22tb_homepage_clientCache_lbs%5C%22%3A%7B%7D%7D%2C%5C%22clientReqOffsetTime%5C%22%3A0%2C%5C%22clientReqTime%5C%22%3A0%2C%5C%22deltaCacheTime%5C%22%3A0%2C%5C%22pageParams%5C%22%3A%7B%5C%22firstRequestInAdvance%5C%22%3A-1%2C%5C%22lastPage%5C%22%3Afalse%2C%5C%22pageNum%5C%22%3A0%2C%5C%22requestInAdvance%5C%22%3A10%2C%5C%22virtualPageNum%5C%22%3A0%7D%2C%5C%22passParams%5C%22%3A%7B%5C%22firstPagePVID%5C%22%3A%5C%22442a30c4-c408-415d-8ca5-b92061f547ac%5C%22%2C%5C%22lastVersion%5C%22%3A%5C%22v7%5C%22%7D%2C%5C%22realBaseCacheTime%5C%22%3A0%2C%5C%22requestType%5C%22%3A%5C%22pullRefresh%5C%22%7D%7D%22%2C%22userId%22%3A%224060247732%22%2C%22nick%22%3A%22tb793426967%22%2C%22areaCode%22%3A%22130623%22%2C%22poiRefreshTime%22%3A%221726644520%22%2C%22cityName%22%3A%22%E4%BF%9D%E5%AE%9A%22%2C%22areaName%22%3A%22%E6%B6%9E%E6%B0%B4%E5%8E%BF%22%2C%22countryCode%22%3A%22CN%22%2C%22countryName%22%3A%22%E4%B8%AD%E5%9B%BD%22%2C%22provinceName%22%3A%22%E6%B2%B3%E5%8C%97%E7%9C%81%22%2C%22gatewayVersion%22%3A%222.0%22%2C%22longitude%22%3A%22115.109334%22%2C%22commonBizParams%22%3A%22%7B%5C%22deviceInfo%5C%22%3A%5C%22%7B%5C%5C%5C%22deviceModel%5C%5C%5C%22%3A%5C%5C%5C%22phone%5C%5C%5C%22%7D%5C%22%7D%22%7D'''

print(request_form_no_slash)
print(len(request_form))
print(len(request_form_no_slash))
print(len(request_form_code))


ord_list = {'{':'%7B', '}':'%7D', '"':'%22', ':':'%3A', ',':'%2C', '\\':'%5C', '/':'%2F', '=':'%3D', '+':'%2B'}
def to_up(s):
    v = s.group()
    return v.upper()
def zh_to_ascii(s):
    """
        中文转换为淘宝地址中的 ASCII
    """
    bytes_diannao = s.encode('utf-8')
    ascii_str = str(bytes_diannao).replace('\\x', '%')
    ascii_str = ascii_str.replace('\\\\', '\\')
    ascii_str = ascii_str.replace('b', '', 1)
    ascii_str = ascii_str.replace("'", '')
    for k, v in ord_list.items():
        ascii_str = ascii_str.replace(k, v)
    ascii_str = re.sub(r'%([^%]{2})', to_up, ascii_str)
    return ascii_str

print(zh_to_ascii('=/+'))

for k, c in ord_list.items():
    print(hex(ord(k)))