import typing


class DatastoreOperation:
    def __init__(self,
                 name,  # type: str
                 done,  # type: bool
                 metadata=None,  # type: typing.Optional[typing.Dict[str, typing.Any]]
                 error=None,  # type: typing.Dict[str, str]
                 response=None  # type: typing.Optional[typing.Dict[str, typing.Any]]
                 ):
        # type: (...) -> None
        self.name = name
        self.done = done

        self.metadata = metadata
        self.error = error
        self.response = response

    @classmethod
    def from_repr(cls, data):
        # type: (typing.Dict[str, typing.Any]) -> DatastoreOperation
        return cls(data['name'], data['done'], data.get('metadata'),
                   data.get('error'), data.get('response'))

    def to_repr(self):
        # type: () -> typing.Dict[str, typing.Any]
        return {
            'done': self.done,
            'error': self.error,
            'metadata': self.metadata,
            'name': self.name,
            'response': self.response,
        }
