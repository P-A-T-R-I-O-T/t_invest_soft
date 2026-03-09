# data/participants_manager.py

import json
import os
from cryptography.fernet import Fernet

# Пути к файлам
KEY_FILE = "data/unique_data/key.key"  # Файл для хранения ключа шифрования
DATA_FILE = "data/unique_data/participants.enc"  # Файл для хранения зашифрованных данных участников

class ParticipantsManager:
    def __init__(self):
        """
        Инициализация менеджера участников.
        При создании объекта:
        - Убеждаемся, что папка data/ существует
        - Загружаем или генерируем ключ шифрования
        - Создаём объект Fernet для шифрования/дешифрования
        """
        # Создаём папку для данных, если её нет
        os.makedirs(os.path.dirname(KEY_FILE), exist_ok=True)
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)  # на всякий случай и для DATA_FILE

        self.key = self.load_or_generate_key()  # Получаем ключ (создаём, если нет)
        self.cipher = Fernet(self.key)  # Объект для шифрования и расшифровки

    def load_or_generate_key(self):
        """
        Пытается загрузить ключ из файла.
        Если файла key.key нет — генерирует новый ключ и сохраняет его.
        Ключ используется для шифрования и расшифровки данных.
        Важно: один и тот же ключ должен использоваться всегда, иначе данные не расшифруются!
        """
        if os.path.exists(KEY_FILE):
            # Ключ уже есть — читаем его из файла
            with open(KEY_FILE, "rb") as f:
                return f.read()
        else:
            # Ключа нет — генерируем новый
            key = Fernet.generate_key()
            # Сохраняем ключ в файл, чтобы использовать в будущем
            with open(KEY_FILE, "wb") as f:
                f.write(key)
            return key

    def add_participant(self, name: str, token: str, is_sandbox: bool = False) -> bool:
        """
        Добавляет нового участника с именем, токеном и флагом песочницы.
        Перед добавлением:
        - Проверяет, что имя и токен не пустые
        - Проверяет, что имя ещё не занято
        Если всё в порядке — шифрует данные и добавляет в файл.

        Возвращает True, если участник успешно добавлен, иначе False.
        """
        if not name or not token:
            print("❌ Ошибка: имя и токен обязательны.")
            return False

        if self.name_exists(name):
            print(f"❌ Ошибка: участник с именем '{name}' уже существует.")
            return False

        # Подготавливаем данные для шифрования
        data = {
            "name": name,
            "token": token,
            "is_sandbox": is_sandbox  # сохраняем статус песочницы
        }
        # Преобразуем данные в строку JSON и шифруем её
        encrypted_data = self.cipher.encrypt(json.dumps(data).encode())

        # Открываем файл в режиме "добавления в бинарном виде" и записываем зашифрованную строку
        # Каждая запись — отдельная строка (с переносом \n)
        with open(DATA_FILE, "ab") as f:
            f.write(encrypted_data + b"\n")

        print(f"✅ Участник '{name}' успешно добавлен. Песочница: {is_sandbox}")
        return True

    def name_exists(self, name: str) -> bool:
        """
        Проверяет, есть ли уже участник с таким именем.
        Для этого:
        - Читает файл построчно
        - Расшифровывает каждую запись
        - Сравнивает имя
        Возвращает True, если имя найдено.
        """
        # Если файла ещё нет — значит, участников нет
        if not os.path.exists(DATA_FILE):
            return False

        try:
            with open(DATA_FILE, "rb") as f:
                for line in f:
                    line = line.strip()  # Убираем пробелы и переносы
                    if not line:  # Пропускаем пустые строки
                        continue
                    # Расшифровываем строку
                    decrypted_data = self.cipher.decrypt(line).decode()
                    # Преобразуем JSON обратно в словарь
                    participant = json.loads(decrypted_data)
                    # Сравниваем имя
            if participant["name"] == name:
                return True
        except Exception as e:
            # Если произошла ошибка (например, повреждённая запись), выводим предупреждение
            print(f"⚠️ Ошибка при чтении файла: {e}")
        return False

    def get_token_by_name(self, name: str) -> str or None:
        """
        Ищет участника по имени и возвращает его токен.
        Используется, например, при входе — чтобы проверить, правильный ли токен ввёл пользователь.
        Возвращает токен (строка) или None, если участник не найден.
        """
        if not os.path.exists(DATA_FILE):
            return None

        try:
            with open(DATA_FILE, "rb") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
            decrypted_data = self.cipher.decrypt(line).decode()
            participant = json.loads(decrypted_data)
            if participant["name"] == name:
                return participant["token"]  # Возвращаем токен
        except Exception as e:
            print(f"⚠️ Ошибка при получении токена: {e}")
        return None

    def get_participant_by_name(self, name: str) -> dict or None:
        """
        Ищет участника по имени и возвращает все его данные (включая флаг песочницы).
        Используется для проверки типа пользователя.
        Возвращает словарь с данными участника или None, если не найден.
        """
        if not os.path.exists(DATA_FILE):
            return None

        try:
            with open(DATA_FILE, "rb") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
            decrypted_data = self.cipher.decrypt(line).decode()
            participant = json.loads(decrypted_data)
            if participant["name"] == name:
                return participant  # Возвращаем все данные участника
        except Exception as e:
            print(f"⚠️ Ошибка при получении данных участника: {e}")
        return None

    def is_sandbox_user(self, name: str) -> bool:
        """
        Проверяет, является ли участник пользователем песочницы.
        Возвращает True, если пользователь песочницы, иначе False (или если не найден).
        """
        participant = self.get_participant_by_name(name)
        if participant and "is_sandbox" in participant:
            return participant["is_sandbox"]
        return False  # По умолчанию считаем реальным пользователем

    def list_participants(self) -> list:
        """
        Возвращает список имён всех участников.
        Используется, например, для выпадающего меню в интерфейсе.
        Возвращает просто список имён: ['Анна', 'Иван', 'Мария']
        """
        names = []
        if not os.path.exists(DATA_FILE):
            return names

        try:
            with open(DATA_FILE, "rb") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    decrypted_data = self.cipher.decrypt(line).decode()
                    participant = json.loads(decrypted_data)
                    names.append(participant["name"])
        except Exception as e:
            print(f"⚠️ Ошибка при чтении списка: {e}")
        return names



    def remove_participant(self, name: str) -> bool:
        """
        Удаляет участника по имени.
        Как работает:
        - Считывает все записи и расшифровывает их
        - Перезаписывает файл, пропуская запись с нужным именем
        Возвращает True, если участник был найден и удалён.
        """
        participants = self.list_all_decrypted()  # Получаем все расшифрованные данные
        success = False  # Флаг: удалили ли кого‑то

        # Перезаписываем файл, не включая удалённого участника
        with open(DATA_FILE, "wb") as f:
            for p in participants:
                if p["name"] != name:
                    # Шифруем и записываем всех, кроме удаляемого
                    encrypted = self.cipher.encrypt(json.dumps(p).encode())
                    f.write(encrypted + b"\n")
                else:
                    success = True  # Нашли и пропустили — значит, удалили

        if success:
            print(f"🗑️ Участник '{name}' удалён.")
        return success



    def list_all_decrypted(self) -> list:
        """
        Вспомогательный метод.
        Возвращает список всех участников в виде словарей (расшифрованных).
        Используется внутри других методов, например, при удалении.
        Не для прямого вызова извне — данные расшифровываются, поэтому нужно быть осторожным.
        """
        participants = []
        if not os.path.exists(DATA_FILE):
            return participants

        try:
            with open(DATA_FILE, "rb") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    decrypted_data = self.cipher.decrypt(line).decode()
                    participant = json.loads(decrypted_data)
                    participants.append(participant)
        except Exception as e:
            print(f"⚠️ Ошибка при расшифровке: {e}")
        return participants
