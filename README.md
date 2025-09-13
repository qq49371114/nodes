# FreeProxiesScraper

Fork from TopFreeProxies.

## 仓库介绍
本仓库自动化功能全部基于 `GitHub Actions` 实现，如有需要可以自行 Fork 实现个性化需求，功能配置在 `./utils/config.ini` 配置文件中。

对网络上各免费节点池及博主分享的节点进行测速筛选出较为稳定高速的节点，再导入到仓库中进行分享记录。所筛选的节点链接在仓库 `./sub/sub_list.json` 文件中，其中大部分为其他 `GitHub` 仓库链接，如果大家有好的订阅链接欢迎提交 PR ，这些链接包含的所有节点会合并在仓库 `./sub/sub_merge.txt` 中。

测速筛选后的节点订阅文件在仓库根目录 `Eterniy`(Base64) 和 `Eternity.yaml`(Clash)。同时在仓库的 `./update` 中保留了原始节点链接的的记录。

订阅转换使用 [subconverter](https://github.com/tindy2013/subconverter) 实现，测速功能使用 [LiteSpeedTest](https://github.com/xxf098/LiteSpeedTest) 在 `GitHub Actions` 环境下实现，所以美国节点较多，不能很好代表国内网络环境下节点可用性，目前正在解决这一问题。

虽然是测速筛选过后的节点，但仍然会出现部分节点不可用的情况，遇到这种情况建议选择`Clash`, `Shadowrocket`之类能自动切换低延迟节点的客户端。

## 使用方法
将以下订阅链接导入相应客户端即可。链接中大部分为 SS 协议节点，少量 Vmess, Trojan ,SSR 协议节点，建议选择协议支持完整的客户端。

- [多协议Base64编码](https://raw.githubusercontent.com/caijh/FreeProxiesScraper/master/Eternity)
- [Clash](https://raw.githubusercontent.com/caijh/FreeProxiesScraper/master/Eternity.yaml)

>`Clash`链接所使用的配置在仓库`./update/provider/`中，有相应配置文件和以国家分类的`proxy-provider`。
>
>需要其它配置可使用订阅转换工具自行转换。
>自用在线订阅转换网址：[sub-web-modify](https://sub.v1.mk/)

## 节点信息
### 高速节点
高速节点数量: `87`
<details>
  <summary>展开复制节点</summary>

    trojan://slch2024@193.9.49.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#05-0004-RELAY
    trojan://slch2024@192.65.217.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252F%2525252FTelegram#05-0005-RELAY
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo5YWMzZDRkZC04ZDUxLTQ5MzEtOWNkYi05MGUzNWE0NTYwNzk@118.170.235.179:10004#05-0006-TW
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDAwNy1NWSIsImFkZCI6InQuY25tamNuLmN5b3UiLCJwb3J0IjoiMTY2MzIiLCJ0eXBlIjoibm9uZSIsImlkIjoiNzQzZGJjZTktZWM3ZC00OWRkLWI5ZDYtM2IxYTE1MWU3MjlmIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoidC5jbm1qY24uY3lvdSIsInRscyI6IiJ9
    trojan://slch2024@185.162.228.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#05-0008-RELAY
    trojan://slch2024@190.93.246.87:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#05-0009-RELAY
    trojan://slch2024@185.193.29.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#05-0019-RELAY
    ssr://eWQtMDIucGFvZnVubGluay5jb206MTA1MjphdXRoX2FlczEyOF9zaGExOmNoYWNoYTIwLWlldGY6cGxhaW46WW5oemJuVmpjbWRyTm1obWFYTm8vP2dyb3VwPVUxTlNVSEp2ZG1sa1pYSSZyZW1hcmtzPU1EVXRNREF5TUMxRFRnJm9iZnNwYXJhbT1ORFUyTnpJeU1qSTFORFV1YldsamNtOXpiMlowTG1OdmJRJnByb3RvcGFyYW09TWpJeU5UUTFPbFJKZGxNeVF3
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTphYzk4NmEyZS1iNWI5LTRkYTYtOGU1OC03YTdmNDNmODgwOWE@118.170.212.135:10017#05-0021-TW
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTphNzYyMmQyNC02N2I4LTQ2YmMtOGYxNi00ZDZhYjlhNDQxM2E@125.231.66.16:10070#05-0022-TW
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTphYzk4NmEyZS1iNWI5LTRkYTYtOGU1OC03YTdmNDNmODgwOWE@125.231.93.197:10056#05-0023-TW
    trojan://slch2024@193.124.224.87:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram#05-0026-RELAY
    trojan://slch2024@190.93.247.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252F#05-0145-RELAY
    trojan://slch2024@176.124.223.91:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252F#05-0147-RELAY
    trojan://slch2024@198.12.145.91:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252F#05-0148-US
    trojan://slch2024@204.93.210.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252F#05-0149-RELAY
    trojan://slch2024@45.67.215.91:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252F#05-0150-RU
    trojan://slch2024@62.72.166.91:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252F#05-0151-RELAY
    trojan://slch2024@96.43.100.91:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252F#05-0152-RELAY
    trojan://slch2024@185.207.197.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252F#05-0165-RELAY
    trojan://slch2024@185.135.9.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252F#05-0166-RELAY
    trojan://slch2024@205.233.181.87:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252F#05-0167-RELAY
    trojan://slch2024@212.183.88.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252F%252525E7%25252594%252525B1%252525E9%2525259B%252525B6%252525E5%252525BC%25252580%252525E5%252525A7%2525258B#06-0027-AT
    trojan://slch2024@185.18.250.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252F%252525E7%25252594%252525B1%252525E9%2525259B%252525B6%252525E5%252525BC%25252580%252525E5%252525A7%2525258B#06-0028-RELAY
    trojan://slch2024@195.26.229.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram%252525F0%2525259F%25252587%252525AE%252525F0%2525259F%25252587%252525B7%25252540ShadowProxy66#06-0029-RELAY
    trojan://slch2024@195.26.229.87:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegramU0001F1E8U0001F1F3#06-0030-RELAY
    trojan://slch2024@193.124.224.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegramU0001F1E8U0001F1F3#06-0031-RELAY
    trojan://slch2024@188.244.122.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252F%252525E7%25252594%252525B1%252525E9%2525259B%252525B6%252525E5%252525BC%25252580%252525E5%252525A7%2525258B#06-0032-RELAY
    trojan://slch2024@185.251.83.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram#06-0033-RELAY
    trojan://slch2024@185.251.80.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252F%252525E7%25252594%252525B1%252525E9%2525259B%252525B6%252525E5%252525BC%25252580%252525E5%252525A7%2525258B#06-0034-RELAY
    trojan://slch2024@185.238.228.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#06-0035-RELAY
    trojan://slch2024@185.251.81.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram#06-0036-RELAY
    trojan://slch2024@185.251.82.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram#06-0037-RELAY
    trojan://slch2024@185.7.240.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram%25252540ShadowProxy66#06-0038-RELAY
    trojan://slch2024@185.16.110.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#06-0039-FR
    trojan://slch2024@185.156.19.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252F%252525E7%25252594%252525B1%252525E9%2525259B%252525B6%252525E5%252525BC%25252580%252525E5%252525A7%2525258B#06-0040-RELAY
    trojan://slch2024@194.76.18.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram#06-0042-KZ
    trojan://slch2024@185.176.26.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram#06-0043-RELAY
    trojan://slch2024@188.42.88.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram#06-0044-RELAY
    trojan://slch2024@188.42.89.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegramU0001F1E8U0001F1F3#06-0045-RELAY
    trojan://slch2024@188.164.248.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram#06-0046-RELAY
    trojan://slch2024@185.18.184.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#06-0047-RELAY
    trojan://slch2024@188.164.248.87:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram#06-0048-RELAY
    trojan://slch2024@185.148.107.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegramU0001F1E8U0001F1F3#06-0052-RELAY
    trojan://slch2024@185.174.138.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram#06-0055-RELAY
    trojan://slch2024@185.176.24.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegramU0001F1E8U0001F1F3#06-0056-RELAY
    trojan://slch2024@185.59.218.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram#06-0057-RELAY
    trojan://slch2024@188.42.145.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#06-0058-RELAY
    trojan://slch2024@199.68.156.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram%252525F0%2525259F%25252587%252525AE%252525F0%2525259F%25252587%252525B7ShadowProxy66#06-0061-US
    trojan://slch2024@209.94.90.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram%252525F0%2525259F%25252587%252525AE%252525F0%2525259F%25252587%252525B7ShadowProxy66#06-0062-US
    trojan://slch2024@192.200.160.87:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#06-0063-US
    trojan://slch2024@195.13.44.87:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram#06-0064-RELAY
    trojan://slch2024@192.200.160.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#06-0065-US
    trojan://slch2024@199.34.229.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram#06-0066-US
    trojan://slch2024@199.34.230.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#06-0067-US
    trojan://slch2024@192.0.54.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#06-0068-US
    trojan://slch2024@185.148.104.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#06-0069-RELAY
    trojan://slch2024@192.0.63.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#06-0070-US
    trojan://slch2024@199.68.156.87:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram#06-0071-US
    trojan://slch2024@198.62.62.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#06-0072-US
    trojan://slch2024@199.181.197.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#06-0073-RELAY
    trojan://slch2024@195.13.44.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram#06-0076-RELAY
    trojan://slch2024@216.205.52.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram#06-0077-RELAY
    trojan://slch2024@185.148.105.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram#06-0078-RELAY
    trojan://slch2024@195.13.45.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram#06-0079-RELAY
    trojan://slch2024@205.233.181.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram#06-0080-RELAY
    trojan://slch2024@209.46.30.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252F%252525E7%25252594%252525B1%252525E9%2525259B%252525B6%252525E5%252525BC%25252580%252525E5%252525A7%2525258B#06-0081-RELAY
    trojan://slch2024@198.62.62.87:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram#06-0082-US
    trojan://slch2024@216.24.57.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram#06-0083-US
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpYVU1UeWdFTTFqVllJdnlzWEtxQTVU@hackney-latest-strike.freesocks.work:443#08-0084-US
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@185.153.197.5:989#08-0085-MD
    ss://YWVzLTI1Ni1nY206MGE5MTRlOWEtM2UzYi00NzBmLWEyNjctN2VhNzA4M2M0NWJi@77.110.110.240:443#23-0086-AT
    ss://YWVzLTI1Ni1nY206YTdmMDgyYzEtMGQxMi00NjA5LWI2YmYtZTc2MGI2NjhjZjIz@77.110.110.240:443#23-0087-AT
    ss://YWVzLTI1Ni1nY206MTAyYWQzZGEtMmQ1NS00OWQ2LWI4YzgtMmQ3ZTA0ZGYzM2Nh@77.110.110.240:443#23-0089-AT
    ss://YWVzLTI1Ni1nY206M2Y0MGJmM2QtMmYxZS00ZjQzLWJmNTQtZTVmZTc0MmEzYjRl@77.110.110.240:443#23-0090-AT
    ss://YWVzLTI1Ni1nY206ZDcwZWY4YjUtNjA0OC00YzBkLWJlNGQtZmM2MDM5OWIwZjQ1@77.110.110.240:443#23-0091-AT
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpqaWZ1UjJOVE0wWXQ@62.133.62.109:443#23-0092-FR
    vmess://eyJ2IjoiMiIsInBzIjoiMjMtMDA5NS1ERSIsImFkZCI6IjU3LjEyOS4yNC4xMjUiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjAzZmNjNjE4LWI5M2QtNjc5Ni02YWVkLThhMzhjOTc1ZDU4MSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvbGlua3Z3cz9lZD0yMDQ4QEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTiIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    ss://YWVzLTEyOC1nY206MTAwODY@160.16.123.124:10087#23-0097-JP
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpQdEh2NGJPNGpQdEJzSFdTbDFuNVFk@45.95.232.236:4248#23-0101-CH
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@104.192.226.106:989#23-0103-UStrojan%2F%2Fslch2024%40195.26.229.1952096%3FallowInsecure%3D1%26sni%3Docost-dy.wmlefl.cc%26ws%3D1%26wspath%3D%25252F%2525E7%252594%2525B1%2525E9%25259B%2525B6%2525E5%2525BC%252580%2525E5%2525A7%25258B%2305-0000-RELAY
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo5dHFoTWRJclRrZ1E0NlB2aHlBdE1I@92.112.126.90:443#23-0120-NL
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo5bGNDdnpOeHBOc25JTnlhWWZ6Yzhl@212.113.106.76:29149#23-0121-AT
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo5ZFZMYWNjR0JxRng@62.60.233.21:443#23-0122-TR
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpVS3Z5aXhLUmRUU3cyOFFwODdrZUVS@macintosh.outlinekeys.net:19609#23-0124-NL
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo0YTJyZml4b3BoZGpmZmE4S1ZBNEFh@45.87.175.171:8080#23-0135-LT
    


</details>

### 所有节点
合并节点总数: `88`
[节点链接](https://raw.githubusercontent.com/caijh/TopFreeProxies/master/sub/sub_merge_base64.txt)

### 节点来源
- [clashnode](https://github.com/imyaoxp/clashnode), 节点数量: `88`


## 仓库声明
订阅节点仅作学习交流使用，只是对网络上节点的优选排序，用于查找资料，学习知识，不做任何违法行为。所有资源均来自互联网，仅供大家交流学习使用，出现违法问题概不负责。

