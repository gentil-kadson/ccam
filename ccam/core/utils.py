def user_directory_path(instance, filename):
    return f"users/{instance.user.username}/{filename}"
