#!/usr/bin/env python

try:
    from file_storage import FileStorage
except ImportError as e:
    print("error encounters", e)

storage = FileStorage()
storage.reload()

