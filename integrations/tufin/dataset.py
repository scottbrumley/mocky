# Dictionaries of Responses
devices_info = {
    "devices":
        {
            "device": [
                {
                    "id": 553,
                    "name": "asa",
                    "ip": "9.9.9.9",
                    "model": "5520",
                    "vendor": "Cisco",
                    "device_type": "asa"
                },
                {
                    "id": 2,
                    "name": "cisco_device_name",
                    "ip": "7.7.7.7",
                    "model": "2940",
                    "vendor": "Cisco",
                    "device_type": "router"
                }
            ]
        }
}
applications_info = {
    "applications":
        {
            "application": [
                {
                    "id": 443,
                    "name": "Service Now",
                    "vendor": "Service Now",
                    "comment": "",
                    "owner": {
                        "name": "Jack Reacher",
                        "id": 2
                    },
                    "status": "CONNECTED",
                    "decommissioned": False
                },
                {
                    "id": 3,
                    "name": "Jira",
                    "vendor": "Atlassian",
                    "comment": "",
                    "owner": {
                        "name": "John Wick",
                        "id": 3
                    },
                    "status": "CONNECTED",
                    "decommissioned": False
                }
            ]
        }
}
app_connections_info = {
    "connections":
        {
            "connection": [
                {
                    "id": 443,
                    "name": "Service Now",
                    "vendor": "Service Now",
                    "services": {
                        "service": [
                            {
                                "id": 5344,
                                "name": "ftp",
                                "type":"host"
                        }
                    ]
                    },
                    "destinations": {
                        "destination": [
                            {
                                "id": 4055,
                                "name": "Finance01",
                                "type":"host"
                        }
                    ]
                    },
                    "sources": {
                        "source": [
                            {
                                "id": 4034,
                                "name": "CRM01",
                                "type":"host"
                        }
                    ]
                    },
                    "comment": "",
                    "owner": {
                        "name": "Jack Reacher",
                        "id": 2
                    },
                    "external": True,
                    "status": "L7_APPLICATION",
                    "decommissioned": False
                },
                {
                    "id": 3,
                    "name": "Jira",
                    "vendor": "Atlassian",
                    "services": {
                        "service": [
                            {
                                "id": 2044,
                                "name": "https",
                                "type":"host"
                        }
                    ]
                    },
                    "destinations": {
                        "destination": [
                            {
                                "id": 4054,
                                "name": "Finance01",
                                "type":"host"
                        }
                    ]
                    },
                    "sources": {
                        "source": [
                            {
                                "id": 4044,
                                "name": "JIRA01",
                                "type":"host"
                        }
                    ]
                    },
                    "comment": "",
                    "owner": {
                        "name": "John Wick",
                        "id": 3
                    },
                    "external": True,
                    "status": "L7_APPLICATION",
                    "decommissioned": False
                }
            ]
        }
}
