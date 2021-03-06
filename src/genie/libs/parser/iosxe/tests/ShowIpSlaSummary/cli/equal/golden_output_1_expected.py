expected_output = {
    'ids': {
        '1': {
            'state': 'active',
            'type': 'tcp-connect',
            'destination': '10.151.213.32',
            'rtt_stats': 'RTT=44',
            'rtt_stats_msecs': 44,
            'return_code': 'OK',
            'last_run': '21 seconds ago',
        },
        '2': {
            'state': 'active',
            'type': 'dns',
            'destination': '10.84.2.123',
            'rtt_stats': '-',
            'return_code': 'Timeout',
            'last_run': '7 seconds ago',
        },
        '3': {
            'state': 'active',
            'type': 'udp-jitter',
            'destination': '10.204.11.1',
            'rtt_stats': 'RTT=1',
            'rtt_stats_msecs': 1,
            'return_code': 'OK',
            'last_run': '54 seconds ago',
        },
        '4': {
            'state': 'active',
            'type': 'udp-jitter',
            'destination': '10.145.33.3',
            'rtt_stats': 'RTT=1',
            'rtt_stats_msecs': 1,
            'return_code': 'OK',
            'last_run': '15 seconds ago',
        },
        '5': {
            'state': 'active',
            'type': 'udp-jitter',
            'destination': '10.115.32.2',
            'rtt_stats': 'RTT=1',
            'rtt_stats_msecs': 1,
            'return_code': 'OK',
            'last_run': '8 seconds ago',
        },
        '6': {
            'state': 'active',
            'type': 'udp-jitter',
            'destination': '11.311.31.2',
            'rtt_stats': 'RTT=1',
            'rtt_stats_msecs': 1,
            'return_code': 'OK',
            'last_run': '40 seconds ago',
        },
        '7': {
            'state': 'active',
            'type': 'icmp-echo',
            'destination': '172.16.94.1',
            'rtt_stats': 'RTT=1',
            'rtt_stats_msecs': 1,
            'return_code': 'OK',
            'last_run': '2 seconds ago',
        }
    }
}