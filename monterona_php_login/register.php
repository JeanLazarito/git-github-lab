<?php
require 'db.php';

$message = "";

if (isset($_POST['register'])) {
    $full_name = $_POST['full_name'];
    $username = $_POST['username'];
    $password = $_POST['password'];
    $confirm_password = $_POST['confirm_password'];

    // check if the username is already taken
    $check = $connection->prepare("SELECT id FROM users WHERE username = ?");
    $check->execute([$username]);

    if ($check->fetch()) {
        $message = "This account already exists.";
    } elseif ($password != $confirm_password) {
        $message = "Passwords do not match.";
    } else {
        // turn the password into a hash
        $hashed = password_hash($password, PASSWORD_DEFAULT);

        $save = $connection->prepare("INSERT INTO users (full_name, username, password) VALUES (?, ?, ?)");
        $save->execute([$full_name, $username, $hashed]);

        header("Location: login.php?registered=yes");
        exit;
    }
}
?>
<!DOCTYPE html>
<html>
<head>
    <title>Registration</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <form method="post" class="box">
        <h1>Registration</h1>

        <p class="message"><?= $message ?></p>

        <label>Full Name</label>
        <input type="text" name="full_name" required>

        <label>Username</label>
        <input type="text" name="username" required>

        <label>Password</label>
        <input type="password" name="password" required>

        <label>Confirm Password</label>
        <input type="password" name="confirm_password" required>

        <button type="submit" name="register">Register</button>

        <p>Already have an account? <a href="login.php">Login</a></p>
    </form>
</body>
</html>