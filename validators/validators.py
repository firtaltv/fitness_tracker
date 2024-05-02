def user_validator(data: dict):
    print(data)
    if not isinstance(data.get('height'), (int, float)):
        return 'Incorrect User input for Height!'
    if isinstance(data.get('height'), (int, float)) and data.get('height') < 0:
        return 'Incorrect User input for Height!'
    if not isinstance(data.get('weight'), (int, float)):
        return 'Incorrect User input for weight!'
    if isinstance(data.get('weight'), (int, float)) and data.get('weight') < 0:
        return 'Incorrect User input for weight!'
    if not isinstance(data.get('age'), (int, float)):
        return 'Incorrect User input for age!'
    if isinstance(data.get('age'), (int, float)) and data.get('weight') < 0:
        return 'Incorrect User input for age!'
