<?php
/*
	数学函数-By wooght 2017
*/
include("e.php");
e('<h1>数学函数math_function</h1>');
e("对浮点数进行四舍五入:[round(3.5)],round(数字,小数位数),保留小数位数应用");
e(round(3.5));
e(round(3.1415926,2),1);
e("[sprintf()],格式化字符串,这里是保留小数位数的应用");
e(sprintf("%.2f",3.1415926),1);
e(sprintf("%.2f,%u",3.1415926,"30dd"));//后者输出30
/*
%% - 返回一个百分号 %
%b - 二进制数
%c - ASCII 值对应的字符
%d - 包含正负号的十进制数（负数、0、正数）
%e - 使用小写的科学计数法（例如 1.2e+2）
%E - 使用大写的科学计数法（例如 1.2E+2）
%u - 不包含正负号的十进制数（大于等于 0）
%f - 浮点数（本地设置）
%F - 浮点数（非本地设置）
%g - 较短的 %e 和 %f
%G - 较短的 %E 和 %f
%o - 八进制数
%s - 字符串
%x - 十六进制数（小写字母）
%X - 十六进制数（大写字母）
*/
e("[(int)2.6],对数字声明是整数,去掉小数");
e((int)2.6,1);
e("[(float)3.1415926],声明是浮点数");
e((float)3.1415926,1);
e("[ceil(.18)],向上取整");
e(ceil(1.8),1);
e("[floor(1.8)],向下取整");
e(floor(1.8),1);
e("[abs(-159)],求绝对值");
e(abs(-158),1);
e("[rand(开始,结束),mt_rand(开始,结束)],输出随机数,包括边界");
e(rand(1,3),1);
e("[fmod(8.2,3)],返回余数");
e(fmod(8.2,3),1);
e("[date(),time()],时间函数");
e(date("Y-m-d H:i:s",time()));
e(time());
e(date("Y/m/d H"),time(),1);
e("[++/--,+++/---应用]");
$num=5;
e($num++);//输出5
echo $num."<br />";//输出6
$num=1;
e($num+++1,1);//输出2
$a=1;$b=2;
e($a>$b?"a大":"b大");
echo "$b+$a,运行<br />";//''单引号不运行,双引号运行
e("[max(数组或多个参数)],最大值,[min(数组或多个参数)]求最小值");
e('max(1,4,2)='.max(1,4,2));
e('min(5,26,2,4)='.max(5,26,2,4),1);
e("[+=/==/===]");
$a=1;
$b="1";//===判断是否相等,包括类型
if($a===$b)e("===");
else e("==");
$a+=1;
if($a++==1) e("one");
else e("two");//输出two,判断位置$a==2,判断后$a==3;
e("a的最终值为:".$a,1);
//算法应用
//冒泡排序
e("[冒泡排序][变量存储表达式]");
$arr=[4,2,8,1,9,5,7,10,3,6];
function maopao($arr,$type){
	//type 1为降序 其他为升序
	if(!is_array($arr)) return $arr;
	else{
		e("原序列为:");
		e($arr);
	};
	for($i=0;$i<count($arr);$i++){
		for($j=$i+1;$j<count($arr);$j++){
			$judge=($type==1)?($arr[$j]>$arr[$i]):($arr[$j]<$arr[$i]);//变量存储一个表达式结果
			if($judge){
				list($arr[$i],$arr[$j])=array($arr[$j],$arr[$i]);
/* 				$bridge=$arr[$i];
				$arr[$i]=$arr[$j];
				$arr[$j]=$bridge; */
			}
		}
	}
	e("新序列为:");
	e($arr);
}
maopao($arr,1);
maopao($arr,2);
e("[list(a,b)=arr],批量赋值",1);
//快速排序法
e("[快速排序],[递归的应用]");
function kuick($arr){
	/*
	判断长度而不判断是否是数组
	递归传递的参数都是数组
	*/
	if(count($arr)<=1) return $arr;
	$arr_l=[];
	$arr_r=[];
	for($i=1;$i<count($arr);$i++){
		$arr[0]>$arr[$i]?$arr_l[]=$arr[$i]:$arr_r[]=$arr[$i];
	}
	$new_arr=array_merge(kuick($arr_l),array($arr[0]),kuick($arr_r));
	return $new_arr;
}
$new_arr=kuick($arr);
e("原数组是:");
e($arr);
e("快速排序结果:");
e($new_arr);
?>