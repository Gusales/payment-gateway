from enum import Enum

class ProviderStatus(str, Enum):
    PENDING = 'PENDING'
    SUCCESS = 'SUCCESS'
    FAILED = 'FAILED'
    CANCELLED = 'CANCELLED'
    EXPIRED = 'EXPIRED'
    REQUIRES_ACTION = 'REQUIRES_ACTION'