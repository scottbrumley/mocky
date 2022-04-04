system_info = f"""<response status="success">
                    <result>
                    <system>
                    <hostname>PA-7080</hostname>
                    <ip-address>1.1.1.1</ip-address>
                    <public-ip-address>unknown</public-ip-address>
                    <netmask>255.255.255.0</netmask>
                    <default-gateway>192.168.1.1</default-gateway>
                    <is-dhcp>no</is-dhcp>
                    <ipv6-address>unknown</ipv6-address>
                    <ipv6-link-local-address>fe80::ea98:6dff:fe54:8200/64</ipv6-link-local-address>
                    <mac-address>be:ef:ca:ce:00:00</mac-address>
                    <time>Wed May 6 21:34:08 2020 </time>
                    <uptime>223 days, 0:56:12</uptime>
                    <devicename>PA-7080</devicename>
                    <family>7000</family>
                    <model>PA-7080</model>
                    <serial>01123123123</serial>
                    <cloud-mode>non-cloud</cloud-mode>
                    <sw-version>9.2.0</sw-version>
                    <global-protect-client-package-version>5.1.1</global-protect-client-package-version>
                    <iot-version>0</iot-version>
                    <app-version>8267-6070</app-version>
                    <app-release-date>2020/05/06 05:12:12 EEST</app-release-date>
                    <av-version>3340-3851</av-version>
                    <av-release-date>2020/05/06 14:00:11 EEST</av-release-date>
                    <threat-version>8267-6070</threat-version>
                    <threat-release-date>2020/05/06 05:12:12 EEST</threat-release-date>
                    <wf-private-version>0</wf-private-version>
                    <wf-private-release-date>unknown</wf-private-release-date>
                    <url-db>paloaltonetworks</url-db>
                    <wildfire-version>451549-454482</wildfire-version>
                    <wildfire-release-date>2020/05/06 20:57:09 EEST</wildfire-release-date>
                    <wildfire-rt>Enabled</wildfire-rt>
                    <url-filtering-version>20200506.20279</url-filtering-version>
                    <global-protect-datafile-version>unknown</global-protect-datafile-version>
                    <global-protect-datafile-release-date>unknown</global-protect-datafile-release-date>
                    <global-protect-clientless-vpn-version>0</global-protect-clientless-vpn-version>
                    <logdb-version>9.2.18</logdb-version>
                    <platform-family>220</platform-family>
                    <vpn-disable-mode>off</vpn-disable-mode>
                    <multi-vsys>off</multi-vsys>
                    <operational-mode>normal</operational-mode>
                    <device-certificate-status>None</device-certificate-status>
                    </system>
                    </result>
                    </response>"""


def jobs_id(job_id):
    return_str = """<response status="success">
                        <result>
                        <job>
                        <tenq>2020/05/07 11:29:48</tenq>
                        <tdeq>11:29:48</tdeq>
                        <id>""" + job_id + """</id>
                        <user>admin</user>
                        <type>Commit</type>
                        <status>FIN</status>
                        <queued>NO</queued>
                        <stoppable>no</stoppable>
                        <result>OK</result>
                        <tfin>11:34:12</tfin>
                        <description/>
                        <positionInQ>0</positionInQ>
                        <progress>100</progress>
                        <details>
                        <line>Configuration committed successfully</line>
                        </details>
                        </job>
                        </result>
                        </response>"""
    return return_str


download_content_upgrade = """<response status="success" code="19">
                        <result>
                        <msg>
                        <line>Download job enqueued with jobid 50</line>
                        </msg>
                        <job>50</job>
                        </result>
                        </response>"""

