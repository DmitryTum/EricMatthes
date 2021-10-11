from pygal_maps_world.i18n import COUNTRIES


def get_country_code(country_name):
    """Возврат для зананной страны ее код"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    if country_name == 'Tuvalu':
        return country_name
    elif country_name == 'Vanuatu':
        return country_name
    return None


