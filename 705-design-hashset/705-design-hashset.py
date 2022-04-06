class MyHashSet:

    def __init__(self):
        self.hashSet = []

    def add(self, key: int) -> None:
        if key in self.hashSet:
            pass
        else:
            self.hashSet.append(key)

    def remove(self, key: int) -> None:
        if key in self.hashSet:
            self.hashSet.remove(key)
        else:
            pass

    def contains(self, key: int) -> bool:
        if key in self.hashSet:
            return True
        else:
            return None


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)