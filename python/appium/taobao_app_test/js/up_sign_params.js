Java.perform(function () {
    if(Java.available){
        console.log("Android Version:",Java.androidVersion);
    }
    // var ClassName=Java.use("com.luoye.test.ClassName");
    // var instance = ClassName.$new();

    var SwitchConfig = Java.use('mtopsdk.mtop.global.SwitchConfig');
    SwitchConfig.isGlobalSpdySwitchOpen.overload().implementation = function () {
        // var ret = this.isGlobalSpdySwitchOpen.apply(this, arguments);
        // console.log('start:' + ret)
        return false;
    };

    var  MapH = Java.use('java.util.HashMap')

    var sign_params = ''
    var now_time = ''

    recv('poke', function onMessage(pokeMessage) {
        console.log('recv(pokie) run:', pokeMessage.data)
        sign_params = pokeMessage.data
        now_time = pokeMessage.now_time
    });
    // function get_new_map(){
    //     Java.cast({'data':123},MapH)
    // }
    let ryw = Java.use("tb.ryw");
    ryw["a"].overload('java.util.HashMap', 'java.util.HashMap', 'java.lang.String', 'java.lang.String', 'boolean', 'java.lang.String').implementation = function (hashMap, hashMap2, str, str2, z, str3) {
        if(hashMap.get('api') == 'mtop.taobao.wireless.home.category'){
            console.log('t:',hashMap.get('t'))
            hashMap.remove('data')
            hashMap.remove('t')
            hashMap.put('data',sign_params)
            hashMap.put('t', now_time)
            console.log('t:',hashMap.get('t'))
        }
        
        // console.log('\r\n',new Date().getTime(),'\r\n')
        // console.log(hashMap.class)
        // console.log(`sign_params:${sign_params}`)
        // send(`${sign_params}`)
        // console.log(`ryw.mo140317a is called: hashMap=${hashMap}, hashMap2=${hashMap2}, str=${str}, str2=${str2}, z=${z}, str3=${str3}`);
        let result = this["a"](hashMap, hashMap2, str, str2, z, str3);
        // console.log(`ryw.mo140317a result=${result}`);
        return result;
    };
});