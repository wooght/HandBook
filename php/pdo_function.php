<?php
include("e.php");
set_time_limit(0);
e('<h1>PDO mysql应用PDO_function</h1>');
//config文件内容
$define=array(
	"SQL_TYPE"=>'mysql',
	"SQL_PASSWORD"=>'wooght565758',
	"SQL_USER"=>'root',
	"SQL_HOST"=>'localhost',
	"SQL_DATABASE"=>'wooght_2017'
);
function set_define($arr){
	foreach($arr as $key=>$val){
		if(!defined($key)){
			define($key,$val);
		}
	}
}
set_define($define);
class MY{
	private $db;//PDO对象
	public $sql_str;//sql语句
	private $exeres;//处理结果
	public $result_num;//返回行数
	public $last_id;//自增长最后ID
	public function __construct(){
		$dbh=SQL_TYPE.':host='.SQL_HOST.';dbname='.SQL_DATABASE;
		e($dbh);
		e("[PDO(类型:地址;数据库名,用户,密码)],PDO连接数据库",1);
		$this->db=new PDO($dbh,SQL_USER,SQL_PASSWORD);
		try{
			e("[setAttribute],设置PDO参数",1);
			e("[\$e->getMessage],获取错误信息",1);
			$this->db->setAttribute(PDO::ATTR_ERRMODE,PDO::CASE_NATURAL);
			$this->db->exec("set names 'utf8'");
		}catch (PDOException $e){
			e("MYSQL_ERROR:don't connect");
			e($e->getMessage());//获取错误信息
		}
	}
	public function query($field){
		$return=$this->db->query($field);//result是一个对象,而并非一个数组
		e("[query返回对象:]");
		var_dump($return);e("",1);
		return $return;
	}
	public function query_one($sql){
		$result=$this->db->query($sql);
		//$result->setFetchMode(PDO::FETCH_ASSOC)
		return $result->fetch(PDO::FETCH_ASSOC);//返回一条,设定以关联数组方式返回
	}
	public function exec($str){
		$result=$this->db->exec($str);//exec无结果集返回,只返回处理影响行数
		$this->last_id=$this->db->lastInsertId();
		return $result;
	}
	public function execute($str){
		//prepare预处理,建立处理 返回查询/处理对象
		//prepare=>execute=>fetch 执行非查询类建议使用此方法而不建议使用query方法
		if($result=$this->db->prepare($str)){
			e("[prepare返回对象]");var_dump($result);e("",1);
			//$result->setFetchMode(PDO::FETCH_ASSOC);//设置关联数组方式返回
			if($result->execute()){
				$fetch=$result->fetchAll(PDO::FETCH_ASSOC);//全部返回,并设定放回方式
				/*
				fetchAll(fetch_style,fetch_argument)第二个参数指第几行,默认为全部.
				PDO::FETCH_ASSOC  关联数组
				PDO::FETCH_NUM 索引数组
				PDO::FETCH_BOTH 两者(默认值)
				*/
				//$this->result_num=$result->fetchColumn();
				$this->result_num=count($fetch);
				return $fetch;
			}
		}else{
			e("no execute");
		}
	}
}
$my=new MY();
$sql="select name,age,phone from vip order by id desc limit 1,2";
$result=$my->query($sql);
e("[foreach遍历query查询的内容]");
foreach($result as $row){
	e($row['name']." ".$row['age']." ".$row['phone']);
}
e("",1);
$result=$my->query_one($sql);
e("[只返回一行obj->fetch()]<br />name:".$result['name'],1);
e("[exec,无结果集返回],返回执行影响行数,0指失败/没有操作");
e($my->exec("update vip set name='游客' where name=''")?"有修改":"没有修改");
e($my->exec("insert into vip (name,age,phone)values('".baby_name()."',".rand(18,45).",".phone().")")?"插入成功":"插入失败",1);
e("[PDO->lastInsertId()],获取自增ID");
e("新增ID为:".$my->last_id,1);

e("[execute]查询,[prepare]预查询");
e("[setFetchMode],设置查询返回方式");
$result=$my->execute($sql);//获得一个关联数组
e("[prepare=>execute=>fetchAll返回数组:]");var_dump($result);
e("");
for($i=0;$i<count($result);$i++){
	e($result[$i]['name']." ".$result[$i]['age']." ".$result[$i]['phone']);
}
e("共查询".$my->result_num."条",1);

