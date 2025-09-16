# Генерация случайного имени файла
random_name <- paste0("scatter_script_", sample(10000:99999, 1), ".R")
cat("Создаю скрипт с именем:", random_name, "\n")

# Код для диаграммы рассеяния
r_code <- '# Генерация случайных данных
set.seed(123) # Для воспроизводимости
x <- rnorm(100, mean = 50, sd = 10)
y <- 2 * x + rnorm(100, mean = 0, sd = 5)

# Создание диаграммы рассеяния
plot(x, y, 
     main = "Диаграмма рассеяния",
     xlab = "X переменная",
     ylab = "Y переменная",
     pch = 19,
     col = "blue")

# Добавление линии регрессии
abline(lm(y ~ x), col = "red", lwd = 2)

# Сохранение графика в файл
filename <- paste0("scatter_plot_", format(Sys.time(), "%Y%m%d_%H%M%S"), ".png")
png(filename)
plot(x, y, 
     main = "Диаграмма рассеяния",
     xlab = "X переменная",
     ylab = "Y переменная",
     pch = 19,
     col = "blue")
abline(lm(y ~ x), col = "red", lwd = 2)
dev.off()

cat("График сохранен в файл:", filename, "\n")'

# Запись кода в файл
writeLines(r_code, random_name)

# Выполнение скрипта
source(random_name)