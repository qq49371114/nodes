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
高速节点数量: `47`
<details>
  <summary>展开复制节点</summary>

    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@156.146.40.194:989#05-0002-SK
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@185.213.23.226:989#05-0004-NO
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpRQ1hEeHVEbFRUTUQ3anRnSFVqSW9q@45.158.171.146:8080#05-0005-FR
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDAwNy1DTiIsImFkZCI6InY1LmhlZHVpYW4ubGluayIsInBvcnQiOiIzMDgwNSIsInR5cGUiOiJub25lIiwiaWQiOiJjYmIzZjg3Ny1kMWZiLTM0NGMtODdhOS1kMTUzYmZmZDU0ODQiLCJhaWQiOiIyIiwibmV0Ijoid3MiLCJwYXRoIjoiL29vb28iLCJob3N0IjoidjUuaGVkdWlhbi5saW5rIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDAxMy1DTiIsImFkZCI6IjE3Lm1hbWFtYWpkLnNpdGUiLCJwb3J0IjoiMjM2MTciLCJ0eXBlIjoibm9uZSIsImlkIjoiMzZjMjlmMmYtMThmMi0zMzk5LTg4NWUtZjQ2MzhlMmM3OTA4IiwiYWlkIjoiMiIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiMTcubWFtYW1hamQuc2l0ZSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDAxNC1DTiIsImFkZCI6IjEzLm1hbWFtYWpkLnNpdGUiLCJwb3J0IjoiMjM2MTMiLCJ0eXBlIjoibm9uZSIsImlkIjoiMzZjMjlmMmYtMThmMi0zMzk5LTg4NWUtZjQ2MzhlMmM3OTA4IiwiYWlkIjoiMiIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiMTMubWFtYW1hamQuc2l0ZSIsInRscyI6IiJ9
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNToxUld3WGh3ZkFCNWdBRW96VTRHMlBn@45.158.171.146:8080#05-0017-FR
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo0YTJyZml4b3BoZGpmZmE4S1ZBNEFh@45.158.171.146:8080#05-0018-FR
    trojan://a94fafdb-10d6-46c2-be8a-5c2e8358fbb0@172.67.187.28:443?allowInsecure=1&sni=dddDdDdDDFfFf.iran2035.dPdNS.ORG&ws=1&wspath=%2525252Fxa846InEcmjyiKVby2Lp#05-0020-RELAY
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDExNy1ERSIsImFkZCI6IjU3LjEyOS4yOC42NCIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiMDNmY2M2MTgtYjkzZC02Nzk2LTZhZWQtOGEzOGM5NzVkNTgxIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9saW5rdndzIiwiaG9zdCI6IiIsInRscyI6InRscyJ9
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpOMll6Tg@ch1.opensocks.site:1443#05-0122-CH
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo5MTc3ZGUxYS1hZWZmLTQzZjEtOTNhNi03ZGQwOGEyZmRjNDE@frk.fastsoonlink.com:40011#06-0028-AU
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo5MTc3ZGUxYS1hZWZmLTQzZjEtOTNhNi03ZGQwOGEyZmRjNDE@sgp.fastsoonlink.com:40005#06-0029-SG
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo5MTc3ZGUxYS1hZWZmLTQzZjEtOTNhNi03ZGQwOGEyZmRjNDE@pr.fastsoonlink.com:40030#06-0030-PL
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo5MTc3ZGUxYS1hZWZmLTQzZjEtOTNhNi03ZGQwOGEyZmRjNDE@ru.fastsoonlink.com:40031#06-0031-RU
    trojan://02XtoczO7V@5.255.102.41:17590?allowInsecure=1&sni=mooshali.arshiacomplus.dpdns.org&ws=1&wspath=%2525252Fhishhhh123#06-0034-NL
    trojan://2ee85121-31de-4581-a492-eb00f606e392@45.91.171.116:443?allowInsecure=1&sni=sto.freeguard.org#06-0036-SE
    trojan://3ZFDxASRw0XIcKYFlp4RSCeSwA8ap7lEAzZB7uNnO38yDYOzDe3p23CxF0OlTx6YSK3j3@toaster.isquirrel.net:443?allowInsecure=1#06-0037-US
    trojan://0C3YaEDx46ODTFTcaF8lXlZ3zeqSlF33wZagexzRjIyODa8RDwp8XSCO93ygCSYcSYABA@blength.appagent.net:18332?allowInsecure=1#06-0038-US
    trojan://B3AO9XlcTxaIATp08S29pS6luwZ8C4qDFzaCFYEDDSA5YDeKZAy3e2ZXRe73zIpxwByN7@kasheet.appagent.net:18333?allowInsecure=1#06-0039-US
    trojan://RzFSy3laClaxnYCcO3jBEpYgDyZx2CO78IC3X46ATFD73RSSZZTx8yCOKYDOqeD8pSeRa@sirens.isquirrel.net:28334?allowInsecure=1#06-0040-US
    trojan://nzSaSa3SFaCNFDCjOCg8A39e53p8l2xaTFCOu7qZx2Z8px4CK3DXeZYAwRRS3zY66laOE@seginus.appagent.net:28331?allowInsecure=1#06-0041-US
    trojan://D0AASSpCKFjOBSwlwqylnOep8BDlgN3e3RY9S3Op2RaZZ58gID8yY3ej56CSuYacZz3EA@delight.appagent.net:443?allowInsecure=1#06-0042-US
    trojan://eYaw9xlNDu4695IF3CyY2leZOTnY8ZSOD3Xa3DClz0xqZy7Z3eaBFaTKOSwCSAOyEap4D@connect.appagent.net:28333?allowInsecure=1#06-0043-US
    trojan://4xS33pu88RaTF37ZxRjzAZc9zxe8OaYBX9CSO3p5SSxquFOFEySnDlCleCFA2DN3gaeDl@mintaka.appagent.net:443?allowInsecure=1#06-0044-US
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@104.192.226.106:989#08-0049-US
    vmess://eyJ2IjoiMiIsInBzIjoiMDgtMDA1MC1ISyIsImFkZCI6IjFlNDI2MDQ2LXQwZmRzMC10MTJjbmotMW9sOTcuaGsucDVwdi5jb20iLCJwb3J0IjoiODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTNmYjY5ZmMtNzdjZi0xMWVlLTg1ZWUtZjIzYzkxMzY5ZjJkIiwiYWlkIjoiMiIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiMWU0MjYwNDYtdDBmZHMwLXQxMmNuai0xb2w5Ny5oay5wNXB2LmNvbSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoiMDgtMDA1Mi1ISyIsImFkZCI6IjY5N2RjNTUxLXQxaTlzMC10bTUzY20tMW9sOTcuaGszLnA1cHYuY29tIiwicG9ydCI6IjgwIiwidHlwZSI6Im5vbmUiLCJpZCI6IjkzZmI2OWZjLTc3Y2YtMTFlZS04NWVlLWYyM2M5MTM2OWYyZCIsImFpZCI6IjIiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6IjY5N2RjNTUxLXQxaTlzMC10bTUzY20tMW9sOTcuaGszLnA1cHYuY29tIiwidGxzIjoiIn0=
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@37.235.49.168:989#08-0053-IS
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@37.235.49.152:989#08-0134-IS
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@154.223.16.212:989#08-0135-CO
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@154.90.62.168:989#08-0138-KR
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@51.15.17.169:989#08-0139-NL
    ss://YWVzLTI1Ni1nY206MGE5MTRlOWEtM2UzYi00NzBmLWEyNjctN2VhNzA4M2M0NWJi@77.110.110.240:443#23-0054-AT
    ss://YWVzLTI1Ni1nY206YTdmMDgyYzEtMGQxMi00NjA5LWI2YmYtZTc2MGI2NjhjZjIz@77.110.110.240:443#23-0055-AT
    ss://YWVzLTI1Ni1nY206MTAyYWQzZGEtMmQ1NS00OWQ2LWI4YzgtMmQ3ZTA0ZGYzM2Nh@77.110.110.240:443#23-0057-AT
    ss://YWVzLTI1Ni1nY206M2Y0MGJmM2QtMmYxZS00ZjQzLWJmNTQtZTVmZTc0MmEzYjRl@77.110.110.240:443#23-0058-AT
    ss://YWVzLTI1Ni1nY206ZDcwZWY4YjUtNjA0OC00YzBkLWJlNGQtZmM2MDM5OWIwZjQ1@77.110.110.240:443#23-0059-AT
    vmess://eyJ2IjoiMiIsInBzIjoiMjMtMDA2My1ERSIsImFkZCI6IjU3LjEyOS4yNC4xMjUiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjAzZmNjNjE4LWI5M2QtNjc5Ni02YWVkLThhMzhjOTc1ZDU4MSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvbGlua3Z3cz9lZD0yMDQ4QEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTiIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    ss://YWVzLTEyOC1nY206MTAwODY@160.16.123.124:10087#23-0065-JP
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpQdEh2NGJPNGpQdEJzSFdTbDFuNVFk@45.95.232.236:4248#23-0069-CH
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo5dHFoTWRJclRrZ1E0NlB2aHlBdE1I@92.112.126.90:443#23-0087-NL
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo5bGNDdnpOeHBOc25JTnlhWWZ6Yzhl@212.113.106.76:29149#23-0088-AT
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo5ZFZMYWNjR0JxRng@62.60.233.21:443#23-0089-TR
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpVS3Z5aXhLUmRUU3cyOFFwODdrZUVS@macintosh.outlinekeys.net:19609#23-0091-NL
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo0YTJyZml4b3BoZGpmZmE4S1ZBNEFh@45.87.175.171:8080#23-0102-LT
    


</details>

### 所有节点
合并节点总数: `49`
[节点链接](https://raw.githubusercontent.com/caijh/TopFreeProxies/master/sub/sub_merge_base64.txt)

### 节点来源
- [clashnode](https://github.com/imyaoxp/clashnode), 节点数量: `49`


## 仓库声明
订阅节点仅作学习交流使用，只是对网络上节点的优选排序，用于查找资料，学习知识，不做任何违法行为。所有资源均来自互联网，仅供大家交流学习使用，出现违法问题概不负责。

