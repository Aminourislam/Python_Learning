test_settings = {
'theme': "",
'language': '',
'notifications': ""
}
key_value_tuple = ('x', 'y')
def add_setting(test_settings,key_value_tuple):
	dic_keys = []
	for x in test_settings.keys():
		dic_keys.append(x)
	key, value = key_value_tuple
	key = str(key).lower()
	value = str(value).lower()

	if key in dic_keys:
		return f"Setting '{key}' already exists! Cannot add a new setting with this name."
	else:
		test_settings[key] = value
		return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(test_settings,key_value_tuple):
	dic_keys = []
	for x in test_settings.keys():
		dic_keys.append(x)


	key, value = key_value_tuple
	key = str(key).lower()
	value = str(value).lower()


	if key in dic_keys:
		test_settings[key] = value
		return f"Setting '{key}' updated to '{value}' successfully!"
	else:
		return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


def delete_setting(test_settings, key):
	key = str(key).lower()
	
	if key in test_settings:
		test_settings.pop(key)
		return f"Setting '{key}' deleted successfully!"
	else:
		return f"Setting not found!"

def view_settings(test_settings):
    if not test_settings:  # simpler empty check
        return "No settings available."
    
    result = "Current User Settings:\n"
    for key, value in test_settings.items():
        result += f"{key.capitalize()}: {value}\n"
    return result