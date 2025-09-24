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
高速节点数量: `45`
<details>
  <summary>展开复制节点</summary>

    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@51.15.17.169:989#05-0001-NL
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDAwNi1SRUxBWSIsImFkZCI6ImRkZHZ2Ym4uOTMxLnBwLnVhIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI0MTc0Yjk1ZC0xMTVlLTRkMzktYWRkNi0xZjhkYjk1YmI4NjAiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLzZXZTNVOURmMVdHeGdGbm9GUHcxIiwiaG9zdCI6ImRkZHZ2Ym4uOTMxLnBwLnVhIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDAwNy1ERSIsImFkZCI6IjU3LjEyOS4yOC4yMTMiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjAzZmNjNjE4LWI5M2QtNjc5Ni02YWVkLThhMzhjOTc1ZDU4MSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvbGlua3Z3cyIsImhvc3QiOiIiLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDAxMy1DTiIsImFkZCI6InY1LmhlZHVpYW4ubGluayIsInBvcnQiOiIzMDgwNSIsInR5cGUiOiJub25lIiwiaWQiOiJjYmIzZjg3Ny1kMWZiLTM0NGMtODdhOS1kMTUzYmZmZDU0ODQiLCJhaWQiOiIyIiwibmV0Ijoid3MiLCJwYXRoIjoiL29vb28iLCJob3N0IjoidjUuaGVkdWlhbi5saW5rIiwidGxzIjoiIn0=
    trojan://o6x5BZAuSj@creativecommons.org:2053?allowInsecure=1&sni=mooshali.arshiacomplus.dpdns.org&ws=1&wspath=%2525252Fhishhhh123#05-0018-RELAY
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDAyMC1HQiIsImFkZCI6IjUxLjc1LjE2MC4yMzciLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjNhZGJhNDYyLTMxOGYtNGE2Yy1hZDdhLTI5MjNiYzc0ZjIwNyIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvbGlua3Zrd3NzIiwiaG9zdCI6IiIsInRscyI6InRscyJ9
    trojan://a94fafdb-10d6-46c2-be8a-5c2e8358fbb0@172.67.187.28:443?allowInsecure=1&sni=dddDdDdDDFfFf.iran2035.dPdNS.ORG&ws=1&wspath=%2525252Fxa846InEcmjyiKVby2Lp#05-0022-RELAY
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDEzOS1NWSIsImFkZCI6IjQ3LjI1MC4xNTkuMTM0IiwicG9ydCI6IjI4MjkzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImZmOWFkMDdjLWUxYjQtNDY3Zi05MGJjLTliMDY3ZjQ3ZGQ1YyIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvYXJraSIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDE0NC1TQyIsImFkZCI6IjE1NC4yMDEuODAuMjE0IiwicG9ydCI6IjExMTU5IiwidHlwZSI6Im5vbmUiLCJpZCI6ImQ5MjAyZmRkLTU2NzktNDNhNy1hOTMzLTBkMDc2MDViYWIzYyIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvYXJraSIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@154.90.62.168:989#06-0046-KR
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpOazlhc2dsRHpIemprdFZ6VGt2aGFB@arxfw2b78fi2q9hzylhn.freesocks.work:443#08-0077-VN
    vmess://eyJ2IjoiMiIsInBzIjoiMDgtMDA3OC1NWSIsImFkZCI6IjM4LjU0Ljk4LjExMCIsInBvcnQiOiIyMDUyIiwidHlwZSI6Im5vbmUiLCJpZCI6IjY2NWQ5YjhmLTE1M2QtNDkwNy1hZGFjLWRlMTJhZmQ5Yzg1MSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6InRscyJ9
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@154.90.63.177:989#08-0154-KRss%2F%2FY2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpwNzhuYUNmMkVmT2xSU0xUWDB3RlZ4%40pupas-shirting-unsung.freesocks.work443%2308-0075-US
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@185.153.197.5:989#08-0155-MD
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@38.165.233.93:989#08-0156-PY
    vmess://eyJ2IjoiMiIsInBzIjoiMjMtMDA4Ny1SRUxBWSIsImFkZCI6ImNzZ28uY29tIiwicG9ydCI6IjIwNTMiLCJ0eXBlIjoibm9uZSIsImlkIjoiOGIwYTU5MmYtMWZlZS00ZGEwLWFkZDYtZjhlMTA4NjExMTY0IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9wcm9maWxlL3RlbGVncmFtQHNzcnN1YiIsImhvc3QiOiJjc2dvLmNvbSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoiMjMtMDA4OC1SRUxBWSIsImFkZCI6ImZhc3RjdXAubmV0IiwicG9ydCI6IjIwNTMiLCJ0eXBlIjoibm9uZSIsImlkIjoiOGIwYTU5MmYtMWZlZS00ZGEwLWFkZDYtZjhlMTA4NjExMTY0IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9wcm9maWxlL3RlbGVncmFtQHNzcnN1YiIsImhvc3QiOiJmYXN0Y3VwLm5ldCIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoiMjMtMDA4OS1SRUxBWSIsImFkZCI6InB1YmcuYWMiLCJwb3J0IjoiMjA1MyIsInR5cGUiOiJub25lIiwiaWQiOiI4YjBhNTkyZi0xZmVlLTRkYTAtYWRkNi1mOGUxMDg2MTExNjQiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL3Byb2ZpbGUvdGVsZWdyYW1Ac3Nyc3ViIiwiaG9zdCI6InB1YmcuYWMiLCJ0bHMiOiIifQ==
    trojan://8b0a592f-1fee-4da0-add6-f8e108611164@104.18.20.69:8443?allowInsecure=1&sni=cdn-node-oss-92.paofu.de&ws=1&wspath=%2525252Fprofile%2525252Ftelegram%25252540ssrsub#23-0090-RELAY
    trojan://8b0a592f-1fee-4da0-add6-f8e108611164@pubg.ac:8443?allowInsecure=1&sni=cdn-node-oss-92.paofu.de&ws=1&wspath=%2525252Fprofile%2525252Ftelegram%25252540ssrsub#23-0091-RELAY
    trojan://auto@172.64.35.83:443?allowInsecure=1&sni=trojanmz.pages.dev&ws=1&wspath=%2525252Ftrojanmz.pages.dev%2525252F%2525253Fed%2525253D2560#23-0115-RELAY
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo0MjAwMGUwMi02YjRkLTQ2YWQtYTU3Mi04MGRiN2RiMmE5Y2U@us33.giamping.com:8080#23-0159-UStrojan%2F%2Fauto%40104.21.64.10443%3FallowInsecure%3D1%26sni%3Dtrojanmz.pages.dev%26ws%3D1%26wspath%3D%25252Ftrojanmz.pages.dev%25252F%25253Fed%25253D2560%2323-0112-RELAY
    trojan://96983eb4-c8f1-316e-ab00-500014ed3d8b@official.taipeicitygovernment.co.ua:8443?allowInsecure=1&sni=207.148.100.75#23-0165-TW
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@154.223.16.212:989#23-0168-CO
    trojan://telegram-id-directvpn@3.127.9.61:22223?allowInsecure=1&sni=trojan.burgerip.co.uk#23-0172-DE
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTowTmVONXRhN0ZMYTVCOURMeXRVMHVt@212.34.140.184:443#23-0179-NL
    vmess://eyJ2IjoiMiIsInBzIjoiMjMtMDE5Ny1ISyIsImFkZCI6IjQ3LjIzOS4xMjguMTk0IiwicG9ydCI6IjU1MTA2IiwidHlwZSI6Im5vbmUiLCJpZCI6IjViOWE1ZDFlLTg4NmUtNGEzMy1iNmUxLTg3ODkwNzYyNjQ0OCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvYXJraT9lZD0yMDQ4IiwiaG9zdCI6IiIsInRscyI6IiJ9
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpvWklvQTY5UTh5aGNRVjhrYTNQYTNB@103.104.247.47:8080#23-0203-NL
    trojan://telegram-id-directvpn@35.181.121.146:22223?allowInsecure=1&sni=trojan.burgerip.co.uk#23-0204-FR
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp1SWE4MUNmVmQ0UVhEeFJtZEc3dU5x@62.210.88.22:443#23-0206-FR
    ss://YWVzLTEyOC1nY206c2hhZG93c29ja3M@149.34.244.82:443#23-0208-NL
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpvWklvQTY5UTh5aGNRVjhrYTNQYTNB@103.104.247.49:8080#23-0209-NL
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpvWklvQTY5UTh5aGNRVjhrYTNQYTNB@45.87.175.35:8080#23-0210-LT
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpvWklvQTY5UTh5aGNRVjhrYTNQYTNB@45.87.175.22:8080#23-0211-LT
    trojan://6e1b9a65-884f-3aa9-9469-bf6ec0f08610@210.203.60.189:443?allowInsecure=1&sni=45.32.28.232#23-0213-TW
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTplVWg0bFNwaTduT1lqMHZTcnFMVWgw@95.163.176.37:8506#23-0216-AT
    ss://YWVzLTEyOC1nY206c2hhZG93c29ja3M@149.34.244.68:443#23-0219-NL
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpRQ1hEeHVEbFRUTUQ3anRnSFVqSW9q@45.87.175.175:8080#23-0220-LT
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpvWklvQTY5UTh5aGNRVjhrYTNQYTNB@45.87.175.65:8080#23-0221-LT
    ss://YWVzLTEyOC1nY206c2hhZG93c29ja3M@212.102.53.194:443#23-0226-GB
    ss://YWVzLTEyOC1nY206c2hhZG93c29ja3M@212.102.53.80:443#23-0227-GB
    ss://YWVzLTEyOC1nY206c2hhZG93c29ja3M@212.102.53.198:443#23-0228-GB
    ss://YWVzLTEyOC1nY206c2hhZG93c29ja3M@212.102.53.81:443#23-0230-GB
    ss://YWVzLTEyOC1nY206c2hhZG93c29ja3M@156.146.62.163:443#23-0231-CH
    


</details>

### 所有节点
合并节点总数: `136`
[节点链接](https://raw.githubusercontent.com/caijh/TopFreeProxies/master/sub/sub_merge_base64.txt)

### 节点来源
- [clashnode](https://github.com/imyaoxp/clashnode), 节点数量: `136`


## 仓库声明
订阅节点仅作学习交流使用，只是对网络上节点的优选排序，用于查找资料，学习知识，不做任何违法行为。所有资源均来自互联网，仅供大家交流学习使用，出现违法问题概不负责。