function baby_name(){
	$first_name=array("王","张","李","邓","杨","蒋","陈","高","苏","黄","唐","田","曾","马","姚","习","蒲","刘","席","伍","梁","吴","于","易","肖","成","欧");
$last_name=array("伟","浩","洁","节","狗狗","子昂","超","川","东","兰","秀","秀群","友","思琪","琦","琴","军","豪","飞","果果","书航","丹月","雨","思思","丝丝","夫夫","甜甜","应","秀文","德华","佳","家辉","嘉辉","程峰","学友","名","佳明","海涛","峰","强","强东","天","哲","哲天","阳","曲","业","金","金晶");
	return $first_name[rand(0,count($first_name)-1)].$last_name[rand(0,count($last_name)-1)];
}
function phone(){
	$first_phone=array("135","136","137","139","189","188","177","159","157","158");
	return $first_phone[rand(0,count($first_phone)-1)].rand(10000000,9999999);
}
/*
事务处理
try {
开启事务
$dbh->beginTransaction();
$dbh->exec(”INSERT INTO `test`.`table` (`name` ,`age`)VALUES ('mick', 22);”);
$dbh->exec(”INSERT INTO `test`.`table` (`name` ,`age`)VALUES ('lily', 29);”);
$dbh->exec(”INSERT INTO `test`.`table` (`name` ,`age`)VALUES ('susan', 21);”);
$dbh->commit();
} catch (Exception $e) {
事务回滚
$dbh->rollBack();
echo “Failed: ” . $e->getMessage();
}
*/
//插入数据供测试

