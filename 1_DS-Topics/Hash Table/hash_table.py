class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        for kv in self.table[index]:
            if kv[0] == key:
                kv[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self.hash_function(key)
        for kv in self.table[index]:
            if kv[0] == key:
                return kv[1]
        return None

    def delete(self, key):
        index = self.hash_function(key)
        for i, kv in enumerate(self.table[index]):
            if kv[0] == key:
                del self.table[index][i]
                return True
        return False

    def __str__(self):
        result = []
        for i, bucket in enumerate(self.table):
            if bucket:
                result.append(f"Index {i}: {bucket}")
        return "\n".join(result)


# Example usage
hash_table = HashTable()

# Insert key-value pairs
hash_table.insert("name", "John Doe")
hash_table.insert("age", 30)
hash_table.insert("city", "New York")

# Retrieve values
print("Name:", hash_table.get("name"))  # Output: John Doe
print("Age:", hash_table.get("age"))  # Output: 30
print("City:", hash_table.get("city"))  # Output: New York

# Delete a key-value pair
hash_table.delete("age")
print("Age after deletion:", hash_table.get("age"))  # Output: None

# Display the hash table
print(hash_table)
