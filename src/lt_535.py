"""
https://leetcode.com/problems/encode-and-decode-tinyurl

Related:
"""

"""
Note: This is a companion problem to the System Design problem: Design TinyURL.

TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
"""

import random

class Codec:

    def __init__(self):
        self._url_length = 6
        self._url_base = 'http://tinyurl.com'
        self._url_codes = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ'
        self.records = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        # Time: O(n), n is the length of longUrl
        # Space: O(n)
        def generate():
            return '{}/{}'.format(self._url_base, ''.join([self._url_codes[random.randint(0, len(self._url_codes) - 1)] for _ in range(self._url_length)]))

        while True:
            output = generate()
            if output not in self.records:
                self.records[output] = longUrl
                return output

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        # Time: O(1)
        # Space: O(1)
        return self.records[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))


if __name__ == '__main__':
    test_cases = [
    ]

    words = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ'
    def generate(n):
        return 'http://' + ''.join([words[random.randint(0, len(words) - 1)] for _ in range(n)])

    codec = Codec()
    urls = []
    for _ in range(10000):
        urls.append('http://{}'.format(generate(random.randint(10, 30))))

    for url in urls:
        assert url == codec.decode(codec.encode(url))
    print('Passed')
