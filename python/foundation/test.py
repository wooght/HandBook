# -- coding: utf-8 -
"""
@project    :HandBook
@file       :test.py
@Author     :wooght
@Date       :2024/4/28 16:26
@Content    :
"""
ips = """185.195.104.31:12333
185.162.93.62:8118
81.43.68.47:8080
118.70.49.64:8080
117.186.232.73:8080
223.215.176.46:8089
140.227.62.35:58888
104.16.155.36:80
23.226.117.85:8080
103.106.115.90:8080
117.71.149.83:8089
36.6.145.196:8089
60.168.80.175:9999
113.121.42.98:9999
37.48.120.146:3128
104.248.29.72:4555
122.9.183.228:8000
183.164.242.70:8089
45.8.105.126:80
200.122.204.106:999
195.211.219.147:5555
12.88.29.66:9080
103.68.207.34:83
120.27.130.59:80
103.82.157.91:8080
103.41.90.49:83
165.227.36.36:80
183.164.242.167:8089
103.138.71.131:8085
103.81.194.172:3125
104.249.6.15:3199
183.164.243.19:8089
185.195.105.78:12333
36.6.145.133:8089
113.223.214.237:8089
37.205.9.194:80
117.69.237.174:8089
114.231.82.16:8089
113.160.154.23:8080
61.158.175.38:9002
84.241.8.234:8080
80.87.213.111:8080
124.220.35.219:8080
59.15.28.76:3128
117.71.155.205:8089
43.143.88.153:3128
203.190.54.222:6666
118.31.1.154:80
95.216.88.139:80
142.93.14.238:8888
121.40.93.125:80
181.209.117.51:8080
180.180.225.235:8080
45.234.60.128:999
83.151.4.172:57812
117.54.114.103:80
202.12.80.16:82
36.6.145.93:8089
37.27.6.46:80
91.226.92.29:80"""
# print(ips)
ip = ips.split('\n')
for i in ip:
    print(i)

import json, time
json_text = '{"startTime":"1716825600000","endTime":"1716903900000","orderIdMatch":"","paymentType":0,"payTypeName":"全部","payType":-1,"startDate":"2024/05/28 00:00","endDate":"2024/05/28 21:45","cashierId":0,"discountType":0,"orderType":0,"offset":0,"limit":10}'
new_json = json.loads(json_text)
print(new_json)

