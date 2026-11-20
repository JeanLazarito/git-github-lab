<?php
require 'db.php';

$message = "";

if (isset($_GET['registered'])) {
    $message = "Registration successful! Please login.";
}

if (isset($_POST['login'])) {
    $username = $_POST['username'];
    $password = $_POST['password'];

    $find = $connection->prepare("SELECT * FROM users WHERE username = ?");
    $find->execute([$username]);
    $user = $find->fetch();

    if ($user && password_verify($password, $user['password'])) {
        $_SESSION['full_name'] = $user['full_name'];
        header("Location: welcome.php");
        exit;
    } else {
        $message = "Wrong username or password.";
    }
}
?>
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <form method="post" class="box">
        <h1>Login</h1>

        <p class="message"><?= $message ?></p>

        <label>Username</label>
        <input type="text" name="username" required>

        <label>Password</label>
        <input type="password" name="password" required>

        <button type="submit" name="login">Login</button>

        <p>No account yet? <a href="register.php">Register</a></p>
    </form>
</body>
</html>