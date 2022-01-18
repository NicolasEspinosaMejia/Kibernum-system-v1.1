from project.composers.identifiers_compose import IdentifiersCompose
from project.services.identifiers_service import IdentifiersService
from project.infrastructure.repositories.common_repository import CommonRepository
from project.configuration_manager import ConfigurationManager
from project.infrastructure.repositories.repository_by_entities_definitions\
    import RepositoryByEntitiesDefinitions
from project.resources.decorators.view_aspect import ViewAspect

@ViewAspect
def get_identification(data):
    service = get_service()
    result = service.get_identification(data)

    return result

def get_service():
    """This method is in charge of making the instances of the services
       and the compose that will be used generically

    Returns:
        object:This method returns an instance of the parent service that
               is being used
    """
    bridge_command_repository = CommonRepository()
    compose = IdentifiersCompose(
        database_cache_repository=bridge_command_repository)
    service = IdentifiersService(compose=compose,
                                 repository=RepositoryByEntitiesDefinitions)

    return service
