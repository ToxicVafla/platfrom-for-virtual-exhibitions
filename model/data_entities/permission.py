from enum import IntFlag

class Permission(IntFlag):
    # Basic types
    access = 2**0  # 1
    create = 2**1  # 2
    edit = 2**2    # 4
    delete = 2**3  # 8

    # Complex types
    reader = access  # access
    writer = access | create  # access | create
    editor = access | create | edit | delete  # access | create | edit | delete