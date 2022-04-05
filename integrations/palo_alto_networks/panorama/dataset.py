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


install_content_upgrade = """<response status="success" code="19">
                        <result>
                        <msg>
                        <line>Content install job enqueued with jobid 51</line>
                        </msg>
                        <job>51</job>
                        </result>
                        </response>"""


pan_os_upgrade_check = """<response status="success">
                            <result>
                            <sw-updates last-updated-at="2020/04/22 09:52:50">
                            <msg/>
                            <versions>
                            <entry>
                            <version>9.1.2-h1</version>
                            <filename>PanOS_220-9.1.2-h1</filename>
                            <size>277</size>
                            <size-kb>283789</size-kb>
                            <released-on>2020/04/29 08:01:29</released-on>
                            <release-notes>
                            <![CDATA[
                            https://prod.itpdownloads.paloaltonetworks.com/software/PAN-OS-9.1.2-h1-RN.pdf?Expires=1589107118&KeyName=contentupdates-prod&Signature=fV7QnxUrqFQ5w7Zfe6MQtKRFxvE=
                            ]]>
                            </release-notes>
                            <downloaded>no</downloaded>
                            <current>no</current>
                            <latest>no</latest>
                            <uploaded>no</uploaded>
                            </entry>
                            <entry>
                            <version>9.1.2</version>
                            <filename>PanOS_220-9.1.2</filename>
                            <size>277</size>
                            <size-kb>283775</size-kb>
                            <released-on>2020/04/08 10:49:11</released-on>
                            <release-notes>
                            <![CDATA[
                            https://www.paloaltonetworks.com/documentation/91/pan-os/pan-os-release-notes
                            ]]>
                            </release-notes>
                            <downloaded>no</downloaded>
                            <current>no</current>
                            <latest>no</latest>
                            <uploaded>no</uploaded>
                            </entry>
                            <entry>
                            <version>9.1.1</version>
                            <filename>PanOS_220-9.1.1</filename>
                            <size>277</size>
                            <size-kb>283762</size-kb>
                            <released-on>2020/02/10 14:10:23</released-on>
                            <release-notes>
                            <![CDATA[
                            https://www.paloaltonetworks.com/documentation/91/pan-os/pan-os-release-notes
                            ]]>
                            </release-notes>
                            <downloaded>no</downloaded>
                            <current>no</current>
                            <latest>no</latest>
                            <uploaded>no</uploaded>
                            </entry>
                            <entry>
                            <version>9.1.0</version>
                            <filename>PanOS_220-9.1.0</filename>
                            <size>421</size>
                            <size-kb>431135</size-kb>
                            <released-on>2019/12/13 12:51:48</released-on>
                            <release-notes>
                            <![CDATA[
                            https://www.paloaltonetworks.com/documentation/91/pan-os/pan-os-release-notes
                            ]]>
                            </release-notes>
                            <downloaded>yes</downloaded>
                            <current>no</current>
                            <latest>no</latest>
                            <uploaded>no</uploaded>
                            </entry>
                            </versions>
                            </sw-updates>
                            </result>
                            </response>"""


pan_os_upgrade_download = """<response status="success" code="19">
                        <result>
                        <msg>
                        <line>Download job enqueued with jobid 52</line>
                        </msg>
                        <job>52</job>
                        </result>
                        </response>"""

pan_os_upgrade_install = """<response status="success" code="19">
                        <result>
                        <msg>
                        <line>Install job enqueued with jobid 54</line>
                        </msg>
                        <job>54</job>
                        </result>
                        </response>"""

restart_fw = """<response status="success">
                        <result>Command succeeded with no output</result>
                        </response>"""

test_security_policy = """<response cmd="status" status="success">
                        <result>
                            <rules>
                                <entry name='FromTrust'>
                                    <index>1</index>
                                    <from>Trust-L3</from>
                                    <source>any</source>
                                    <source-region>none</source-region>
                                    <to>
                                        <member>Untrust-L3</member>
                                    </to>
                                    <destination>any</destination>
                                    <destination-region>none</destination-region>
                                    <user>any</user>
                                    <source-device>any</source-device>
                                    <destinataion-device>any</destinataion-device>
                                    <category>any</category>
                                    <application_service>0:any/any/any/any</application_service>
                                    <action>allow</action>
                                    <icmp-unreachable>no</icmp-unreachable>
                                    <terminal>yes</terminal>
                                </entry>
                            </rules>
                        </result>
                    </response>"""


