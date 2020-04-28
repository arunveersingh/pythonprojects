def found():
    print("python found me!")


# Without below steps path_test.py was not discoverable

# import path_test
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
#   File "C:\Program Files\JetBrains\PyCharm 2020.1\plugins\python\helpers\pydev\_pydev_bundle\pydev_import_hook.py", line 21, in do_import
#     module = self._system_import(name, *args, **kwargs)
# ModuleNotFoundError: No module named 'path_test'
# import sys
# sys.path.append('python_beyond_basics')
# import path_test
# path_test.found()
# python found me!