expected_output = {
    "interfaces": {
        "Port-channel1": {
            "name": "Port-channel1",
            "protocol": "lacp",
            "members": {
                "GigabitEthernet2": {
                    "interface": "GigabitEthernet2",
                    "oper_key": 1,
                    "admin_key": 0,
                    "port_num": 1,
                    "lacp_port_priority": 32768,
                    "flags": "SA",
                    "activity": "active",
                    "partner_id": "001e.49ff.a3e6",
                    "age": 25,
                    "port_state": 61,
                },
                "GigabitEthernet3": {
                    "interface": "GigabitEthernet3",
                    "oper_key": 1,
                    "admin_key": 0,
                    "port_num": 1,
                    "lacp_port_priority": 32768,
                    "flags": "SA",
                    "activity": "active",
                    "port_state": 61,
                    "partner_id": "001e.49ff.a3e6",
                    "age": 19,
                },
            },
        },
        "Port-channel2": {
            "name": "Port-channel2",
            "protocol": "lacp",
            "members": {
                "GigabitEthernet4": {
                    "interface": "GigabitEthernet4",
                    "oper_key": 2,
                    "admin_key": 0,
                    "port_num": 1,
                    "lacp_port_priority": 32768,
                    "flags": "SP",
                    "port_state": 60,
                    "activity": "passive",
                    "partner_id": "001e.49ff.a3e6",
                    "age": 15,
                },
                "GigabitEthernet5": {
                    "interface": "GigabitEthernet5",
                    "oper_key": 2,
                    "admin_key": 0,
                    "port_num": 1,
                    "lacp_port_priority": 32768,
                    "flags": "SP",
                    "port_state": 60,
                    "activity": "passive",
                    "partner_id": "001e.49ff.a3e6",
                    "age": 1,
                },
                "GigabitEthernet6": {
                    "interface": "GigabitEthernet6",
                    "oper_key": 2,
                    "admin_key": 0,
                    "port_num": 1,
                    "lacp_port_priority": 32768,
                    "flags": "SP",
                    "port_state": 60,
                    "activity": "passive",
                    "partner_id": "001e.49ff.a3e6",
                    "age": 0,
                },
            },
        },
    }
}
