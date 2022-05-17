GET_COUNTRY_SCHEMA = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "id": {
            "type": "integer"
        },
        "capital_id": {
            "type": "integer"
        },
        "name": {
            "type": "string"
        },
        "population": {
            "type": "integer"
        }
    },
    "required": [
        "id",
        "capital_id",
        "name",
        "population"
    ]
}
