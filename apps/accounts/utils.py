def avatar_path(instance, filename):
    return f'{instance.email}/avatar/{filename}'


def cv_path(instance, filename):
    return f'{instance.email}/cv/{filename}'
