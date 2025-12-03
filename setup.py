#!/usr/bin/env python

# © 2025 EarthDaily Analytics Corp.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup

version = "4.0.0post1"

def do_setup():
    setup(
        name="descarteslabs",
        description="Discontinued. Please use earthone-earthdaily instead.",
        long_description="Discontinued. Please use earthone-earthdaily instead.",
        author="EarthDaily Analytics",
        author_email="support@earthdaily.com",
        url="https://github.com/earthdaily/earthone-python",
        version=version,
    )

if __name__ == "__main__":
    do_setup()
