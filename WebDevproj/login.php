



<?php

setcookie("username", "admin", time() - (3600), "/");
unset($_COOKIE["username"]);
session_abort();


    


  

$servername = "localhost";
$username = "root";
$password = "";
$dbname = "project";

$conn = new mysqli($servername, $username, $password, $dbname);


if (isset($_POST["username"]) && isset($_POST["password"])) {
    

$u = $_POST["username"] ?? "";
$p = $_POST["password"] ?? "";


$sql = "SELECT username, password FROM user WHERE username = '$u' AND password = '$p'";
$result = $conn->query($sql);
if ($result->num_rows > 0) {
    while($row = $result->fetch_assoc()) {
        session_start();
        $_SESSION["username"] = $row["username"];
        $_COOKIE["username"] = "admin";
        setcookie("username", "admin", time() + (3600), "/");
        
        header("Location: index.php");
        exit;
    }
} else {
    $loginError = "Invalid username or password.";
}

$conn->close();
}

?>


<!Doctype html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link rel="stylesheet" href="style.css">
    <link rel="icon" href="pizza.png" type="image/x-icon">
    <style>
        body {
            background-color: #333;
                
            }
        div.back {
            background-color: #ffffff;    
            margin-left: 10%;
            margin-right: 10%;
            padding: 20px;
            margin-bottom: 50px;
            margin-top: 50px;
        }
        form{
            text-align: center;
            
        }
        header {
            text-align: center;
            margin-top: 20px;
        }
        a.CreateAccount {
            text-allign: center;
            font-size: 20px;
            text-decoration: none;
            color : #2111c8;
            center;
        }
        a.CreateAccount:hover {
            text-decoration: underline;
            font-size: 25px;
        }

        footer {
            border: 2px solid #000000;
            border-radius: 30px;
            padding: 20px;
            margin-left: 25%;
            margin-right: 25%;
            margin-bottom: 150px;
            margin-top: 50px;
        }
        input[type="submit"] {
            background-color: #000000;
            color: white;
            padding: 10px 20px;
            border: none;
            cursor: pointer;
            font-size: 20px;
        }

        input[type="submit"]:hover {
            background-color: #1a08a2;
            font-size: 25px;
        }
    </style>
</head>

<body>
<header>
    <a href="home.html">Home</a>
    <a href="menu.php">Menu</a>
   <a href="login.php" style="background-color: #a20808; color: white; padding: 10px; text-decoration: underline; font-size: 40px;">Login</a>
</header>
<div class="back">
<br>
<footer>

<center>
<a href="create.php" title="CreateAccount" class="CreateAccount">Create New Account</a></center>

<br>
<h1 style="text-align: center;">Login with existing account</h1>
<br>
<form action="login.php" method="post">
Username: <input type="text" name="username"><br><br>
Password: <input type="password" name="password"><br><br>
<br>
<input type="submit" value="Login">
</form>
<?php
if (isset($loginError)) {
    echo "<p style='color: red; text-align: center;'>$loginError</p>";
}
?>
</footer>
</div>
</body>
</html>