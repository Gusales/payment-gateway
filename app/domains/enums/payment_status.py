from enum import Enum

class PaymentStatus(str, Enum):
    CREATED = 'created'
    PROCESSING = 'processing' 
    PENDING = 'pending'
    APPROVED = 'approved'
    FAILED = 'failed'
    CANCELLED = 'cancelled'
    EXPIRED = 'expired'