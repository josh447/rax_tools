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
cs_dfw = pyrax.connect_to_cloudservers(region="DFW")
cs_ord = pyrax.connect_to_cloudservers(region="ORD")
cs_iad = pyrax.connect_to_cloudservers(region="IAD")
cs_syd = pyrax.connect_to_cloudservers(region="SYD")
cs_hkg = pyrax.connect_to_cloudservers(region="HKG")


region = raw_input("""Which Region do you want to connect to?\n
1. DFW\n2. ORD\n3. IAD\n4. SYD\n5. HKG\n: """)

number_of_servers = int(raw_input("How many servers do you want to build?: "))


def list_flavors():
    print "Here is a list of flavors."
    if region == "DFW" or region == "dfw" or region == "1":
        flvs_dfw = cs_dfw.list_flavors()
        for flv in flvs_dfw:
            print "ID:", flv.id, flv.name
    elif region == "ORD" or region == "ord" or region == "2":
        flvs_ord = cs_ord.list_flavors()
        for flv in flvs_ord:
            print "ID:", flv.id, flv.name
    elif region == "IAD" or region == "iad" or region == "3":
        flvs_iad = cs_iad.list_flavors()
        for flv in flvs_iad:
            print "ID:", flv.id, flv.name
    elif region == "SYD" or region == "syd" or region == "4":
        flvs_syd = cs_syd.list_flavors()
        for flv in flvs_syd:
            print "ID:", flv.id, flv.name
    elif region == "HKG" or region == "hkg" or region == "5":
        flvs_hkg = cs_hkg.list_flavors()
        for flv in flvs_hkg:
            print "ID:", flv.id, flv.name
    else:
        return
list_flavors()

flavor = raw_input("Please select the flavor ID above you want to use: ")


def list_images():
    print "Here is a list of images."
    if region == "DFW" or region == "dfw" or region == "1":
        imgs_dfw = cs_dfw.images.list()
        for img in imgs_dfw:
            print "Name: %s\n  ID: %s" % (img.name, img.id)
    elif region == "ORD" or region == "ord" or region == "2":
        imgs_ord = cs_ord.images.list()
        for img in imgs_ord:
            print "Name: %s\n ID: %s" % (img.name, img.id)
    elif region == "IAD" or region == "iad" or region == "3":
        imgs_iad = cs_iad.images.list()
        for img in imgs_iad:
            print "Name: %s\n ID: %s" % (img.name, img.id)
    elif region == "SYD" or region == "syd" or region == "4":
        imgs_syd = cs_syd.images.list()
        for img in imgs_syd:
            print "Name: %s\n ID: %s" % (img.name, img,id)
    elif region == "HKG" or region == "hkg" or region == "5":
        imgs_hkg = cs_hkg.images.list()
        for img in imgs_hkg:
            print "Name: %s\n ID: %s" % (img.name, img,id)
    else:
        return
list_images()

image = raw_input("Please select the image ID above you want to use: ")

print "Your Server(s) will now build.... \n"

def server_build():
    for i in range(number_of_servers):
        server_name = pyrax.utils.random_ascii(8)
        if region == "DFW" or region == "dfw" or  region == "1":
            server_dfw = cs_dfw.servers.create(server_name, image, flavor)
            print "Name:", server_dfw.name
            print "ID:", server_dfw.id
            print "Status:", server_dfw.status
            print "Admin Password:", server_dfw.adminPass
            print "Networks:", server_dfw.networks
            print "\n" 
        elif region == "ORD" or region == "ord" or region == "2":
            server_ord = cs_ord.servers.create(server_name, image, flavor)
            print "Name:", server_ord.name
            print "ID:", server_ord.id
            print "Status:", server_ord.status
            print "Admin Password:", server_ord.adminPass
            print "Networks:", server_ord.networks
            print "\n"
        elif region == "IAD" or region == "iad" or region == "3":
            server_iad = cs_iad.servers.create(server_name, image, flavor)
            print "Name:", server_iad.name
            print "ID:", server_iad.id
            print "Status:", server_iad.status
            print "Admin Password:", server_iad.adminPass
            print "Networks:", server_iad.networks
            print "\n"
        elif region == "SYD" or region == "syd" or region == "4":
            server_syd = cs_syd.servers.create(server_name, image, flavor)
            print "Name:", server_syd.name
            print "ID:", server_syd.id
            print "Status:", server_syd.status
            print "Admin Password:", server_syd.adminPass
            print "Networks:", server_syd.networks
            print "\n"
        elif region == "HKG" or region == "hkg" or region == "5":
            server_hkg = cs_hkg.servers.create(server_name, image, flavor)
            print "Name:", server_hkg.name
            print "ID:", server_hkg.id
            print "Status:", server_hkg.status
            print "Admin Password:", server_hkg.adminPass
            print "Networks:", server_hkg.networks
            print "\n"
        else:
            return
server_build()
