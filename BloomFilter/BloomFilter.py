class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.bit_list = 0

    def hash1(self, str1):
        result = 0
        for c in str1:
            code = ord(c)
            result = result * 17 + code
        return result % self.filter_len

    def hash2(self, str1):
        result = 0
        for c in str1:
            code = ord(c)
            result = result * 223 + code
        return result % self.filter_len

    def add(self, str1):
        self.bit_list |= self.hash1(str1)
        self.bit_list |= self.hash2(str1)
        return None

    def is_value(self, str1):
        return self.bit_list & (self.hash1(str1) | self.hash2(str1)) == self.hash1(
            str1
        ) | self.hash2(str1)
