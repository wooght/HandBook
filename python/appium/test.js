function mapToString(hash_map) {
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

var split_str = '************************************************************************'
Java.perform(function () {
    if(Java.available){
        console.log("Android Version:",Java.androidVersion);
    }
    var SwitchConfig = Java.use('mtopsdk.mtop.global.SwitchConfig');
    var MtopResponse = Java.use('mtopsdk.mtop.domain.MtopResponse');
    var StreamOtherResponse = Java.use('com.alibaba.android.nextrpc.stream.internal.response.StreamOtherResponse');
    var NetworkCallbackAdapter = Java.use('mtopsdk.mtop.network.NetworkCallbackAdapter')
    var StreamNetworkCallbackAdapter = Java.use('mtopsdk.mtop.network.StreamNetworkCallbackAdapter')
    var b = Java.use('mtopsdk.network.domain.b')
    var a = Java.use('mtopsdk.framework.domain.a')
    var e = Java.use("mtopsdk.network.impl.e")

    var security_b = Java.use('mtopsdk.security.util.b')
    var security_c = Java.use("mtopsdk.security.util.c")
    var ryw = Java.use("tb.ryw")
    var MtopConvert = Java.use('mtopsdk.mtop.util.MtopConvert')

    // var C24701b = Java.use('mtopsdk.network.domain.C24701b')

    // var IpChange = Java.use('com.android.alibaba.p069ip.runtime.IpChange')


    // 关闭spdy协议
    SwitchConfig.isGlobalSpdySwitchOpen.overload().implementation = function () {
        // var ret = this.isGlobalSpdySwitchOpen.apply(this, arguments);
        // console.log('start:' + ret)
        return false;
    };
    // 加密模块 列表,详情都调用 返回的是各种秘钥
    // security_b.a.overload('java.lang.String').implementation = function(str){
    //     console.log('security_a:bArr', this.a(str))
    //     return this.a(str)
    // }

    // 接口里面提取数据  估计和 request有关而非Response
    // ryw.a.overload('java.util.Map', 'java.lang.String', 'boolean').implementation = function(map, str, z){
    //     console.log('ryw.a(map, str, boolean):', map.get('data'))     // map.get('data') 接口里面的数据 但没有看到详情和列表
    //     return this.a(map, str, z)
    // }
    // ryw.a.overload('java.util.Map', 'java.lang.String').implementation = function(map, str){
    //     console.log('ryw.a(map, str):', map.get('data'))     // map.get('data') 
    //     return this.a(map, str)
    // }

    // 正常二进制码, 转换后的二进制码
    // MtopConvert.jsonToOutputDO.overload('[B', 'java.lang.Class').implementation = function(b, cls){
    //     console.log('jsontooutputdo:', b)
    //     return this.jsonToOutputDO(b, cls)
    // }


    MtopResponse.parseJsonByte.overload().implementation = function(){
        this.parseJsonByte()
        var dataJsonObject = this.dataJsonObject.value
        var originJsonObject = this.originJsonObject.value
        // console.log(dataJsonObject)
        console.log('\r\n-------------------------------------------------------------------------')
        // console.log(this.bytedata.value)
        console.log(split_str+"\r\n", this.api.value, this.v.value)
    };
    // MtopResponse.$init.overload("java.lang.String", "java.lang.String").implementation = function(str,str1){
    //     console.log(this.retMsg)
    //     return this.$init(str, str1)
    // };
    // MtopResponse.$init.overload("java.lang.String", "java.lang.String", "java.lang.String","java.lang.String").implementation = function(str,str1, str2, str3){
        
    //     this.$init(str, str1, str2, str3)
    //     console.log('str:', str)
    // };
    /**
     * 明天还是从这里出发 找到调用此方法的位置
     */
    // MtopResponse.setBytedata.overload("[B").implementation = function(bArr){
    //     this.setBytedata(bArr)
    //     if(bArr[0]==123){
    //         console.log('bArr', bArr[0])
    //     }else{
    //         console.log('bArr !123:', bArr[0])
    //     }
    // };


    // StreamOtherResponse.setByteData.overload("[B").implementation = function(bArr){
    //     this.setByteData(bArr)
    //     console.log('StreamOtherResponse bArr', bArr[0])
    // };
    // NetworkCallbackAdapter.onFinish.overload("mtopsdk.network.domain.b", "java.lang.Object", "boolean").implementation = function(bVar, obj, z){
    //     this.onFinish(bVar, obj, z)
    //     console.log('final b bVar:', bVar)
    // };

    // StreamNetworkCallbackAdapter.$init.overload("mtopsdk.framework.domain.a").implementation = function(aVar){
    //     this.$init(aVar)
    //     console.log('a aVar:', aVar)    // 得到值 mtopsdk.framework.domain.a@6e8db15
    //     console.log('a aVar.j', aVar.j)
    //     console.log('a aVar.f24933a', aVar.f24933a)
    //     console.log('a aVar.c', aVar.c)
    //     console.log('a aVar.g', aVar.g.value)
    //     console.log('a aVar.m', aVar.m.data)
    // }

    // 参数.g为数据流(转换后的数据流)
    StreamNetworkCallbackAdapter.buildMtopResponse.overload('mtopsdk.network.domain.b').implementation = function(bArr){
        console.log('\r\n\r\n\r\n\r\n')
        // console.log('buidMtopResponse bVar:', bArr)
        // var result = this.buildMtopResponse(bArr)
        // console.log('mtopresponse.bytedata:', result.bytedata.value)
        // console.log('mtopresponse.mtopcontext:', this.mtopContext)
        bArr.class.getFields().forEach(function(field){
            console.log('field${field}', field)
        })
        var g_value = bArr.g.value
        if(g_value != null){
            
            
            console.log('bArr.a:', bArr.a.value)    // request headers
            console.log('bArr.b:', bArr.b.value)    // 200 状态
            console.log('bArr.c:', bArr.c.value)    // 
            console.log('bArr.d:', bArr.d.value)    // 

            console.log('bArr.e:', bArr.e.value)    // 
            console.log('bArr.f:', bArr.f.value)    // 
            // console.log('bArr.g:', bArr.g.value)    // 正常二进制
            console.log('bArr.h:', bArr.h.value)    // tb.ryq@a7ae814
            // console.log('bArr.i:', bArr.i.value)    // 文本内容
            console.log('bArr.j:', bArr.j.value)    // null
            console.log('bArr.$ipChange:', bArr.$ipChange)    // 
        }
        
        return this.buildMtopResponse(bArr)
    }

    // var a = Java.use("mtopsdk.network.domain.b$a");
    // a["a"].overload('[B').implementation = function (bArr) {
    //     console.log(`a.m99362a is called: bArr=${bArr}`);
    //     let result = this["a"](bArr);
    //     console.log(`a.m99362a result=${result}`);
    //     return result;
    // };

    // var C24708e = Java.use("mtopsdk.network.impl.e");
    // C24708e["a"].overload('[B', 'com.alibaba.fastjson.JSONObject').implementation = function (bArr, jSONObject) {
    //     console.log(`C24708e.m99394a is called: bArr=${bArr}, jSONObject=${jSONObject}`);
    //     this["a"](bArr, jSONObject);
    // };

    // var C24708e = Java.use("mtopsdk.network.impl.e");
    // C24708e["a"].overload('[B', 'java.lang.String', 'int', 'int').implementation = function (bArr, str, i, i2) {
    //     console.log(`C24708e.m99395a is called: bArr=${bArr}, str=${str}, i=${i}, i2=${i2}`);
    //     this["a"](bArr, str, i, i2);
    // };

    // var C24708e = Java.use("mtopsdk.network.impl.e");
    // C24708e["a"].overload('[B', 'java.util.Map').implementation = function (bArr, map) {
    //     console.log(`C24708e.m99396a is called: bArr=${bArr}, map=${map}`);
    //     this["a"](bArr, map);
    // };

    // var C24708e = Java.use("mtopsdk.network.impl.e");
    // C24708e["a"].overload('mtopsdk.network.impl.e', '[B', 'java.util.Map').implementation = function (c24708e, bArr, map) {
    //     console.log(`C24708e.m99390a is called: c24708e=${c24708e}, bArr=${bArr}, map=${map}`);
    //     this["a"](c24708e, bArr, map);
    // };
    
    // let C24708e = Java.use("mtopsdk.network.impl.e");
    // C24708e["a"].overload('[B').implementation = function (bArr) {
    //     if(Math.max(bArr) > 128){
    //         console.log(`C24708e.m99391a is called: bArr=${bArr}`);
    //     }else{
    //         console.log('type bArr:', typeof(bArr))
    //         // console.log('bArr name', Object.values(bArr))
    //         console.log('bArr name', bArr)
    //     }
    //     this["a"](bArr);
    // };

    // 详情页才走这,正常二进制
    // let C24708e = Java.use("mtopsdk.network.impl.e");
    // C24708e["onDataReceived"].implementation = function (progressEvent, obj) {
    //     console.log(`------------------------: progressEvent=${progressEvent.getBytedata()}, obj=${obj}`);
    //     this["onDataReceived"](progressEvent, obj);
    // };
    let ParcelableNetworkListenerWrapper = Java.use("anetwork.channel.aidl.adapter.ParcelableNetworkListenerWrapper");
    ParcelableNetworkListenerWrapper["dispatchCallback"].implementation = function (b, obj) {
        console.log(`ParcelableNetworkListenerWrapper.dispatchCallback is called: b=${b}, obj=${obj}`);
        console.log('dispatchcallback params obj:', Object.keys(obj))
        console.log('dispatchcallback params obj.out:', obj.out)
        // 强制类型转换
        var ProgressEvent = Java.use('anetwork.channel.aidl.DefaultProgressEvent')
        try{
            var oo = Java.cast(obj, ProgressEvent)
            console.log('dispatchcallback params oo.mContext:', oo.out.value)
            console.log('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\r\n')
        } catch {
            console.log('is not defaultprogressevent')
        }
        
        this["dispatchCallback"](b, obj);
    };

    // 详情页返回正常二进制,列表页返回加密二进制
    // let DefaultProgressEvent = Java.use("anetwork.channel.aidl.DefaultProgressEvent");
    // DefaultProgressEvent["getBytedata"].implementation = function () {
    //     console.log(`DefaultProgressEvent.getBytedata is called`);
    //     let result = this["getBytedata"]();
    //     console.log(`==================== result=${result}`);
    //     return result;
    // };

    
    // 明文,像headers    详情走这里,列表不走这
    /**
     * Response{ code=200, message=SUCCESS, headers{null=[HTTP/1.1 200 OK], s_tid=[213e36fd17256258692297383ed3db]
    */
    // StreamNetworkCallbackAdapter.onResponse.overload("tb.ryn", "mtopsdk.network.domain.b").implementation = function(rynVar, bVar){
    //     this.onResponse(rynVar, bVar)
    //     console.log('on Response b bVar:', bVar)
    // }

    // 正常二进制码 已经转换后的二进制 详情页走g(两次), 列表页走的c
    // b.$init.overload("mtopsdk.network.domain.b$a").implementation = function(aVar){
    //     this.$init(aVar)
    //     console.log('===>', this.g)
    //     var b_list = this.g.value
    //     if(b_list==undefined){
    //         console.log('b aVar g: null')
    //     }else{
    //         console.log('b aVar g[0]:', b_list)
            
    //     }
    //     console.log('b aVar c:', this.c.value)  // 有g则无c,有c则无g    有c则为SUCCESS
    // }

    // 正常二进制,已经转换后的二进制
    // e.a.overload('[B', 'com.alibaba.fastjson.JSONObject').implementation = function(bArr, JSONObject){
    //     this.a(bArr, JSONObject)
    //     console.log('e.a.overload:bArr', bArr)
    // }

    // StreamNetworkCallbackAdapter.$init.overload('mtopsdk.framework.domain.a').implementation = function(c246661){
    //     this.$init(c246661)
    //     if(c246661 == null){
    //         console.log('c246661:', 'null')
    //     }else{
    //         console.log('c246661:', c246661)
    //         console.log('mtopContext:', c246661.f87778b)
    //     }
    //     return this.$init(c246661)
    // }
    /**
     *  b 为可见内容 类似 headers 无具体内容
     */
    // StreamNetworkCallbackAdapter.onReceiveData.overload('mtopsdk.network.domain.b').implementation = function(b){
    //     this.onReceiveData(b)
    //     console.log('onReceiveData.mtopContext', this.mtopContext.f87784h)
    //     console.log('onReceiveData.c24701b:', b)
    // }

    // 应该是Response 返回值二进制基类
    // a.$init.overload().implementation = function(){
    //     this.$init()
    //     console.log('a.init b:', this.k)
    //     return this.$init()
    // }
});
/**
 * api 数据处理方向:    StreamNetworkCallbackAdapter.buildMtopResponse  用的 mtopsdk.network.domain.b
 */