# Copyright 2014 Joshua Richards
#
#
# All Rights Reserved.
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



#The purpose of this script is to quickly deploy several cloud servers for build testing purposes.
#What I want to do?
#	1. How many servers do you want to build?
#	2. What Flavor Server?  (select from a list)
#	3. What image?
#	4. What do you want to name the servers? (needs to ta name test 1 - however many servers are inputed in step 1.)

import os
import pyrax

pyrax.set_setting("identity_type", "rackspace")
creds_file = os.path.expanduser("~/.rackspace_cloud_credentials")
pyrax.set_credential_file(creds_file)
cs = pyrax.cloudservers

servers = raw_input("How many servers do you want to build?: ")
