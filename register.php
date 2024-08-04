<!-- templates/register.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Register NFC Key</title>
</head>
<body>
    <h1>Register NFC Key</h1>
    <form action="/register" method="post">
        <input type="text" name="username" placeholder="Username" required>
        <input type="text" name="nfc_key" placeholder="NFC Key" required>
        <button type="submit">Register</button>
    </form>
</body>
</html>
