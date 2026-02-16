from enum import Enum

class ReferenceType(str, Enum):
    ORDER = 'ORDER'
    SUBSCRIPTION = 'SUBSCRIPTION'
    INVOICE = 'INVOICE' 
    DONATION = 'DONATION' 
    TOPUP = 'TOPUP' 
    BOOKING = 'BOOKING'
    FEE = 'FEE' 
    ADJUSTMENT = 'ADJUSTMENT'