import humps


def pythonize_json_response(data: dict) -> dict:
    return humps.decamelize(humps.dekebabize(data))
