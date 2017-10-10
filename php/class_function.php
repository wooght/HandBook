<?php
/*
	面向对象-By wooght 2017
*/
//error_reporting(E_ERROR | E_WARNING | E_PARSE); 开启运行时错误报告
//E_ALL  所有错误
//error_reporting(0);//关闭错误报告
include("e.php");
e('<h1>面向对象class_function</h1>');
e('[$this->$one=$two]变量作为变量名');
class a{
	public function __construct($one="one",$two=false){
		$this->$one=$two;
	}
	protected function one(){
		e("is protected");
	}
	private function three(){
		e("is private");
	}
}
$a=new a("one","一");
e($a->one,1);
class b extends a{
	//extends 类继承,单一继承
	public function ask(){
		$this->one();
		//$this->three();
	}
}
e("[public>protected>private],三个权限关系,private子类也不能直接访问");
$b=new b();
$b->ask();
e("",1);
/*

function __construct() - 构造函数(public),里面可以用很多参数.这里的参数与实例化对象的参数必须相同
function __destruct() - 析构函数(public),用于一个类的结束时释放内存,关闭文件等等

public - 定义公开的属性,类的内部外部都可以对它定义的属性进行读取修改.
private - 封装定义的属性(私有),类的内部可以对它定义的属性进行读取和修改,而外部(包括子类)不能.外部只能通过内部的函数才能访问它定义的属性,也可以通过这种方法改变值.
protected - 同private,但是子类拥有对定义属性的访问和修改权限
*/
e("[__construct,__destruct],构造函数,析构函数");
class c_struct{
	public function __construct(){
		e("class a construct OK",1);
	}
	public function __destruct(){
		e("class a destruct ok");
		e("destruct 在没有主动访问时,当程序结束时/类使用结束时自动访问.");
	}
}
$a=new c_struct();
e("[__set(),__inset()]set用法");
class c_set{
	public function __set($name,$values){
		if(!isset($this->$name)){
			$this->$name=$values;
		}
	}
	public function __isset($name){
		e(isset($this->$name));
	}
	public function e_us(){
		e("function_name:".__FUNCTION__);
		e("class_name:".__CLASS__);
		e("",1);
	}
}
//这里对$a进行从新定义,之前的$a被释放,那么__destruct会触发
$a=new c_set();
$a->__set("one","一");
e($a->one."set成功",1);
e("[__FUNCTION__,__CLASS__],类系统常量");
$a->e_us();
e("[method_exists(obj/objname,method_function)],判断类中是否定义method_function方法.");
e(method_exists($a,"aabc")?"method exists":"method not exists",1);
e("[class_exists(objname)],判断是否已经定义类");
e(class_exists("c_set")?"class exists":"class not exists",1);

e("[static]静态方法/属性");
class c_static{
	public static $a=100;//定义静态属性
	const __WOOGHT__="const wooght";//定义常量
	public static function say(){
		e("static 方法访问成功,静态方法访问成功!");
	}
	public function ask(){
		e(self::__WOOGHT__);
		e(self::$a);//内部访问常量,静态属性的方法.
	}
}
/*
final
 - 只能用于定义类和类里面的方法,不能定义属性
 - 被final定义的类和方法不能被子类继承和方法覆盖.

static - 在类中用于描述成员属性和方法是静态的.实例的对象是不能访问到static定义的方法和属性的
	类内部访问静态属性可以用self::属性名,类名称::属性名
	静态方法不能访问非静态属性以及方法
*/
$c=new c_static();
e(c_static::$a);
e($c::$a);
c_static::say();
$c::say();
e("",1);
e("[const]定义常量,self::的用法");
e(c_static::__WOOGHT__);
e("实例化访问常量:".$c::__WOOGHT__);
$c->ask();
e("",1);

e("[__call],定义的方法不存在时,触发此函数");
class c_call{
	function __call($name,$values){
		e($name." method 没有找到,传递参数为:");
		e($values);
	}
}
$d=new c_call();
e($d->abcd("a","b"),1);

//单例模式
/*
单例类：

	所有的单例类至少拥有以下三种公共元素：
 
	它们必须拥有一个构造函数，并且必须被标记为private。
	它们拥有一个保存类的实例的静态成员变量。
	它们拥有一个访问这个实例的公共的静态方法
	有一个空的__clone（）方法，防止被复制或在克隆
*/
class instance{
	private $db;
	static private $_instance; 
	private function __construct(){
		$this->db="db_name";
	}
/* 	private __clone(){
		e("clone error");
		//克隆为空，防止克隆
	} */
	public static function getInstance(){
		if(self::$_instance==NULL){
			self::$_instance=new self();
		}
		return self::$_instance;
	}
	public function ask($name){
		$this->a=$name;
	}
}
e("[getInstance],单例模式");
$in=instance::getInstance();
$in->ask("in");
$bn=instance::getInstance();
e($bn->a,1);//这里输出内容还是$in设置的变量，之实例化一次

//调用函数
e("[spl_autoload_register(),__autoload()],调用函数");
function load($name){
	e($name."类不存在,是否调用".$name.".php文件");
}
//load函数要通过spl_autoload_register()函数触发
spl_autoload_register("load");
/*
function __autoload($class){
	e($class."类不存在,是否调用".$class.".php文件");
}
__autoload()函数会自动触发
*/
$load=new wooght();
e("",1);

/*
抽象类，接口
abstract - 声明抽象方法抽象类的关键字
 - 抽象方法是指没有抽象类的方法,及没有{}的方法.
 - 抽象类是指里面至少有一个抽象方法的类
 - 抽象方法和抽象类都必须用abstract来修饰
 - 抽象类里面可以有不是抽象方法的方法
 - 抽象方法不能是private属性的

abstract class person
{
public $text;
abstract function fun1();
abstract function fun2();
function fun3(){
...
}
}

class text extends person
{
function fun1()
{
...
}
function fun2()
{
...
}
} - 抽象类不能直接被实例化,而继承它的子类(必须有父类中的所有抽象方法)可以实例化


interface - 声明接口的关键字

 - 接口是特殊的抽象类
 - 接口里面的方法必须全是抽象方法
 - 接口里面不能有变量,只能有常量
 - 接口里面的方法必须都是public属性的
 - 接口继承另一个接口使用extends
implements - 子类去实现接口的所有抽象方法使用的关键字

interface One
{
const constant="constant value";//定义一个常量
function fun1();
function fun2();
}

class two implements One
{
function fun1()
{
...
}
function fun2()
{
...
}
} - 实现了全部方法,可以使用子类去实例化对象了

class Four implements 接口一,接口二,...//继承在前,接口实现在后
{
//必须把所有接口中的方法都实现才能实例化
} - 一个类可以实现多个接口

class Four extends 类名 implements 接口一,接口二,..
{
//所有接口中的方法都要实现才可以实例化
} - 一个类不仅额可以实现多个接口,还可以继承一个类的同上实现多个接口,但一定要把类放在前面
*/