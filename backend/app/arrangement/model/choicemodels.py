"""
This module contains choice classes used in schema and models
"""


class StageChoices:
    PLANNING = 'planning'
    REQUISITIONING = 'requisitioning'
    READY_TO_LAUNCH = 'ready_to_launch'
    IN_PRODUCTION = 'in_production'

    CHOICES = (
        PLANNING,
        REQUISITIONING,
        READY_TO_LAUNCH,
        IN_PRODUCTION,
    )


class EventTypeChoice:
    ARRANGEMENT_EVENT = 'arrangement_event'
    HOLIDAY_EVENT = 'holiday_event'

    CHOICES = (
        ARRANGEMENT_EVENT,
        HOLIDAY_EVENT,
    )


class AssociationTypeChoice:
    NO_ASSOCIATION = 'no_association'
    COLLISION_RESOLVED_ORIGINATING_OF_SERIE = 'collision_resolved_originating_of_serie'

    CHOICES = (
        NO_ASSOCIATION,
        COLLISION_RESOLVED_ORIGINATING_OF_SERIE,
    )


