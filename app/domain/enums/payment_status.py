from enum import Enum

class PaymentStatus(str, Enum):
    CREATED = 'CREATED'
    PROCESSING = 'PROCESSING' 
    PENDING = 'PENDING'
    APPROVED = 'APPROVED'
    FAILED = 'FAILED'
    CANCELLED = 'CANCELLED'
    EXPIRED = 'EXPIRED'