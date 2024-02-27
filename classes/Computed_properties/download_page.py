import requests
import time as tm


class Web_page_dowload():
    def __init__(self, url: str):
        self._url = url
        self._page = None
        self._load_time_secs = None
        self._page_size = None

    @property
    def url(self):
        return f"This is the url you are trying to use {self._url}"
    
    #Decorator to sett a new value in the "url" attrributes
    @url.setter
    def url(self, new_url):
        self._url = new_url

    @url.deleter
    def url(self):
        del self._url 

    
    @property
    def page(self):
        if self._page is None:
            self.download_page()
        return self._page
    
    @property
    def page_size(self):
        if self._page_size is None:
            self.download_page()
        return self._page_size
    
    @property
    def time_elapsed(self):
        if self._load_time_secs is None:
            self.download_page()
        return self._load_time_secs
    
    #method used to change the info contained on those attributes that are read only and computed
    #only when needed
    def download_page(self):
        start_time = tm.perf_counter()

        with requests.get(self._url) as r:
            self._page = r.text

        end_time = tm.perf_counter()

        self._page_size = len(self._page)
        self._load_time_secs = end_time-start_time


urls = [
    'https://www.google.com',
    'https://www.python.org',
    'https://www.yahoo.com'
]

for url in urls:
    page = Web_page_dowload(url)
    print(f'{url} \tsize={format(page.page_size, "_")} \telapsed={page.time_elapsed:.2f} secs')

#print(page.page)
del page.url