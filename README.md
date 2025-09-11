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
高速节点数量: `81`
<details>
  <summary>展开复制节点</summary>

    trojan://slch2024@185.59.218.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram#05-0001-RELAY
    trojan://slch2024@188.244.122.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#05-0002-RELAY
    trojan://slch2024@185.174.138.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram#05-0003-RELAY
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@185.153.197.5:989#05-0005-MD
    trojan://slch2024@216.205.52.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram#05-0010-RELAY
    trojan://slch2024@190.93.247.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#05-0011-RELAY
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDAxOC1ISyIsImFkZCI6IjFlNDI2MDQ2LXQwZmRzMC10MTJjbmotMW9sOTcuaGsucDVwdi5jb20iLCJwb3J0IjoiODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTNmYjY5ZmMtNzdjZi0xMWVlLTg1ZWUtZjIzYzkxMzY5ZjJkIiwiYWlkIjoiMiIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiMWU0MjYwNDYtdDBmZHMwLXQxMmNuai0xb2w5Ny5oay5wNXB2LmNvbSIsInRscyI6IiJ9
    trojan://slch2024@185.238.228.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252F#05-0141-RELAY
    trojan://slch2024@213.241.198.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252F#05-0143-RELAY
    trojan://slch2024@198.202.211.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252F#05-0144-RELAY
    trojan://slch2024@192.169.220.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252F#05-0145-US
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpvWklvQTY5UTh5aGNRVjhrYTNQYTNB@193.29.139.144:8080#05-0146-NL
    trojan://slch2024@199.34.228.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252F#05-0147-US
    trojan://slch2024@204.93.210.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252F#05-0148-RELAY
    trojan://slch2024@213.182.199.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252F#05-0149-RELAY
    trojan://slch2024@185.18.184.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252F#05-0152-RELAY
    trojan://slch2024@185.148.105.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252F#05-0153-RELAY
    trojan://slch2024@194.53.53.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252F#05-0155-RELAY
    trojan://slch2024@188.164.158.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegramU0001F1E8U0001F1F3#06-0028-RELAY
    trojan://slch2024@188.164.159.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegramU0001F1E8U0001F1F3#06-0029-RELAY
    trojan://slch2024@212.183.88.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#06-0030-AT
    trojan://slch2024@195.26.229.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram#06-0031-RELAY
    trojan://slch2024@193.124.224.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram#06-0032-RELAY
    trojan://slch2024@185.251.80.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#06-0033-RELAY
    trojan://slch2024@185.251.83.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram#06-0034-RELAY
    trojan://slch2024@185.251.81.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#06-0035-RELAY
    trojan://slch2024@185.251.82.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram#06-0036-RELAY
    trojan://slch2024@185.7.240.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram#06-0037-RELAY
    trojan://slch2024@185.16.110.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram#06-0038-FR
    trojan://slch2024@185.156.19.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegramU0001F1E8U0001F1F3#06-0040-RELAY
    trojan://slch2024@194.36.55.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#06-0041-RELAY
    vmess://eyJ2IjoiMiIsInBzIjoiMDYtMDA0Mi1ISyIsImFkZCI6IjEwMy4yNDIuMTUuMjAzIiwicG9ydCI6IjE2NTg2IiwidHlwZSI6Im5vbmUiLCJpZCI6ImZkYzA2NDI0LTY1ZGEtNDEzMy05NTNhLTUxZTMzZTNlNmQzNyIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6InRscyJ9
    trojan://slch2024@194.76.18.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram#06-0044-KZ
    trojan://slch2024@185.176.26.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram#06-0045-RELAY
    trojan://slch2024@188.42.88.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram#06-0046-RELAY
    trojan://slch2024@188.42.89.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#06-0047-RELAY
    trojan://slch2024@188.164.248.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram#06-0049-RELAY
    trojan://slch2024@188.164.248.87:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram#06-0050-RELAY
    trojan://slch2024@185.148.107.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram%25252540ShadowProxy66#06-0051-RELAY
    trojan://slch2024@185.176.24.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegramU0001F1E8U0001F1F3#06-0052-RELAY
    trojan://slch2024@209.94.90.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram#06-0055-US
    trojan://slch2024@192.0.54.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#06-0056-US
    trojan://slch2024@199.34.229.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram#06-0057-US
    trojan://slch2024@195.13.44.87:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram#06-0058-RELAY
    trojan://slch2024@185.148.106.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram#06-0059-RELAY
    vmess://eyJ2IjoiMiIsInBzIjoiMDYtMDA2Mi1RQSIsImFkZCI6IjE1Ni4yNDQuNDYuMTk4IiwicG9ydCI6IjM2MjM2IiwidHlwZSI6Im5vbmUiLCJpZCI6ImExZmQxYWI4LTA5YzItNDlhNy05Y2YwLWRkNWEwNGM2NjZhMSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6InRscyJ9
    trojan://slch2024@192.200.160.87:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#06-0063-US
    trojan://slch2024@192.200.160.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#06-0064-US
    trojan://slch2024@185.148.104.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#06-0065-RELAY
    trojan://slch2024@199.34.230.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#06-0066-US
    trojan://slch2024@192.0.63.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#06-0067-US
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpYVU1UeWdFTTFqVllJdnlzWEtxQTVU@hackney-latest-strike.freesocks.work:443#08-0068-US
    trojan://slch2024@190.93.247.87:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0069-RELAY
    trojan://slch2024@190.93.244.87:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0070-RELAY
    trojan://slch2024@190.93.246.87:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0071-RELAY
    trojan://slch2024@199.68.156.87:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0072-US
    trojan://slch2024@216.24.57.87:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0073-US
    trojan://slch2024@194.76.18.87:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0074-KZ
    trojan://slch2024@192.0.54.87:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0075-US
    trojan://slch2024@199.34.229.87:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0076-US
    trojan://slch2024@216.24.57.195:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252FTelegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0077-US
    trojan://slch2024@190.93.245.87:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0078-RELAY
    trojan://slch2024@212.183.88.87:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0079-AT
    trojan://slch2024@198.62.62.87:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0080-US
    ss://YWVzLTI1Ni1jZmI6cXdlclJFV1ElMjU0MCUyNTQw@p141.panda001.net:4652#08-0081-KR
    trojan://slch2024@199.34.230.87:2096?allowInsecure=1&sni=ocost-dy.wmlefl.cc&ws=1&wspath=%2525252F#08-0156-US
    ss://YWVzLTI1Ni1nY206MGE5MTRlOWEtM2UzYi00NzBmLWEyNjctN2VhNzA4M2M0NWJi@77.110.110.240:443#23-0082-AT
    ss://YWVzLTI1Ni1nY206YTdmMDgyYzEtMGQxMi00NjA5LWI2YmYtZTc2MGI2NjhjZjIz@77.110.110.240:443#23-0083-AT
    ss://YWVzLTI1Ni1nY206MTAyYWQzZGEtMmQ1NS00OWQ2LWI4YzgtMmQ3ZTA0ZGYzM2Nh@77.110.110.240:443#23-0085-AT
    ss://YWVzLTI1Ni1nY206M2Y0MGJmM2QtMmYxZS00ZjQzLWJmNTQtZTVmZTc0MmEzYjRl@77.110.110.240:443#23-0086-AT
    ss://YWVzLTI1Ni1nY206ZDcwZWY4YjUtNjA0OC00YzBkLWJlNGQtZmM2MDM5OWIwZjQ1@77.110.110.240:443#23-0087-AT
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpqaWZ1UjJOVE0wWXQ@62.133.62.109:443#23-0088-FR
    vmess://eyJ2IjoiMiIsInBzIjoiMjMtMDA5MS1ERSIsImFkZCI6IjU3LjEyOS4yNC4xMjUiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjAzZmNjNjE4LWI5M2QtNjc5Ni02YWVkLThhMzhjOTc1ZDU4MSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvbGlua3Z3cz9lZD0yMDQ4QEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTiIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    ss://YWVzLTEyOC1nY206MTAwODY@160.16.123.124:10087#23-0093-JPtrojan%2F%2Fslch2024%40199.68.156.1952096%3FallowInsecure%3D1%26sni%3Docost-dy.wmlefl.cc%26ws%3D1%26wspath%3D%25252FTelegram%2525F0%25259F%252587%2525AE%2525F0%25259F%252587%2525B7ShadowProxy66%2305-0004-US
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpQdEh2NGJPNGpQdEJzSFdTbDFuNVFk@45.95.232.236:4248#23-0097-CH
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo5dHFoTWRJclRrZ1E0NlB2aHlBdE1I@92.112.126.90:443#23-0116-NL
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo5bGNDdnpOeHBOc25JTnlhWWZ6Yzhl@212.113.106.76:29149#23-0117-AT
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo5ZFZMYWNjR0JxRng@62.60.233.21:443#23-0118-TR
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpVS3Z5aXhLUmRUU3cyOFFwODdrZUVS@macintosh.outlinekeys.net:19609#23-0120-NL
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo0YTJyZml4b3BoZGpmZmE4S1ZBNEFh@45.87.175.171:8080#23-0131-LT
    


</details>

### 所有节点
合并节点总数: `86`
[节点链接](https://raw.githubusercontent.com/caijh/TopFreeProxies/master/sub/sub_merge_base64.txt)

### 节点来源
- [clashnode](https://github.com/imyaoxp/clashnode), 节点数量: `86`


## 仓库声明
订阅节点仅作学习交流使用，只是对网络上节点的优选排序，用于查找资料，学习知识，不做任何违法行为。所有资源均来自互联网，仅供大家交流学习使用，出现违法问题概不负责。

