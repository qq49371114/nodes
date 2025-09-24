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
高速节点数量: `63`
<details>
  <summary>展开复制节点</summary>

    trojan://a94fafdb-10d6-46c2-be8a-5c2e8358fbb0@172.67.187.28:443?allowInsecure=1&sni=dddDdDdDDFfFf.iran2035.dPdNS.ORG&ws=1&wspath=%2525252Fxa846InEcmjyiKVby2Lp#05-0001-RELAY
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@156.146.40.194:989#05-0003-SK
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@51.15.17.169:989#05-0004-NL
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDAwNS1SRUxBWSIsImFkZCI6ImRkZHZ2Ym4uOTMxLnBwLnVhIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI0MTc0Yjk1ZC0xMTVlLTRkMzktYWRkNi0xZjhkYjk1YmI4NjAiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLzZXZTNVOURmMVdHeGdGbm9GUHcxIiwiaG9zdCI6ImRkZHZ2Ym4uOTMxLnBwLnVhIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDAwNy1GUiIsImFkZCI6IjUxLjc1LjE2MS4xMDIiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjE4MDVjM2FlLWVkODQtNGU3ZS04Y2EyLWZlOWFjZDA4OTdiMCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvbGlua3Zrd3NzIiwiaG9zdCI6IiIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDAwOC1NWSIsImFkZCI6IjQ3LjI1MC4xNTkuMTM0IiwicG9ydCI6IjI4MjkzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImZmOWFkMDdjLWUxYjQtNDY3Zi05MGJjLTliMDY3ZjQ3ZGQ1YyIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvYXJraSIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    ss://Y2hhY2hhMjAtaWV0Zjphc2QxMjM0NTY@103.36.91.32:8388#05-0009-SG
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDEwNi1GUiIsImFkZCI6IjU3LjEyOC4xODkuMjQwIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiIwM2ZjYzYxOC1iOTNkLTY3OTYtNmFlZC04YTM4Yzk3NWQ1ODEiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2xpbmt2d3MiLCJob3N0IjoiIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDExMi1NWSIsImFkZCI6IjIxMS4yNS4yNDYuMTMxIiwicG9ydCI6IjM0NzgxIiwidHlwZSI6Im5vbmUiLCJpZCI6IjdkZDIwMDdiLTBjZDAtNGJhYy1hOGRmLTM0NDhiNTk1NDVmZCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvYXJraSIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDExOC1ISyIsImFkZCI6IjY5N2RjNTUxLXQxaTlzMC10bTUzY20tMW9sOTcuaGszLnA1cHYuY29tIiwicG9ydCI6IjgwIiwidHlwZSI6Im5vbmUiLCJpZCI6IjkzZmI2OWZjLTc3Y2YtMTFlZS04NWVlLWYyM2M5MTM2OWYyZCIsImFpZCI6IjIiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6IjY5N2RjNTUxLXQxaTlzMC10bTUzY20tMW9sOTcuaGszLnA1cHYuY29tIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDEyMS1TQyIsImFkZCI6IjE1NC4yMDEuODAuMjE0IiwicG9ydCI6IjExMTU5IiwidHlwZSI6Im5vbmUiLCJpZCI6ImQ5MjAyZmRkLTU2NzktNDNhNy1hOTMzLTBkMDc2MDViYWIzYyIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvYXJraSIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDEyMi1ISyIsImFkZCI6IjguMjE3LjE3MS4xOTMiLCJwb3J0IjoiMzYzMDAiLCJ0eXBlIjoibm9uZSIsImlkIjoiNjc4Y2RiMTQtMjJhNi00ZmIyLWEwNDAtYjM1M2VjYjk4OWNlIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9hcmtpIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDEyMy1ISyIsImFkZCI6IjguMjE3LjE3MS4xOTMiLCJwb3J0IjoiNTUwOTYiLCJ0eXBlIjoibm9uZSIsImlkIjoiMmI0ZDMxNTctZWQ3Zi00NmMyLWJjNGEtNWJiOGMxZjgxZTQwIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9hcmtpIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDEyNC1ISyIsImFkZCI6IjguMjE3LjIyMC4zMCIsInBvcnQiOiIzMTEyMyIsInR5cGUiOiJub25lIiwiaWQiOiIxMmY3MTY0Yi1lM2UxLTQyNjQtODZjYy02ODAyODkwMmNkMTkiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2Fya2kiLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDEyNS1ISyIsImFkZCI6IjguMjE3LjIyMC4zMCIsInBvcnQiOiIzOTY0OCIsInR5cGUiOiJub25lIiwiaWQiOiIyYzI1ODNiNi1lY2UwLTRkM2QtYTdmNS1jZjM3YzRhNmZhOGQiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2Fya2kiLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDEyNi1ISyIsImFkZCI6IjQ3LjIzOS44MS4xMTMiLCJwb3J0IjoiMjk3NjAiLCJ0eXBlIjoibm9uZSIsImlkIjoiZmQyOTg3Y2MtYjI1Zi00OTY2LTg0NmEtYjBkNjVkM2MxZTRiIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9hcmtpIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDEyNy1ISyIsImFkZCI6IjQ3Ljc2LjE1Ny4yMzQiLCJwb3J0IjoiMTQ0NzkiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTA2MDZjMTQtY2JhNC00M2ZmLTk1ODYtOWVkZDhiZWYyMWE0IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9hcmtpIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDEyOC1ISyIsImFkZCI6IjguMjE4LjguODQiLCJwb3J0IjoiMjMzMjYiLCJ0eXBlIjoibm9uZSIsImlkIjoiODcxZDA0ZGYtZmM1OC00NzBhLWJhY2EtZGFhZTI4ODY5MTY0IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9hcmtpIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoiMDYtMDA0NC1NWSIsImFkZCI6IjM4LjU0Ljk4LjExMCIsInBvcnQiOiIyMDUyIiwidHlwZSI6Im5vbmUiLCJpZCI6IjY2NWQ5YjhmLTE1M2QtNDkwNy1hZGFjLWRlMTJhZmQ5Yzg1MSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6InRscyJ9
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpwNzhuYUNmMkVmT2xSU0xUWDB3RlZ4@pupas-shirting-unsung.freesocks.work:443#08-0059-US
    vmess://eyJ2IjoiMiIsInBzIjoiMDgtMDA2MC1ISyIsImFkZCI6IjFlNDI2MDQ2LXQwZmRzMC10MTJjbmotMW9sOTcuaGsucDVwdi5jb20iLCJwb3J0IjoiODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTNmYjY5ZmMtNzdjZi0xMWVlLTg1ZWUtZjIzYzkxMzY5ZjJkIiwiYWlkIjoiMiIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiMWU0MjYwNDYtdDBmZHMwLXQxMmNuai0xb2w5Ny5oay5wNXB2LmNvbSIsInRscyI6IiJ9
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@154.90.62.168:989#08-0062-KR
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@154.90.63.177:989#08-0063-KR
    trojan://BAu7ZSyD3IZppnCOxCzaFXje3SECzZgX83e3x7yZA8SDCacyagKFlEO6O0AlTSwDDe4SF@louber.missionsec.us:443?allowInsecure=1#08-0147-AU
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@154.223.16.212:989#08-0148-CO
    vmess://eyJ2IjoiMiIsInBzIjoiMDgtMDE0OS1ISyIsImFkZCI6ImhrdC5nb3RvY2hpbmF0b3duLm5ldCIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiI5M2ZiNjlmYy03N2NmLTExZWUtODVlZS1mMjNjOTEzNjlmMmQiLCJhaWQiOiIyIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiJoa3QuZ290b2NoaW5hdG93bi5uZXQiLCJ0bHMiOiIifQ==
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@185.153.197.5:989#08-0150-MD
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@37.235.49.168:989#08-0151-IS
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@38.165.233.93:989#08-0152-PY
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@46.183.184.60:989#08-0153-HR
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpOazlhc2dsRHpIemprdFZ6VGt2aGFB@arxfw2b78fi2q9hzylhn.freesocks.work:443#08-0154-VN
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@185.213.23.226:989#08-0155-NO
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTowTmVONXRhN0ZMYTVCOURMeXRVMHVt@212.34.140.184:443#23-0064-NL
    trojan://f282b878-8711-45a1-8c69-5564172123c1@172.67.181.173:443?allowInsecure=1&sni=vpn.stupidworld.web.id&ws=1&wspath=%2525252F#23-0065-RELAY
    trojan://6e1b9a65-884f-3aa9-9469-bf6ec0f08610@210.203.60.189:443?allowInsecure=1&sni=45.32.28.232#23-0074-TW
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo0MjAwMGUwMi02YjRkLTQ2YWQtYTU3Mi04MGRiN2RiMmE5Y2U@fr09.giamping.com:8080#23-0076-DE
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpRY3N1a242cVNIbEtpVG5oMDhhOUNi@94.237.105.27:8443#23-0079-FI
    trojan://bpb-trojan@104.17.148.22:443?allowInsecure=1&sni=10-bpb-wORkER-paNel.pAGEs.DeV#23-0091-RELAY
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTowTmVONXRhN0ZMYTVCOURMeXRVMHVt@promo1o.bystrivpn.ru:443#23-0158-NL
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTplVWg0bFNwaTduT1lqMHZTcnFMVWgw@95.163.176.37:8506#23-0163-AT
    ss://YWVzLTEyOC1nY206c2hhZG93c29ja3M@149.34.244.68:443#23-0166-NL
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpRQ1hEeHVEbFRUTUQ3anRnSFVqSW9q@45.87.175.175:8080#23-0167-LT
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpjdklJODVUclc2bjBPR3lmcEhWUzF1@45.87.175.164:8080#23-0168-LT
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTozNjBlMjFkMjE5NzdkYzEx@104.167.197.25:57456#23-0169-UStrojan%2F%2Fo6x5BZAuSj%40creativecommons.org2053%3FallowInsecure%3D1%26sni%3Dmooshali.arshiacomplus.dpdns.org%26ws%3D1%26wspath%3D%25252Fhishhhh123%2305-0016-RELAY
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpvWklvQTY5UTh5aGNRVjhrYTNQYTNB@103.104.247.47:8080#23-0170-NL
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpvWklvQTY5UTh5aGNRVjhrYTNQYTNB@45.87.175.92:8080#23-0171-LT
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpvWklvQTY5UTh5aGNRVjhrYTNQYTNB@45.87.175.65:8080#23-0173-LT
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTozNjBlMjFkMjE5NzdkYzEx@45.139.24.24:57456#23-0174-RU
    trojan://telegram-id-directvpn@13.36.222.54:22223?allowInsecure=1&sni=trojan.burgerip.co.uk#23-0179-FR
    trojan://telegram-id-privatevpns@13.36.222.54:22222?allowInsecure=1&sni=trojan.burgerip.co.uk#23-0180-FR
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNToxUld3WGh3ZkFCNWdBRW96VTRHMlBn@45.87.175.178:8080#23-0182-LT
    trojan://telegram-id-privatevpns@15.236.175.74:22222?allowInsecure=1&sni=trojan.burgerip.co.uk#23-0187-FR
    trojan://telegram-id-directvpn@15.236.175.74:22223?allowInsecure=1&sni=trojan.burgerip.co.uk#23-0188-FR
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo0YTJyZml4b3BoZGpmZmE4S1ZBNEFh@151.242.251.144:8080#23-0189-AE
    trojan://telegram-id-directvpn@18.153.45.158:22223?allowInsecure=1&sni=trojan.burgerip.co.uk#23-0197-DE
    trojan://telegram-id-privatevpns@18.153.45.158:22222?allowInsecure=1&sni=trojan.burgerip.co.uk#23-0198-DE
    ss://YWVzLTEyOC1nY206c2hhZG93c29ja3M@212.102.53.194:443#23-0200-GB
    ss://YWVzLTEyOC1nY206c2hhZG93c29ja3M@212.102.53.80:443#23-0201-GB
    ss://YWVzLTEyOC1nY206c2hhZG93c29ja3M@212.102.53.198:443#23-0202-GB
    ss://YWVzLTEyOC1nY206c2hhZG93c29ja3M@212.102.53.81:443#23-0205-GB
    ss://YWVzLTEyOC1nY206c2hhZG93c29ja3M@156.146.62.163:443#23-0206-CH
    ss://YWVzLTEyOC1nY206c2hhZG93c29ja3M@149.34.244.82:443#23-0207-NL
    


</details>

### 所有节点
合并节点总数: `78`
[节点链接](https://raw.githubusercontent.com/caijh/TopFreeProxies/master/sub/sub_merge_base64.txt)

### 节点来源
- [clashnode](https://github.com/imyaoxp/clashnode), 节点数量: `78`


## 仓库声明
订阅节点仅作学习交流使用，只是对网络上节点的优选排序，用于查找资料，学习知识，不做任何违法行为。所有资源均来自互联网，仅供大家交流学习使用，出现违法问题概不负责。

