import pytest

from pprint import pprint


from sample import User, UserSchema


@pytest.fixture(scope='session')
def schema() -> UserSchema:
    return UserSchema()


@pytest.fixture(scope='session')
def user() -> User:
    return User('Example User', 'user@example.com')


@pytest.fixture(scope='session')
def another_user(scope='session') -> User:
    return User('Another User', 'another@example.com')


@pytest.fixture(scope='session')
def user_list(user: User, another_user: User) -> list:
    return [user, another_user]


def test_dump_user(schema: UserSchema, user: User):
    serialized = schema.dump(user)
    assert 'name' in serialized
    assert 'email' in serialized
    assert 'dumped_at' in serialized

def test_dump_many(schema: UserSchema, user_list: list):
    serialized = schema.dump(user_list, many=True)
    print("\ndumping the list:")
    pprint(serialized)
    assert len(serialized) == 2