/*
mysql_query()函数应用
e("[mysql_connect()]连接数据库");
$con=mysql_connect("localhost","root","wooght565758");
if($con)e('connect ok');
e("[mysql_select_db()],选择数据库");
mysql_select_db("wooght_2017");
$sql="insert into vip (name,age,phone)values('";
$num=0;
$start_time=time();
e("开始时间:".date("H:i:s",$start_time));
for($i=0;$i<10000;$i++){
	$query=mysql_query($sql_run);
	if($query) $num++;
}
$end_time=time();
e("结束时间:".date("H:i:s",$end_time));
e("用时:".date("H:i:s",abs($start_time-$end_time)-28800));
e("成功:".$num."条,平均速度:".($end_time-$start_time)/$num)."/个";
e("姓:".($first_length+1)."个,名:".($last_length+1)."个");
*/
/*
PHP PDO属性列表
 
 

PDO::PARAM_BOOL
 表示一个布尔类型
 PDO::PARAM_NULL
 表示一个SQL中的NULL类型
 PDO::PARAM_INT
 表示一个SQL中的INTEGER类型
 PDO::PARAM_STR
 表示一个SQL中的SQL CHAR，VARCHAR类型
 PDO::PARAM_LOB
 表示一个SQL中的large object类型
 PDO::PARAM_STMT
 表示一个SQL中的recordset类型，还没有被支持
 PDO::PARAM_INPUT_OUTPUT
 Specifies that the parameter is an INOUT parameter for a stored procedure. You must bitwise-OR this value with an explicit PDO::PARAM_* data type.
 PDO::FETCH_LAZY
 将每一行结果作为一个对象返回
 PDO::FETCH_ASSOC
 仅仅返回以键值作为下标的查询的结果集，名称相同的数据只返回一个
 PDO::FETCH_NAMED
 仅仅返回以键值作为下标的查询的结果集，名称相同的数据以数组形式返回
 PDO::FETCH_NUM
 仅仅返回以数字作为下标的查询的结果集
 PDO::FETCH_BOTH
 同时返回以键值和数字作为下标的查询的结果集
 PDO::FETCH_OBJ
 以对象的形式返回结果集
 PDO::FETCH_BOUND
 将PDOStatement::bindParam()和PDOStatement::bindColumn()所绑定的值作为变量名赋值后返回
 PDO::FETCH_COLUMN
 表示仅仅返回结果集中的某一列
 PDO::FETCH_CLASS
 表示以类的形式返回结果集
 PDO::FETCH_INTO
 表示将数据合并入一个存在的类中进行返回
 PDO::FETCH_FUNC
 PDO::FETCH_GROUP
 PDO::FETCH_UNIQUE
 PDO::FETCH_KEY_PAIR
 以首个键值下表，后面数字下表的形式返回结果集
 PDO::FETCH_CLASSTYPE
 PDO::FETCH_SERIALIZE
 表示将数据合并入一个存在的类中并序列化返回
 PDO::FETCH_PROPS_LATE
 Available since PHP 5.2.0
 PDO::ATTR_AUTOCOMMIT
 在设置成true的时候，PDO会自动尝试停止接受委托，开始执行
 PDO::ATTR_PREFETCH
 设置应用程序提前获取的数据大小，并非所有的数据库哦度支持
 PDO::ATTR_TIMEOUT
 设置连接数据库超时的值
 PDO::ATTR_ERRMODE
 设置Error处理的模式
 PDO::ATTR_SERVER_VERSION
 只读属性，表示PDO连接的服务器端数据库版本
 PDO::ATTR_CLIENT_VERSION
 只读属性，表示PDO连接的客户端PDO驱动版本
 PDO::ATTR_SERVER_INFO
 只读属性，表示PDO连接的服务器的meta信息
 PDO::ATTR_CONNECTION_STATUS
 PDO::ATTR_CASE
 通过PDO::CASE_*中的内容对列的形式进行操作
 PDO::ATTR_CURSOR_NAME
 获取或者设定指针的名称
 PDO::ATTR_CURSOR
 设置指针的类型，PDO现在支持PDO::CURSOR_FWDONLY和PDO::CURSOR_FWDONLY
 PDO::ATTR_DRIVER_NAME
 返回使用的PDO驱动的名称
 PDO::ATTR_ORACLE_NULLS
 将返回的空字符串转换为SQL的NULL
 PDO::ATTR_PERSISTENT
 获取一个存在的连接
 PDO::ATTR_STATEMENT_CLASS
 PDO::ATTR_FETCH_CATALOG_NAMES
 在返回的结果集中，使用自定义目录名称来代替字段名。
 PDO::ATTR_FETCH_TABLE_NAMES
 在返回的结果集中，使用自定义表格名称来代替字段名。
 PDO::ATTR_STRINGIFY_FETCHES
 PDO::ATTR_MAX_COLUMN_LEN
 PDO::ATTR_DEFAULT_FETCH_MODE
 Available since PHP 5.2.0
 PDO::ATTR_EMULATE_PREPARES
 Available since PHP 5.1.3.
 PDO::ERRMODE_SILENT
 发生错误时不汇报任何的错误信息，是默认值
 PDO::ERRMODE_WARNING
 发生错误时发出一条php的E_WARNING的信息
 PDO::ERRMODE_EXCEPTION
 发生错误时抛出一个PDOException
 PDO::CASE_NATURAL
 回复列的默认显示格式
 PDO::CASE_LOWER
 强制列的名字小写
 PDO::CASE_UPPER
 强制列的名字大写
 PDO::NULL_NATURAL
 PDO::NULL_EMPTY_STRING
 PDO::NULL_TO_STRING
 PDO::FETCH_ORI_NEXT
 获取结果集中的下一行数据，仅在有指针功能时有效
 PDO::FETCH_ORI_PRIOR
 获取结果集中的上一行数据，仅在有指针功能时有效
 PDO::FETCH_ORI_FIRST
 获取结果集中的第一行数据，仅在有指针功能时有效
 PDO::FETCH_ORI_LAST
 获取结果集中的最后一行数据，仅在有指针功能时有效
 PDO::FETCH_ORI_ABS
 获取结果集中的某一行数据，仅在有指针功能时有效
 PDO::FETCH_ORI_REL
 获取结果集中当前行后某行的数据，仅在有指针功能时有效
 PDO::CURSOR_FWDONLY
 建立一个只能向后的指针操作对象
 PDO::CURSOR_SCROLL
 建立一个指针操作对象，传递PDO::FETCH_ORI_*中的内容来控制结果集
 PDO::ERR_NONE (string)
 设定没有错误时候的错误信息
 PDO::PARAM_EVT_ALLOC
 Allocation event
 PDO::PARAM_EVT_FREE
 Deallocation event
 PDO::PARAM_EVT_EXEC_PRE
 Event triggered prior to execution of a prepared statement.
 PDO::PARAM_EVT_EXEC_POST
 Event triggered subsequent to execution of a prepared statement.
 PDO::PARAM_EVT_FETCH_PRE
 Event triggered prior to fetching a result from a resultset.
 PDO::PARAM_EVT_FETCH_POST
 Event triggered subsequent to fetching a result from a resultset.
 PDO::PARAM_EVT_NORMALIZE
 Event triggered during bound parameter registration allowing the driver to normalize the parameter name.


*/
?>