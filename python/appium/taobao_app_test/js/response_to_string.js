function echo(s){
    console.log(s)
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
Java.perform(function () {
    if(Java.available){
        console.log("Android Version:",Java.androidVersion);
    }
    // var ClassName=Java.use("com.luoye.test.ClassName");
    // var instance = ClassName.$new();

    var SwitchConfig = Java.use('mtopsdk.mtop.global.SwitchConfig');
    SwitchConfig.isGlobalSpdySwitchOpen.overload().implementation = function () {
        // 关闭spdy协议
        return false;
    };

    // let MtopResponse = Java.use("mtopsdk.mtop.domain.MtopResponse");
    // MtopResponse["toString"].implementation = function () {
    //     console.log(`MtopResponse.toString is called`);
    //     let result = this["toString"]();
    //     // console.log(`MtopResponse.toString result=${result.api}`);
    //     return result;
    // };
    // MtopResponse["parseJsonByte"].implementation = function () {
    //     console.log(`MtopResponse.parseJsonByte is called`);
    //     this["parseJsonByte"]();
    //     // console.log(`${this.dataJsonObject}`)
    //     //https://trade-acs.m.taobao.com/gw/mtop.taobao.detail.batchgetdetail/1.0/
    //     get_caller_function(this)
    //     // console.log(this.dataJsonObject)
    // };
    // let MtopRequest = Java.use("mtopsdk.mtop.domain.MtopRequest");
    // MtopRequest["toString"].implementation = function () {
    //     console.log(`MtopRequest.toString is called`);
    //     let result = this["toString"]();
    //     console.log(`MtopRequest.toString result=${result}`);
        
    //     return result;
    // };
    // MtopRequest["getData"].implementation = function () {
    //     console.log(`MtopRequest.getData is called`);
    //     let result = this["getData"]();
    //     console.log(`MtopRequest.getData result=${result}`);
    //     echo(`${this.apiName}`)
    //     return result;
    // };

    let ryw = Java.use("tb.ryw")
    ryw["a"].overload('java.util.HashMap', 'java.util.HashMap', 'java.lang.String', 'java.lang.String', 'boolean', 'java.lang.String').implementation = function (hashMap, hashMap2, str, str2, z, str3) {
        if(hashMap.get('api') == 'mtop.taobao.wireless.home.newface.awesome.get'){
            console.log(`hashMap:${hashMap}, hashMap2:${hashMap2}, str:${str}, str2:${str2}, z:${z}, str3:${str3}`)
        }
        var result = this['a'](hashMap, hashMap2, str, str2, z, str3)
        var result_sign = result.toString()
        return result;
    };
});