class HashMap:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.length = 0
        self.buckets = [[] for _ in range(capacity)]

    def _hash(self, key):
        return abs(hash(key)) % self.capacity

    def put(self, key, value):
        index = self._hash(key)
        bucket = self.buckets[index]
        entry = [key, value]
        for i in bucket:
            if i[0] == entry[0]:
                i[1] = value
                return
        bucket.append(entry)
        self.length += 1

    def get(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]
        for i in bucket:
            if i[0] == key:
                return i[1]
        raise KeyError("Key not found")

    def remove(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket.pop(i)
                self.length -= 1
                return
        raise KeyError("Key not found")

    def contains(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]
        return any(i[0] == key for i in bucket)

    def __repr__(self):
        pairs = []
        for bucket in self.buckets:
            for key, value in bucket:
                pairs.append(f"{key!r}: {value!r}")
        return "{" + ", ".join(pairs) + "}"


    def __len__(self):
        return self.length