raw_json = '{"appInfo":{"app":"com.meituan.erp.retail.admin","version":"1.18.10","sdkVersion":"1.7.8"},"communicationInfo":{"nop":"--"},"environmentInfo":{"osVersion":"17.4.1","osName":"iOS","clientType":"iphone","platform":"iOS"},"deviceInfo":{"secondaryDeviceInfo":{"signature":"d441f2bc79adf3cb3f55c4ebda30901a"},"deviceModel":"iPhone 12","keyDeviceInfo":{"idfa":"00000000-0000-0000-0000-000000000000","idfv":"87B522E9-EAD2-4982-BD0B-AE05689FF484"},"isJailBreak":false},"idInfo":{"uuid":"0000000000000183F2B1959F4472B92BF813928B4498BA164619479778148387","requiredId":4,"dpid":"183f2b1959f4472b92bf813928b4498ba164619479778148387","localId":"19b182cb45b04500d3a9cd872910ce9691eaec6f38436be23d","unionId":"183f2b1959f4472b92bf813928b4498ba164619479778148387"}}'
print(len(raw_json))
data = json.loads('{"data":"dTR0l1hKznndqltvTwhzR81dCc6UF8DisFsV30DLnSbo1NvHtgVJhxcp6lSJapTIo6U5Lud35fRcbuAWy4IYBQGSzAHFjB3KlkkbxDmWfoomws3futBYmspnp8loUxLMJZq7laEcbgQEkHyBsan+A7nZzQHr+jfT0rln88qD3ajMMwFmmTovunTL6cpNNlMSyZOJpSFq8yT1fwuV703Uoo+HtmCV70k1lsF9Xy0Oz4gJ+OGjDWEUts03N1NiV+6n+1sijVzdB3A3s5niDKZbXjHxMoIhF+dI1Mwq+G1muBfyXBc2AbqBaBqoJIPRwvLEoxeEL5l6zAPrj8f1WwQngmzVECh\/ZWwRxSwtBMm0jQ5mvsuoRjS2xSwQqwx\/ZUfHoqLoPQzAcjC9ja2R2rtC5JA0BYVWDqwfwTe3tSUpm8MKrnYlibgXRYqIuuJSQMkWuFF8vSuTp8nlrzvoaT2\/WumvwEn9t40zKZR9nW6HrBRBReCKEwQY5p2BfDSnGiU5KpFNDzTA3us6jbw0A++XJTyRIPXQXZAvprP1GsAURL4bHQPNTHIc8rEu5NvdiM1ErdcPpfPgsAKUtlYGmwbUAQNJEiqtyakmkaHOF2xigwxkpzgzNOEof9mB2kD2EbXy4buQyZKmNvfyo6RP+u\/k174Zq26Iwf0qEHRIKacyZNKD1FFmDvZliMz6Fy51vfZFWvZsrMcORjfwSkp7VQ9trTTlnbjppAOeb\/NL0Id7naFDMRuBbbPPXUjaKuzvC2iyiQdXkQSUGK0q+oH0UM8rvLwTDWHByCTx\/Ip5p\/PUHNClDJ9GOG5Et9aGgReggkFggVnG61NbKXD6ji7ZAL0cfo5qMOLW3YHS5hypKiAC5Q6rksGmuJtzZkv887YtdjuR++Q+kObKe++85MgXxTARwvMyvacoe9duzot7VEpM8k0JpXCtJRIXOw2Xq\/DmO4ZEWUJ93RwjEByMhKAKggaQFbJYx6UANBLsmB+9my6csJJASxXodvNFv45ygcwrUzHGkupRTvnI\/g\/n2af79OrUTI54M8rUdO7qXItJ5kds7a9O6\/PL+wzH6VuT\/ksqLJHgMhk2Q3bL7hDLqE017+dx5RZiGfY9pKNWpaWmzWYoIIJuygtvhKqfCh9QNCzJ44KceoPe7b9vpacpH69dDsClDEABtNPKvqr9mPnfq6vbGfETs1iCK+SBffNmsiL9mU7KvkoC8f+HzUTfAFfznQ8OqmiUraqDf8NbwEkF3\/69FeCcy8hNTY0WWLgJFeavXQE1qTKKHCQ2M4OioTlxs5YQ8dEcaRRH8mW3SmOpaeNYEwpCUgcGKUC04hNXeKeF6X9MlYwJFk2gcONpnVF\/5Ql4hNzwJ\/95cby+Ufd+MKzkolh6kiOKMZv7LTZxw48V\/Xjcf8SFqVaowAiyVLr4rjXG2iFXuXiXQDwn32fL84S+K8b3ft1yLzTe4ljH2DlGFQiDm+KEhH0ePDiRZ9z4io6UwutAL3M\/P2xp2uQWu2fdvR2rMODB+Pdb0btAEy1x1YRCwWqDfomc5SNWXokgzeqxwK7JlB9nLRSdzbkkRIVZ\/Rdur3Ju+yqLKSAO9ZTayu7JsLElaezYcmU0l0TlD7SO3lHchMknOB\/eZZFHrzyg8yq+lJYcH0pfTY3kppduy2FMXrWG6O5pinYk7YN\/2VnASYhESk+wZw8FonAdCONbM4LT1gwKwaXT36dkFfnhNJuvtnsNcs2PP2KMZcq0YbMFHgLfHRaamMn+7NzRkyytPx8EeaCEXrjFfN9I7hZOXmHPCPubuDqLKI8bRi2MkzUTEHuPCPm\/kopZ9RglfVphdgS0pHqqY\/\/7CCZrSJ9gWbeuT7vyT6WxtPDueqZynOjCnvewPGi6gFgfhRcecMpDKK1JV6qEyD7PoTBsE0Uy+BHMq3T6D9b27\/dos5HUvj8acAXXSu64TJksKC7nKjEu2wsCIzSiy66e0mfQUjwGATWu9cddjxl1dfBdjWo1R0hGZuKHNADxySD3UqgnzolNkIHTllaNddMLfGa4eWgB1xFpYVr0qymrpdmphQp6lr4VU\/2kt8cSIwU9aH7akMjsPiXcdSg3IEhxIQQuOuUnpl4upFIpAGgnAPc05TS0FcV49DD51FXghVPbx28uTeI9NxAAHhWtv6yUQO5s2f81BeZU5kpZMPq0IDhkxWq4xdZHBKw0qoLf\/7dSI6kLJ+y1gyUsBym\/b+tEjzSG4FF0ptDx0IF\/pK94RMF2q08LUAfrZfgFoMvwcRGK5dJKlEM36gAh32SjdzH8PfBSKS+lCMlnNZM\/V9exuz9R9+FAVkpLB3BJHaClffiJkpDhPMYREe75u\/+yXiENG60fMxrb3ii\/k85InXazkoRKosTwxbBfuWA0sneQQCTtsGOe9bYZo0sClet8L6mzy0jAanXgYTzVDEGbfB\/hhwSjU56NKT6aFxTIfF0QHlWE5zJu7OX0vPjDPvceQaq+xEHzQ2TK6z1oGKeUOmkpIteMubmOGA7qSYW7Ep86rv85reynohEvPODDZ\/tqPJ12MxfcWeNOnzLBKxaGI6JIJVA1yU2uXfDc2qdx+Cb8bx0htVbcZ1qO5Zvsxt3XhGrHXEf4GpQsa73Uzjv1bTU9q4YlrMYxElza2B53rs2YXUdA7Ao40d4AnD9h\/80IQasMVHnuF9leZgWt4tHPXoQ+PQsSkGwydna2Q3YiJkIixKEKblpUavLZwx52UCqZ5f0PVdmdJjOpaiaZJ3SzTKpcm5vq\/4DRigp1K1lEihtCHvpQ0HamZH2hFnAdTJZZu1m\/NX2kL8tVoBgCms\/o7tisDkryO7dp3Nw9nY9m0tlClM9TOSen1wW4IcWm1SuNGKI4xiKBkQvugI+Mu1ARcNUeXl\/tOYK31HEMbuI5DVZYuhJulozLJhJFgztSK1I6y2wHaBcGDLw73cvQd+X0aIwHz50Oc5jOqtWv9IXXeLTlqnJxqtoikOUkZlqxY158j2abFbVT0Qn+g19kNA0q8O3ggxhenKbwl4F6nbQC1nsvNfvyX7i7C4Dv2FZ37GgkLeYwYbkUyVed7wp+Ia1FOyBmm4t19jn1NoZJFTLe+pNt5PFXxbwjlZh6tLdz6teI9zZPYFGhyjVvnwDZ62GnTTRtw0P4P\/8rNoAXW62dC0HUeGKxvim45ewFNjWER1iCaqjJBA3mI2sCuuZlkKr6kAP7aXT+xAVldz9BHfy40zVjUvcPGFay+At5m9dqPQ+mClO10YB2SMxscX3qYKVrgPC1ifcVTd6J+4+6+tV955MA3VFpQKF7npFJDWaWAbBnR0cI7iae4nAbgxjiOPFKxF0IMguwYtDZcwXZkvDIPxS2DrUoFszo7RWzWBdG15a7yYYl7ui1GyzHc2QJQuIfA9zfKbpUylHk6470KgDsUffYwMGZlkkJJwuQE\/uaaK7RkBjAytRqlzaXQOuv41Nhrgd8AbJupfdgj0NVDphZ89vIa\/hJDqe3pgVZlab0lEaiidk56tNT7bYHw8yxWfIl4ToCQR9bccuHJlzlrLbdbUaeubpbXq5Or80updmPA9x4+XZUXbJxipXaXmH8FKhiA1mImX4Jwn7qGM1HLVhz32NtppnQ0uWIb36oAaNXdTA7hVHsiAUpVYVo1on7btSUwhh10UiGecJ8Zmb65cAx52GPN6SHLGSmzz47V6LYNv6Mb14A7Sj5KmJZdFwuF8ugvoD3bCJeg+JBEERZJRm0n9vp0Q8sdm+qLxFTTdcoGILSMge4rIFl3gPar6Bj9aAImZPhyvG0+SHmZpHsSexA9hmWc8VllccUFDAudLIxG1SbS0yypJU\/3bdKfr1GXTgQNj7G5srhe79LmbUlnZDhCHRaYp1IQyu4x\/zU6pHhAcU5GVVGGz0tv90tzn6ep6n+bXaul6U4m7nnwBa5JR1dbla348qzUxrLIp20NRy1NmkW+\/z+4iDXtO4QAQHhAxS47a3URCEKzkCmLCBGC2zBjnQK0mi5HmN8HOzt\/3+oLs\/3EjMYLUA4DJUNotOdtWyQHVX758FE2JZ5EWJb9eGLNgx4mfuJVKbFmkdbVjSfHlIuXJ9SpDi0xQjXMwNCQizm882xKdyOGcBsnsQobBdL7NAlwj4iDh11lfwYvlj9hGrcXfAFnJjbr\/0Ip3R169IEoTVeDlKP7I9OWFH+FtUOQBOhmOPKzkiRpWH2E\/+efDnCR8d7hlnzAFE+xKh+8BKDNCcnfND1uHxQQzMpqVwaNo5d+GzkoCE2Xr36tu8bNXr4blFQzyqfkK0FMlo1GdzRDSnqVaroMUGh845Uz+kTE207edCwUSb3pLQaczlc7zjo+CaBvzdA\/Z7mNnbx3yYvoEElwx9meSa59iwxHDGYnEXTRwwE7AMwQ0GMGqE9Mt+0lBsOKeXK3b+2fDRPbgLYOTjOSbVDxMa4I1oCqEPOES6L0ojtIVl\/KRD8nvlOCoO6ry2M4ZH+UF7ZX\/0rCZQ\/oHWxGFZ5WbVYXVesFh4achwMFEwwkyQYH1+k+gq+\/QRn2e1byRSImlGhAJY8v9utjmrK4VWuIEcIgeGlZlL76ZiazkKX+o0Qv+Yg3LJaLg\/alaTNCz3sy8j1\/t6rtcOA8yAVBfUKIKmS603VqLCCMA+kbg5Y2CT6UkFgIiul4kUf2SPtwKu11FLIB+mCaGQAb+zFOjknju7V1rD2YGK4LKx+jrgB2Apc9QQXkZc14sFQcjZRodHslLuktcZpIjP4+BXy10DFQIVOADpeFhygwwqu6ICGInKzL3M9whcnBtVgB77i0A\/GD0fin308sQiZ4i5SAzrwZGdM8IskQhJ6KWrzrRabyaSpShPfVhH3a5lqRacuzPqJ1nMq40Mv\/TbAYaBIq\/+ONpN7AzjKfWQUxRRAkWhq05UUiQYEwC8a6ROKFSQtCSDhnyDmFOC2sS3Q0fzka2WTgP4tNiNfl2iXfbzuPXtzjh9a2odaKWOjSWNUA7bPHRgcLARY1UORLsEWYmv7J\/WnhuSyXiwzl\/Fk7Xxg5YEAQ7TDoQx098fO83taWq0K+xOvhckmjeal4\/QaxQFQBCRdkx81gBfmxqksyqBiOloM+9YimEkRhYQyelHvBjlxuvB6AOTq19QBb22LeVxC1pLCf5316m2SW6DLpfcZgjsKEFh3xuvTIwIGubQY7zMJMjl5znRq8w3b30qt4tLWMqZGjcNj4gzd07dgR97Y9FZDXOUbXUcL9eUjN8tsfUk7vMdasTSkx1dI6BKXbcUMburZSYLzyjxL+r0g0S28W3uMpp6\/53wldmf1+2NXc\/YpsFScQMqtPZPxIvnBVs0hPezvhJrPBo9CWDWuxpGMSMd4gZ7n82J2Nl3NUNovPD7k4Cfj3d9ssKzO19\/EiHPyBAIXnzKidIB6Emk6ER2jh5QfkwPYeherfnA4c010xtK7NxBBotJyi6HWrkFOPDe0NzYuc+7K1bEQ1yQb4KBW1DKqQojbV7vG7QqFiK1yO3Aluv67xnjIb6Ierw6jMmjQPc1q3BW7jct7YYQQInrOBz563yYyXlsnrQB8lFLweJk5l1wnWpVHysS\/Yyy6wrpG7zhsDry\/Gva7dAHsZ8CzSCC0om9HXNqJu5U7iblR1x02jUr7YZm6NM2PDb7gpvxnRkaL\/rAzEzvHgO99wfu2RYadl0Vgl66hLFzKcnNxHT1KXxV\/rs2cFOFRyZZI3GnKQ+t7FkbiB5BDsGCVsEk9A0Lrawqj3TvLEqR6VlG0po6cmmMx6\/OCSw1NEJ2\/j3TGhLL3l8D9zi1haCsXgfL8PsFfnpbvNqmxkhz48s6ynRikVTMD2teW4YMBQ3TwxtsIJRDhdToZHXE6MktKGmLAppIE\/llvtiC4vagr8Zr6aSO\/dTPQ0N9OAHu6ibY4EO7gkDVP92k+Tnyvixtneua6iTSvV6tAvOADUvQ4RezitK4T1QMV6r\/0h53s6nDbVX1RVn0ROTxs32VgAtZM8HpfGd7f7IkgHoqeo33dUnaHrBFsG1Cjox3MRWHow3iwbgSwAfySavDTXikONHE92Tw2VR+v\/drBqO1kcaC7Gf0aMgkwJuAcPtMQp\/TJj0UNgqhdynYvH4iSp1W5zAsaauIlsoYtPqm\/y644IOSM0FcD7\/4sjhr+DG7mROR87JxAK4rm+lnCIpuL0Vimcg\/+K4dsj7OIaKVXsTJZ5wQfDAm54ZqGt17dz7eI6XbzoiSrwZo\/BLUZFYuzY09o7vGW1PgJuyEWuVrabv5FYr4Ac7Gn36Oao9UmPVChjEDqF\/lTAs4Qx2tBqA7QHrrXnKVbZSHpUYwne6audquO1W20bkGFUm9blX1Cq2RohW4VUj31\/AVf7M0qF7dnX2IH7UPjzgT7BEep7OfbKqAM9k1N+6yo\/WQ7th5q3JzFVR6wqHvSCkRcbvnG9z6S6ZW+zIPmIw2IM3zKEujbkYhpKQlT0GDiPo6TRe8hxdMOORDmpAJDWv+HtprYoeV2JP6uiNaHiYXOQ0RJXcAF\/RyjlsvIQ\/MCo6Az9aSctz6cYcGkBzQVk\/uDduPE4KX4kEB0kYOM2WVBStvajCuFii7jRi+3z79rpxwpFlpoSQHDe2+iEMYSNU\/SVbgtMlmg12Lt5g==","dfpVersion":"5.4.18","os":"iOS","mtgVersion":"5.4.18","time":"2024-05-29 18:25:22","ext":"3"}')
for key, value in data.items():
    print(key, value)

