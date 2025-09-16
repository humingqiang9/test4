#!/usr/bin/env Rscript

# Генерируем случайные данные
set.seed(123) # Для воспроизводимости
x <- rnorm(100, mean = 50, sd = 10)
y <- 2 * x + rnorm(100, mean = 0, sd = 5)

# Создаем диаграмму рассеяния
plot(x, y, 
     main = "Диаграмма рассеяния",
     xlab = "Переменная X",
     ylab = "Переменная Y",
     pch = 19,
     col = "blue")

# Добавляем линию регрессии
model <- lm(y ~ x)
abline(model, col = "red", lwd = 2)

# Сохраняем график в файл
filename <- "scatter_plot.png"
png(filename)
plot(x, y, 
     main = "Диаграмма рассеяния",
     xlab = "Переменная X",
     ylab = "Переменная Y",
     pch = 19,
     col = "blue")
abline(model, col = "red", lwd = 2)
dev.off()

cat("Диаграмма рассеяния сохранена в файл:", filename, "\n")