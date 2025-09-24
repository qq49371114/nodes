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
高速节点数量: `46`
<details>
  <summary>展开复制节点</summary>

    ss://YWVzLTI1Ni1jZmI6YW1hem9uc2tyMDU@18.185.56.207:443#05-0004-DE
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDAwNS1HQiIsImFkZCI6IjUxLjc1LjE2MC4yMzciLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjNhZGJhNDYyLTMxOGYtNGE2Yy1hZDdhLTI5MjNiYzc0ZjIwNyIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvbGlua3Zrd3NzIiwiaG9zdCI6IiIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDAxNS1ISyIsImFkZCI6ImFmbHp6dWwubWVpcXVhbmtvbmdqaWFuLmNvbSIsInBvcnQiOiI1MjUxMiIsInR5cGUiOiJub25lIiwiaWQiOiIzNDJiYWNmZC0yYjhmLTNmNDktYTE2ZS00MzlkYjViMGI5ZDUiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLzU2NGRmYTIwLyIsImhvc3QiOiJhZmx6enVsLm1laXF1YW5rb25namlhbi5jb20iLCJ0bHMiOiIifQ==
    trojan://02XtoczO7V@creativecommons.org:443?allowInsecure=1&sni=mooshali.arshiacomplus.dpdns.org&ws=1&wspath=%2525252Fhishhhh123#05-0021-RELAY
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDEyNi1NWSIsImFkZCI6IjQ3LjI1MC4xNTkuMTM0IiwicG9ydCI6IjI4MjkzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImZmOWFkMDdjLWUxYjQtNDY3Zi05MGJjLTliMDY3ZjQ3ZGQ1YyIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvYXJraSIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDEzOC1TQyIsImFkZCI6IjE1NC4yMDEuODAuMjE0IiwicG9ydCI6IjExMTU5IiwidHlwZSI6Im5vbmUiLCJpZCI6ImQ5MjAyZmRkLTU2NzktNDNhNy1hOTMzLTBkMDc2MDViYWIzYyIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvYXJraSIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@154.90.62.168:989#06-0047-KR
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpOazlhc2dsRHpIemprdFZ6VGt2aGFB@arxfw2b78fi2q9hzylhn.freesocks.work:443#08-0077-VN
    vmess://eyJ2IjoiMiIsInBzIjoiMDgtMDA3OC1NWSIsImFkZCI6IjM4LjU0Ljk4LjExMCIsInBvcnQiOiIyMDUyIiwidHlwZSI6Im5vbmUiLCJpZCI6IjY2NWQ5YjhmLTE1M2QtNDkwNy1hZGFjLWRlMTJhZmQ5Yzg1MSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6InRscyJ9
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@51.15.17.169:989#08-0079-NL
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@154.223.16.212:989#08-0148-CO
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@154.90.63.177:989#08-0149-KR
    vmess://eyJ2IjoiMiIsInBzIjoiMDgtMDE1MS1ISyIsImFkZCI6ImhrdC5nb3RvY2hpbmF0b3duLm5ldCIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiI5M2ZiNjlmYy03N2NmLTExZWUtODVlZS1mMjNjOTEzNjlmMmQiLCJhaWQiOiIyIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiJoa3QuZ290b2NoaW5hdG93bi5uZXQiLCJ0bHMiOiIifQ==
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@185.153.197.5:989#08-0152-MD
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@38.165.233.93:989#08-0153-PY
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo0YTJyZml4b3BoZGpmZmE4S1ZBNEFh@151.242.251.144:8080#23-0084-AE
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpvWklvQTY5UTh5aGNRVjhrYTNQYTNB@103.104.247.47:8080#23-0098-NL
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpjdklJODVUclc2bjBPR3lmcEhWUzF1@45.87.175.185:8080#23-0105-LT
    trojan://NISHIKUITAN222@104.27.16.148:443?allowInsecure=1#23-0113-RELAY
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTowTmVONXRhN0ZMYTVCOURMeXRVMHVt@212.34.140.184:443#23-0118-NL
    trojan://telegram-id-directvpn@35.181.121.146:22223?allowInsecure=1&sni=trojan.burgerip.co.uk#23-0120-FR
    trojan://telegram-id-privatevpns@35.181.121.146:22222?allowInsecure=1&sni=trojan.burgerip.co.uk#23-0121-FR
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp1SWE4MUNmVmQ0UVhEeFJtZEc3dU5x@62.210.88.22:443#23-0154-FR
    ss://YWVzLTEyOC1nY206c2hhZG93c29ja3M@149.34.244.82:443#23-0158-NL
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNToxUld3WGh3ZkFCNWdBRW96VTRHMlBn@45.87.175.188:8080#23-0159-LT
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNToxUld3WGh3ZkFCNWdBRW96VTRHMlBn@45.87.175.178:8080#23-0160-LT
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpvWklvQTY5UTh5aGNRVjhrYTNQYTNB@103.104.247.49:8080#23-0161-NL
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpvWklvQTY5UTh5aGNRVjhrYTNQYTNB@45.87.175.35:8080#23-0162-LT
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpvWklvQTY5UTh5aGNRVjhrYTNQYTNB@45.87.175.22:8080#23-0166-LT
    trojan://96983eb4-c8f1-316e-ab00-500014ed3d8b@official.taipeicitygovernment.co.ua:8443?allowInsecure=1&sni=207.148.100.75#23-0171-TW
    trojan://6e1b9a65-884f-3aa9-9469-bf6ec0f08610@210.203.60.189:443?allowInsecure=1&sni=45.32.28.232#23-0174-TW
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTplVWg0bFNwaTduT1lqMHZTcnFMVWgw@95.163.176.37:8506#23-0180-AT
    ss://YWVzLTEyOC1nY206c2hhZG93c29ja3M@149.34.244.68:443#23-0183-NL
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpRQ1hEeHVEbFRUTUQ3anRnSFVqSW9q@45.87.175.175:8080#23-0184-LT
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpjdklJODVUclc2bjBPR3lmcEhWUzF1@45.87.175.164:8080#23-0185-LT
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpvWklvQTY5UTh5aGNRVjhrYTNQYTNB@45.87.175.65:8080#23-0187-LT
    trojan://telegram-id-directvpn@13.36.222.54:22223?allowInsecure=1&sni=trojan.burgerip.co.uk#23-0190-FR
    trojan://telegram-id-privatevpns@13.36.222.54:22222?allowInsecure=1&sni=trojan.burgerip.co.uk#23-0191-FR
    vmess://eyJ2IjoiMiIsInBzIjoiMjMtMDE5Mi1ISyIsImFkZCI6IjQ3LjIzOS4xMjguMTk0IiwicG9ydCI6IjU4MDU2IiwidHlwZSI6Im5vbmUiLCJpZCI6IjBkNWE1MDkxLWM5MjMtNGZiNi05ZGZkLTk1ZWNmZDYwY2RlZSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvYXJraT9lZD0yMDQ4IiwiaG9zdCI6IiIsInRscyI6IiJ9
    trojan://telegram-id-directvpn@15.236.175.74:22223?allowInsecure=1&sni=trojan.burgerip.co.uk#23-0194-FR
    ss://YWVzLTEyOC1nY206c2hhZG93c29ja3M@212.102.53.194:443#23-0201-GB
    ss://YWVzLTEyOC1nY206c2hhZG93c29ja3M@212.102.53.80:443#23-0202-GB
    ss://YWVzLTEyOC1nY206c2hhZG93c29ja3M@212.102.53.198:443#23-0203-GB
    ss://YWVzLTEyOC1nY206c2hhZG93c29ja3M@212.102.53.81:443#23-0205-GB
    ss://YWVzLTEyOC1nY206c2hhZG93c29ja3M@156.146.62.163:443#23-0206-CH
    


</details>

### 所有节点
合并节点总数: `52`
[节点链接](https://raw.githubusercontent.com/caijh/TopFreeProxies/master/sub/sub_merge_base64.txt)

### 节点来源
- [clashnode](https://github.com/imyaoxp/clashnode), 节点数量: `52`


## 仓库声明
订阅节点仅作学习交流使用，只是对网络上节点的优选排序，用于查找资料，学习知识，不做任何违法行为。所有资源均来自互联网，仅供大家交流学习使用，出现违法问题概不负责。

