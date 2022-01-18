from flask_cors import CORS
from pyms.flask.app import Microservice

from project.configuration_manager import ConfigurationManager
from project.infrastructure.contexts.redis_context import RedisContext
from project.processors.configuration import\
    Configuration
from project.infrastructure.repositories.redis_repository import\
    RedisRepository


class PatentsSystemMicroservice(Microservice):

    def init_libs(self):
        self.config["CORS_HEADERS"] = "Content-Type"
        self.init_local_services()

    def init_local_services(self):
        database_cache_connection_string_name = "REDIS_EC_CROSS"
        self.database_cache_context = RedisContext(
            database_cache_connection_string_name)
        self.database_cache_repository =\
            RedisRepository(self.database_cache_context)


def create_app():
    microservice = PatentsSystemMicroservice(path=__file__)
    ConfigurationManager.microservice = microservice

    app = microservice.create_app()
    CORS(app, resources={r"/academic-system/*": {"origins": "*"}})

    return app
