<?php
/*
	文件函数-By wooght 2017
*/
include("e.php");
e('<h1>正则表达式file_function</h1>');
$dir="file/wooght";
e("[is_dir(dir_str)]判断目录是否存在,[mk_dir(dir_str)]创建目录");
if(!is_dir($dir)){
	mkdir($dir);//mkdir(dir_str,0777)
	e($dir."已经创建",1);
}else{
	rmdir($dir);//非空不能删除
	e($dir."已经删除",1);
}
e("[opendir(str)],打开目录,返回目录对象.[readdir(dirobj)]从目录对象中依次读取/遍历文件夹");
$dir=opendir("./");
//遍历整个文件夹
while($file=readdir($dir)){
	e($file);
}
closedir($dir);//关闭opendir打开的目录
e("",1);
e("[scandir(str)],将目录内容存入数组中");
e(scandir("./"),1);

$dir="file/wooght2";
e("[copy(file,newfile)],copy文件");
if(is_dir($dir)){
	e(copy("file/wooght.txt",$dir."/wooght.txt")?"copy成功":"copy失败");
}else{
	mkdir($dir);
	e(copy("file/wooght.txt",$dir."/wooght.txt")?"copy成功2":"copy失败2");
}
e("",1);
e("[file_exists(dirstr)],判断文件是否存在");
e(file_exists($dir."/wooght.txt")?"wooght.txt存在":"wooght.txt不存在",1);
e("[unlink(dir_str)],删除指定地址文件");
e(unlink($dir."/wooght.txt")?"copy文件删除成功":"copy文件删除失败",1);
e("[dirname(dir)],返回文件的目录部分");
e(dirname("abc/bcd/a.txt"),1);
e("[touch(dir_str)],更新文件创建时间,如果没有文件则创建文件");
e(touch("file/wooght2/a.txt")?"up/mk ok new time=".date("Y-m-d H:i:s"):"no",1);//文件已经存在,则只修改时间.
e("<h1>文件编辑</h1>");
$fdir="file/wooght.txt";
$file=fopen($fdir,"r");
/*
r,只读
r+,读写
w,写   清空文件 无则创建
w+,读写  清空文件 无则创建
a,写，从末尾开始写
a+,读写，从末尾开始写
*/
e("[fopen(dir,type)],打开文件,设置打开方式,[fgetc(fileobj)],读取打开文件的第一个字符");
e(fgetc($file),1);
fclose($file);//关闭fopen()打开的文件
$file=fopen("file/wooght3.txt","r+");
e("[fgets(fileobj,length)],读取文件对象的一行数据,length为指定长度,读取位置为length-1");
e("[fread(fileobj,length)],与fgets()相同,但不受行的限制");
$num=fgets($file,filesize("file/wooght3.txt")+1);
if(!empty($num)){
	e("old num iS :".$num);
	$num*=2;
}else{
	e("old num is empty");
	$num=2;
}
e(fwrite($file,$num."\r\n")?"write ok":"write field",1);
fclose($file);
e("[filesize(dir)],获取文件大小");
e(filesize($fdir),1);
e("[file_get_contents(dir_str)],读取指定文件地址的全部内容");
$file_str=file_get_contents($fdir);
$new_str=mb_substr($file_str,0,strlen($file_str),"utf-8");
e($new_str."mb_substr不转换编码",1);
e("string函数[iconv(now,new,str)],转换字符串的编码形式,编码切换,转换编码");
e(iconv("gbk","utf-8",$file_str),1);
