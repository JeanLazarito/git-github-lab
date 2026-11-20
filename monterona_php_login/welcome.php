<?php
require 'db.php';

// if not logged in, go back to login
if (!isset($_SESSION['full_name'])) {
    header("Location: login.php");
    exit;
}
?>
<!DOCTYPE html>
<html>
<head>
    <title>Welcome</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="box welcome-box">
        <h1>Welcome, <?= $_SESSION['full_name'] ?>!</h1>

        <div class="buttons">
            <a class="button" href="register.php">Register Another Account</a>
            <a class="button" href="logout.php">Exit</a>
        </div>
    </div>
</body>
</html>