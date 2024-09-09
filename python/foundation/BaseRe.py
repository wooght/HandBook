# -- coding: utf-8 -
"""
@project    :HandBook
@file       :BaseRe.py
@Author     :wooght
@Date       :2024/5/14 16:40
@Content    : 正则表达式
"""

import re

'''
基本字符
    .   可以代替除换行符(\n)以外的任何一个字符
    *   前面的子表达式,字符可以出现0到无限次
    ?   前面的子表达式,字符可以出现0到1次  
    \   特殊字符变成普通字符
    \d  一个数字
    \D  数字以外的所有字符
    ()  子表达式及一个分组,可以提出来
    \w  单词字符 [a-zA-Z0-9_] 包含下划线,但是不包含-
    \s  空白字符,空格,换行符
    \S  非空白字符
    +   前面的子表达式,字符可以出现1次到无限次
    {m} 匹配前一个字符串m次
    {m,n}   匹配前一个字符串m到n次
    ^   匹配模式在字符串开头
    $   匹配模式在字符串末尾
    [^] 否定  [^a-z] 否定小写字母
    
    *? +? ?? {}? 表示非贪婪模式
    
    正则表达式前要加 r
    r'表达式'
'''

"""
    match(pattern, string, flag=0)
    只从字符串的最开始与pattern匹配,匹配成功返回匹配对象(只有一个结果), 否则返回None
"""
s1 = 'abcdef-g123456'
s2 = '.abcw79237'
pattern = re.compile(r"\w+")        # compile 可以不用,只是速度会慢一点
result1 = re.match(pattern, s1)
print(result1.group())              # abcdef 只有一个结果,group(1)会报错
result2 = re.match(pattern, s2)
print(type(result2).__name__)       # NoneType 从第一个位置开始匹配,第一个位置不匹配,则返回None
result11 = re.match(r"\w+", s1)
print(result11.group())             # abcdef
print(result11.span())              # (0, 6) 开始,结束的位置

"""
    search(pattern, string, flag=0)
    方式和match一样,但不一定从第一个位置开始匹配,而是从任意位置开始匹配,只匹配一次,不匹配则返回None
"""
result22 = re.search(r"\w+", s2)
print(result22.group())        # abcw79237

"""
    findall(pattern, string)
    匹配所有,返回一个列表
"""
s3 = 'abc-123-a123'
result3 = re.findall(r'\w+', s3)
print(result3)                  # ['abc', '123', 'a123']
print(result3.count('abc'))     # 1 list.count(s) s在列表中出现的次数

"""
    group()     返回一个匹配项
    groups()    返回包含所有匹配的元祖
"""
s4 = 'wooght@126.com'
result4 = re.search(r'(\w+)@(\w+)\.(\w+)', s4)
print(result4.groups())         # ('wooght', '126', 'com')
result44 = re.search(r'(\w)+@(\w)+\.(\w+)', s4)
print(result44.groups())        # ('t', '6', 'com')
# (\w)+ 表示括号里面的字符可以出现1到无数次,但是必须是一样的字符
# (\w) 表示括号里面只有一个字符

"""
    re 模块的属性    flag
    re.I    匹配不分大小写
    re.S    表示.可以匹配全部字符,包括换行符
"""
s5 = '''one
two
three
'''
result5 = re.match(r'.*', s5, re.S)
print(result5.group())
# one
# two
# three
result55 = re.match(r'.*', s5)
print(result55.group())             # one

html = '''
<html>
    <head>
        <title>网页</title>
    </head>
    <body>
        <div class='one'>
            <p>这里是一个段落</p>
            <img src="abc/abc.jpg" />
        </div>
    </body>
</html>
'''
rhtml1 = re.search(r'<img src=\"(.*)\"', html)
print(rhtml1.group(0))      # <img src="abc/abc.jpg"
print(rhtml1.group(1))      # abc/abc.jpg
# group(0) 表示匹配表达式本身 1表示()

"""
    sub(pattern, repl, string, count=0, flag=0)
    替换  repl 可以是字符串,也可以是有返回值的函数
"""
rhtml2 = re.sub(r'<.*?>', '', html)     # 替换掉网页代码
rhtml2 = re.sub(r'\s', '', rhtml2)      # 替换掉空格和换行符
print(rhtml2)       # 网页这里是一个段落

