<?php
/*
	数组函数-By wooght 2017
*/
header("Content-type:text/html;charset=utf-8;");
e('<h1>数组函数array_function</h1>');
function e($str,$h=false){
	echo $str.($h?"<hr />":"<br />");
}
$arr=array(1,2,3);
e("[count(arr)],返回数组元素个数");
var_dump($arr);
echo "<br />";
e(count($arr));
$arr=["a"=>[1,2],"b"=>[3,4]];
print_r($arr);echo "<br />";
e(count($arr),1);
$str="one two three";
e("[explode(str1,str2)],将str2以str1分割组成数组");
print_r(explode(" ",$str));
e(" ",1);
$arr=[1,2,3,"four"];
e("[implode(str1,arr)]将arr元素以str1为连接符连接为一个字符串");
e(implode("-",$arr),1);
e("[join()],功能通implode,但join参数不能变");
e(join(" ",$arr),1);
$arr2=["one","two","three","4"];
$str="one two three 4 one";
e("[str_replace()]前两个参数是数组的情况");
e(str_replace($arr2,$arr,$str),1);
$arr=[1,5,3,4,2];
e("[sort(arr)],对数组进行升序排列,成功返回1,[rsort(arr)]为降序排列");
print_r($arr);
echo "<br />";
sort($arr);
print_r($arr);
echo "<br />";
rsort($arr);
print_r($arr);
e("",1);
$arr=["one"=>[1,2],"two"=>[2,3]];
e("[array_key_exists(key,arr)],判断数组arr中是否出现建指key");
e(array_key_exists("two",$arr)?"YES":"NO",1);
$arr=["one","two","three"];
e("[in_array(obj,arr)]判断给定数值是否出现在数组中");
e(in_array("one",$arr)?"YES":"NO");
$arr=[["one",2],[3,4]];
e(in_array(["one",2],$arr)?"YES":"NO",1);//输出YES
$arr=array("one"=>1,"two"=>2);
e("[array_key(arr)],返回数组所有键值,并以数组方式返回");
print_r(array_keys($arr));
e("",1);
$arr=[1,2,3];
e("[list(a,b..)=arr],以数组的☞以此给变量赋值");
list($a,$b,$c)=$arr;
e($a.$b.$c);
$arr=[[1,2,3],[4,5,6],[7,8,9]];
list($d,$e)=$arr;
var_dump($d);
e("",1);
$arr=[1,2,3];
$arr2=[["a","b"],["c","d"]];
$arr3=["one"=>"ooo","two"=>"ttt"];
var_dump(array_merge($arr,$arr2,$arr3));
$arr=["one"=>1,"two"=>2];
e("[foreach]foreach循环应用,遍历应用");
foreach($arr as $key=>$val){
	e("K至为：".$key.",value值为：".$val);
}
e("",1);





