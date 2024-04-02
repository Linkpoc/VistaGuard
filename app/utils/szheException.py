

class reqBadExceptin(Exception):
    "this is user's Exception for check the length of name "
    def __init__(self,url):
        self.url = url
    def __str__(self):
        return "请求失败 {}".format(self.url)


def test():
    print('hi')


if __name__ == '__main__':
    test()
