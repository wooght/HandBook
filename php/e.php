<?php
/*
	输出函数-By wooght 2017
*/
header("Content-type:text/html;charset=utf-8;");
function e($str,$h=false){
	if(is_array($str)){
		print_r($str);
	}else{
		if(preg_match("/\[(.*)\]/",$str)){
			$str=preg_replace("/\[([^\[\s]*)\]/","<u><b>[$1]</b></u>",$str);
		}
		echo $str;
	}
	echo $h?"<hr />":"<br />";
}