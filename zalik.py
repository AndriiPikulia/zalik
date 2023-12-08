def analyze_file(file_path):
    try:
        with open(file_path, 'r') as file:
            line_count = 1

            for line in file:
                line = line.strip()  
                words_count = len(line.split()) # Підрахування кількості слів
                symbols_count = len(line) # Підрахування кількості символів

                # Виведення результату для рядка
                print(f"Рядок {line_count}: Слів - {words_count}, Символів - {symbols_count}")
                line_count += 1

    except FileNotFoundError:           # Виведення помилки якщо вказаний невірний шлях до файлу
        print("Не вдалося відкрити файл.")
    except Exception as e:
        print(f"Виникла помилка: {e}")

def main():
    file_path = input("Введіть шлях до текстового файлу: ")
    analyze_file(file_path)

if __name__ == "__main__":
    main()