# Copyright (C) 2020 rupansh <rupanshsekar@hotmail.com>
#
# Licensed under the GNU General Public License v3.0;
#
# You may not use this file except in compliance with the license.
#
# If you think you will copy my hardwork and get away with it, DMCA welcomes you!

from os import listdir


IMPLS = [impl.replace(".py", "") for impl in listdir("./implementations") if impl != "__init__.py" and impl.endswith(".py")]
print("Available APIs:", " ".join(IMPLS), "\n")
AVAIL = list()


def sms_api_impl(some_c):
    AVAIL.append(some_c())
