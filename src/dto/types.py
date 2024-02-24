from enum import Enum


class OrderStatus(Enum):

    NEW = "new"
    IN_PROGRESS = "in_progress"
    DELIVERED = "delivered"
    CANCELED = "canceled"
