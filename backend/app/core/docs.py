main_description = """
WeBook API - API for flexible booking and event management solution
"""

tags_metadata = [

    {
        "name": "person",
        "description": "Represents a **person** entity. Does not represent a user however.",
    },
    {
        "name": "arrangement",
        "description": "**Arrangements** are in practice a sequence of events, or an arrangement of events. Arrangements have events that happen in a concerted nature, and share the same purpose and or context. A realistic example of an arrangement could be an exhibition, which may have events stretching over a large timespan, but which have a shared nature, which is of especial organizational interest"

    },
    {
        "name": "audience",
        "description": "**Audience** represents a target audience, and is used for categorical purposes in arrangement",
    },
    {
        "name": "location & room",
        "description": "**Location** represents a physical location, for instance a building. In practice a location is a group of rooms, primarily helpful in contextualization and filtering"
                       "\n\n**Room** represents a physical real-world room. All rooms belong to a location",
    },
    {
        "name": "organization & org.type",
        "description": "**Organizations** represent real world organizations"
                       "\n\nAn **organization type** is an arbitrary classification that is applicable to organizations For example non-profit organizations, or public organizations. This is for categorical purposes",
    },
    {
        "name": "article",
        "description": "An **article** is a consumable entity, on the same level in terms of being a resource as room and person. In practice an article could for instance be a projector, or any other sort of inanimate physical entity",
    },
    {
        "name": "event",
        "description": "The **event** model represents an event, or happening that takes place in a set span of time, and which may reserve certain resources for use in that span of time (such as a room, or a person etc..).",
    },
    {
        "name": "screen show generator",
        "description": "HTML Generator For Screen Display",
    },
    {
        "name": "user",
        "description": "Operations with users. The **login** logic is also here.",
    },
    {
        "name": "confirmation receipt",
        "description": "**Confirmation receipts** are used to petition a person to confirm something, and allows a tracked record of confirmation"
    },

    {
        "name": "timeline",
        "description": "A **timeline event** model represents an event on a timeline (part of arrangement), not to be confused with an event on a calendar, which is represented by the Event model."
    },
    {
        "name": "note",
        "description": "**Notes** are annotations that can be associated with other key models in the application. The practical purpose is to annotate information on these associated models.",
    },

    {
        "name": "calendar",
        "description": "Represents an implementation, or a version of a calendar. **Calendars** are built based on resources, namely which resources are wanted to be included. May be personal to a select user, or globally shared and available for all users",
    },
    {
        "name": "business hours",
        "description": "A business hour model represents a from-to record keeping track of businesshours. Primarily used visually to differentiate between business times, and outside of business times, in for instance the calendar. May apply to resources.",
    },
    {
        "name": "service provider & type",
        "description": "A **service type** is a type categorization of service providers"
                       "\n\nThe **service provider** provides services that can be consumed by events. An organization may provide multiple services, and thus be represented through multiple service provider records",
    },
    {
        "name": "event service",
        "description": "The **event service** model is a many-to-many mapping relationship between Event and ServiceProvider",
    },

    {
        "name": "requisition of service",
        "description": "",
    },

]