ii = 0
def abc(mm):
    global ii
    ii += 1
    v = int(mm.group())
    if (v % 2 == 0):
        return str(v / 2)
    return str(v * 2)
s6 = 'A23BB34CCC56'
print(re.sub(r'(\d+)', abc, s6))  # sub 第二个参数是函数的情况
print('共匹配{}次'.format(ii))

result6 = re.sub(r'(\d+)[^\d]+(\d+)', r'\2 \1', s6)
print(result6)              # A34 23CCC56       反向替换

"""
    在网页中的应用
    查找地址
    查找IP
    查找特定值
"""
ip89result = '''
<a href="https://proxy.ip3366.net/" target="_blank" data-type="img"><img src="img/hfad.png"></a><br><script type="text/javascript" src="js/jquery.min.js"></script>
<div id="adarea"onclick=location.href='https://proxy.ip3366.net/' style="cursor: pointer;display: none;position: fixed;right:15px;bottom:15px;width: 285px;height: 250px;background: url(/img/fkad.png) no-repeat;">
<div id="adclose" style="cursor: pointer; position: absolute;  top: 0px;  left: 0px;  display: block;  width: 20px;  height: 20px;font-family: cursive;background: url(img/close.png) no-repeat;" title="点击关闭"> </div>
</div>
<script type="text/javascript">
$(function(){
$('#adarea').slideDown(500);
$('#adclose').click(function(){
$('#adarea').slideUp(500);
});
});
</script>
223.85.12.114:2222<br>182.131.17.19:80<br>112.53.184.170:9091<br>171.221.210.114:80<br>更好用的代理ip请访问：https://proxy.ip3366.net/
'''

href = re.findall(r'(https://[^/]*/)', ip89result)                  # 获取所有网址
print(href)     # ['https://proxy.ip3366.net/', 'https://proxy.ip3366.net/', 'https://proxy.ip3366.net/']
ips = re.findall(r'(\d{3}(\.\d{2,3}){3}:\d{2,5})', ip89result)      # 获取所有IP地址
print(ips)
# [('223.85.12.114:2222', '.114'), ('182.131.17.19:80', '.19'), ('112.53.184.170:9091', '.170'), ('171.221.210.114:80', '.114')]
slide = re.findall(r'slide\w+\((\d+)\)', ip89result)
print(slide)            # ['500', '500']

