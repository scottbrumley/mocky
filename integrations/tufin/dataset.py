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
                    "id": "443",
                    "name": "Service Now",
                    "vendor": "Service Now",
                    "comment": "",
                    "owner": {
                        "name": "Jack Reacher",
                        "id": "2"
                    },
                    "status": "CONNECTED",
                    "decommissioned": False
                },
                {
                    "id": "3",
                    "name": "Jira",
                    "vendor": "Atlassian",
                    "comment": "",
                    "owner": {
                        "name": "John Wick",
                        "id": "3"
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
                    "applicationId": "10202",
                    "name": "Service Now",
                    "vendor": "Service Now",
                    ""
                    "comment": "",
                    "owner": {
                        "name": "Jack Reacher",
                        "id": "2"
                    },
                    "status": "L7_APPLICATION",
                    "decommissioned": False
                },
                {
                    "applicationId": "1110",
                    "name": "Jira",
                    "vendor": "Atlassian",
                    "comment": "",
                    "owner": {
                        "name": "John Wick",
                        "id": "3"
                    },
                    "status": "L7_APPLICATION",
                    "decommissioned": False
                }
            ]
        }
}