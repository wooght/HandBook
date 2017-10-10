<?php
/*
	字符串函数-By wooght 2017
*/
header("Content-type:text/html;charset=utf-8;");
e('<h1>字符串函数string_function</h1>');
function e($str,$h=false){
	echo $str.($h?"<hr />":"<br />");
}
$a=12345.1;
e("[(string)字符串声明]");
e((string)$a,1);
$str="123456";
e("[strlen(string),字符串长度]");
e(strlen($str),1);
$str="我有三";
e("[mb_strlen(string,chaset)],返回指定编码的字符串长度");
e(mb_strlen($str,"utf-8"),1);
$str="wooght";
e("[substr(string,位置,length)],返回字符串中的一部分");
e(substr($str,2,4),1);
$str="你好吗a";
e("[mb_substr()],返回字符串中的一部分,可指定编码");
e(mb_substr($str,2,2,"utf-8"),1);
e("[ord(char)],返回字符的ASII码");
e(ord("a"),1);
e("[strtotime(string)],将时间转变为时间暨");
e(strtotime("2017-9-11 21:24:55"),1);
e("[microtime()],返回微秒数");
e(microtime(),1);
$a="航城科技-城市";
$b="城";
e("[ucwords(str)],字符串第一个字母大写");
e(ucwords("wooght"),1);
e("[strpos(string1,string2)],返回后者在前者第一次出现的位置");
e(strpos($a,$b),11);
e("[strrchr(string1,string2)],返回后者在前者最后一次出现的位置的以后的所有字符串");
e(strrchr($a,$b),1);
e("[trim(string,char)],移除字符串前后的空白字符或者指定前后两端的字符");
e(trim(" ab>c abc>",">"),1);
e("[htmlspecialchars(html-string)],显示HTML字符--html_entity_decode是反函数");
e(htmlspecialchars("<b>加粗了吗>?</b>"),1);
e("[strip_tags(string)]移除变量中的html,php字符");
e(strip_tags("<?php echo '哈哈'?><b>加粗了吗</b>"),1);
e("[strcmp(string1,string2)],比较两个字符串是否相同,相同为0,不同为-1");
e(strcmp("abc","eee"));
e("[str_replace(str1,str2,str3)],将str3中的str1替换为str2");
e(str_replace("老大","^(*￣(oo)￣)^","我是老大,你是小弟"),1);
e("[json_encode(array)],对数组进行json编码,[json_decode()]为json_encode的反函数");
e(json_encode(array("one"=>"1","two"=>"2")),1);