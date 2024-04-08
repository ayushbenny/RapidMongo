import json
from pymongo.mongo_client import MongoClient
import os

from RapidMongo.utils import find_config


class RapidMongo:
    def __init__(self, **kwargs) -> None:
        self.__dict__.update(kwargs)
        self.config_file = self._find_config_file()
        self.connection = self._connection()
        self.mongo_connection = self._mongo_connection
        self.check_connection = self._check_connection()

    def _find_config_file(self):
        file_name = "config.json"
        script_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(script_dir)
        _find_config = find_config(file_name, project_root)
        return _find_config

    def _connection(self):
        with open(self.config_file, "rb") as data:
            json_load = json.load(data)
            py_mongo_credentials = json_load.get("py_mongo_cred", None)
            mongo_uri = f'mongodb+srv://{py_mongo_credentials.get("username")}:{py_mongo_credentials.get("password")}@{py_mongo_credentials.get("mongo_url")}'
            return mongo_uri

    @property
    def _mongo_connection(self):
        _client = MongoClient(self.connection)
        if _client:
            return _client
        else:
            return dict(
                "Connection Failed. Please make sure you have entered correct credentials"
            )

    def _check_connection(self):
        ping = self.mongo_connection.admin.command("ping")
        if ping.get("ok") == 1:
            return True
        else:
            return dict(
                "Connection Failed. Please make sure you have entered correct credentials"
            )

    def insert_data(self):
        if self.check_connection:
            if self.db_name:
                db_instance = self.mongo_connection[self.db_name]
            if self.collection:
                collection_instance = db_instance[self.collection]
            if isinstance(self.data, list) and all(
                isinstance(doc, dict) for doc in self.data
            ):
                collection_instance.insert_many(self.data)
            else:
                return dict(message="Invalid data format. Expecting a list of dictionaries.")