amazon_span = "<div data-asin='B0CFTYRVL5' data-index='25' data-uuid='fbaf624b-0574-4e5e-9d0f-255eaf221187' data-component-type='s-search-result' class='sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20 gsx-ies-anchor'><div class='sg-col-inner'><div cel_widget_id='MAIN-SEARCH_RESULTS-25' class='s-widget-container s-spacing-small s-widget-container-height-small celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_94'><span class='a-declarative' data-version-id='v1nyb4igz33igf2j9heq96r9jtz' data-render-id='r5219jlj3ih9i2ne0gf0g0d5md' data-action='puis-card-container-declarative' data-csa-c-func-deps='aui-da-puis-card-container-declarative' data-csa-c-item-id='amzn1.asin.B0CFTYRVL5' data-csa-c-posx='22' data-csa-c-type='item' data-csa-c-owner='puis'><div class='puis-card-container s-card-container s-overflow-hidden aok-relative puis-expand-height puis-include-content-margin puis puis-v1nyb4igz33igf2j9heq96r9jtz s-latency-cf-section puis-card-border'><div class='a-section a-spacing-base'><div class='s-product-image-container aok-relative s-text-center s-image-overlay-grey puis-image-overlay-grey s-padding-left-small s-padding-right-small puis-spacing-small s-height-equalized puis puis-v1nyb4igz33igf2j9heq96r9jtz'><span data-component-type='s-product-image' class='rush-component' data-version-id='v1nyb4igz33igf2j9heq96r9jtz' data-render-id='r5219jlj3ih9i2ne0gf0g0d5md'><a class='a-link-normal s-no-outline' tabindex='-1' href='/-/zh/dp/B0CFTYRVL5/ref=sr_1_94?dib=eyJ2IjoiMSJ9.RhlytuBRpsRlwN1seBb478b5FPc0s4dy3fpueiwGo5vg6v3hhz8rcRqij04zcwq382jPnBdVS14ozX0U7DH2G_6vehocwQ53D5locIJi96iZM9-z_VTkDodijX3aYlwr9AzX8NCWBvMaWafZ8xJ1w8ES3wY0iAbA4rPapMBPY2A7A3GA0L7fI-286qml2KM_c5fPX4tr4-mDcIsRGOudMZUkk1OMNu2euDN99s0-EvJVgoWfROXeg6zcGB8fUpoqOSFknYUCIE1_U4psQlTaE3pfCPDwPExRfem5E7jI5hA.jOcdWw1bjIjiI5J0xsxqw5LNlXJtimF_0nYvL4bIZog&amp;dib_tag=se&amp;qid=1722008664&amp;s=computers-intl-ship&amp;sr=1-94'><div class='a-section aok-relative s-image-square-aspect'><img class='s-image' src='https://m.media-amazon.com/images/I/71AnOk+M6HL._AC_UL320_.jpg' srcset='https://m.media-amazon.com/images/I/71AnOk+M6HL._AC_UL320_.jpg 1x, https://m.media-amazon.com/images/I/71AnOk+M6HL._AC_UL480_QL65_.jpg 1.5x, https://m.media-amazon.com/images/I/71AnOk+M6HL._AC_UL640_QL65_.jpg 2x, https://m.media-amazon.com/images/I/71AnOk+M6HL._AC_UL800_QL65_.jpg 2.5x, https://m.media-amazon.com/images/I/71AnOk+M6HL._AC_UL960_QL65_.jpg 3x' alt='2024 升级版儿童平板电脑,10 英寸 Android 13 平板电脑,带保护套,八核,谷歌儿童空间,家长控制,4GB+64GB,Wifi,BT5.3,YouTube,送给幼儿的绝佳礼物 ler(蓝色) ler(蓝色 )' data-image-index='94' data-image-load='' data-image-latency='s-product-image' data-image-source-density='1'/></div></a></span></div><div class='a-section a-spacing-small puis-padding-left-small puis-padding-right-small'><div data-cy='title-recipe' class='a-section a-spacing-none a-spacing-top-small s-title-instructions-style'><h2 class='a-size-mini a-spacing-none a-color-base s-line-clamp-4'><a class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal' href='/-/zh/dp/B0CFTYRVL5/ref=sr_1_94?dib=eyJ2IjoiMSJ9.RhlytuBRpsRlwN1seBb478b5FPc0s4dy3fpueiwGo5vg6v3hhz8rcRqij04zcwq382jPnBdVS14ozX0U7DH2G_6vehocwQ53D5locIJi96iZM9-z_VTkDodijX3aYlwr9AzX8NCWBvMaWafZ8xJ1w8ES3wY0iAbA4rPapMBPY2A7A3GA0L7fI-286qml2KM_c5fPX4tr4-mDcIsRGOudMZUkk1OMNu2euDN99s0-EvJVgoWfROXeg6zcGB8fUpoqOSFknYUCIE1_U4psQlTaE3pfCPDwPExRfem5E7jI5hA.jOcdWw1bjIjiI5J0xsxqw5LNlXJtimF_0nYvL4bIZog&amp;dib_tag=se&amp;qid=1722008664&amp;s=computers-intl-ship&amp;sr=1-94'><span class='a-size-base-plus a-color-base a-text-normal'>2024 升级版儿童平板电脑,10 英寸 Android 13 平板电脑,带保护套,八核,谷歌儿童空间,家长控制,4GB+64GB,Wifi,BT5.3,YouTube,送给幼儿的绝佳礼物 ler(蓝色) ler(蓝色 )</span> </a> </h2></div><div data-cy='reviews-block' class='a-section a-spacing-none a-spacing-top-micro'><div class='a-row a-size-small'><span aria-label='4.2 颗星，最多 5 颗星'><span class='a-declarative' data-version-id='v1nyb4igz33igf2j9heq96r9jtz' data-render-id='r5219jlj3ih9i2ne0gf0g0d5md' data-action='a-popover' data-csa-c-func-deps='aui-da-a-popover' data-a-popover='{&quot;closeButton&quot;:true,&quot;closeButtonLabel&quot;:&quot;&quot;,&quot;activate&quot;:&quot;onmouseover&quot;,&quot;name&quot;:&quot;&quot;,&quot;position&quot;:&quot;triggerBottom&quot;,&quot;popoverLabel&quot;:&quot;&quot;,&quot;url&quot;:&quot;/review/widgets/average-customer-review/popover/ref=acr_search__popover?ie=UTF8&amp;asin=B0CFTYRVL5&amp;ref_=acr_search__popover&amp;contextId=search&quot;}' data-csa-c-type='widget'><a href='javascript:void(0)' role='button' class='a-popover-trigger a-declarative'><i data-cy='reviews-ratings-slot' class='a-icon a-icon-star-small a-star-small-4 aok-align-bottom'><span class='a-icon-alt'>4.2 颗星，最多 5 颗星</span></i><i class='a-icon a-icon-popover'></i></a></span><div id='reviews_spacing' class='aok-inline-block'></div> </span><span data-component-type='s-client-side-analytics' class='rush-component' data-version-id='v1nyb4igz33igf2j9heq96r9jtz' data-render-id='r5219jlj3ih9i2ne0gf0g0d5md'><div style='display: inline-block' class='s-csa-instrumentation-wrapper alf-search-csa-instrumentation-wrapper' data-csa-c-type='alf-af-component' data-csa-c-content-id='alf-customer-ratings-count-component' data-csa-c-slot-id='alf-reviews' data-csa-op-log-render='' data-csa-c-layout='GRID' data-csa-c-asin='B0CFTYRVL5'><span aria-label='603 评级'><a class='a-link-normal s-underline-text s-underline-link-text s-link-style' href='/-/zh/dp/B0CFTYRVL5/ref=sr_1_94?dib=eyJ2IjoiMSJ9.RhlytuBRpsRlwN1seBb478b5FPc0s4dy3fpueiwGo5vg6v3hhz8rcRqij04zcwq382jPnBdVS14ozX0U7DH2G_6vehocwQ53D5locIJi96iZM9-z_VTkDodijX3aYlwr9AzX8NCWBvMaWafZ8xJ1w8ES3wY0iAbA4rPapMBPY2A7A3GA0L7fI-286qml2KM_c5fPX4tr4-mDcIsRGOudMZUkk1OMNu2euDN99s0-EvJVgoWfROXeg6zcGB8fUpoqOSFknYUCIE1_U4psQlTaE3pfCPDwPExRfem5E7jI5hA.jOcdWw1bjIjiI5J0xsxqw5LNlXJtimF_0nYvL4bIZog&amp;dib_tag=se&amp;qid=1722008664&amp;s=computers-intl-ship&amp;sr=1-94#customerReviews'><span class='a-size-base s-underline-text'>603</span> </a> </span></div></span></div><div class='a-row a-size-base'><span class='a-size-base a-color-secondary'>过去一个月有500+顾客购买</span></div></div><div data-cy='price-recipe' class='a-section a-spacing-none a-spacing-top-small s-price-instructions-style'><div class='a-row a-size-base a-color-base'><div class='a-row'><a class='a-link-normal s-no-hover s-underline-text s-underline-link-text s-link-style a-text-normal' href='/-/zh/dp/B0CFTYRVL5/ref=sr_1_94?dib=eyJ2IjoiMSJ9.RhlytuBRpsRlwN1seBb478b5FPc0s4dy3fpueiwGo5vg6v3hhz8rcRqij04zcwq382jPnBdVS14ozX0U7DH2G_6vehocwQ53D5locIJi96iZM9-z_VTkDodijX3aYlwr9AzX8NCWBvMaWafZ8xJ1w8ES3wY0iAbA4rPapMBPY2A7A3GA0L7fI-286qml2KM_c5fPX4tr4-mDcIsRGOudMZUkk1OMNu2euDN99s0-EvJVgoWfROXeg6zcGB8fUpoqOSFknYUCIE1_U4psQlTaE3pfCPDwPExRfem5E7jI5hA.jOcdWw1bjIjiI5J0xsxqw5LNlXJtimF_0nYvL4bIZog&amp;dib_tag=se&amp;qid=1722008664&amp;s=computers-intl-ship&amp;sr=1-94'><span class='a-price' data-a-size='xl' data-a-color='base'><span class='a-offscreen'>US$99.99</span><span aria-hidden='true'><span class='a-price-symbol'>US$</span><span class='a-price-whole'>99<span class='a-price-decimal'>.</span></span><span class='a-price-fraction'>99</span></span></span></a></div><div class='a-row'></div></div></div><div data-cy='delivery-recipe' class='a-section a-spacing-none a-spacing-top-micro'><div class='a-row a-size-base a-color-secondary s-align-children-center'><span aria-label='配送, 预计8月7日周三送达'><span class='a-color-base'>配送, 预计</span><span class='a-color-base a-text-bold'>8月7日周三</span><span class='a-color-base'>送达</span></span></div><div class='a-row a-size-base a-color-secondary s-align-children-center'><span class='a-size-small a-color-base'>配送至中国</span></div></div><div class='a-section a-spacing-none a-spacing-top-mini'><div class='a-row'><div class='puis-atcb-container' data-atcb-uid='atcb-B0CFTYRVL5-94' data-atcb-props='{&quot;cartType&quot;:&quot;DEFAULT&quot;,&quot;csrfToken&quot;:&quot;1@g+UZ8E92r9HKyG+o6LY/ekJ0ARxjTpOKjrBYJ1NAef2+AAAAAQAAAABmo8RZcmF3AAAAAGfA1H5nd8xGEcC3127HUQ==@ML8U5V&quot;,&quot;sessionId&quot;:&quot;130-4306403-0052132&quot;,&quot;locale&quot;:&quot;zh-CN&quot;}'><div class='a-section puis-atcb-add-container aok-inline-block'><span class='a-declarative' data-version-id='v1nyb4igz33igf2j9heq96r9jtz' data-render-id='r5219jlj3ih9i2ne0gf0g0d5md' data-action='puis-atcb-add-action-retail' data-csa-c-func-deps='aui-da-puis-atcb-add-action-retail' data-puis-atcb-add-action-retail='{&quot;messageError&quot;:&quot;无法添加商品&quot;,&quot;additionalParameters&quot;:{},&quot;asin&quot;:&quot;B0CFTYRVL5&quot;,&quot;url&quot;:&quot;https://data.amazon.com/api/marketplaces/ATVPDKIKX0DER/cart/carts/retail/items?ref=sr_atc_rt_add_94&amp;sr=1-94&amp;qid=1722008664&amp;discoveredAsins.0=B0CFTYRVL5&quot;,&quot;offerListingId&quot;:&quot;EEZlDsi2DbPxdpnvcu%2FgsNXs%2F1V9xU5BVfZ5qDJDOFfD44uZSieJXdthe%2F2QXFo74WMAg0J1GKkmuZn%2Fyb1r4ioYMRsceEZ9%2FdSYsPbR%2BS5CfkvwIau%2Fh8MQPXOGVtMfeCYDPBlmCMVLshFaDfpkSGlpRRQTDQDlxImLN810WeTmjbzqXgRK%2FBs8G6396pkD&quot;,&quot;messageSuccess&quot;:&quot;商品已添加&quot;}' data-csa-c-type='widget'><div data-csa-c-type='action' data-csa-c-content-id='s-search-add-to-cart-action' data-csa-c-device-type='DESKTOP' data-csa-c-device-env='WEB' data-csa-c-device-os='UNRECOGNIZED' data-csa-c-action-name='addToCart' data-csa-c-item-type='asin' data-csa-c-item-id='B0CFTYRVL5'><span class='a-button a-button-primary a-button-icon'><span class='a-button-inner'><i class='a-icon a-icon-cart'></i><button class='a-button-text' type='button'>加入购物车</button></span></span></div></span></div><div class='a-row puis-atcb-remove-group aok-hidden'><span class='a-size-mini a-color-secondary puis-atcb-remove-group-message a-text-bold'></span><span class='a-size-mini'>-</span><span class='a-declarative' data-version-id='v1nyb4igz33igf2j9heq96r9jtz' data-render-id='r5219jlj3ih9i2ne0gf0g0d5md' data-action='puis-atcb-remove-action-retail' data-csa-c-func-deps='aui-da-puis-atcb-remove-action-retail' data-puis-atcb-remove-action-retail='{&quot;messageError&quot;:&quot;无法移除商品&quot;,&quot;url&quot;:&quot;https://data.amazon.com/api/marketplaces/ATVPDKIKX0DER/cart/carts/retail/items?ref=sr_atc_rt_rmv_94&amp;sr=1-94&amp;qid=1722008664&quot;,&quot;messageSuccess&quot;:&quot;商品已移除&quot;}' data-csa-c-type='widget'><div class='aok-inline-block' data-csa-c-type='action' data-csa-c-content-id='s-search-add-to-cart-action' data-csa-c-device-type='DESKTOP' data-csa-c-device-env='WEB' data-csa-c-device-os='UNRECOGNIZED' data-csa-c-action-name='removeFromCart' data-csa-c-item-type='asin' data-csa-c-item-id='B0CFTYRVL5'><a class='a-size-mini a-link-normal s-underline-text s-underline-link-text s-link-style' href='#'>移除</a></div></span></div><div class='a-section puis-atcb-error-container aok-hidden'><div class='a-box a-alert-inline a-alert-inline-error' role='alert'><div class='a-box-inner a-alert-container'><i class='a-icon a-icon-alert'></i><div class='a-alert-content'><span class='a-size-mini puis-atcb-error-message'></span></div></div></div></div><div class='a-section puis-atcb-extra-container'></div></div></div></div><div data-cy='secondary-offer-recipe' class='a-section a-spacing-none a-spacing-top-mini puis-interactive-asin-expander-hide'><div class='a-row a-size-base a-color-secondary'><span class='a-size-base a-color-secondary'>更多购买选择</span><br/><span class='a-color-base'>US$98.00</span><span class='a-letter-space'></span><span class='a-declarative' data-version-id='v1nyb4igz33igf2j9heq96r9jtz' data-render-id='r5219jlj3ih9i2ne0gf0g0d5md' data-action='s-show-all-offers-display' data-csa-c-func-deps='aui-da-s-show-all-offers-display' data-s-show-all-offers-display='{&quot;assetMismatch&quot;:&quot;Abandon&quot;,&quot;url&quot;:&quot;/gp/aod/ajax/ref=sr_1_94_aod?asin=B0CFTYRVL5&amp;pc=sp&amp;s=computers-intl-ship&amp;dib_tag=se&amp;dib=eyJ2IjoiMSJ9.RhlytuBRpsRlwN1seBb478b5FPc0s4dy3fpueiwGo5vg6v3hhz8rcRqij04zcwq382jPnBdVS14ozX0U7DH2G_6vehocwQ53D5locIJi96iZM9-z_VTkDodijX3aYlwr9AzX8NCWBvMaWafZ8xJ1w8ES3wY0iAbA4rPapMBPY2A7A3GA0L7fI-286qml2KM_c5fPX4tr4-mDcIsRGOudMZUkk1OMNu2euDN99s0-EvJVgoWfROXeg6zcGB8fUpoqOSFknYUCIE1_U4psQlTaE3pfCPDwPExRfem5E7jI5hA.jOcdWw1bjIjiI5J0xsxqw5LNlXJtimF_0nYvL4bIZog&amp;qid=1722008664&amp;sr=1-94&amp;rrid=W0YJ2BPS8F24JH6CDT50&quot;,&quot;fallbackUrl&quot;:&quot;/gp/offer-listing/B0CFTYRVL5/ref=sr_1_94_olp?s=computers-intl-ship&amp;dib_tag=se&amp;dib=eyJ2IjoiMSJ9.RhlytuBRpsRlwN1seBb478b5FPc0s4dy3fpueiwGo5vg6v3hhz8rcRqij04zcwq382jPnBdVS14ozX0U7DH2G_6vehocwQ53D5locIJi96iZM9-z_VTkDodijX3aYlwr9AzX8NCWBvMaWafZ8xJ1w8ES3wY0iAbA4rPapMBPY2A7A3GA0L7fI-286qml2KM_c5fPX4tr4-mDcIsRGOudMZUkk1OMNu2euDN99s0-EvJVgoWfROXeg6zcGB8fUpoqOSFknYUCIE1_U4psQlTaE3pfCPDwPExRfem5E7jI5hA.jOcdWw1bjIjiI5J0xsxqw5LNlXJtimF_0nYvL4bIZog&amp;qid=1722008664&amp;sr=1-94&quot;}' data-csa-c-type='widget'><a class='a-link-normal s-link-style s-underline-text s-underline-link-text' href='/-/zh/gp/offer-listing/B0CFTYRVL5/ref=sr_1_94_olp?s=computers-intl-ship&amp;dib_tag=se&amp;dib=eyJ2IjoiMSJ9.RhlytuBRpsRlwN1seBb478b5FPc0s4dy3fpueiwGo5vg6v3hhz8rcRqij04zcwq382jPnBdVS14ozX0U7DH2G_6vehocwQ53D5locIJi96iZM9-z_VTkDodijX3aYlwr9AzX8NCWBvMaWafZ8xJ1w8ES3wY0iAbA4rPapMBPY2A7A3GA0L7fI-286qml2KM_c5fPX4tr4-mDcIsRGOudMZUkk1OMNu2euDN99s0-EvJVgoWfROXeg6zcGB8fUpoqOSFknYUCIE1_U4psQlTaE3pfCPDwPExRfem5E7jI5hA.jOcdWw1bjIjiI5J0xsxqw5LNlXJtimF_0nYvL4bIZog&amp;qid=1722008664&amp;sr=1-94'>（2件二手商品和新品优惠）</a></span><div id='all-offers-display' class='a-section aok-hidden'><div id='all-offers-display-spinner' class='a-spinner-wrapper aok-hidden'><span class='a-spinner a-spinner-medium'></span></div></div><span class='a-declarative' data-version-id='v1nyb4igz33igf2j9heq96r9jtz' data-render-id='r5219jlj3ih9i2ne0gf0g0d5md' data-action='close-all-offers-display' data-csa-c-func-deps='aui-da-close-all-offers-display' data-csa-c-type='widget'><div id='aod-background' class='a-section aok-hidden aod-darken-background'></div></span></div></div><div class='a-section a-spacing-none a-spacing-top-small puis-interactive-asin-expander-hide'><div class='a-row'><div class='aok-inline-block aok-align-center'><div class='a-section s-color-variation-image'><span class='a-declarative' data-version-id='v1nyb4igz33igf2j9heq96r9jtz' data-render-id='r5219jlj3ih9i2ne0gf0g0d5md' data-action='a-tooltip' data-csa-c-func-deps='aui-da-a-tooltip' data-a-tooltip='{&quot;inlineContent&quot;:&quot;粉红色&quot;,&quot;position&quot;:&quot;triggerTop&quot;}' data-csa-c-type='widget'><div><span data-component-type='s-product-image' class='rush-component' data-version-id='v1nyb4igz33igf2j9heq96r9jtz' data-render-id='r5219jlj3ih9i2ne0gf0g0d5md'><a class='a-link-normal s-no-outline' tabindex='-1' href='/-/zh/dp/B0CFTVBH4K/ref=sr_1_94?dib=eyJ2IjoiMSJ9.RhlytuBRpsRlwN1seBb478b5FPc0s4dy3fpueiwGo5vg6v3hhz8rcRqij04zcwq382jPnBdVS14ozX0U7DH2G_6vehocwQ53D5locIJi96iZM9-z_VTkDodijX3aYlwr9AzX8NCWBvMaWafZ8xJ1w8ES3wY0iAbA4rPapMBPY2A7A3GA0L7fI-286qml2KM_c5fPX4tr4-mDcIsRGOudMZUkk1OMNu2euDN99s0-EvJVgoWfROXeg6zcGB8fUpoqOSFknYUCIE1_U4psQlTaE3pfCPDwPExRfem5E7jI5hA.jOcdWw1bjIjiI5J0xsxqw5LNlXJtimF_0nYvL4bIZog&amp;dib_tag=se&amp;qid=1722008664&amp;s=computers-intl-ship&amp;sr=1-94'><div class='a-section aok-relative s-image-square-aspect'><img class='s-image' src='https://m.media-amazon.com/images/I/4138zbSKIvL._AC_US40_.jpg' srcset='https://m.media-amazon.com/images/I/4138zbSKIvL._AC_US40_.jpg 1x, https://m.media-amazon.com/images/I/4138zbSKIvL._AC_US60_QL65_.jpg 1.5x, https://m.media-amazon.com/images/I/4138zbSKIvL._AC_US80_QL65_.jpg 2x, https://m.media-amazon.com/images/I/4138zbSKIvL._AC_US100_QL65_.jpg 2.5x, https://m.media-amazon.com/images/I/4138zbSKIvL._AC_US120_QL65_.jpg 3x' alt='粉红色' data-image-index='0' data-image-load='' data-image-latency='s-product-image' data-image-source-density='1' onload='window.uet &amp;&amp; uet('cf')'/></div></a></span></div></span></div></div><div class='aok-inline-block aok-align-center'><div class='a-section s-color-variation-image'><span class='a-declarative' data-version-id='v1nyb4igz33igf2j9heq96r9jtz' data-render-id='r5219jlj3ih9i2ne0gf0g0d5md' data-action='a-tooltip' data-csa-c-func-deps='aui-da-a-tooltip' data-a-tooltip='{&quot;inlineContent&quot;:&quot;紫色&quot;,&quot;position&quot;:&quot;triggerTop&quot;}' data-csa-c-type='widget'><div><span data-component-type='s-product-image' class='rush-component' data-version-id='v1nyb4igz33igf2j9heq96r9jtz' data-render-id='r5219jlj3ih9i2ne0gf0g0d5md'><a class='a-link-normal s-no-outline' tabindex='-1' href='/-/zh/dp/B0CFTW488R/ref=sr_1_94?dib=eyJ2IjoiMSJ9.RhlytuBRpsRlwN1seBb478b5FPc0s4dy3fpueiwGo5vg6v3hhz8rcRqij04zcwq382jPnBdVS14ozX0U7DH2G_6vehocwQ53D5locIJi96iZM9-z_VTkDodijX3aYlwr9AzX8NCWBvMaWafZ8xJ1w8ES3wY0iAbA4rPapMBPY2A7A3GA0L7fI-286qml2KM_c5fPX4tr4-mDcIsRGOudMZUkk1OMNu2euDN99s0-EvJVgoWfROXeg6zcGB8fUpoqOSFknYUCIE1_U4psQlTaE3pfCPDwPExRfem5E7jI5hA.jOcdWw1bjIjiI5J0xsxqw5LNlXJtimF_0nYvL4bIZog&amp;dib_tag=se&amp;qid=1722008664&amp;s=computers-intl-ship&amp;sr=1-94'><div class='a-section aok-relative s-image-square-aspect'><img class='s-image' src='https://m.media-amazon.com/images/I/41KEo85U9eL._AC_US40_.jpg' srcset='https://m.media-amazon.com/images/I/41KEo85U9eL._AC_US40_.jpg 1x, https://m.media-amazon.com/images/I/41KEo85U9eL._AC_US60_QL65_.jpg 1.5x, https://m.media-amazon.com/images/I/41KEo85U9eL._AC_US80_QL65_.jpg 2x, https://m.media-amazon.com/images/I/41KEo85U9eL._AC_US100_QL65_.jpg 2.5x, https://m.media-amazon.com/images/I/41KEo85U9eL._AC_US120_QL65_.jpg 3x' alt='紫色' data-image-index='0' data-image-load='' data-image-latency='s-product-image' data-image-source-density='1' onload='window.uet &amp;&amp; uet('cf')'/></div></a></span></div></span></div></div></div></div></div></div></div></span></div></div></div>"
pattern = re.compile(r"<span class=\'a-size-base-plus a-color-base a-text-normal\'>([^\<]*)</span>")
result = re.search(pattern, amazon_span)
print(result.groups()[0])

star_pattern = re.compile(r"<span class=\'a-icon-alt\'>(\d\.\d) 颗星，最多 5 颗星</span>")
result = re.search(star_pattern, amazon_span)
print(result.groups()[0])

sale_pattern = re.compile(r"过去一个月有(\d+)\+顾客购买")
result = re.search(sale_pattern, amazon_span)
print(result.groups()[0])

import time
print(int(time.time()))