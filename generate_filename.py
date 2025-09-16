import random
import string

def generate_random_filename():
    """Генерирует случайное имя файла с расширением .py"""
    filename = ''.join(random.choices(string.ascii_lowercase, k=10)) + '.py'
    return filename

if __name__ == "__main__":
    print(generate_random_filename())