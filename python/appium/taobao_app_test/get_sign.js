function call_new_sign(hashMap, hashMap2, str, str2, z, str3){
    /**
     * ���������ڴ���ʵ������,�����µ�x-sign
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
     * �����ڴ�ʵ������falcoId
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