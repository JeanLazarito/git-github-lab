<?php
session_start();

$dbName = "user_accounts_db";
$dbHost = "127.0.0.1";
$dbUser = "root";
$dbPass = "root";

try {
    $connection = mysqli_connect($dbHost, $dbUser, $dbPass, $dbName);
} catch (mysqli_sql_exception $e) {
    header("Location: offlineMsg.php");
    exit();
}
?>