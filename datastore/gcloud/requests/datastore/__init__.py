# TODO(keving) add this back
# from pkg_resources import get_distribution
# __version__ = get_distribution('gcloud-requests-datastore').version

from gcloud.requests.datastore.constants import CompositeFilterOperator
from gcloud.requests.datastore.constants import Consistency
from gcloud.requests.datastore.constants import Direction
from gcloud.requests.datastore.constants import Mode
from gcloud.requests.datastore.constants import MoreResultsType
from gcloud.requests.datastore.constants import Operation
from gcloud.requests.datastore.constants import PropertyFilterOperator
from gcloud.requests.datastore.constants import ResultType
from gcloud.requests.datastore.datastore import Datastore
from gcloud.requests.datastore.datastore import SCOPES
from gcloud.requests.datastore.datastore_operation import DatastoreOperation
from gcloud.requests.datastore.entity import Entity
from gcloud.requests.datastore.entity import EntityResult
from gcloud.requests.datastore.filter import CompositeFilter
from gcloud.requests.datastore.filter import Filter
from gcloud.requests.datastore.filter import PropertyFilter
from gcloud.requests.datastore.key import Key
from gcloud.requests.datastore.key import PathElement
from gcloud.requests.datastore.property_order import PropertyOrder
from gcloud.requests.datastore.query import GQLQuery
from gcloud.requests.datastore.query import Query
from gcloud.requests.datastore.query import QueryResultBatch
from gcloud.requests.datastore.value import Value


# __all__ = ['__version__', 'CompositeFilter', 'CompositeFilterOperator',
__all__ = ['CompositeFilter', 'CompositeFilterOperator',
           'Consistency', 'Datastore', 'DatastoreOperation', 'Direction',
           'Entity', 'EntityResult', 'Filter', 'GQLQuery', 'Key', 'Mode',
           'MoreResultsType', 'Operation', 'PathElement', 'PropertyFilter',
           'PropertyFilterOperator', 'PropertyOrder', 'Query',
           'QueryResultBatch', 'ResultType', 'SCOPES', 'Value']
