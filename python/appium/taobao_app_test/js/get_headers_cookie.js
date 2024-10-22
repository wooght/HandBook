function get_fields(c){
    /**
     * 遍历属性
     */
    // c.class.getFields().forEach(function(field){
    //     console.log('field${field}', c[field.name])
    // })
    // return c.class
    var fields_arr = {}
    Object.keys(c).forEach(function(key){
        console.log(`${key}:`, c[key].value)
        fields_arr[key] = c[key].value
    })
    return fields_arr
}
function mapString(map){
    /**
     * map 转String
     */
    var entrySet = map.entrySet();
    var iterator = entrySet.iterator();
    var map_arr = []
    while (iterator.hasNext()){
        map_arr.push(iterator.next())
    }
    return map_arr.join(',')
}
var allow_api = ['mtop.taobao.wireless.home.newface.awesome.get',
                'mtop.taobao.wireless.home.category',
                'mtop.taobao.detail.data.get']
function allow_request(url){
    var is_allow = false
    allow_api.forEach(function(api){
        if(url.indexOf(api) != -1 ){
            is_allow = true
        }
    })
    return is_allow
}
Java.perform(function () {
    // android 版本
    if (Java.available) {
        console.log("Android Version:", Java.androidVersion);
    }
    // 关闭spdy协议
    var SwitchConfig = Java.use('mtopsdk.mtop.global.SwitchConfig');
    SwitchConfig.isGlobalSpdySwitchOpen.overload().implementation = function () {
        // var ret = this.isGlobalSpdySwitchOpen.apply(this, arguments);
        // console.log('start:' + ret)
        return false;
    };
    var send_cookie = false
    var send_headers = false

    let CookieManager = Java.use("anetwork.channel.cookie.CookieManager");
    // result Request 请求 cookies
    CookieManager["getCookie"].implementation = function (str) {
        // console.log(`CookieManager.getCookie is called: str=${str}`);
        let result = this["getCookie"](str);
        if(allow_request(str)){
            if (!send_cookie){
                send({'type':'cookies', 'cookies':`${result}`});
                send_cookie = false;
        }}
        return result;
    };
    // c24666a 为Request,response 的综合内容
    let rye = Java.use("tb.rye");
    rye["a"].overload('mtopsdk.framework.domain.a').implementation = function (c24666a) {
        // c24666a.k 为 Request = Java.use("mtopsdk.network.domain.Request");
        if(allow_api.indexOf(c24666a.k.value.r.value) != -1){
            if (!send_headers){
                console.log(c24666a.k.value.c.value)
                send({'type':'headers', 'headers':mapString(c24666a.k.value.c.value), 'api':c24666a.k.value.r.value})
                send_headers = false;
        }}
        let result = this["a"](c24666a);
        return result;
    };
})