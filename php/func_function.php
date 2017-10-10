<?php
/*
	函数及常量-By wooght 2017
*/
include("e.php");
//时间大于time()才会保存,小于time()就会消失
setcookie("ck",'CK',time()+100);
set_time_limit(0);//设置程序响应时间,0指无限制
e('<h1>函数及常量func_function</h1>');
e("[setcookie(name,value,time,path)],设定cookie");
isset($_COOKIE['ck'])?e($_COOKIE['ck']):e('no cookie');
e("",1);
e(date("H:i:s",1));
$date=date_create("2017-09-12 9:46:50");
e(date_format($date,"Y-m-d H:i:s"));
e(date("y-m-d H:i:s")."北京时间");
date_default_timezone_set("America/New_York");//Asia/Shanghai
e("[date_default_timezone_set(timezone)]设置默认时区");
e(date("Y-m-d H:i:s"),1);
sleep(1);
e("[sleep(num)]程序休眠num秒时间,程序会等num秒才执行完");
e(date("H:i:s"),1);
function ask(){
	//$num=func_get_arg;
	$arr=func_get_args();
	e("[func_get_args()]将函数的参数以数组的形式获取");
	e($arr,1);
	e("[func_get_arg(num)]获取函数第num个参数的值");
	$num=func_get_arg(1);
	e($num,1);
}
if(function_exists("ask")){
	ask(1,2);
	e("[function_exists(func)]检查函数是否定义");
	e("is exist是",1);
}
e("[__FUNCTION__]函数名常量");
function wooght(){
	e(__FUNCTION__,1);
}
wooght();
$GLOBALS['global']="is globals";
e("[默认参数赋值]");
function abc($a="默认"){
	e("默认参数值:".$a);
	e($GLOBALS['global']);//函数内部,类的内部访问全局变量的方法
}
abc();
abc(1);
e("",1);
e("[\$GLOBALS[name]],定义全局变量");
e($global."外部访问");//外部可以直接访问全局变量
e("",1);
e("[constant]系统常量");
e(PHP_VERSION);//PHP版本
e(PHP_OS);//当前系统环境
e("开始".PHP_EOL."结束");//系统换行符,unix则输出:\n,Windows则输出:\r\n
e("[define()],定义常量,区分大小写,[defined],判断是否定义");
define("WOOGHT","我");
if(defined("WOOGHT")) e("is defined");
else e("no defined");
e(WOOGHT,1);//访问自定义常量
e("[\$_SERVER],服务器/运作信息");
e($_SERVER['HTTP_HOST']);//主机地址
e($_SERVER['DOCUMENT_ROOT'],1);//根目录

e("[get_defined_constants]获取已设定的常量,包括系统和自定义的");
e(get_defined_constants(true));

/*
PHP_EOL - 当前操作系统的行尾符,用作换行符的替换用
 - 可以跨平台使用

PHP_VERSION - php版本

PHP_OS - 运行PHP的操作系统

PHP_SAPI - PHP运行方式

$_SERVER['REQUEST_URI'] - 访问此页面所需的URI
 - 输出的地址格式例子:/shiyan/110331/1.php 

$_SERVER['SCRIPT_NAME'] - 包含当前脚本的路径
 - 输出:/shiyan/110331/1.php

$_SERVER['HTTP_HOST'] - 主机地址
 - localhost

$_SERVER['SERVER_NAME'] - 服务器域名
 - localhost

$_SERVER['SCRIPT_FILENAME'] - 当前文件所在位置
 - G:\wwwroot\shiyan\110331\1.php

$_SERVER['DOCUMENT_ROOT'] - 网站根目录
 - G:\wwwroot

$_SERVER['PHP_SELF'] - 脚本文件的绝对地址
 - /shiyan/110331/1.php

$_SERVER['HTTP_CLIENT_IP'] - 客户端（及浏览器）所在的电脑的IP地址

$_REQUEST[]具有$_POST[]和$_GET[]的功能，但速度最慢！

$_SERVER['HTTP_REFERER'] - 值连接/提交到当前页面的父页面
*/