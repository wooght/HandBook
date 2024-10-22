/**
 * 准备工作
 * 自定义辅助函数
 */
function get_fields(c){
    /**
     * 遍历属性
     */
    // 第一种方法 获取对象的属性及字段
    c.class.getFields().forEach(function(field){
        console.log('field${field}', c[field.name])
    })
    // 第二种方法,获取字典对象的keys
    Object.keys(c).forEach(function(key){
        console.log(`${key}:`, c[key].value)
    })
}
/**'
 * 遍历运行进程栈/栈帖
 */
function get_caller_function(obj){
    var current_thread = Java.use('java.lang.Thread').currentThread();
    var stackTrace = current_thread.getStackTrace();
    var caller_list = []
    stackTrace.forEach(function(stackFrame){
        caller_list.push(stackFrame.toString())
    })
    echo('\ncaller start ,顺序执行:',  1)
    caller_list.reverse() // 倒序操作
    caller_list.forEach(function(it){
        echo(it)
    })
    echo('\ncaller end')
}
/**
 * map转String 两种方法
 * @param {*} hash_map 
 * @returns 
 */
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
function mapString(map){
    var entrySet = map.entrySet();
    var iterator = entrySet.iterator();
    
    while (iterator.hasNext()){
        console.log(iterator.next())
    }
}

/**
 * 需要单独运行app中Java的方法
 * 主动触发APP中函数运行, 需要在hook主体中进行调用
 */
function call_new_sign(hashMap, hashMap2, str, str2, z, str3){
    /**
     * 触发函数 获取sign 等签名
     */
    var ryw = Java.use("tb.ryw")
    var result_sign
    // 触发函数运行
    Java.perform(function(){
        Java.choose('tb.ryw', {
            onMatch: function(instance){
                // console.log(`custom run ryw.a: hashMap=${hashMap}, hashMap2=${hashMap2}, str=${str}, str2=${str2}, z=${z}, str3=${str3}`);
                result_sign = instance['a'](hashMap, hashMap2, str, str2, z, str3)
            },
            onComplete:function(){
                var a = 1
            }
        })
    })
    // 返回结果
    return result_sign
}


/**
 * hook 主体内容
 * 一般操作为对函数进行插桩,获取函数的返回结果或或者变量值
 * 此部分代码与app同时运行
 */
Java.perform(function(){
    /**
     * 基本属性,变量
     */
    Java.available;         // 返回是否可以获取Java运行内容
    Java.androidVersion;    // 返回Android 版本
    let A = Java.use('X.A') // 获取Java中X.A实例
    var o = Java.cast(obj, A)   // 强制转换类型 将obj 转换为A
    
    /**
     * 打桩到某个类实例的某个函数,当app运行到这个函数时,会运行这里的内容
     */
    A['function_name'].overload('[B', 'java.lang.String', 'int').implementation = function(b, s, i){
        // 第一种格式
        // 内容...
    }
    A['function_name'].implementation = function(b, s, i){
        // 第二种格式
        // 内容
        // 运行app自己的内容
        var result = this['function_name'](b, s, i)
        var s = this.mContext       // 获取实例的属性
        // 对数据进行处理
        var j = JSON.parse(s)       // 将字符串转换为json
        var s = JSON.stringify(j)   // 将json转换为字符串
        console.log(`${s}`)         // 输出到控制台
        var s_langth = s.length     // 获取长度
        if(s_langth != 0){
            // 判断语句
            /**
             *  s_langth != null/false/true  js中这些为小写
             */
        }
        // 如果变量为一个对象
        obj.e.value // 获取对象属性值

        // hashMap
        var h = Java.USE('java.util.HashMap')
        h.remove('key')     //删除hashMap元素
        h.put('key', value) // 添加元素
        h.get('key')        // 获取元素
        // 遍历hashMap
        Object.keys(h).forEach(function(k){
            h.get(k)
        })
        // send 发送数据到python ,python需要绑定on_message函数 script.on('message', on_message)
        send({'id':h.get('id'), 'des':h.get('des')})   // 可以是字典,字符串,JSON等
        // send(JSON.stringify(result_dict[simVideoUrlModel.sourceId.value]))

        // 如果有返回值,必须返回内容
        return result
    }
    A.$init.overload('java.util.List').implementation = function(list){
        // 第三种情况,运行构造函数
        // 循环list
        for(var i = 0; i < list.toArray().length; i++){
            console.log(l.get(i))
        }
        list.forEach(function(item){
            console.log(item)
        })
    }
    A["$init"].implementation = function(s){
        // 第四种情况, 运行构造函数
        return this.$init(s)    // 运行构造函数
    }


    /**
     * rpc 与外部python进行函数调用
     * 分三部:
     * 1:定义函数rpc对应关系/接口
     * 2:定义函数变量
     * 3:定义函数
     */
    // 函数变量
    var extract_sign = function(txt, now_time, s){
        hhmm.remove('t')            
            hhmm.put('t', now_time)     // 设置当前请求时间
            st3 = s
            var sign_result = call_new_sign(hhmm, hhmm2, st, st2 ,zz, st3)
            var falcoid = get_falcoId()
            return {'data':`${sign_result}`, 'falcoid':falcoid, 'form_data':hhmm.get('data').toString(), 't':t}
    }
    // 函数对应接口
    rpc.exports = {
        getAppSign:extract_sign,
        setDetailHm:set_detail_hm

    }
})