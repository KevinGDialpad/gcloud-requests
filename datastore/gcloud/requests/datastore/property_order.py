import typing

# TODO(keving) Make the absolute imports work
# from gcloud.requests.datastore.constants import Direction

from .constants import Direction


# https://cloud.google.com/datastore/docs/reference/data/rest/v1/projects/runQuery#PropertyOrder
class PropertyOrder:
    def __init__(self, prop: str,
                 direction: Direction = Direction.ASCENDING) -> None:
        self.prop = prop
        self.direction = direction

    def __eq__(self, other):
        # type: (typing.Any) -> bool
        if not isinstance(other, PropertyOrder):
            return False

        return bool(
            self.prop == other.prop
            and self.direction == other.direction)

    def __repr__(self) -> str:
        return str(self.to_repr())

    @classmethod
    def from_repr(cls, data):
        # type: (typing.Dict[str, typing.Any]) -> PropertyOrder
        prop = data['property']['name']
        direction = Direction(data['direction'])
        return cls(prop=prop, direction=direction)

    def to_repr(self):
        # type: () -> typing.Dict[str, typing.Any]
        return {
            'property': {'name': self.prop},
            'direction': self.direction.value,
        }
