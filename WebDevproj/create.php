<!Doctype html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create Account</title>
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
            margin-top: 50px;
        }
        form{
            text-align: center;
            
        }
        header {
            text-align: center;
            margin-top: 20px;
        }
        a.login {
            text-allign: center;
            font-size: 20px;
            text-decoration: none;
            color : #2111c8;
            center;
        }
        a.login:hover {
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
    <a href="menu.php">See Menu</a>
    <a href="login.php" style="background-color: #a20808; color: white; padding: 10px; text-decoration: underline; font-size: 40px;">Login</a>
</header>
<div class="back">
<br>
<center>
<a href="login.php" class="login">Login With Existing Account</a>
</center>
<footer>
<form action="create.php" method="post">
Username: <input type="text" name="username"><br><br>
Password: <input type="password" name="password"><br><br>
First Name: <input type="text" name="firstname"><br><br>
Last Name: <input type="text" name="lastname"><br><br>
<br>


<input type="submit" value="Create Account">
</form>

<?php
    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "project";
    $conn = new mysqli($servername, $username, $password, $dbname);
    if (isset($_POST["username"]) && isset($_POST["password"]) && isset($_POST["firstname"]) && isset($_POST["lastname"])) {
    $n = $_POST["username"];
    $p = $_POST["password"];
    $f = $_POST["firstname"];
    $l = $_POST["lastname"];
    
    $sql = "INSERT INTO user (username, password, firstname, lastname) VALUES ('$n', '$p', '$f', '$l')";
    if ($conn->query($sql) === TRUE) {
        echo "<center>";
        echo "New account created successfully";
        echo "</center>";

    } else {
        echo "<center>";
        echo "Error: " . $sql . "<br>" . $conn->error; 
        echo "</center>";
    }
    $conn->close();
    }   


?>
</footer>
</div>
</body>
</html>