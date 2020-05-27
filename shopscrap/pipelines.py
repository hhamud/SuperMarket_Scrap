
import pymongo
from scrapy.utils.project import get_project_settings

settings = get_project_settings()


class MongoDBshopscrap(object):
    def __init__(self):
        connection = pymongo.MongoClient(
            settings.get('MONGODB_SERVER'),
            settings.get('MONGODB_PORT')
        )
        db = connection[settings.get('MONGODB_DB')]
        self.collection = db[settings.get('MONGODB_COLLECTION')]

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item
    