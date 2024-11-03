class HashTable:
    def __init__(self):
        self.table = {}

    def insert(self, key, value):
        self.table[key] = value

    def search(self, key):
        return self.table.get(key, None)

    def delete(self, key):
        if key in self.table:
            del self.table[key]
            print(f"Ключ '{key}' успішно видалено.")
        else:
            print(f"Ключ '{key}' не знайдено.")

hash_table = HashTable()
hash_table.insert("name", "John")
hash_table.insert("age", 25)
print("Пошук 'name':", hash_table.search("name"))

hash_table.delete("name")
print("Пошук 'name' після видалення:", hash_table.search("name"))
