from pkg_resources import get_distribution
__version__ = get_distribution('gcloud-requests-auth').version

from gcloud.requests.auth.iam import IamClient
from gcloud.requests.auth.token import Token
from gcloud.requests.auth.utils import decode
from gcloud.requests.auth.utils import encode


__all__ = ['__version__', 'IamClient', 'Token', 'decode', 'encode']
