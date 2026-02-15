from enum import Enum

class ReferenceType(str, Enum):
    ORDER = 'order'
    SUBSCRIPTION = 'subscription'
    INVOICE = 'invoice' 
    DONATION = 'donation' 
    TOPUP = 'topup' 
    BOOKING = 'booking'
    FEE = 'fee' 
    ADJUSTMENT = 'adjustment'