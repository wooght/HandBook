function echo(s){
    console.log(`\r\n ${s}`)
}
function call_new_sign(hashMap, hashMap2, str, str2, z, str3){
    /**
     * 主动调用内存中实例方法,生成新的x-sign
     */
    var ryw = Java.use("tb.ryw")
    Java.perform(function(){
        Java.choose('tb.ryw', {
            onMatch: function(instance){
                var result = instance['a'](hashMap, hashMap2, str, str2, z, str3)
                console.log('call_new_sign:', result)
            }
        })
    })
    return NaN
}

function get_falcoId(){
    var result = ''
    /**
     * 调用内存实例生成falcoId
     */
    var FullTraceAnalysis = Java.use("com.taobao.analysis.fulltrace.FullTraceAnalysis");
    Java.perform(function(){
        Java.choose('com.taobao.analysis.fulltrace.FullTraceAnalysis', {
            onMatch: function(instance){
                result = instance['createRequest']('mtop')
                console.log('new falcoId:', result)
            },
            onComplete: function(){
                echo('get falcoId end')
            }
        });
    });
    return result
}

function mapToString(hash_map){
    /**
     * 将map转换为String
     */
    var result = "";
    var keyset = hash_map.keySet();
    var it = keyset.iterator();
    while (it.hasNext()) {
        var keystr = it.next().toString();
        var valuestr = hash_map.get(keystr).toString();
        result += keystr +"="+valuestr+"&";
    }
    return result.substring(0, result.length - 1);
}

function get_caller_function(obj){
    /**
     * 遍历运行栈队列/栈帖
     */
    var current_thread = Java.use('java.lang.Thread').currentThread();
    var stackTrace = current_thread.getStackTrace();
    echo('stack trace start:')
    stackTrace.forEach(function(stackFrame){
        console.log(stackFrame.toString())
    })
    echo('stack trace end')
}

function get_fields(c){
    /**
     * 遍历属性
     */
    c.class.getFields().forEach(function(field){
        console.log('field${field}', field)
    })
}

