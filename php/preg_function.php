<?php
/*
	正则表达式-By wooght 2017
*/
header("Content-type:text/html;charset=utf-8;");
include("e.php");
e('<h1>正则表达式preg_function</h1>');
/*
"+" - 表示前导字符必须在目标中连续出现一次或者多次
"*" - 表示前导字符必须在目标中出现零次或者连续多次
"?" - 标识前导字符必须在目标中连续出现零次或者一次
{n1,n2} - 前导字符必须在目标中连续出现n1,到n2次

\s - 用于匹配单个空格符,包括tab键和换行符
\S - 用于匹配单个空格符之外的所有字符
\d - 用于匹配从0到9的数字
\D - 用语匹配非数字字符 等价于[^0-9]
\w - 用于匹配字母,数字或者下划线字符
\W - 用于匹配所有与\w不匹配的字符
. - 用于匹配除换行符之外的所有字符及所有的单一字符
 - 可以把\s和\S,\w和\W看作互为逆运算
 在javascript中,元字符前面不能有链接字符"+",直接跟在前面内容之后就可以了
 
"^" - 表示规定匹配模式必须出现在目标字符串的开头
"$" - 表示规定模式必须出现在咪表字符串的结尾
"\b" - 表示规定匹配模式必须出现在目标字符串的开头或者结尾两个边界之一
"\B" - 表示规定匹配模式必须在目标字符串的开头和结尾两个边界之内

"|" - 管道符"或"
/to|too|2/ - 将与目标对象当中的to,too,2相匹配
"[^]" -管道符"否定"
/[^a-c]/ - 与目标字符串中除a,b,c之外的任何字符相匹配
 - 当"^"出现在[]内我们就认为是否定符,在[]之外或者没有[]就为定位符

 - 转义字符,用于匹配字符串中的元字符
*/
// /Th\*/ - 匹配Th*,而不能匹配The.
$preg="/^[a-zA-Z0-9]+@[a-zA-Z0-9]+(\.([a-zA-Z0-9]+))+$/";
e("[preg_match(patten,str)],匹配str中的内容是否满足patten规则");
e("wooght@126.com.cn ".(preg_match($preg,"wooght@126.com.cn")?"is email":"no email"));
e("wooght@126.com. ".(preg_match($preg,"wooght@126.com.")?"is email":"no email"),1);

$str="one two three";
e("[preg_split(patten,string)]将string中的元素以patten为界分割为数组");
$arr=preg_split("/\s/",$str,-1);
e($arr,1);

e("[preg_replace(patten,replacement,str)]将str中匹配的patten替换为replacement,并直接返回新string");
$str="one two three-four";
$patten="/\s(\w)+\-/";// /\s\w{3,5}\-/,/\s(\w)+\-/
e(preg_replace($patten,"3-",$str),1);
e("[preg_replace(patten,replacement,str)],参数patten和replacement可同时为数组");
$patten_arr=array("/^(one)/","/\stwo/","/\sthree/");
$replace_arr=array("一","二","三");
e(preg_replace($patten_arr,$replace_arr,$str),1);
e('[\\n,$n反向应用]');
$str="匹配HTML标签-<b>哈哈</b><a>哈哈</b>";
e("源代码为:".htmlspecialchars($str));
$patten="/<(.*)>([^<|>]*)<\/\\1>/";
e("替换HTML代码:".htmlspecialchars((preg_replace($patten,"$2",$str))),1);
e("[?:/?=/?!预处理]");
$str="wooghtabc";
e(preg_match("/wooght(?:w|a)/",$str)?"OK":"NO",1);//?:预匹配
/*
 - ? 应用
 - (?:pattern) 匹配 pattern 但不获取匹配结果，也就是说这是一个非获取匹配，不进行存储供以后使用。这在使用 "或" 字符 (|) 来组合一个模式的各个部分是很有用。例如， 'industr(?:y|ies) 就是一个比 'industry|industries' 更简略的表达式。

 - (?=pattern) 正向预查，在任何匹配 pattern 的字符串开始处匹配查找字符串。这是一个非获取匹配，也就是说，该匹配不需要获取供以后使用。例如，'Windows (?=95|98|NT|2000)' 能匹配 "Windows 2000" 中的 "Windows" ，但不能匹配 "Windows 3.1" 中的 "Windows"。预查不消耗字符，也就是说，在一个匹配发生后，在最后一次匹配之后立即开始下一次匹配的搜索，而不是从包含预查的字符之后开始。 

 - (?!pattern) 负向预查，在任何不匹配 pattern 的字符串开始处匹配查找字符串。这是一个非获取匹配，也就是说，该匹配不需要获取供以后使用。例如'Windows (?!95|98|NT|2000)' 能匹配 "Windows 3.1" 中的 "Windows"，但不能匹配 "Windows 2000" 中的 "Windows"。预查不消耗字符，也就是说，在一个匹配发生后，在最后一次匹配之后立即开始下一次匹配的搜索，而不是从包含预查的字符之后开始
*/