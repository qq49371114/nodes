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
高速节点数量: `48`
<details>
  <summary>展开复制节点</summary>

    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@156.146.40.194:989#05-0008-SK
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDAxNC1TRSIsImFkZCI6ImNvbmZpZ2ZyZWUtYm9sYmwua29yb3NoLnNob3AiLCJwb3J0IjoiMjA2MCIsInR5cGUiOiJub25lIiwiaWQiOiIwYjQyOThhMy01YWZmLTQyMDctOTFlNS1hMGRlYjNiMjBiOTQiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiY29uZmlnZnJlZS1ib2xibC5rb3Jvc2guc2hvcCIsInRscyI6IiJ9
    trojan://4174b95d-115e-4d39-add6-1f8db95bb860@172.67.153.179:443?allowInsecure=1&sni=qqqqqqqqqqa.www890604.dpdns.org&ws=1&wspath=%2525252FuzJNzgkkYWRWGxgFnoFPw1#05-0021-RELAY
    trojan://YwuvGJk36B@creativecommons.org:2053?allowInsecure=1&sni=kotlet.arshiacomplus.dpdns.org&ws=1&wspath=%2525252Fyamtekodasayahhh#05-0022-RELAY
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpjNDA2NDFjMWY4OWU3YWNi@tr.vpnsparta.pro:57456#05-0026-TR
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDEzNy1NWSIsImFkZCI6IjQ3LjI1MC4xNTkuMTM0IiwicG9ydCI6IjI4MjkzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImZmOWFkMDdjLWUxYjQtNDY3Zi05MGJjLTliMDY3ZjQ3ZGQ1YyIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvYXJraSIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@154.90.62.168:989#06-0051-KR
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpwNzhuYUNmMkVmT2xSU0xUWDB3RlZ4@pupas-shirting-unsung.freesocks.work:443#08-0080-US
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpOazlhc2dsRHpIemprdFZ6VGt2aGFB@arxfw2b78fi2q9hzylhn.freesocks.work:443#08-0082-VN
    vmess://eyJ2IjoiMiIsInBzIjoiMDgtMDA4My1NWSIsImFkZCI6IjM4LjU0Ljk4LjExMCIsInBvcnQiOiIyMDUyIiwidHlwZSI6Im5vbmUiLCJpZCI6IjY2NWQ5YjhmLTE1M2QtNDkwNy1hZGFjLWRlMTJhZmQ5Yzg1MSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6InRscyJ9
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@51.15.17.169:989#08-0084-NL
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@154.90.63.177:989#08-0151-KR
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@185.153.197.5:989#08-0152-MD
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@38.165.233.93:989#08-0153-PY
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo0YTJyZml4b3BoZGpmZmE4S1ZBNEFh@45.87.175.171:8080#23-0089-LT
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTowTmVONXRhN0ZMYTVCOURMeXRVMHVt@promo1o.bystrivpn.ru:443#23-0096-NL
    trojan://BAu7ZSyD3IZppnCOxCzaFXje3SECzZgX83e3x7yZA8SDCacyagKFlEO6O0AlTSwDDe4SF@louber.missionsec.us:443?allowInsecure=1&sni=louber.missionsec.us#23-0100-AU
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo0YTJyZml4b3BoZGpmZmE4S1ZBNEFh@45.87.175.192:8080#23-0101-LT
    trojan://NISHIKUITAN222@198.41.223.165:443?allowInsecure=1&sni=il.ylks.xyz&ws=1&wspath=%2525252F#23-0102-RELAY
    ss://YWVzLTI1Ni1nY206OWYzZDFhNmQzMTQ2ODU5OQ@195.58.49.100:1901#23-0106-RU
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpNZ0VVOHFTbHdmNTM@83.217.9.64:443#23-0108-TR
    vmess://eyJ2IjoiMiIsInBzIjoiMjMtMDEwOS1WTiIsImFkZCI6IjE2MC4xOS43OC4yMzciLCJwb3J0IjoiNDA2MDgiLCJ0eXBlIjoibm9uZSIsImlkIjoiMTY3ZGM1YTgtNmY3Mi00OWIzLWEwYzktZTQxZTQwM2JkNDAwIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9hcmtpP2VkPTIwNDgiLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMjMtMDExMC1GUiIsImFkZCI6IjE0Ni41OS41NS41MCIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiMDNmY2M2MTgtYjkzZC02Nzk2LTZhZWQtOGEzOGM5NzVkNTgxIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9saW5rdndzIiwiaG9zdCI6IiIsInRscyI6IiJ9
    trojan://ba320329-6546-441a-a348-039fc53dd88a@hkt.ksy8126.com:7003?allowInsecure=1&sni=us-la.ksy8126.com#23-0115-HK
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpmOGY3YUN6Y1BLYnNGOHAz@103.163.218.2:990#23-0117-VN
    trojan://6et7U7udLe@qige.zaide.tech:22846?allowInsecure=1&sni=qige.zaide.tech#23-0120-JP
    trojan://3r372@91.195.240.94:443?allowInsecure=1&sni=tj786.37927.online#23-0121-DE
    vmess://eyJ2IjoiMiIsInBzIjoiMjMtMDE1OS1ISyIsImFkZCI6IjQ3LjIzOS44MS4xMTMiLCJwb3J0IjoiMTcwMDIiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTc3OThhYzItODBkNC00ZTdmLTg0Y2MtODIyMTI0NGVkNzQxIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9hcmtpP2VkPTIwNDgiLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMjMtMDE2MS1ISyIsImFkZCI6IjguMjEwLjIzMC4xNzkiLCJwb3J0IjoiNDUzMjQiLCJ0eXBlIjoibm9uZSIsImlkIjoiODhhZTM0MTAtNWFmNi00YTc2LWJiMGYtOTQwZDZmZmY0ZjFhIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9hcmtpP2VkPTIwNDgiLCJob3N0IjoiIiwidGxzIjoiIn0=
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo0YTJyZml4b3BoZGpmZmE4S1ZBNEFh@vip.nl-16-07.galaxymc-ssh.ir:8080#23-0164-LT
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTowTmVONXRhN0ZMYTVCOURMeXRVMHVt@212.34.140.184:443#23-0167-NL
    vmess://eyJ2IjoiMiIsInBzIjoiMjMtMDE3OC1ISyIsImFkZCI6IjQ3LjI0Mi4yMTQuMTc4IiwicG9ydCI6IjUyOTgzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjcyYTEzZTBiLTVlNTUtNGQ2Zi05NDA0LWRiMmYwYTQ4MmY5NyIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvYXJraT9lZD0yMDQ4IiwiaG9zdCI6IiIsInRscyI6IiJ9
    trojan://96983eb4-c8f1-316e-ab00-500014ed3d8b@official.taipeicitygovernment.co.ua:8443?allowInsecure=1&sni=207.148.100.75#23-0181-TW
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo0MjAwMGUwMi02YjRkLTQ2YWQtYTU3Mi04MGRiN2RiMmE5Y2U@us33.giamping.com:8080#23-0190-USss%2F%2FYWVzLTI1Ni1jZmI6YW1hem9uc2tyMDU%4018.185.56.207443%2323-0160-DE
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@154.223.16.212:989#23-0193-CO
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp1SWE4MUNmVmQ0UVhEeFJtZEc3dU5x@62.210.88.22:443#23-0206-FR
    ss://YWVzLTEyOC1nY206c2hhZG93c29ja3M@149.34.244.82:443#23-0207-NL
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpvWklvQTY5UTh5aGNRVjhrYTNQYTNB@45.87.175.35:8080#23-0208-LT
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpvWklvQTY5UTh5aGNRVjhrYTNQYTNB@45.87.175.22:8080#23-0209-LT
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTplVWg0bFNwaTduT1lqMHZTcnFMVWgw@95.163.176.37:8506#23-0212-AT
    ss://YWVzLTEyOC1nY206c2hhZG93c29ja3M@149.34.244.68:443#23-0214-NL
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpvWklvQTY5UTh5aGNRVjhrYTNQYTNB@45.87.175.65:8080#23-0215-LT
    ss://YWVzLTEyOC1nY206c2hhZG93c29ja3M@212.102.53.194:443#23-0219-GB
    ss://YWVzLTEyOC1nY206c2hhZG93c29ja3M@212.102.53.80:443#23-0220-GB
    ss://YWVzLTEyOC1nY206c2hhZG93c29ja3M@212.102.53.198:443#23-0221-GB
    ss://YWVzLTEyOC1nY206c2hhZG93c29ja3M@212.102.53.81:443#23-0223-GB
    ss://YWVzLTEyOC1nY206c2hhZG93c29ja3M@156.146.62.163:443#23-0224-CH
    


</details>

### 所有节点
合并节点总数: `446`
[节点链接](https://raw.githubusercontent.com/caijh/TopFreeProxies/master/sub/sub_merge_base64.txt)

### 节点来源
- [clashnode](https://github.com/imyaoxp/clashnode), 节点数量: `446`


## 仓库声明
订阅节点仅作学习交流使用，只是对网络上节点的优选排序，用于查找资料，学习知识，不做任何违法行为。所有资源均来自互联网，仅供大家交流学习使用，出现违法问题概不负责。

