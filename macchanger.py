import subprocess
import optparse
import re
parser=optparse.OptionParser()
def mac_changer(interface,new_mac):

    subprocess.call(interface + "down", shell=True)
    subprocess.call(interface + "hw ether" + new_mac)
    subprocess.call(interface + "up")


parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="TYpe the Interface you want to change mac-adress of")
parser.add_option("-m", "--mac", dest="new_mac", help="TYpe the Mac-Address you want  ")

parser.parse_args()

interface = input("interface>")
new_mac = input("mac you want >")

print("changing Mac-address of"+interface+"to"+new_mac)

subprocess.call(interface+"down", shell=True)
subprocess.call(interface+"hw ether"+new_mac)
subprocess.call(interface+"up")

mac_changer(interface, new_mac)
ifconfig_result = subprocess.check_output(["ifconfig", interface])
mac_address_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
print(mac_address_result)

# OR *(FoR SECURITY)*
# subprocess.call([interface, "down"])
# subprocess.call([interface, "hw ether", new_mac])
# subprocess.call([interface, "up"])