print(int(time.time()*1000))

cookie_str = 'cookiesu=641717409901065; device_id=28697ab957c58af6e1bc39514f12cacd; s=cj1chgmc9d; __utma=1.1253666201.1717411348.1717411348.1717411348.1; __utmz=1.1717411348.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); Hm_lvt_1db88642e346389874251b5a1eded6e3=1717494626,1717501036,1717501108,1717507106; remember=1; xq_a_token=0060d1c93c77fb305165e3fef50b1526a69b9c7c; xqat=0060d1c93c77fb305165e3fef50b1526a69b9c7c; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjIxNzQxMDE0MTQsImlzcyI6InVjIiwiZXhwIjoxNzIwMDAzOTg0LCJjdG0iOjE3MTc1MDc3NzE0OTcsImNpZCI6ImQ5ZDBuNEFadXAifQ.qepJx_5jwSBY14twKU7LBWFAqeJwq4nOTDAp2WHibaGWWaYPAU-jE_qGr7kDKm09C6X1oaCmCwV0XP8_NaxKx4Q3cMn4_Jj9aIjWyYmUa7uBgk7rGnj8O5_qIyeDZuw-4CMvbtcBwT3cG1vB6LboyHmy3ZXQgI9XtcDepBtBAFzyQmlIOF3F5ITAU6QNA4Nlj1jB_gTsHoNj4zQhysAk--sdfpGyFXN6rlOo1WyVijt4Lt2ih0-mdliqw4m6W0i2ofuxBoO3TPlWEgUBUxRN4jA_VnidNl6-89MtEC9ZbaP3fF-uOM3s8gtd-XqxZ5iSjo2OLwYH-hx7QCTCJkTJjw; xq_r_token=32e36cf3345eb5a1a4a61c66c8358973cd2febf3; xq_is_login=1; u=2174101414; acw_tc=2760779017175105978745691eb5ee09bb429ec03389f855b38176fa8b4e30; snbim_minify=true; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1717510878; .thumbcache_f24b8bbe5a5934237bbc0eda20c1b6e7=0PSxoucTbw5xVEpgxRvOOsBvoeD4hnE+hu0Ty9IHzLJeOlg6O+Ejg7gp10iY5f/B5nmlfu9lM57zuPMqpkOBhg%3D%3D; is_overseas=0'
cookie_one_str = cookie_str.split(';')
print('cookie----->')
for cookie in cookie_one_str:
    print(cookie.strip())


a = {'a':{'b':1}, 'c':2}
a['a']['bb']['cc'] = 3
print(a)