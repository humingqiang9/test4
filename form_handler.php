<?php
// Скрипт для обработки формы
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Получаем данные из формы
    $name = htmlspecialchars(trim($_POST['name']));
    $email = htmlspecialchars(trim($_POST['email']));
    
    // Простая валидация
    if (empty($name) || empty($email)) {
        echo "Пожалуйста, заполните все поля.";
        exit;
    }
    
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        echo "Некорректный адрес электронной почты.";
        exit;
    }
    
    // Подготавливаем данные для сохранения
    $data = "Имя: " . $name . "\n";
    $data .= "Email: " . $email . "\n";
    $data .= "Дата: " . date("Y-m-d H:i:s") . "\n";
    $data .= "------------------------\n";
    
    // Сохраняем данные в файл
    $filename = "form_submissions.txt";
    file_put_contents($filename, $data, FILE_APPEND | LOCK_EX);
    
    echo "Форма успешно отправлена!";
} else {
    // Если скрипт вызван напрямую, показываем форму
    ?>
    <!DOCTYPE html>
    <html>
    <head>
        <title>Форма обратной связи</title>
        <meta charset="UTF-8">
    </head>
    <body>
        <h2>Форма обратной связи</h2>
        <form method="post" action="">
            <label for="name">Имя:</label><br>
            <input type="text" id="name" name="name" required><br><br>
            
            <label for="email">Email:</label><br>
            <input type="email" id="email" name="email" required><br><br>
            
            <input type="submit" value="Отправить">
        </form>
    </body>
    </html>
    <?php
}
?>