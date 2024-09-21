

class URLShortener:

    def __init__(self, base_url):
        self.base_url = base_url
        self.url_count = 0
        self.url_dict = dict()

    def add_url(self, url):
        if url in self.url_dict:
            raise ValueError("The URL already exists in the url_dict")
        else:
            self.url_count += 1
            short_url = self.base_url + str(self.url_count)
            self.url_dict[url] = short_url
        return short_url

    def generate_url(self):
        pass

    def display_url(self):
        if not self.url_dict:
            print("The url is not present in dictionary")
        for url, shorturl in self.url_dict.items():
            print(f"{url} ---> {shorturl}")


if __name__ == "__main__":
    shorter = URLShortener("https://short.url/")

    shorter.add_url("https://www.python.com")
    shorter.add_url("https://www.example.com")
    shorter.add_url("https://www.pandas.org")

    shorter.display_url()
