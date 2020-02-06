from src.resources.health import Health
from src.resources.users import Users


def setup(api):
    api.add_resource(Health, '/v1/health')
    api.add_resource(Users, '/v1/users', endpoint="users")
    api.add_resource(Users, '/v1/users/<id>', endpoint="user")
