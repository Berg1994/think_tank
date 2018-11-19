import pymongo

from think_tank import start_urls_data
from think_tank import settings


class StartUrls(object):

    def __init__(self):
        self.mongo_host = settings.MONGODB_HOST
        self.mongo_port = settings.MONGODB_POST
        self.mongo_db = settings.MONGODB_DB
        self.mongo_collection = settings.MONGODB_COLLECTIONS_START_URLS

        self.conn = pymongo.MongoClient(host=self.mongo_host,
                                        port=self.mongo_port)
        self.db = self.conn[self.mongo_db]
        self.collection = self.db[self.mongo_collection]

    def save_url(self):
        """
        存入链接
        """
        for url_data in start_urls_data.START_URLS_DATA:
            self.collection.update_one({'id': url_data['id']}, {'$set': url_data}, True)

    def get_url(self, tag):
        """
        获取链接
        :param self: 网站名称
        :return: 返回url链接详情
        """
        res = self.collection.find_one({'tag': str(tag)})
        return res

    def del_url(self):
        """
        删除链接
        :return:
        """
        pass

    def update_url(self):
        """
        更新链接
        :return:
        """
        pass
