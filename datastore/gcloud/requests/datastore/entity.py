import typing

from gcloud.requests.datastore.key import Key
from gcloud.requests.datastore.value import Value


class Entity:
    key_kind = Key
    value_kind = Value

    def __init__(self, key, properties=None):
        # type: (Key, typing.Dict[str, dict]) -> None
        self.key = key
        self.properties = {k: self.value_kind.from_repr(v).value
                           for k, v in (properties or {}).items()}

    def __eq__(self, other):
        # type: (typing.Any) -> bool
        if not isinstance(other, Entity):
            return False

        return bool(self.key == other.key
                    and self.properties == other.properties)

    def __repr__(self) -> str:
        return str(self.to_repr())

    @classmethod
    def from_repr(cls, data):
        # type: (typing.Dict[str, typing.Any]) -> Entity
        return cls(cls.key_kind.from_repr(data['key']), data.get('properties'))

    def to_repr(self):
        # type: () -> typing.Dict[str, typing.Any]
        return {
            'key': self.key.to_repr(),
            'properties': self.properties,
        }


class EntityResult:
    entity_kind = Entity

    def __init__(self, entity: Entity, version: str,
                 cursor: str = '') -> None:
        self.entity = entity
        self.version = version
        self.cursor = cursor

    def __eq__(self, other):
        # type: (typing.Any) -> bool
        if not isinstance(other, EntityResult):
            return False

        return bool(self.entity == other.entity
                    and self.version == other.version
                    and self.cursor == self.cursor)

    def __repr__(self) -> str:
        return str(self.to_repr())

    @classmethod
    def from_repr(cls, data):
        # type: (typing.Dict[str, typing.Any]) -> EntityResult
        return cls(cls.entity_kind.from_repr(data['entity']), data['version'],
                   data.get('cursor', ''))

    def to_repr(self):
        # type: () -> typing.Dict[str, typing.Any]
        data = {
            'entity': self.entity.to_repr(),
            'version': self.version,
        }
        if self.cursor:
            data['cursor'] = self.cursor

        return data
