test_settings = {
    'theme': 'black',
    'language': 'English',
    'notifications': "Enabled"
}
def add_setting(settings, keysetting): 
    key, val = keysetting
    key = key.lower()
    val = val.lower() 
    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    settings[key] = val
    return f"Setting '{key}' added with value '{val}' successfully!"

def update_setting(settings, keysetting):
    key, value = keysetting
    key = key.lower()
    value = value.lower()
    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings, keysettings):
    keysettings = keysettings.lower()
    if keysettings in settings:
        settings.pop(keysettings)
        return f"Setting '{keysettings}' deleted successfully!"
    return "Setting not found!"

def view_settings(dictionary):
    if not dictionary:
        return "No settings available."
    result = "Current User Settings:\n"
    for key, value in dictionary.items():
        result += f'{key.capitalize()}: {value}\n'
    return result

print(add_setting(test_settings, ("volume", "high")))
print(view_settings(test_settings))

