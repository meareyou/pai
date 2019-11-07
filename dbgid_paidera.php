<?php
require_once 'dbgid_hash.php';
$dbgid=new dbgid_encrypt;
$dbgxcode=file_get_contents(realpath('chiper.enc'));
$dbgid->dbgid_hash($dbgxcode);