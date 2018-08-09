file_in = "osim-rl/osim/models/gait9dof18musc.osim"
file_out = "mujoco_gait9dof18musc.xml"

import xml.etree
from lxml import etree
parser = etree.XMLParser(recover=True)
e = etree.fromstring(xmlstring, parser=parser)

e = xml.etree.ElementTree.parse('thefile.xml').getroot()
