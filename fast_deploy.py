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

number_of_servers = int(raw_input("How many servers do you want to build?: "))


def list_flavors():
    print "Here is a list of flavors."
    flvs = cs.list_flavors()
    for flv in flvs:
        print "ID:", flv.id, flv.name
list_flavors()

flavor = raw_input("Please select the flavor ID above you want to use: ")


def list_images():
    print "Here is a list of images."
    imgs = cs.images.list()
    for img in imgs:
        print "Name: %s\n  ID: %s" % (img.name, img.id)
list_images()

image = raw_input("Please select the image ID above you want to use: ")

print "Your Server(s) will now build.... \n"

def server_build():
    for i in range(number_of_servers):
        server_name = pyrax.utils.random_ascii(8)
        server = cs.servers.create(server_name, image, flavor)
        print "Name:", server.name
        print "ID:", server.id
        print "Status:", server.status
        print "Admin Password:", server.adminPass
        print"Networks:", server.networks
        print "\n" 
server_build()
