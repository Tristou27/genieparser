import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Any,
        Optional, Use, SchemaTypeError, Schema)

class ShowOspf3InterfaceSchema(MetaParser):

    # Sub Schema
    def validate_ospf_interface_list(value):
        # Pass ospf3-interface list as value
        if not isinstance(value, list):
            raise SchemaTypeError('ospf-interface is not a list')
        entry_schema = Schema({
                "bdr-id": str,
                "dr-id": str,
                "interface-name": str,
                "neighbor-count": str,
                "ospf-area": str,
                "ospf-interface-state": str
            })
        # Validate each dictionary in list
        for item in value:
            entry_schema.validate(item)
        return value

    # Main Schema
    schema = {
        "ospf3-interface-information": {
            "ospf3-interface": Use(validate_ospf_interface_list)
        }
    }

class ShowOspf3Interface(ShowOspf3InterfaceSchema):
    """ Parser for:
    * show ospf interface
    """
    cli_command = 'show ospf interface'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # use the pattern r'[0-9]{1,3}(\.[0-9]{1,3}){3}' to pick up on ip addresses
        # in 'area', 'dr_id' and 'bdr_id'
        p1 = re.compile(r'^(?P<interface>\S+) +(?P<state>\S+) +(?P<area>[0-9]{1,3}(\.[0-9]{1,3}){3})'
            r' +(?P<dr_id>[0-9]{1,3}(\.[0-9]{1,3}){3}) +(?P<bdr_id>[0-9]{1,3}(\.[0-9]{1,3}){3}) +(?P<nbrs>\S+)$')

        entry_list = []

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()

                interface_entry = {}
                interface_entry['interface-name'] = group['interface']
                interface_entry['ospf-interface-state'] = group['state']
                interface_entry['ospf-area'] = group['area']
                interface_entry['dr-id'] = group['dr_id']
                interface_entry['bdr-id'] = group['bdr_id']
                interface_entry['neighbor-count'] = group['nbrs']

                entry_list.append(interface_entry)

        if entry_list:
            data = {
                "ospf3-interface-information": {
                    "ospf3-interface": entry_list
                }
            }
            return data
        else:
            return None

