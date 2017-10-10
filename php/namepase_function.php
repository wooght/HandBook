<?php
//namepase by wooght 2017
namespace Base_one;
include("e.php");
e("引入外部文件，不会并入到命名空间里,公共空间",1);
function abc($str){
	e($str);
}
namespace Base_two;
function abc($str){
	e($str,1);
}
use Base_one;
Base_one\abc("where");//如果不用use 引入base_one,这里将报错，找不到
\Base_one\abc("base_one abc");//前面加了\，表示全局  可以找到。
abc("\表示全局");
namespace Base_one\two;
function abc($str){
	e($str,1);
}
class ask{
	public function __construct($s){
		e($s);
		e(__CLASS__."实例化成功",1);
	}
}
namespace Base_two\two;
function abc(){
	//use Base_one\two;
	\Base_one\two\abc('use 不能用在函数中...');
}
abc();
use Base_two;
Base_two\abc("相对调用");
class ask{
	public function __construct($a){
		e(__CLASS__."实例化成功");
		e($a,1);
	}
}
$a=new ask('本命名空间直接调用');
namespace Base_two\two\three;
use Base_two\two as bt;
$a=new bt\ask("调用给于别名");
$b=new \Base_two\two\ask("如调用上一级的元素,用别名或者全局",1);
//use Base_two\two;
//$c=new Base_two\two\ask('');//报未找到错误
//调用多级空间,如果和当前空间同一级,则只能调用到上一级

namespace Base_one\two\three;
use Base_two;
Base_two\abc("当use有多个引用是,末尾空间名不能一样,可别名替代");
//use Base_two\two;
$b=new Base_two\two\ask("");
use Base_one;
$c=new Base_one\two\ask("引入顶级命名空间,其下的子命名空间也引入");
?>