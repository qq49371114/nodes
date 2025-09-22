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
高速节点数量: `55`
<details>
  <summary>展开复制节点</summary>

    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@156.146.40.194:989#05-0000-SK
    trojan://wb6368@92.243.75.49:2087?allowInsecure=1&sni=hsdgbuys.pages.dev&ws=1&wspath=%2525252F#05-0008-RELAY
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDAwOS1SRUxBWSIsImFkZCI6ImRkZHZ2Ym4uOTMxLnBwLnVhIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI0MTc0Yjk1ZC0xMTVlLTRkMzktYWRkNi0xZjhkYjk1YmI4NjAiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLzZXZTNVOURmMVdHeGdGbm9GUHcxIiwiaG9zdCI6ImRkZHZ2Ym4uOTMxLnBwLnVhIiwidGxzIjoidGxzIn0=
    trojan://o6x5BZAuSj@creativecommons.org:2053?allowInsecure=1&sni=mooshali.arshiacomplus.dpdns.org&ws=1&wspath=%2525252Fhishhhh123#05-0018-RELAY
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@51.15.17.169:989#05-0117-NL
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpRQ1hEeHVEbFRUTUQ3anRnSFVqSW9q@45.158.171.146:8080#05-0130-FR
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNToxUld3WGh3ZkFCNWdBRW96VTRHMlBn@45.158.171.146:8080#05-0133-FR
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo0YTJyZml4b3BoZGpmZmE4S1ZBNEFh@45.158.171.146:8080#05-0134-FR
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo5MTc3ZGUxYS1hZWZmLTQzZjEtOTNhNi03ZGQwOGEyZmRjNDE@frk.fastsoonlink.com:40011#06-0025-AU
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo5MTc3ZGUxYS1hZWZmLTQzZjEtOTNhNi03ZGQwOGEyZmRjNDE@sgp.fastsoonlink.com:40005#06-0026-SG
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo5MTc3ZGUxYS1hZWZmLTQzZjEtOTNhNi03ZGQwOGEyZmRjNDE@pr.fastsoonlink.com:40030#06-0027-PL
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo5MTc3ZGUxYS1hZWZmLTQzZjEtOTNhNi03ZGQwOGEyZmRjNDE@ru.fastsoonlink.com:40031#06-0028-RU
    trojan://02XtoczO7V@5.255.102.41:17590?allowInsecure=1&sni=mooshali.arshiacomplus.dpdns.org&ws=1&wspath=%2525252Fhishhhh123#06-0031-NL
    trojan://2ee85121-31de-4581-a492-eb00f606e392@45.91.171.116:443?allowInsecure=1&sni=sto.freeguard.org#06-0033-SE
    trojan://0C3YaEDx46ODTFTcaF8lXlZ3zeqSlF33wZagexzRjIyODa8RDwp8XSCO93ygCSYcSYABA@blength.appagent.net:18332?allowInsecure=1#06-0035-US
    trojan://B3AO9XlcTxaIATp08S29pS6luwZ8C4qDFzaCFYEDDSA5YDeKZAy3e2ZXRe73zIpxwByN7@kasheet.appagent.net:18333?allowInsecure=1#06-0036-US
    trojan://RzFSy3laClaxnYCcO3jBEpYgDyZx2CO78IC3X46ATFD73RSSZZTx8yCOKYDOqeD8pSeRa@sirens.isquirrel.net:28334?allowInsecure=1#06-0037-US
    trojan://nzSaSa3SFaCNFDCjOCg8A39e53p8l2xaTFCOu7qZx2Z8px4CK3DXeZYAwRRS3zY66laOE@seginus.appagent.net:28331?allowInsecure=1#06-0038-US
    trojan://D0AASSpCKFjOBSwlwqylnOep8BDlgN3e3RY9S3Op2RaZZ58gID8yY3ej56CSuYacZz3EA@delight.appagent.net:443?allowInsecure=1#06-0039-US
    trojan://4xS33pu88RaTF37ZxRjzAZc9zxe8OaYBX9CSO3p5SSxquFOFEySnDlCleCFA2DN3gaeDl@mintaka.appagent.net:443?allowInsecure=1#06-0041-US
    trojan://Z3aK0aZqwyNcz7S3l3ncNCODYxNFnA8SCOOSOZ3y3AX8xA4a0RZ3gxn39aqYAaBOyzR43acKOCzSX3S@hanger.appagent.net:28331?allowInsecure=1#06-0042-US
    trojan://Npgx9nO3OBaZF5yxARYl93lFX08TlR3waDla733az8SqXe3YS3zjESECSZpAw428a6SID@metallic.isquirrel.net:443?allowInsecure=1#08-0046-US
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@185.213.23.226:989#08-0047-NO
    trojan://F9OKESxKjSDExSeaOw7XyINxDzaOZqeKxCeIczYYED8ewZ2Yl9AppAySO3XwFNy3lCaXDDCFnlACSB0@pricey.appagent.net:28334?allowInsecure=1#08-0050-US
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpwNzhuYUNmMkVmT2xSU0xUWDB3RlZ4@pupas-shirting-unsung.freesocks.work:443#08-0051-US
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTplNDQ2OTMxMC0wMGZjLTQ1MjctOGFmYS03MTc4OGIzYmNlZjc@gw.liangyuandianwan.com:35602#08-0053-CN
    vmess://eyJ2IjoiMiIsInBzIjoiMDgtMDA1NC1ISyIsImFkZCI6ImMwMDRlNmZlLXQxaTlzMC10bTUzY20tMW9sOTcuaGt0LnRjcGJici5uZXQiLCJwb3J0IjoiODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTNmYjY5ZmMtNzdjZi0xMWVlLTg1ZWUtZjIzYzkxMzY5ZjJkIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiYzAwNGU2ZmUtdDFpOXMwLXRtNTNjbS0xb2w5Ny5oa3QudGNwYmJyLm5ldCIsInRscyI6IiJ9
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@154.90.62.168:989#08-0057-KR
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@154.223.16.212:989#08-0058-CO
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpOazlhc2dsRHpIemprdFZ6VGt2aGFB@arxfw2b78fi2q9hzylhn.freesocks.work:443#08-0143-VN
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo5dHFoTWRJclRrZ1E0NlB2aHlBdE1I@switcher-nick-croquet.freesocks.work:443#08-0144-NL
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@192.71.166.100:989#08-0145-GR
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@51.15.23.63:989#08-0146-NL
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@154.90.63.177:989#08-0147-KR
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@185.153.197.5:989#08-0148-MD
    vmess://eyJ2IjoiMiIsInBzIjoiMDgtMDE0OS1ISyIsImFkZCI6IjY5N2RjNTUxLXQxaTlzMC10bTUzY20tMW9sOTcuaGszLnA1cHYuY29tIiwicG9ydCI6IjgwIiwidHlwZSI6Im5vbmUiLCJpZCI6IjkzZmI2OWZjLTc3Y2YtMTFlZS04NWVlLWYyM2M5MTM2OWYyZCIsImFpZCI6IjIiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6IjY5N2RjNTUxLXQxaTlzMC10bTUzY20tMW9sOTcuaGszLnA1cHYuY29tIiwidGxzIjoiIn0=
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@38.165.233.93:989#08-0150-PY
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@46.183.184.60:989#08-0151-HR
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@37.235.49.168:989#08-0152-IS
    ss://YWVzLTI1Ni1nY206MGE5MTRlOWEtM2UzYi00NzBmLWEyNjctN2VhNzA4M2M0NWJi@77.110.110.240:443#23-0059-AT
    ss://YWVzLTI1Ni1nY206YTdmMDgyYzEtMGQxMi00NjA5LWI2YmYtZTc2MGI2NjhjZjIz@77.110.110.240:443#23-0060-AT
    ss://YWVzLTI1Ni1nY206MTAyYWQzZGEtMmQ1NS00OWQ2LWI4YzgtMmQ3ZTA0ZGYzM2Nh@77.110.110.240:443#23-0062-AT
    ss://YWVzLTI1Ni1nY206M2Y0MGJmM2QtMmYxZS00ZjQzLWJmNTQtZTVmZTc0MmEzYjRl@77.110.110.240:443#23-0063-AT
    ss://YWVzLTI1Ni1nY206ZDcwZWY4YjUtNjA0OC00YzBkLWJlNGQtZmM2MDM5OWIwZjQ1@77.110.110.240:443#23-0064-AT
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpqaWZ1UjJOVE0wWXQ@62.133.62.109:443#23-0065-FR
    vmess://eyJ2IjoiMiIsInBzIjoiMjMtMDA2OC1ERSIsImFkZCI6IjU3LjEyOS4yNC4xMjUiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjAzZmNjNjE4LWI5M2QtNjc5Ni02YWVkLThhMzhjOTc1ZDU4MSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvbGlua3Z3cz9lZD0yMDQ4QEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTiIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    ss://YWVzLTEyOC1nY206MTAwODY@160.16.123.124:10087#23-0070-JP
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpQdEh2NGJPNGpQdEJzSFdTbDFuNVFk@45.95.232.236:4248#23-0074-CH
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@104.192.226.106:989#23-0076-US
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo5dHFoTWRJclRrZ1E0NlB2aHlBdE1I@92.112.126.90:443#23-0093-NL
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo5bGNDdnpOeHBOc25JTnlhWWZ6Yzhl@212.113.106.76:29149#23-0094-AT
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo5ZFZMYWNjR0JxRng@62.60.233.21:443#23-0095-TR
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpVS3Z5aXhLUmRUU3cyOFFwODdrZUVS@macintosh.outlinekeys.net:19609#23-0097-NL
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo0YTJyZml4b3BoZGpmZmE4S1ZBNEFh@45.87.175.171:8080#23-0108-LT
    


</details>

### 所有节点
合并节点总数: `49`
[节点链接](https://raw.githubusercontent.com/caijh/TopFreeProxies/master/sub/sub_merge_base64.txt)

### 节点来源
- [clashnode](https://github.com/imyaoxp/clashnode), 节点数量: `49`


## 仓库声明
订阅节点仅作学习交流使用，只是对网络上节点的优选排序，用于查找资料，学习知识，不做任何违法行为。所有资源均来自互联网，仅供大家交流学习使用，出现违法问题概不负责。