var split_str = '************************************************************************'
Java.perform(function () {
    if(Java.available){
        console.log("Android Version:",Java.androidVersion);
    }
    /**
     * 实例化类
     */
    // var ClassName=Java.use("com.luoye.test.ClassName");
    // var instance = ClassName.$new();
    var SwitchConfig = Java.use('mtopsdk.mtop.global.SwitchConfig');


    // 采用了spdy自定义完了协议,所以要关闭spdy协议,要不然接口工具(fiddler,charles)抓不到
    SwitchConfig.isGlobalSpdySwitchOpen.overload().implementation = function () {
        // var ret = this.isGlobalSpdySwitchOpen.apply(this, arguments);
        // console.log('start:' + ret)
        return false;
    };
    echo(get_falcoId())

    // var MtopResponse = Java.use('mtopsdk.mtop.domain.MtopResponse');
    // MtopResponse.parseJsonByte.overload().implementation = function(){
    //     this.parseJsonByte()
    //     var dataJsonObject = this.dataJsonObject.value
    //     var originJsonObject = this.originJsonObject.value
    //     // console.log(dataJsonObject)
    //     console.log('\r\n-------------------------------------------------------------------------')
    //     // console.log(this.bytedata.value)
    //     console.log(split_str+"\r\n", this.api.value, this.v.value)
    //     echo(get_falcoId())
    // };

    var security_b = Java.use('mtopsdk.security.util.b')
    var security_c = Java.use("mtopsdk.security.util.c")
    // 加密模块 列表,详情都调用 返回的是各种秘钥
    // security_b.a.overload('java.lang.String').implementation = function(str){
    //     console.log('\r\n \r\n')
    //     console.log('security_a:bArr', this.a(str))
    //     return this.a(str)
    // }

    /**
     * 会返回请求部分headers或者Form data
     * result 时一个秘钥,但未找到用处
     */
    // let C24711b = Java.use("mtopsdk.security.util.b");
    // C24711b["b"].implementation = function (str) {
    //     console.log(`C24711b.m99439b is called: str=${str}`);
    //     let result = this["b"](str);
    //     console.log(`C24711b.m99439b result=${result}`);
    //     return result;
    // };

    let ryw = Java.use("tb.ryw");
    // var instance_ryw = ryw.$new();
    // ryw["a"].overload('java.util.Map', 'java.lang.String').implementation = function (map, str) {
    //     console.log(`ryw.m140331a is called: map=${map}, str=${str}`);
    //     let result = this["a"](map, str);
    //     console.log(`ryw.m140331a result=${result}`);
    //     return result;
    // };
    // ryw["a"].overload('java.lang.String', 'java.lang.String', 'java.lang.String', 'java.util.HashMap', 'int').implementation = function (str, str2, str3, hashMap, i) {
    //     console.log(`ryw.mo140314a is called: str=${str}, str2=${str2}, str3=${str3}, hashMap=${hashMap}, i=${i}`);
    //     let result = this["a"](str, str2, str3, hashMap, i);
    //     console.log(`ryw.mo140314a result=${result}`);
    //     return result;
    // };
    // ryw["a"].overload('java.util.HashMap', 'java.lang.String', 'java.lang.String').implementation = function (hashMap, str, str2) {
    //     console.log(`ryw.mo140323a is called: hashMap=${hashMap}, str=${str}, str2=${str2}`);
    //     let result = this["a"](hashMap, str, str2);
    //     console.log(`ryw.mo140323a result=${result}`);
    //     return result;
    // };

    // let rzi = Java.use("tb.rzi");
    // rzi["a"].implementation = function (c24718c) {
    //     console.log(`rzi.mo140343a is called: c24718c=${c24718c}`);
    //     let result = this["a"](c24718c);
    //     console.log(`rzi.mo140343a result=${result}`);
    //     return result;
    // };

    /**
     * 参数map有headers中的值,result也有headers中的值
     */
    // ryw["a"].overload('java.util.Map', 'java.lang.String', 'boolean').implementation = function (map, str, z) {
    //     console.log(`ryw.m140332a is called: map=${map}, str=${str}, z=${z}`);
    //     let result = this["a"](map, str, z);
    //     console.log('ryw.m140332a params map', mapToString(map))        // 有x-sid, x-devid, x-extdata等 headers字段
    //     console.log(`ryw.m140332a result=${mapToString(result)}`);
    //     return result;
    // };

    /**
     * 重点:
     * hashMap: url参数及headers部分参数:  exParams, appKey,api,坐标(lat,lng),ttid,extdata,utdid,deviceId,sid,uid
     * result:x-sgext, x-umt, x-mini-wua, x-sign 等headers字段
     */
    let HttpHeaderConstant = Java.use("mtopsdk.common.util.HttpHeaderConstant");
    // ryw["a"].overload('java.util.HashMap', 'java.util.HashMap', 'java.lang.String', 'java.lang.String', 'boolean', 'java.lang.String').implementation = function (hashMap, hashMap2, str, str2, z, str3) {
    //     console.log(`ryw.mo140317a is called: hashMap=${hashMap}, hashMap2=${hashMap2}, str=${str}, str2=${str2}, z=${z}, str3=${str3}`);
    //     // console.log('hashMap', hashMap)
    //     // var new_hashMap = mapToString(hashMap).replace('/t=(\d+)/g', new Date().getTime())
    //     // var new_hashMap = hashMap
    //     // new_hashMap.put('t', '112223444')
    //     // console.log('new_hashMap:', new_hashMap.get('t'))
    //     // instance_ryw.f117786f = true
    //     let result = this["a"](hashMap, hashMap2, str, str2, z, str3);
    //     let result_test = call_new_sign(hashMap, hashMap2, str, str2, z, str3)
    //     console.log(`ryw.mo140317a resul: =${result}`);
    //     console.log('send time:', new Date().getTime())
    //     return result;
    // };

    /**
     * 运算 headers中的x-falco_id, client_trace_id
     */
    // let MtopNetworkProp = Java.use("mtopsdk.mtop.common.MtopNetworkProp");
    // let InnerProtocolParamBuilderImpl = Java.use("mtopsdk.mtop.protocol.builder.impl.InnerProtocolParamBuilderImpl");
    // InnerProtocolParamBuilderImpl["buildExtParams"].implementation = function (c24666a, map) {
    //     get_caller_function(this)
    //     get_fields(c24666a)
    //     // console.log('object.prototype.propertyisenumerable:', String.prototype.isPrototypeOf(map))
    //     var mtp = c24666a.d.value
    //     echo('native c24666a.d.value:'+mtp.clientTraceId.value)
    //     // console.log('buildExtParams map::', mapToString(map))
    //     console.log('run before map:', map.get('x-falco-id'))
    //     var new_mtp_d = MtopNetworkProp.$new()
    //     console.log('new:', new_mtp_d)
    //     console.log(HttpHeaderConstant.CLIENT_TRACE_ID.value, new_mtp_d.clientTraceId)
    //     map.put(HttpHeaderConstant.CLIENT_TRACE_ID.value, mtp.clientTraceId.value)
        
    //     echo(map.get('x-c-traceid'))
    //     console.log(`InnerProtocolParamBuilderImpl.buildExtParams is called: c24666a=${c24666a}, map=${map}`);
    //     this["buildExtParams"](c24666a, map);
    //     console.log('run after map.falco_id:', map.get('x-falco-id'))
    //     console.log('client_trace_id:', c24666a.f87780d)
    // };

    /**
     * buildParams(C24666a)
     *  返回headers的所有params
     * 
     */
    // InnerProtocolParamBuilderImpl["buildParams"].implementation = function (a) { //需要分析a参数
    //     echo('buildParams 运行')
    //     echo(a)                                         // C24666a a,b,c,d..g,...k request各对象内容
    //     a.class.getFields().forEach(function(field){
    //         console.log('field${field}', field)
    //     })
    //     echo(`a:${a.a}`)
    //     echo('d:',a.f87780d)
    //     echo(`c:${a.d.value}`)
    //     echo(`e:${a.e}`)
    //     echo(`f:${a.f}`)
    //     echo(`g:${a.g}`)
    //     echo(`h:${a.h}`)
    //     echo(`i:${a.i}`)
    //     echo(`j:${a.j}`)
    //     echo(`k:${a.k}`)
    //     echo(`l:${a.l}`)
    //     echo(`m:${a.m}`)
    //     echo(`n:${a.n}`)
    //     echo(`o:${a.o}`)
    //     var result = this['buildParams'](a)
    //     console.log('buildParams result:', mapToString(result))     // 包含所有params
    //     echo(typeof result)
    //     get_caller_function(this)
    //     return result
    // };

    // let rxz = Java.use("tb.rxz");
    // rxz["b"].implementation = function (a) {
    //     echo('rxz.b(params):'+a.d.value.clientTraceId.value)
    //     let result = this["b"](a);
    //     console.log(`rxz.mo140277b result=${result}`);
    //     return result;
    // };

    /**
     * 重点, request所有数据中转
     */
    // let ryj = Java.use("tb.ryj");
    // ryj["a"].overload('java.lang.String', 'mtopsdk.framework.domain.a').implementation = function (str, c24666a) {
    //     echo(`c24666a.h.value:${c24666a.h.value}`)
    //     echo(`c24666a.g.value.falcoId:${c24666a.g.value.falcoId.value}`)
    //     var a = c24666a
    //     echo(`a:${a.a}`)
    //     echo(`b:${a.b.value}`)
    //     echo(`c:${a.c.value}`)
    //     echo(`d:${a.d.value}`)
    //     echo(`e:${a.e}`)
    //     echo(`f:${a.f}`)
    //     echo(`g:${a.g.value.falcoId}`)
    //     echo(`h:${a.h}`)
    //     echo(`i:${a.i}`)
    //     echo(`j:${a.j}`)
    //     echo(`k:${a.k}`)
    //     echo(`l:${a.l}`)
    //     echo(`m:${a.m}`)
    //     echo(`n:${a.n}`)
    //     echo(`o:${a.o}`)
    //     echo(`ryj.mo140285a is called: str=${str}, c24666a.d.value=${c24666a.d.value.clientTraceId.value}`);
    //     // _a时一个list 分别要调用list中的函数对数据进行处理
    //     var a = this._a.value
    //     echo(`_a:${this._a.value.class}`)
    //     for(var i=0; i<a.size(); i++){
    //         echo(a.get(i))
    //     }
    //     var result = this["a"](str, c24666a);
    //     echo(`ryj 运行结束, c24666a.d.value:${c24666a.d.value.clientTraceId.value}`)
    // };

    /**
     * 这个函数将falcoId 填充到 clientTraceId
     */
    // let ryd = Java.use("tb.rya");
    // ryd["b"].overload('mtopsdk.framework.domain.a').implementation = function (c24666a) {
    //     var a = c24666a
    //     echo(`a:${a.a}`)
    //     echo(`b:${a.b.value}`)
    //     echo(`c:${a.c.value}`)
    //     echo(`d:${a.d.value}`)
    //     echo(`e:${a.e}`)
    //     echo(`f:${a.f}`)
    //     echo(`g:${a.g.value.falcoId}`)
    //     echo(`h:${a.h}`)
    //     echo(`i:${a.i}`)
    //     echo(`j:${a.j}`)
    //     echo(`k:${a.k}`)
    //     echo(`l:${a.l}`)
    //     echo(`m:${a.m}`)
    //     echo(`n:${a.n}`)
    //     echo(`o:${a.o}`)
    //     console.log(`rxw.m140279a is called: c24666a=${c24666a.d.value}`);
    //     let result = this["b"](c24666a);
    //     console.log(`rxw.m140279a is ca_end: c24666a=${c24666a.d.value}`);
    //     console.log(`rxw.m140279a result=${result}`);
    //     return result;
    // };


    // ryj["b"].implementation = function (str, c24666a) {
    //     console.log(`ryj.mo140286b is called: str=${str}, c24666a=${c24666a.d.value.clientTraceId.value}`);
    //     this["b"](str, c24666a);
    // };

    //  ryw["a"].overload('java.util.HashMap', 'java.util.HashMap', 'java.lang.String', 'java.lang.String', 'boolean', 'java.lang.String').implementation = function (hashMap, hashMap2, str, str2, z, str3) {
    //     console.log('/r/n',new Date().getTime(),'/r/n')
    //     echo(hashMap.class)
    //     var t = hashMap.get('t')
    //     hashMap.remove('t')
    //     hashMap.put('t', t + 2)
    //     console.log("\r\n",t,hashMap.get('t'))
    //     get_fields(hashMap)
    //     console.log(`ryw.mo140317a is called: hashMap=${hashMap}, hashMap2=${hashMap2}, str=${str}, str2=${str2}, z=${z}, str3=${str3}`);
    //      let result = this["a"](hashMap, hashMap2, str, str2, z, str3);
    //      console.log(`ryw.mo140317a result=${result}`);
    //      get_caller_function(this)
    //      return result;
    //  };

    // ryw["a"].overload('java.util.HashMap', 'java.util.HashMap').implementation = function (hashMap, hashMap2) {
    //     console.log(`ryw.mo140316a is called: hashMap=${hashMap}, hashMap2=${hashMap2}`);
    //     let result = this["a"](hashMap, hashMap2);
    //     console.log(`ryw.mo140316a result=${result}`);
    //     return result;
    // };

    // let MtopBusiness = Java.use("com.taobao.tao.remotebusiness.MtopBusiness");
    // MtopBusiness["startRequest"].overload('int', 'java.lang.Class').implementation = function (i, cls) {
    //     console.log(`MtopBusiness.startRequest is called: i=${i}, cls=${cls}`);
    //     this["startRequest"](i, cls);
    // };

    // MtopBusiness["startRequest"].overload('java.lang.Class').implementation = function (cls) {
    //     console.log(`MtopBusiness.startRequest is called: cls=${cls}`);
    //     this["startRequest"](cls);
    // };

    // MtopBusiness["syncRequest"].implementation = function () {
    //     console.log(`MtopBusiness.syncRequest is called`);
    //     let result = this["syncRequest"]();
    //     console.log(`MtopBusiness.syncRequest result=${result}`);
    //     return result;
    // };

    // let MtopBuilder = Java.use("mtopsdk.mtop.intf.MtopBuilder");
    // MtopBuilder["asyncRequest"].overload('mtopsdk.mtop.common.MtopListener').implementation = function (mtopListener) {
    //     console.log(`MtopBuilder.asyncRequest is called: mtopListener=${mtopListener}`);
    //     echo(mtopListener.$className)       // $Proxy14 ?
    //     echo(typeof mtopListener)
    //     console.log('fields:', mtopListener.class.getFields())
    //     let result = this["asyncRequest"](mtopListener);
    //     console.log(`MtopBuilder.asyncRequest result=${result}`);
    //     return result;
    // };

    // let MtopBuilder = Java.use("mtopsdk.mtop.intf.MtopBuilder");
    // MtopBuilder["asyncRequest"].overload('mtopsdk.mtop.common.MtopListener').implementation = function (mtopListener) {
    //     console.log(`MtopBuilder.asyncRequest is called: mtopListener=${mtopListener}`);
    //     echo(`this.fullTraceId:${this.fullTraceId}`)
    //     echo('mtopListerner fields:')
    //     echo(mtopListener.class)
    //     get_fields(mtopListener)                // ? 看不到字段
    //     echo('mtopListerner fields end;')
    //     let result = this["asyncRequest"](mtopListener);
    //     get_fields(result.mtopContext.value.k.value)
    //     echo('分割:')
    //     echo(result)
    //     get_fields(result)
    //     return result;
    // };
    /**
     * 重点 生成 falcoId
     */
    // let FullTraceAnalysis = Java.use("com.taobao.analysis.fulltrace.FullTraceAnalysis");
    // FullTraceAnalysis["createRequest"].implementation = function (str) {
    //     console.log(`FullTraceAnalysis.createRequest is called: str=${str}`);
    //     let result = this["createRequest"](str);
    //     console.log(`FullTraceAnalysis.createRequest result=${result}`);
    //     echo(get_falcoId())
    //     return result;
    // };

    // ryw["b"].overload('mtopsdk.mtop.global.MtopConfig').implementation = function (mtopConfig) {
    //     console.log(`ryw.m140328b is called: mtopConfig=${mtopConfig}`);
    //     this["b"](mtopConfig);
    // };

    // let rzi = Java.use("tb.rzi");
    // rzi["a"].implementation = function (c24718c) {
    //     console.log(`rzi.mo140343a is called: c24718c=${c24718c}`);
    //     let result = this["a"](c24718c);
    //     console.log(`rzi.mo140343a result=${result}`);
    //     return result;
    // };
/*
mtopsdk.mtop.protocol.builder.impl.InnerProtocolParamBuilderImpl.buildExtParams(Native Method)
mtopsdk.mtop.protocol.builder.impl.InnerProtocolParamBuilderImpl.buildParams(Taobao:359)
mtopsdk.mtop.protocol.builder.impl.InnerProtocolParamBuilderImpl.buildParams(Native Method)
tb.rxz.b(Taobao:45)     
tb.ryj.a(Taobao:60)     // 运算得到clientTraceId
mtopsdk.mtop.intf.MtopBuilder.asyncRequest(Taobao:941)
mtopsdk.mtop.intf.MtopBuilder.asyncRequest(Taobao:957)
com.taobao.tao.remotebusiness.MtopBusiness.startRequest(Taobao:292)
com.taobao.tao.remotebusiness.MtopBusiness.startRequest(Taobao:242)
com.taobao.message.sync_sdk.CrossPlatformSyncSDK$DefaultHostApplication$5.startRequest(Taobao:756)
调用顺序:
    buildParams(c24666a):
        ryw:mo140317a(hansMap, hashMap2, str, str2, z, ..)      
            return hashMap  // headers 主要参数
        buildExtParams(c24666a, map)    // 运算给map添加client-trace-id, x-falco-id
        return map  // 所有params
        
                             
    ryj.mo140286b  
    ryj.mo140285a
    rxz.b
    ryw.mo140317a return x-sgext,x-sign

        

*/
/*
x-sgext=JBP7cw5K+mWm8t5wdTcT+HPKQ8tAz1DJRctK2ELKQNhQykTJRchDyUbKRthDzUSdR8lByxCZS5lGzkefUMpCylDMUMtD2EPLQ8xQz1DKUMpQylDKUMlQyVDLUMJQyVDLUMtQy1DLUMtQy1DLUNgW2EPYQ9hEnUTMRphQy0PLQ8tQy1DOSs9Qy1DYQthC2EDYQ9gJuB2qUMtQ21PPFttT20PYQ6QynAC5MqoyvzK5S7o7jDLGLM8syVXMRd1C3UPdRphVw1XDVctVzlXOVc5Vy1XKS89ByUXdBpEApEakQ91D3UXNFs5Fw0rJVctVy1XLVctVw1XILM0sylXJVc5VwlWYVZ9VykKkRKRByV7KQchezErWQsNey17LXsteyl7LXstezEGkSqRC1kPWLJosyVXLVcosmSzMS9ZC1kLJQNZC1kWkEKRC1kXWQtZD1kLLQM5emUHWQc9C1kOkF6QmrT2pJco9qSbKNsYsnSzIXstezkLMXs1K1kLKQMssykOkI4w2zBCWAZMbtjLUR7oys1y6OLkZoUO/NIIEujK6MroyujK6OY4dmhvKQ6kxzxm+IpghlAGQEZcQljHPNboWvwSwN4wyujK6ProysCqNHK0YuizKQqRD3UPVSsNDw0HNVcxVy1XMVcpD3UTdQ91Cw1XKQslVzFXMLMpBpELWQcpewkrNLMpApDKoGLoLjDLUMrEmujK6MoIyuRi6EqoyojK4NrosykWkQ6RCzCzKXsleykrWQMJeykfOXsleyV7OStZFyV7IQaQ=&nq=WIFI&data={"tryRequest":"false","address":"河北省 保定市 涞水县 108国道 靠近东河山村 ","globalLbs":"{\"globalAreaCode\":\"510104\",\"globalCityCode\":\"510100\",\"globalLat\":\"30.633133\",\"globalLng\":\"104.110722\",\"globalProvinceCode\":\"510000\",\"globalTownCode\":\"510104030\"}","cityCode":"130600","provinceCode":"130000","utdid":"Zs7Pnkn0r40DAKSy/CBlF7cX","latitude":"39.633542","edition":"{\"actualLanguageCode\":\"zh-CN\",\"countryId\":\"CN\",\"countryNumCode\":\"156\",\"currencyCode\":\"CNY\",\"realEditionCode\":\"CN\",\"selectedEditionCode\":\"CN\"}","containerParams":"{\"newface_home_main\":{\"baseCacheTime\":0,\"bizParams\":{\"currentTabType\":\"home\",\"deviceLevel\":\"m\",\"globalAreaCode\":\"510104\",\"globalCityCode\":\"510100\",\"globalLat\":\"30.633133\",\"globalLng\":\"104.110722\",\"globalProvinceCode\":\"510000\",\"globalTownCode\":\"510104030\",\"guessModelVersion\":\"20230917\",\"isComplexTexture\":true,\"lastVersion\":\"v7\",\"multiTab\":\"{\\\"tabId\\\":\\\"pindao_0009\\\"}\",\"new2021UIEnable\":true,\"newContentEnable\":\"true\",\"newface_home_main\":{\"framework\":\"microservices\"},\"screenHeight\":\"1280\",\"screenWidth\":\"720\",\"selectTab\":\"home\"},\"clientReqOffsetTime\":0,\"clientReqTime\":1726311647388,\"deltaCacheTime\":0,\"passParams\":{\"lastVersion\":\"v7\",\"miniAppRelation\":\"isAdd\",\"passParamTopBarCatTabSwitch\":\"true\",\"poiRefreshTime\":\"1726280542\",\"topBarHourParams\":\"{\\\"sysFormBizType\\\":\\\"tab_hour\\\",\\\"hideLeftIcon\\\":\\\"true\\\",\\\"title\\\":\\\"小时达\\\",\\\"type\\\":\\\"hourlyDelivery\\\",\\\"darkTitleColor\\\":\\\"#aaaaaa\\\",\\\"subTabRemindIconType\\\":\\\"alwayShow\\\",\\\"selectedTitleColor\\\":\\\"#111111\\\",\\\"refreshSearchText\\\":\\\"true\\\",\\\"titleColor\\\":\\\"#666666\\\",\\\"sysFormResourceName\\\":\\\"小时达\\\",\\\"dyFormSubId\\\":340411,\\\"addToPos3\\\":\\\"true\\\",\\\"isImmersive\\\":\\\"false\\\",\\\"darkSelectedTitleColor\\\":\\\"#111111\\\",\\\"id\\\":\\\"74085\\\",\\\"hideRightIcon\\\":\\\"true\\\"}\",\"topBarTheme\":\"{\\\"areaSwitch_img\\\":\\\"https://gw.alicdn.com/tfs/TB1q69XzuT2gK0jSZFvXXXnFXXa-108-108.png\\\",\\\"indicatorColor\\\":\\\"#FF5000\\\",\\\"bgImg\\\":\\\"\\\",\\\"darkTitleColor\\\":\\\"#aaaaaa\\\",\\\"selectedTitleColor\\\":\\\"#111111\\\",\\\"isFestival\\\":\\\"false\\\",\\\"bgColor\\\":\\\"#FAFAFA\\\",\\\"titleColor\\\":\\\"#666666\\\",\\\"darkIndicatorColor\\\":\\\"#ffffff\\\",\\\"areaSwitch_darkImg\\\":\\\"https://gw.alicdn.com/tfs/TB1QIahzpP7gK0jSZFjXXc5aXXa-108-108.png\\\",\\\"areaSwitch_darkModeImg\\\":\\\"https://gw.alicdn.com/tfs/TB1q69XzuT2gK0jSZFvXXXnFXXa-108-108.png\\\",\\\"darkSelectedTitleColor\\\":\\\"#111111\\\",\\\"areaSwitch_lightImg\\\":\\\"https://gw.alicdn.com/tfs/TB1q69XzuT2gK0jSZFvXXXnFXXa-108-108.png\\\"}\",\"visualAllInOne\":\"{}\",\"whiteNavi\":\"true\"},\"realBaseCacheTime\":1726296992560,\"requestType\":\"multiTabSelect\"},\"newface_home_sub\":{\"baseCacheTime\":0,\"bizParams\":{\"currentExposureItemID\":\"\",\"currentRequestType\":\"multiTabSelect\",\"deviceLevel\":\"m\",\"firstPagePVID\":\"36f317d4-e9da-4b7c-aaa3-98b667e0894e\",\"framework\":\"microservices\",\"guessModelVersion\":\"20230917\",\"homePagePopResult\":\"{}\",\"hundredClickItemId\":\"\",\"isComplexTexture\":true,\"latestHundredItem\":\"681034575545,807946785567,711317781693,667349687734,799548398944\",\"miniAppRelation\":\"isAdd\",\"multiTab\":\"{\\\"tabId\\\":\\\"pindao_0009\\\"}\",\"new2021UIEnable\":true,\"overlayTime\":\" \",\"screenHeight\":\"1280\",\"screenWidth\":\"720\",\"selectTab\":\"home\",\"supportDynamicLayout\":\"true\",\"tb_homepage_clientCache_lbs\":{}},\"clientReqOffsetTime\":0,\"clientReqTime\":1726311647393,\"deltaCacheTime\":0,\"pageParams\":{\"firstRequestInAdvance\":-1,\"lastPage\":false,\"pageNum\":0,\"requestInAdvance\":10,\"virtualPageNum\":0},\"passParams\":{\"contains_common_field\":\"hit_taobao_fresh\",\"dynamicLayoutEnable\":\"true\",\"firstPagePVID\":\"36f317d4-e9da-4b7c-aaa3-98b667e0894e\",\"iconTheme\":\"{\\\"backgroundColor\\\":\\\"#00FFFFFF\\\",\\\"clipCorner\\\":\\\"true\\\",\\\"backgroundImage\\\":\\\"\\\",\\\"festivalBgColor\\\":\\\"#FFFFFF\\\",\\\"bottomGraColor\\\":\\\"#00FFFFFF\\\",\\\"topGraColor\\\":\\\"#00FFFFFF\\\"}\",\"lastVersion\":\"v7\",\"lbsClientStore\":\"{\\\"TMALL_MARKET\\\":{\\\"biz\\\":\\\"TMALL_MARKET\\\",\\\"chls\\\":[{\\\"chl\\\":\\\"TMALL_MARKET_B2C\\\",\\\"stores\\\":[],\\\"simpleStores\\\":[{\\\"ext\\\":{\\\"relatedType\\\":\\\"CHOOSE_ADDR\\\",\\\"businessType\\\":\\\"REGION_TYPE_REGION\\\",\\\"relateId\\\":\\\"13916638513\\\"},\\\"storeId\\\":\\\"112\\\"}]}],\\\"ts\\\":1726296992708},\\\"HM_YOUXUAN\\\":{\\\"biz\\\":\\\"HM_YOUXUAN\\\",\\\"chls\\\":[{\\\"chl\\\":\\\"TAOBAO_FRESH_MUL_CHANNEL\\\",\\\"stores\\\":[],\\\"simpleStores\\\":[{\\\"ext\\\":{},\\\"storeId\\\":\\\"1081900490\\\"}]}],\\\"ts\\\":1726296992708}}\",\"nextPageBackupKeyPrefix\":\"prod_backup_88_2_5_smu:ul_3_android_10.39.10_base\",\"personalLastPosParam\":\"{\\\"serverPersonalBizListMap\\\":{\\\"3007\\\":[{\\\"area\\\":\\\"icon\\\",\\\"bizType\\\":\\\"baiyibutie\\\",\\\"posIndex\\\":0},{\\\"area\\\":\\\"icon\\\",\\\"bizType\\\":\\\"miaosha\\\",\\\"posIndex\\\":1},{\\\"area\\\":\\\"icon\\\",\\\"bizType\\\":\\\"zhibo\\\",\\\"posIndex\\\":2},{\\\"area\\\":\\\"icon\\\",\\\"bizType\\\":\\\"elm\\\",\\\"posIndex\\\":3},{\\\"area\\\":\\\"icon\\\",\\\"bizType\\\":\\\"paim\\\",\\\"posIndex\\\":4},{\\\"area\\\":\\\"icon\\\",\\\"bizType\\\":\\\"tamllnongchang\\\",\\\"bubbleAioRes\\\":{\\\"bubbleList\\\":[{\\\"contentType\\\":\\\"static\\\",\\\"contentValue\\\":\\\"免费\\\",\\\"isGuide\\\":false,\\\"showForce\\\":false,\\\"utLogMap\\\":{\\\"x_content_id\\\":\\\"\\\",\\\"x_sub_biz_type\\\":\\\"tamllnongchang\\\",\\\"up_pvid\\\":\\\"a2a288e2-756f-4ddb-be36-f72da8c71020\\\",\\\"x_bubble_type\\\":0,\\\"x_content_value\\\":\\\"免费\\\",\\\"match_score\\\":0.0,\\\"match_way\\\":\\\"Igraph\\\",\\\"priority\\\":0.0,\\\"x_content_type\\\":\\\"static\\\",\\\"x_abid\\\":\\\"350779\\\",\\\"tpp_buckets\\\":\\\"29418#0#350779#0\\\",\\\"score\\\":3.007786376086844,\\\"x_ts\\\":1726296992,\\\"x_verison\\\":\\\"standard_edition\\\",\\\"x_id\\\":1211,\\\"group_id\\\":\\\"4025\\\",\\\"x_biz_type\\\":\\\"icon\\\",\\\"x_pvid\\\":\\\"a2a288e2-756f-4ddb-be36-f72da8c71020\\\"}}],\\\"subBizType\\\":\\\"tamllnongchang\\\"},\\\"posIndex\\\":5},{\\\"area\\\":\\\"icon\\\",\\\"bizType\\\":\\\"hbqdao\\\",\\\"posIndex\\\":6},{\\\"area\\\":\\\"icon\\\",\\\"bizType\\\":\\\"ddz\\\",\\\"bubbleAioRes\\\":{\\\"bubbleList\\\":[{\\\"contentType\\\":\\\"static\\\",\\\"contentValue\\\":\\\"single_message_bar_1\\\",\\\"isGuide\\\":false,\\\"showForce\\\":false,\\\"utLogMap\\\":{\\\"x_content_id\\\":\\\"\\\",\\\"x_sub_biz_type\\\":\\\"ddz\\\",\\\"up_pvid\\\":\\\"a2a288e2-756f-4ddb-be36-f72da8c71020\\\",\\\"x_bubble_type\\\":0,\\\"x_content_value\\\":\\\"single_message_bar_1\\\",\\\"match_score\\\":0.0,\\\"match_way\\\":\\\"Igraph\\\",\\\"priority\\\":0.0,\\\"x_content_type\\\":\\\"static\\\",\\\"x_abid\\\":\\\"350779\\\",\\\"tpp_buckets\\\":\\\"29418#0#350779#0\\\",\\\"score\\\":0.021082975492670075,\\\"x_ts\\\":1726296992,\\\"x_verison\\\":\\\"standard_edition\\\",\\\"x_id\\\":868627,\\\"group_id\\\":\\\"4025\\\",\\\"x_biz_type\\\":\\\"icon\\\",\\\"x_pvid\\\":\\\"a2a288e2-756f-4ddb-be36-f72da8c71020\\\"}}],\\\"subBizType\\\":\\\"ddz\\\"},\\\"posIndex\\\":7},{\\\"area\\\":\\\"icon\\\",\\\"bizType\\\":\\\"sqxxx\\\",\\\"posIndex\\\":8},{\\\"area\\\":\\\"icon\\\",\\\"bizType\\\":\\\"yfd\\\",\\\"bubbleAioRes\\\":{\\\"bubbleList\\\":[{\\\"contentType\\\":\\\"dynamic\\\",\\\"contentValue\\\":\\\"https://img.alicdn.com/imgextra/i2/O1CN01kdyuYZ23b5Mk1OXNp_!!6000000007273-54-tps-183-144.apng\\\",\\\"isGuide\\\":false,\\\"showForce\\\":false,\\\"utLogMap\\\":{\\\"x_content_id\\\":\\\"\\\",\\\"x_sub_biz_type\\\":\\\"yfd\\\",\\\"up_pvid\\\":\\\"a2a288e2-756f-4ddb-be36-f72da8c71020\\\",\\\"x_bubble_type\\\":0,\\\"x_content_value\\\":\\\"https://img.alicdn.com/imgextra/i2/O1CN01kdyuYZ23b5Mk1OXNp_!!6000000007273-54-tps-183-144.apng\\\",\\\"match_score\\\":0.0,\\\"match_way\\\":\\\"Igraph\\\",\\\"priority\\\":0.0,\\\"x_content_type\\\":\\\"dynamic\\\",\\\"x_abid\\\":\\\"350779\\\",\\\"tpp_buckets\\\":\\\"29418#0#350779#0\\\",\\\"score\\\":0.017069850523226716,\\\"x_ts\\\":1726296992,\\\"x_verison\\\":\\\"standard_edition\\\",\\\"x_id\\\":1731,\\\"group_id\\\":\\\"4025\\\",\\\"x_biz_type\\\":\\\"icon\\\",\\\"x_pvid\\\":\\\"a2a288e2-756f-4ddb-be36-f72da8c71020\\\"}}],\\\"subBizType\\\":\\\"yfd\\\"},\\\"posIndex\\\":9},{\\\"area\\\":\\\"icon\\\",\\\"bizType\\\":\\\"rmhd\\\",\\\"posIndex\\\":10},{\\\"area\\\":\\\"icon\\\",\\\"bizType\\\":\\\"lvx\\\",\\\"posIndex\\\":11},{\\\"area\\\":\\\"icon\\\",\\\"bizType\\\":\\\"aljkayf\\\",\\\"posIndex\\\":12},{\\\"area\\\":\\\"icon\\\",\\\"bizType\\\":\\\"xiany\\\",\\\"posIndex\\\":13},{\\\"area\\\":\\\"icon\\\",\\\"bizType\\\":\\\"taopp\\\",\\\"posIndex\\\":14},{\\\"area\\\":\\\"icon\\\",\\\"bizType\\\":\\\"taobrs\\\",\\\"posIndex\\\":15},{\\\"area\\\":\\\"icon\\\",\\\"bizType\\\":\\\"taogc\\\",\\\"posIndex\\\":16},{\\\"area\\\":\\\"icon\\\",\\\"bizType\\\":\\\"uxsy\\\",\\\"posIndex\\\":17},{\\\"area\\\":\\\"icon\\\",\\\"bizType\\\":\\\"tmallqiche\\\",\\\"posIndex\\\":18},{\\\"area\\\":\\\"icon\\\",\\\"bizType\\\":\\\"tmallgj\\\",\\\"posIndex\\\":19},{\\\"area\\\":\\\"icon\\\",\\\"bizType\\\":\\\"fresh\\\",\\\"posIndex\\\":20},{\\\"area\\\":\\\"icon\\\",\\\"bizType\\\":\\\"tmallcs\\\",\\\"posIndex\\\":21},{\\\"area\\\":\\\"icon\\\",\\\"bizType\\\":\\\"chongzzx\\\",\\\"posIndex\\\":22},{\\\"area\\\":\\\"icon\\\",\\\"bizType\\\":\\\"zzgz\\\",\\\"posIndex\\\":23},{\\\"area\\\":\\\"icon\\\",\\\"bizType\\\":\\\"qbpd\\\",\\\"posIndex\\\":24}]}}\",\"poiRefreshTime\":\"1726280542\",\"visualAllInOne\":\"{}\"},\"realBaseCacheTime\":0,\"requestType\":\"multiTabSelect\"}}","userId":"4060247732","nick":"tb793426967","areaCode":"130623","poiRefreshTime":"1726302518","cityName":"保定","areaName":"涞水县","countryCode":"CN","countryName":"中国","provinceName":"河北省","gatewayVersion":"2.0","longitude":"115.109334","commonBizParams":"{\"abTestInfo\":\"{\\\"performanceAbTestInfo\\\":\\\"{\\\\\\\"bucketId\\\\\\\":\\\\\\\"20002\\\\\\\",\\\\\\\"bucketType\\\\\\\":\\\\\\\"test\\\\\\\",\\\\\\\"testId\\\\\\\":\\\\\\\"tb_start_exp\\\\\\\"}\\\"}\",\"deviceInfo\":\"{\\\"deviceModel\\\":\\\"phone\\\"}\",\"lastClickItemId\":\"\",\"networkStatus\":\"poor\",\"ucpFatigueData\":\"{\\\"c\\\":0,\\\"r\\\":\\\"0|21423|500000002|9448|40168|47852|20240911|8#\\\"}\"}"}&pv=6.3&sign=azYBCM006xAAJ+E+eT6h7Q+64VtGJ+E36Msd0YapLh6+eHEi0xNS+R6c0R7/1Em/A96jMCcFbk5KjcVzQn3VO7iLt65hN+E34PfhN+&deviceId=AqG65eu5Gpa1TRU6pBy5oeIvE-NbacZRFaSYUrt0qtBF&sid=25601ccd9fad1321ce4f2a5cebbd86dd&uid=4060247732&x-features=27&x-app-conf-v=0&x-mini-wua=aYATWQeWMnQKIPRY4BgCaU+9rQkHzuHwkHZBPVQbrkPR9gS9K5q5RJqXPWBcPXoBWQt7AUydahDRbVyouFzPojTwWXuXFo08xD6FoCFL4AqkcUBy26b+2MgxRkajYJqV2FIjl5O1oyan87ePwVyK5Kma2ohKsg+J2BhtwoDjTPeD/NvwKDzei11usIDgnSBOYGKY=&appKey=21646297&api=mtop.taobao.wireless.home.newface.awesome.get&umt=9PkBUyJLPO/6swKR7jqIji6UIHxjKPea&lat=39.633542&f-refer=mtop&lng=115.109334&utdid=Zs7Pnkn0r40DAKSy/CBlF7cX&netType=WIFI&x-app-ver=10.39.10&extdata=openappkey=DEFAULT_AUTH&x-c-traceid=04C92WDn&ttid=703304@taobao_android_10.39.10&t=1726311647&v=1.0&x-falco-id=04C92WDn&x-page-url=http://m.taobao.com/index.htm&x-page-name=com.taobao.tao.welcome.Welcome&user-agent=MTOPSDK/3.1.1.7 (Android;12;Xiaomi;2206122SC) DeviceType(Phone)
*/
});
