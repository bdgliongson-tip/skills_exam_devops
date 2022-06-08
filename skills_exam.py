from ncclient import manager
import xml.dom.minidom

m = manager.connect(
    host="192.168.56.101",
    port=830,
    username="cisco",
    password="cisco123!",
    hostkey_verify=False
)

choice = ''

while choice != "q":
    print("[1]- change devices hostname")
    print('[2]- Add description to Gigabit Ethernet 1')
    print("[3]- add new loopback")
    print("[q]- quit program")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Change hostname")
        hostname = """
        <config>
            <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                <hostname>Liongson_SkillsExam</hostname>
            </native>
        </config>
        """
        reply = m.edit_config(target="running", config=hostname)
        print(xml.dom.minidom.parseString(reply.xml).toprettyxml())

    elif choice == "2":
        print("Add interface description to G1")
        G1_desc = """
        <config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
            <interfaces xmlns="http://openconfig.net/yang/interfaces">
                <interface>
                    <name>GigabitEthernet1</name>
                        <config>
                            <description nc:operation="replace">Interface G1</description>
                        </config>
                </interface>
            </interfaces>
        </config>
        """
        reply = m.edit_config(
            target="running", config=G1_desc, default_operation="none")
        print(xml.dom.minidom.parseString(reply.xml).toprettyxml())

    elif choice == "3":
        print("add new loopback")
        new_loopback = """
        <config>
	        <native
		    xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
		        <interface>
			        <Loopback>
				        <name>1</name>
				        <description>New Interface</description>
				        <ip>
					        <address>
						        <primary>
							        <address>10.1.1.5</address>
							        <mask>255.255.255.0</mask>
						        </primary>
					        </address>
				        </ip>
			        </Loopback>
		        </interface>
	        </native>
        </config>
        """
        reply = m.edit_config(target="running", config=new_loopback)
        print(xml.dom.minidom.parseString(reply.xml).toprettyxml())

    elif choice == "q":
        print("Program Closing...")
