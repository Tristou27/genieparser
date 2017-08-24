# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparset
from metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

# Parser
from parser.nxos.show_mcast import ShowIpMrouteVrfAll,\
                                   ShowIpv6StaticRouteMulticast,\
                                   ShowIpStaticRouteMulticast,\
                                   ShowIpv6MrouteVrfAll


# =======================================
# Unit test for 'show ip mroute vrf all'
# =======================================
class test_show_ip_mroute_vrf_all(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        'vrf': 
            {'VRF': 
                {'address_family': 
                    {'ipv4': {}}},
            'VRF1': 
                {'address_family': 
                    {'ipv4': 
                        {'multicast_group': 
                            {'232.0.0.0/8': 
                                {'source_address': 
                                    {'*': 
                                        {'flags': 'pim '
                                                 'ip',
                                        'incoming_interface_list': 
                                            {'Null': 
                                                {'rpf_nbr': '0.0.0.0'}},
                                        'oil_count': 0,
                                        'uptime': '3d11h'}}},
                            '239.5.5.5/32': 
                                {'source_address': 
                                    {'*': 
                                        {'flags': 'igmp '
                                                 'ip '
                                                 'pim',
                                        'incoming_interface_list': 
                                            {'Null': 
                                                {'rpf_nbr': '0.0.0.0'}},
                                        'oil_count': 1,
                                        'outgoing_interface_list': 
                                            {'loopback1': 
                                                {'oil_flags': 'igmp',
                                                'oil_uptime': '3d11h'}},
                                        'uptime': '3d11h'}}}}}}},
            'VRF2': 
                {'address_family': 
                    {'ipv4': 
                        {'multicast_group': 
                            {'224.192.1.10/32': 
                                {'source_address': 
                                    {'*': 
                                        {'flags': 'igmp '
                                                  'ip '
                                                  'pim',
                                        'incoming_interface_list': 
                                            {'port-channel8': 
                                                {'rpf_nbr': '159.103.50.233'}},
                                       'oil_count': 3,
                                        'outgoing_interface_list': 
                                            {'Vlan803': 
                                                {'oil_flags': 'igmp',
                                                'oil_uptime': '09:15:11'},
                                            'Vlan812': 
                                                {'oil_flags': 'igmp',
                                                'oil_uptime': '09:14:42'},
                                            'Vlan864': 
                                                {'oil_flags': 'igmp',
                                                'oil_uptime': '09:11:22'}},
                                       'uptime': '09:15:11'},
                                    '192.168.112.3/32': 
                                        {'flags': 'pim '
                                                  'ip',
                                        'incoming_interface_list': 
                                            {'Vlan807': 
                                                {'rpf_nbr': '159.103.211.228'}},
                                        'oil_count': 1,
                                        'outgoing_interface_list': 
                                            {'port-channel9': 
                                                {'oil_flags': 'pim',
                                                'oil_uptime': '09:31:16'}},
                                        'uptime': '09:31:16'},
                                    '192.168.112.4/32': 
                                        {'flags': 'pim '
                                                  'ip',
                                        'incoming_interface_list': 
                                            {'Ethernet1/1.10': 
                                                {'rpf_nbr': '159.103.211.228'}},
                                        'oil_count': 1,
                                        'outgoing_interface_list': 
                                            {'Ethernet1/2.20': 
                                                {'oil_flags': 'pim',
                                                'oil_uptime': '09:31:16'}},
                                        'uptime': '09:31:16'}}}}}}},
            'default': 
                {'address_family': 
                    {'ipv4': 
                        {'multicast_group': 
                            {'232.0.0.0/8': 
                                {'source_address': 
                                    {'*': 
                                        {'flags': 'pim '
                                                  'ip',
                                        'incoming_interface_list': 
                                            {'Null': 
                                                {'rpf_nbr': '0.0.0.0'}},
                                        'oil_count': 0,
                                        'uptime': '00:41:05'}}},
                            '239.1.1.1/32': 
                                {'source_address': 
                                    {'*': 
                                        {'flags': 'igmp '
                                                  'pim '
                                                  'ip',
                                        'incoming_interface_list': 
                                            {'Ethernet9/13': 
                                                {'rpf_nbr': '10.2.3.2'}},
                                        'oil_count': 1,
                                        'outgoing_interface_list': 
                                            {'loopback2': 
                                                {'oil_flags': 'igmp',
                                                'oil_uptime': '3d11h'}},
                                        'uptime': '3d11h'}}}}}}}}}

    golden_output = {'execute.return_value': '''\
        IP Multicast Routing Table for VRF "default"

        (*, 232.0.0.0/8), uptime: 9w2d, pim ip 
          Incoming interface: Null, RPF nbr: 0.0.0.0
          Outgoing interface list: (count: 0)

        (*, 239.1.1.1/32), uptime: 3d11h, igmp pim ip 
          Incoming interface: Ethernet9/13, RPF nbr: 10.2.3.2
          Outgoing interface list: (count: 1)
            loopback2, uptime: 3d11h, igmp


        IP Multicast Routing Table for VRF "VRF1"

        (*, 232.0.0.0/8), uptime: 3d11h, pim ip 
          Incoming interface: Null, RPF nbr: 0.0.0.0
          Outgoing interface list: (count: 0)

        (*, 239.5.5.5/32), uptime: 3d11h, igmp ip pim 
          Incoming interface: Null, RPF nbr: 0.0.0.0
          Outgoing interface list: (count: 1)
            loopback1, uptime: 3d11h, igmp 

        IP Multicast Routing Table for VRF "VRF2"

        (*, 224.192.1.10/32), uptime: 09:15:11, igmp ip pim
           Incoming interface: port-channel8, RPF nbr: 159.103.50.233
           Outgoing interface list: (count: 3)
             Vlan864, uptime: 09:11:22, igmp
             Vlan812, uptime: 09:14:42, igmp
             Vlan803, uptime: 09:15:11, igmp

        (192.168.112.3/32, 224.192.1.10/32), uptime: 09:31:16, pim ip
           Incoming interface: Vlan807, RPF nbr: 159.103.211.228
           Outgoing interface list: (count: 1)
             port-channel9, uptime: 09:31:16, pim        

        (192.168.112.4/32, 224.192.1.10/32), uptime: 09:31:16, pim ip
           Incoming interface: Ethernet1/1.10, RPF nbr: 159.103.211.228
           Outgoing interface list: (count: 1)
             Ethernet1/2.20, uptime: 09:31:16, pim  

        IP Multicast Routing Table for VRF "default"

        (*, 232.0.0.0/8), uptime: 00:41:05, pim ip 
          Incoming interface: Null, RPF nbr: 0.0.0.0
          Outgoing interface list: (count: 0)


        IP Multicast Routing Table for VRF "VRF"
      '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        ip_mroute_vrf_all_obj = ShowIpMrouteVrfAll(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = ip_mroute_vrf_all_obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        ip_mroute_vrf_all_obj = ShowIpMrouteVrfAll(device=self.device)
        parsed_output = ip_mroute_vrf_all_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


# =========================================
# Unit test for 'show ipv6 mroute vrf all'
# =========================================
class test_show_ipv6_mroute_vrf_all(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        'vrf': 
            {'VRF': 
                {'address_family': 
                    {'ipv6': {}}},
            'VRF1': 
                {'address_family': 
                    {'ipv6': 
                        {'multicast_group': 
                            {'ff1e:1111::1:0/128': 
                                {'source_address': 
                                    {'*': 
                                        {'flags': 'mld pim6 ipv6',
                                        'incoming_interface_list': 
                                            {'loopback10': 
                                                {'rpf_nbr': '2001:9999::1'}},
                                        'oil_count': '3',
                                        'uptime': '00:04:03'},
                                    '2001::222:1:1:1234/128': 
                                        {'flags': 'ipv6 pim6 m6rib',
                                        'incoming_interface_list': 
                                            {'Ethernet1/33.10': 
                                                {'rpf_nbr': '2001::222:1:1:1234, internal'}},
                                        'oil_count': '3',
                                        'uptime': '00:04:03'},
                                    '2001::222:1:2:1234/128': {'flags': 'ipv6 pim6 m6rib',
                                                             'incoming_interface_list': {'Ethernet1/33.11': {'rpf_nbr': '2001::222:1:2:1234, '
                                                                                                                        'internal'}},
                                                             'oil_count': '3',
                                                             'outgoing_interface_list': {'Ethernet1/33.11': {'oif_rpf': True,
                                                                                                             'oil_flags': 'm6rib',
                                                                                                             'oil_uptime': '00:04:03'}},
                                                             'uptime': '00:04:03'},
                                    '2001::222:2:3:1234/128': {'flags': 'pim6 m6rib ipv6',
                                                             'incoming_interface_list': {'Ethernet1/26': {'rpf_nbr': 'fe80::10, '
                                                                                                                     'internal'}},
                                                             'oil_count': '1',
                                                             'uptime': '00:04:03'},
                                    '2001::222:2:44:1234/128': {'flags': 'pim6 m6rib ipv6',
                                                              'incoming_interface_list': {'Ethernet1/26': {'rpf_nbr': 'fe80::10, '
                                                                                                                      'internal'}},
                                                              'oil_count': '1',
                                                              'uptime': '00:04:03'}}},
                            'ff1e:1111:ffff::/128': 
                                {'source_address': 
                                    {'*': 
                                        {'flags': 'mld pim6 ipv6',
                                        'incoming_interface_list': {'Ethernet1/33.10': {'rpf_nbr': '2001::222:1:1:1'}},
                                        'oil_count': '2',
                                        'uptime': '00:04:03'},
                                    '2001::222:1:1:1234/128': {'flags': 'ipv6 pim6 m6rib',
                                                               'incoming_interface_list': {'Ethernet1/33.10': {'rpf_nbr': '2001::222:1:1:1234, '
                                                                                                                          'internal'}},
                                                               'oil_count': '3',
                                                               'uptime': '00:04:03'},
                                    '2001::222:1:2:1234/128': {'flags': 'ipv6 pim6 m6rib',
                                                               'incoming_interface_list': {'Ethernet1/33.11': {'rpf_nbr': '2001::222:1:2:1234, '
                                                                                                                          'internal'}},
                                                               'oil_count': '2',
                                                               'outgoing_interface_list': {'Ethernet1/33.11': {'oif_rpf': True,
                                                                                                               'oil_flags': 'm6rib',
                                                                                                               'oil_uptime': '00:04:03'}},
                                                               'uptime': '00:04:03'},
                                    '2001::222:2:3:1234/128': {'flags': 'pim6 m6rib ipv6',
                                                               'incoming_interface_list': {'Ethernet1/26': {'rpf_nbr': 'fe80::10, '
                                                                                                                       'internal'}},
                                                               'oil_count': '1',
                                                               'uptime': '00:04:03'},
                                    '2001::222:2:44:1234/128': {'flags': 'pim6 m6rib ipv6',
                                                                'incoming_interface_list': {'Ethernet1/26': {'rpf_nbr': 'fe80::10, '
                                                                                                                        'internal'}},
                                                                'oil_count': '1',
                                                                'uptime': '00:04:03'}}},
                            'ff1e:2222:ffff::/128': 
                                {'source_address': 
                                    {'*': 
                                        {'flags': 'mld pim6 ipv6',
                                        'incoming_interface_list': 
                                            {'Ethernet1/26': 
                                                {'rpf_nbr': 'fe80::10'}},
                                        'oil_count': '1',
                                        'uptime': '00:04:03'},
                                    '2001::222:1:1:1234/128': {'flags': 'ipv6 m6rib pim6',
                                                               'incoming_interface_list': {'Ethernet1/33.10': {'rpf_nbr': '2001::222:1:1:1234'}},
                                                               'oil_count': '2',
                                                               'uptime': '00:04:03'},
                                    '2001::222:1:2:1234/128': {'flags': 'ipv6 m6rib pim6',
                                                               'incoming_interface_list': {'Ethernet1/33.11': {'rpf_nbr': '2001::222:1:2:1234'}},
                                                               'oil_count': '2',
                                                               'outgoing_interface_list': {'Ethernet1/33.11': {'oif_rpf': True,
                                                                                                               'oil_flags': 'm6rib',
                                                                                                               'oil_uptime': '00:04:03'}},
                                                               'uptime': '00:04:03'},
                                    '2001::222:2:3:1234/128': {'flags': 'ipv6 m6rib pim6',
                                                               'incoming_interface_list': {'Ethernet1/26': {'rpf_nbr': 'fe80::10'}},
                                                               'oil_count': '1',
                                                               'uptime': '00:04:02'},
                                    '2001::222:2:44:1234/128': {'flags': 'ipv6 m6rib pim6',
                                                                'incoming_interface_list': {'Ethernet1/26': {'rpf_nbr': 'fe80::10'}},
                                                                'oil_count': '1',
                                                                'uptime': '00:04:02'}}},
                            'ff1e:2222:ffff::1:0/128': 
                                {'source_address': 
                                    {'*': {'flags': 'mld pim6 ipv6',
                                          'incoming_interface_list': {'Ethernet1/26': {'rpf_nbr': 'fe80::10'}},
                                          'oil_count': '1',
                                          'uptime': '00:04:03'},
                                    '2001::222:1:1:1234/128': {'flags': 'ipv6 '
                                                                      'm6rib '
                                                                      'pim6',
                                                              'incoming_interface_list': {'Ethernet1/33.10': {'rpf_nbr': '2001::222:1:1:1234'}},
                                                              'oil_count': '3',
                                                              'uptime': '00:04:03'},
                                    '2001::222:1:2:1234/128': {'flags': 'ipv6 '
                                                                      'm6rib '
                                                                      'pim6',
                                                              'incoming_interface_list': {'Ethernet1/33.11': {'rpf_nbr': '2001::222:1:2:1234'}},
                                                              'oil_count': '2',
                                                              'outgoing_interface_list': {'Ethernet1/33.11': {'oif_rpf': True,
                                                                                                              'oil_flags': 'm6rib',
                                                                                                              'oil_uptime': '00:04:03'}},
                                                              'uptime': '00:04:03'}}},
                            'ff1e:3333::1:0/128': 
                                {'source_address': 
                                    {'*': 
                                        {'flags': 'mld pim6 ipv6',
                                        'incoming_interface_list': {'Ethernet1/26': {'rpf_nbr': 'fe80::10'}},
                                        'oil_count': '1',
                                        'uptime': '00:04:03'},
                                    '2001::222:1:1:1234/128': {'flags': 'ipv6 m6rib pim6',
                                                             'incoming_interface_list': {'Ethernet1/33.10': {'rpf_nbr': '2001::222:1:1:1234'}},
                                                             'oil_count': '2',
                                                             'uptime': '00:04:03'},
                                    '2001::222:1:2:1234/128': {'flags': 'ipv6 m6rib pim6',
                                                             'incoming_interface_list': {'Ethernet1/33.11': {'rpf_nbr': '2001::222:1:2:1234'}},
                                                             'oil_count': '3',
                                                             'outgoing_interface_list': {'Ethernet1/33.11': {'oif_rpf': True,
                                                                                                             'oil_flags': 'm6rib',
                                                                                                             'oil_uptime': '00:04:03'}},
                                                             'uptime': '00:04:03'}}},
                            'ff1e:3333:ffff::/128': 
                                {'source_address': 
                                    {'*': 
                                        {'flags': 'mld pim6 ipv6',
                                        'incoming_interface_list': {'Ethernet1/26': {'rpf_nbr': 'fe80::10'}},
                                        'oil_count': '1',
                                        'uptime': '00:04:03'},
                                    '2001::222:1:1:1234/128': {'flags': 'ipv6 '
                                                                       'm6rib '
                                                                       'pim6',
                                                               'incoming_interface_list': {'Ethernet1/33.10': {'rpf_nbr': '2001::222:1:1:1234'}},
                                                               'oil_count': '3',
                                                               'uptime': '00:04:03'},
                                    '2001::222:1:2:1234/128': {'flags': 'ipv6 '
                                                                       'm6rib '
                                                                       'pim6',
                                                               'incoming_interface_list': {'Ethernet1/33.11': {'rpf_nbr': '2001::222:1:2:1234'}},
                                                               'oil_count': '2',
                                                               'outgoing_interface_list': {'Ethernet1/33.11': {'oif_rpf': True,
                                                                                                               'oil_flags': 'm6rib',
                                                                                                               'oil_uptime': '00:04:03'}},
                                                               'uptime': '00:04:03'},
                                    '2001::222:2:3:1234/128': {'flags': 'ipv6 '
                                                                       'm6rib '
                                                                       'pim6',
                                                               'incoming_interface_list': {'Ethernet1/26': {'rpf_nbr': 'fe80::10'}},
                                                               'oil_count': '1',
                                                               'uptime': '00:04:01'},
                                    '2001::222:2:44:1234/128': {'flags': 'ipv6 '
                                                                        'm6rib '
                                                                        'pim6',
                                                                'incoming_interface_list': {'Ethernet1/26': {'rpf_nbr': 'fe80::10'}},
                                                                'oil_count': '1',
                                                                'uptime': '00:04:00'}}},
                            'ff30::/12': 
                                {'source_address': 
                                    {'*': 
                                        {'flags': 'pim6 ipv6',
                                        'incoming_interface_list': {'Null': {'rpf_nbr': '0::'}},
                                        'oil_count': '0',
                                        'uptime': '19:55:47'}}}}}}},
            'default': 
                {'address_family': 
                    {'ipv6': 
                        {'multicast_group': 
                            {'ff30::/12': 
                                {'source_address': 
                                    {'*': 
                                        {'flags': 'pim6 ipv6',
                                        'incoming_interface_list': {'Null': {'rpf_nbr': '0::'}},
                                        'oil_count': '0',
                                        'uptime': '00:11:23'}}}}}}}}}
 
    golden_output = {'execute.return_value': '''\
        IPv6 Multicast Routing Table for VRF "default"

        (*, ff30::/12), uptime: 3d11h, pim6 ipv6 
          Incoming interface: Null, RPF nbr: 0::
          Outgoing interface list: (count: 0)


        IPv6 Multicast Routing Table for VRF "VRF1"

        (*, ff30::/12), uptime: 3d11h, pim6 ipv6 
          Incoming interface: Null, RPF nbr: 0::
          Outgoing interface list: (count: 0)
          
        (*, ff1e:1111::1:0/128), uptime: 00:04:03, mld pim6 ipv6 
          Incoming interface: loopback10, RPF nbr: 2001:9999::1
          Outgoing interface list: (count: 3)
            Ethernet1/26, uptime: 00:02:58, pim6
            port-channel1001, uptime: 00:04:01, pim6
            Ethernet1/33.11, uptime: 00:04:03, mld

        (2001::222:1:1:1234/128, ff1e:1111::1:0/128), uptime: 00:04:03, ipv6 pim6 m6rib 
          Incoming interface: Ethernet1/33.10, RPF nbr: 2001::222:1:1:1234, internal
          Outgoing interface list: (count: 3)
            Ethernet1/26, uptime: 00:02:58, pim6
            port-channel1001, uptime: 00:04:01, pim6
            Ethernet1/33.11, uptime: 00:04:03, m6rib

        (2001::222:1:2:1234/128, ff1e:1111::1:0/128), uptime: 00:04:03, ipv6 pim6 m6rib 
          Incoming interface: Ethernet1/33.11, RPF nbr: 2001::222:1:2:1234, internal
          Outgoing interface list: (count: 3)
            Ethernet1/26, uptime: 00:02:58, pim6
            port-channel1001, uptime: 00:04:01, pim6
            Ethernet1/33.11, uptime: 00:04:03, m6rib, (RPF)

        (2001::222:2:3:1234/128, ff1e:1111::1:0/128), uptime: 00:04:03, pim6 m6rib ipv6 
          Incoming interface: Ethernet1/26, RPF nbr: fe80::10, internal
          Outgoing interface list: (count: 1)
            Ethernet1/33.11, uptime: 00:04:03, m6rib

        (2001::222:2:44:1234/128, ff1e:1111::1:0/128), uptime: 00:04:03, pim6 m6rib ipv6 
          Incoming interface: Ethernet1/26, RPF nbr: fe80::10, internal
          Outgoing interface list: (count: 1)
            Ethernet1/33.11, uptime: 00:04:03, m6rib

        (*, ff1e:1111:ffff::/128), uptime: 00:04:03, mld pim6 ipv6 
          Incoming interface: Ethernet1/33.10, RPF nbr: 2001::222:1:1:1
          Outgoing interface list: (count: 2)
            Ethernet1/26, uptime: 00:04:01, pim6
            Ethernet1/33.11, uptime: 00:04:03, mld

        (2001::222:1:1:1234/128, ff1e:1111:ffff::/128), uptime: 00:04:03, ipv6 pim6 m6rib 
          Incoming interface: Ethernet1/33.10, RPF nbr: 2001::222:1:1:1234, internal
          Outgoing interface list: (count: 3)
            Ethernet1/26, uptime: 00:02:58, pim6
            port-channel1001, uptime: 00:04:00, pim6
            Ethernet1/33.11, uptime: 00:04:03, m6rib

        (2001::222:1:2:1234/128, ff1e:1111:ffff::/128), uptime: 00:04:03, ipv6 pim6 m6rib 
          Incoming interface: Ethernet1/33.11, RPF nbr: 2001::222:1:2:1234, internal
          Outgoing interface list: (count: 2)
            Ethernet1/26, uptime: 00:04:01, pim6
            Ethernet1/33.11, uptime: 00:04:03, m6rib, (RPF)

        (2001::222:2:3:1234/128, ff1e:1111:ffff::/128), uptime: 00:04:03, pim6 m6rib ipv6 
          Incoming interface: Ethernet1/26, RPF nbr: fe80::10, internal
          Outgoing interface list: (count: 1)
            Ethernet1/33.11, uptime: 00:04:03, m6rib

        (2001::222:2:44:1234/128, ff1e:1111:ffff::/128), uptime: 00:04:03, pim6 m6rib ipv6 
          Incoming interface: Ethernet1/26, RPF nbr: fe80::10, internal
          Outgoing interface list: (count: 1)
            Ethernet1/33.11, uptime: 00:04:03, m6rib

        (*, ff1e:2222:ffff::/128), uptime: 00:04:03, mld pim6 ipv6 
          Incoming interface: Ethernet1/26, RPF nbr: fe80::10
          Outgoing interface list: (count: 1)
            Ethernet1/33.11, uptime: 00:04:03, mld

        (2001::222:1:1:1234/128, ff1e:2222:ffff::/128), uptime: 00:04:03, ipv6 m6rib pim6 
          Incoming interface: Ethernet1/33.10, RPF nbr: 2001::222:1:1:1234
          Outgoing interface list: (count: 2)
            Ethernet1/26, uptime: 00:04:01, pim6
            Ethernet1/33.11, uptime: 00:04:03, m6rib

        (2001::222:1:2:1234/128, ff1e:2222:ffff::/128), uptime: 00:04:03, ipv6 m6rib pim6 
          Incoming interface: Ethernet1/33.11, RPF nbr: 2001::222:1:2:1234
          Outgoing interface list: (count: 2)
            Ethernet1/26, uptime: 00:04:01, pim6
            Ethernet1/33.11, uptime: 00:04:03, m6rib, (RPF)

        (2001::222:2:3:1234/128, ff1e:2222:ffff::/128), uptime: 00:04:02, ipv6 m6rib pim6 
          Incoming interface: Ethernet1/26, RPF nbr: fe80::10
          Outgoing interface list: (count: 1)
            Ethernet1/33.11, uptime: 00:04:02, m6rib

        (2001::222:2:44:1234/128, ff1e:2222:ffff::/128), uptime: 00:04:02, ipv6 m6rib pim6 
          Incoming interface: Ethernet1/26, RPF nbr: fe80::10
          Outgoing interface list: (count: 1)
            Ethernet1/33.11, uptime: 00:04:02, m6rib

        (*, ff1e:2222:ffff::1:0/128), uptime: 00:04:03, mld pim6 ipv6 
          Incoming interface: Ethernet1/26, RPF nbr: fe80::10
          Outgoing interface list: (count: 1)
            Ethernet1/33.11, uptime: 00:04:03, mld

        (2001::222:1:1:1234/128, ff1e:2222:ffff::1:0/128), uptime: 00:04:03, ipv6 m6rib pim6 
          Incoming interface: Ethernet1/33.10, RPF nbr: 2001::222:1:1:1234
          Outgoing interface list: (count: 3)
            Ethernet1/26, uptime: 00:02:58, pim6
            port-channel1001, uptime: 00:04:02, pim6
            Ethernet1/33.11, uptime: 00:04:03, m6rib

        (2001::222:1:2:1234/128, ff1e:2222:ffff::1:0/128), uptime: 00:04:03, ipv6 m6rib pim6 
          Incoming interface: Ethernet1/33.11, RPF nbr: 2001::222:1:2:1234
          Outgoing interface list: (count: 2)
            Ethernet1/26, uptime: 00:04:02, pim6
            Ethernet1/33.11, uptime: 00:04:03, m6rib, (RPF)

        (*, ff1e:3333::1:0/128), uptime: 00:04:03, mld pim6 ipv6 
          Incoming interface: Ethernet1/26, RPF nbr: fe80::10
          Outgoing interface list: (count: 1)
            Ethernet1/33.11, uptime: 00:04:03, mld

        (2001::222:1:1:1234/128, ff1e:3333::1:0/128), uptime: 00:04:03, ipv6 m6rib pim6 
          Incoming interface: Ethernet1/33.10, RPF nbr: 2001::222:1:1:1234
          Outgoing interface list: (count: 2)
            Ethernet1/26, uptime: 00:04:01, pim6
            Ethernet1/33.11, uptime: 00:04:03, m6rib

        (2001::222:1:2:1234/128, ff1e:3333::1:0/128), uptime: 00:04:03, ipv6 m6rib pim6 
          Incoming interface: Ethernet1/33.11, RPF nbr: 2001::222:1:2:1234
          Outgoing interface list: (count: 3)
            Ethernet1/26, uptime: 00:02:58, pim6
            port-channel1001, uptime: 00:04:01, pim6
            Ethernet1/33.11, uptime: 00:04:03, m6rib, (RPF)

        (*, ff1e:3333:ffff::/128), uptime: 00:04:03, mld pim6 ipv6 
          Incoming interface: Ethernet1/26, RPF nbr: fe80::10
          Outgoing interface list: (count: 1)
            Ethernet1/33.11, uptime: 00:04:03, mld

        (2001::222:1:1:1234/128, ff1e:3333:ffff::/128), uptime: 00:04:03, ipv6 m6rib pim6 
          Incoming interface: Ethernet1/33.10, RPF nbr: 2001::222:1:1:1234
          Outgoing interface list: (count: 3)
            Ethernet1/26, uptime: 00:02:58, pim6
            port-channel1001, uptime: 00:04:01, pim6
            Ethernet1/33.11, uptime: 00:04:03, m6rib

        (2001::222:1:2:1234/128, ff1e:3333:ffff::/128), uptime: 00:04:03, ipv6 m6rib pim6 
          Incoming interface: Ethernet1/33.11, RPF nbr: 2001::222:1:2:1234
          Outgoing interface list: (count: 2)
            Ethernet1/26, uptime: 00:04:01, pim6
            Ethernet1/33.11, uptime: 00:04:03, m6rib, (RPF)

        (2001::222:2:3:1234/128, ff1e:3333:ffff::/128), uptime: 00:04:01, ipv6 m6rib pim6 
          Incoming interface: Ethernet1/26, RPF nbr: fe80::10
          Outgoing interface list: (count: 1)
            Ethernet1/33.11, uptime: 00:04:01, m6rib

        (2001::222:2:44:1234/128, ff1e:3333:ffff::/128), uptime: 00:04:00, ipv6 m6rib pim6 
          Incoming interface: Ethernet1/26, RPF nbr: fe80::10
          Outgoing interface list: (count: 1)
            Ethernet1/33.11, uptime: 00:04:00, m6rib

        (*, ff30::/12), uptime: 19:55:47, pim6 ipv6 
          Incoming interface: Null, RPF nbr: 0::
          Outgoing interface list: (count: 0)

        IPv6 Multicast Routing Table for VRF "default"

        (*, ff30::/12), uptime: 00:11:23, pim6 ipv6 
          Incoming interface: Null, RPF nbr: 0::
          Outgoing interface list: (count: 0)


        IPv6 Multicast Routing Table for VRF "VRF"
      '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        ipv6_mroute_vrf_all_obj = ShowIpv6MrouteVrfAll(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = ipv6_mroute_vrf_all_obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        ipv6_mroute_vrf_all_obj = ShowIpv6MrouteVrfAll(device=self.device)
        parsed_output = ipv6_mroute_vrf_all_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


# ===============================================
# Unit test for 'show ip static route multicast'
# ===============================================
class test_show_ip_static_route_multicast(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'vrf': 
            {'VRF1': 
                {'address_family': 
                    {'ipv4': 
                        {'mroute': 
                            {'10.2.2.2/32': 
                                {'path': 
                                    {'0.0.0.0/32%sanity1 Vlan2': 
                                        {'neighbor_address': '0.0.0.0/32%sanity1 '
                                                              'Vlan2',
                                        'urib': True,
                                        'vrf_id': '2'}}},
                            '10.2.2.3/32': 
                                {'path': 
                                    {'0.0.0.0/32%sanity1 Vlan2': 
                                        {'neighbor_address': '0.0.0.0/32%sanity1 '
                                                             'Vlan2',
                                        'urib': True,
                                        'vrf_id': '2'}}}}}}},
            'default': 
                {'address_family': 
                    {'ipv4': 
                        {'mroute': 
                            {'112.0.0.0/8': 
                                {'path': 
                                    {'0.0.0.0/32 Null0': 
                                        {'interface_name': 'Null0',
                                        'neighbor_address': '0.0.0.0/32',
                                        'urib': True,
                                        'vrf_id': '1'}}},
                            '212.0.0.0/8': 
                                {'path': 
                                    {'0.0.0.0/32 Null0': 
                                        {'interface_name': 'Null0',
                                        'neighbor_address': '0.0.0.0/32',
                                        'urib': True,
                                        'vrf_id': '1'}}}}}}},
            'management': 
                {'address_family': 
                    {'ipv4': 
                        {'mroute': 
                            {'0.0.0.0/0': 
                                {'path': 
                                    {'172.31.200.1/32': 
                                        {'neighbor_address': '172.31.200.1/32',
                                        'urib': True,
                                        'vrf_id': '3'}}}}}}},
            'sanity1': 
                {'address_family': 
                    {'ipv4': 
                        {'mroute': 
                            {'10.2.2.2/32': 
                                {'path': 
                                    {'0.0.0.0/32 Vlan2': 
                                        {'interface_name': 'Vlan2',
                                        'neighbor_address': '0.0.0.0/32',
                                        'urib': True,
                                        'vrf_id': '4'}}},
                            '10.2.2.3/32': 
                                {'path': 
                                    {'0.0.0.0/32 Vlan2': 
                                        {'interface_name': 'Vlan2',
                                        'neighbor_address': '0.0.0.0/32',
                                        'urib': True,
                                        'vrf_id': '4'}}}}}}}}}

    golden_output = {'execute.return_value': '''\
        Mstatic-route for VRF "default"(1)
        IPv4 MStatic Routes:
          112.0.0.0/8, configured nh: 0.0.0.0/32 Null0
            (installed in urib)
          212.0.0.0/8, configured nh: 0.0.0.0/32 Null0
            (installed in urib)

            Static-route for VRF "VRF1"(2)
        IPv4 Unicast Static Routes:
          10.2.2.2/32, configured nh: 0.0.0.0/32%sanity1 Vlan2
            (installed in urib)
          10.2.2.3/32, configured nh: 0.0.0.0/32%sanity1 Vlan2
            (installed in urib)

        Static-route for VRF "management"(3)
        IPv4 Unicast Static Routes:
          0.0.0.0/0, configured nh: 172.31.200.1/32
            (installed in urib)
            rnh(installed in urib)

        Static-route for VRF "sanity1"(4)
        IPv4 Unicast Static Routes:
          10.2.2.2/32, configured nh: 0.0.0.0/32 Vlan2
            (installed in urib)
          10.2.2.3/32, configured nh: 0.0.0.0/32 Vlan2
            (installed in urib)
      '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        ip_static_route_multicast_obj = ShowIpStaticRouteMulticast(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = ip_static_route_multicast_obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        ip_static_route_multicast_obj = ShowIpStaticRouteMulticast(device=self.device)
        parsed_output = ip_static_route_multicast_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


# =================================================
# Unit test for 'show ipv6 static route multicast'
# =================================================
class test_show_ipv6_static_route_multicast(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        'vrf': 
            {'default': 
                {'address_family': 
                    {'ipv6': 
                        {'mroute': 
                            {'126::/16': 
                                {'path': 
                                    {'0:: Null0': 
                                        {'bfd_enable': False,
                                        'interface_name': 'Null0',
                                        'mroute_int': 'Null0',
                                        'neighbor_address': '0::',
                                        'nh_vrf': 'default',
                                        'preference': '1',
                                        'reslv_tid': '80000001',
                                        'rnh_status': 'not '
                                                      'installed '
                                                      'in '
                                                      'u6rib',
                                        'vrf_id': '1'}}},
                            '127::/16': 
                                {'path': 
                                    {'0:: port-channel8': 
                                        {'bfd_enable': False,
                                        'interface_name': 'port-channel8',
                                        'mroute_int': 'port-channel8',
                                        'neighbor_address': '0::',
                                        'nh_vrf': 'default',
                                        'preference': '2',
                                        'reslv_tid': '80000001',
                                        'rnh_status': 'not '
                                                      'installed '
                                                      'in '
                                                      'u6rib',
                                        'vrf_id': '1'}}},
                            '226::/16': 
                                {'path': 
                                    {'0:: Null0': 
                                        {'bfd_enable': False,
                                        'interface_name': 'Null0',
                                        'mroute_int': 'Null0',
                                        'neighbor_address': '0::',
                                        'nh_vrf': 'default',
                                        'preference': '1',
                                        'reslv_tid': '80000001',
                                        'rnh_status': 'not '
                                                      'installed '
                                                      'in '
                                                      'u6rib',
                                        'vrf_id': '1'}}},
                            '227::/16': 
                                {'path': 
                                    {'0:: Ethernet1/2.10': 
                                        {'bfd_enable': False,
                                        'interface_name': 'Ethernet1/2.10',
                                        'mroute_int': 'Ethernet1/2.10',
                                        'neighbor_address': '0::',
                                        'nh_vrf': 'default',
                                        'preference': '3',
                                        'reslv_tid': '80000001',
                                        'rnh_status': 'not '
                                                   'installed '
                                                   'in '
                                                   'u6rib',
                                        'vrf_id': '1'}}}}}}}}}
  
    golden_output = {'execute.return_value': '''\
        IPv6 Configured Static Routes for VRF "default"(1)

        126::/16 -> Null0, preference: 1
        nh_vrf(default) reslv_tid 80000001
        real-next-hop: 0::, interface: Null0
          rnh(not installed in u6rib)
          bfd_enabled no
        226::/16 -> Null0, preference: 1
        nh_vrf(default) reslv_tid 80000001
        real-next-hop: 0::, interface: Null0
          rnh(not installed in u6rib)
          bfd_enabled no
        127::/16 -> port-channel8, preference: 2
        nh_vrf(default) reslv_tid 80000001
        real-next-hop: 0::, interface: port-channel8
          rnh(not installed in u6rib)
          bfd_enabled no
        227::/16 -> Ethernet1/2.10, preference: 3
        nh_vrf(default) reslv_tid 80000001
        real-next-hop: 0::, interface: Ethernet1/2.10
          rnh(not installed in u6rib)
          bfd_enabled no   

          IPv6 Configured Static Routes for VRF "default"(1)    
      '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        ipv6_static_route_multicast_obj = ShowIpv6StaticRouteMulticast(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = ipv6_static_route_multicast_obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        ipv6_static_route_multicast_obj = ShowIpv6StaticRouteMulticast(device=self.device)
        parsed_output = ipv6_static_route_multicast_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()