#
#   Copyright 2020 The SpaceONE Authors.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at 
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import os
from setuptools import setup, find_packages

setup(
    name='spaceone-config-test-PyPI-2FA',
    version=os.environ.get('PACKAGE_VERSION'),
    description='SpaceONE config service PyPI test',
    long_description='',
    url='',
    author='MEGAZONE SpaceONE Team',
    author_email='pyt4105@gmail.com',
    license='Apache License 2.0',
    packages=find_packages(),
    zip_safe=False,
)
