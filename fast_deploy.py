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
