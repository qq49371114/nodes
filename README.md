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
高速节点数量: `36`
<details>
  <summary>展开复制节点</summary>

    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpqSEg4S2dmZDZJWHB2eDJzdkNWRzFI@5.188.181.41:8443#05-0002-ES
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpZeDJzRjRYUkhlN3JTOE5nNmVsbTdC@83.172.138.149:8443#05-0003-DE
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpRY3N1a242cVNIbEtpVG5oMDhhOUNi@94.237.105.27:8443#05-0009-FI
    trojan://wb6368@92.243.75.49:2087?allowInsecure=1&sni=hsdgbuys.pages.dev&ws=1&wspath=%2525252F#05-0025-RELAY
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpEOEZDQzVDMC00QUI2LTQ5NzgtQkFDNy01NUIzMUQ2N0Q3NkU@freed.themars.top:31101#06-0029-CN
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpEOEZDQzVDMC00QUI2LTQ5NzgtQkFDNy01NUIzMUQ2N0Q3NkU@freed.themars.top:31102#06-0030-CN
    vmess://eyJ2IjoiMiIsInBzIjoiMDYtMDAzMS1DTiIsImFkZCI6InhkZC5kYXNodWFpLmN5b3UiLCJwb3J0IjoiNDUwNzMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYzJmZjQ2ZTMtMTE3Zi00NTc1LWI4ZDItMzhkZDcwNmUxNWJmIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoieGRkLmRhc2h1YWkuY3lvdSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoiMDYtMDAzNi1KUCIsImFkZCI6Imd2OWdxLWcwNS5qcDAxLW5uLXZtMC5lbnRyeS5mcjA1MjguYXJ0IiwicG9ydCI6IjIxNTg1IiwidHlwZSI6Im5vbmUiLCJpZCI6ImJiNjM0NjVmLTY1ZjgtMzI1Ny1iNmIzLTkzYWVhNjBjMTRiMyIsImFpZCI6IjEiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6Imd2OWdxLWcwNS5qcDAxLW5uLXZtMC5lbnRyeS5mcjA1MjguYXJ0IiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDYtMDAzNy1KUCIsImFkZCI6ImtrNXdoLWcwNS5qcDAxLW5uLXZtMC5lbnRyeS5mcjA1MjguYXJ0IiwicG9ydCI6IjIxNTg1IiwidHlwZSI6Im5vbmUiLCJpZCI6ImQ4OWFiZjM0LTRjYzgtMzU3My04NzZjLWUxOTNjNmNiMWE4YiIsImFpZCI6IjEiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6ImtrNXdoLWcwNS5qcDAxLW5uLXZtMC5lbnRyeS5mcjA1MjguYXJ0IiwidGxzIjoidGxzIn0=
    trojan://XWnVX2ASHl@5.255.103.217:37757?allowInsecure=1&sni=moshali.arshiacomplus.dpdns.org&ws=1&wspath=%2525252Fmoshaliplus#06-0038-NL
    trojan://9e76767d-4bfa-4f04-a800-42e2f63afed2@de.viefast.net:443?allowInsecure=1&sni=csapp.catch.net.tw#06-0044-DE
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@51.15.17.169:989#08-0052-NL
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@154.90.63.177:989#08-0053-KR
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@38.54.57.90:989#08-0054-BR
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpOazlhc2dsRHpIemprdFZ6VGt2aGFB@arxfw2b78fi2q9hzylhn.freesocks.work:443#08-0055-VN
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@38.165.233.93:989#08-0056-PY
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@46.183.184.60:989#08-0057-HR
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@185.153.197.5:989#08-0059-MD
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@91.132.94.200:989#08-0060-SI
    ss://Y2hhY2hhMjAtaWV0Zjphc2QxMjM0NTY@103.149.182.191:8388#08-0061-HK
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@171.22.254.17:989#08-0062-MT
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTozNjBlMjFkMjE5NzdkYzEx@104.167.197.25:57456#08-0127-US
    ss://YWVzLTI1Ni1nY206MGE5MTRlOWEtM2UzYi00NzBmLWEyNjctN2VhNzA4M2M0NWJi@77.110.110.240:443#23-0063-AT
    ss://YWVzLTI1Ni1nY206YTdmMDgyYzEtMGQxMi00NjA5LWI2YmYtZTc2MGI2NjhjZjIz@77.110.110.240:443#23-0064-AT
    ss://YWVzLTI1Ni1nY206MTAyYWQzZGEtMmQ1NS00OWQ2LWI4YzgtMmQ3ZTA0ZGYzM2Nh@77.110.110.240:443#23-0066-AT
    ss://YWVzLTI1Ni1nY206M2Y0MGJmM2QtMmYxZS00ZjQzLWJmNTQtZTVmZTc0MmEzYjRl@77.110.110.240:443#23-0067-AT
    ss://YWVzLTI1Ni1nY206ZDcwZWY4YjUtNjA0OC00YzBkLWJlNGQtZmM2MDM5OWIwZjQ1@77.110.110.240:443#23-0068-AT
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpqaWZ1UjJOVE0wWXQ@62.133.62.109:443#23-0069-FR
    ss://YWVzLTEyOC1nY206MTAwODY@160.16.123.124:10087#23-0074-JPss%2F%2FcmM0LW1kNToxNGZGUHJiZXpFM0hEWnpzTU9yNg%4023.251.121.2428080%2308-0051-US
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpQdEh2NGJPNGpQdEJzSFdTbDFuNVFk@45.95.232.236:4248#23-0078-CH
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo5dHFoTWRJclRrZ1E0NlB2aHlBdE1I@92.112.126.90:443#23-0097-NL
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo5bGNDdnpOeHBOc25JTnlhWWZ6Yzhl@212.113.106.76:29149#23-0098-AT
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo5ZFZMYWNjR0JxRng@62.60.233.21:443#23-0099-TR
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpVS3Z5aXhLUmRUU3cyOFFwODdrZUVS@macintosh.outlinekeys.net:19609#23-0101-NL
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo0YTJyZml4b3BoZGpmZmE4S1ZBNEFh@45.87.175.171:8080#23-0112-LT
    


</details>

### 所有节点
合并节点总数: `35`
[节点链接](https://raw.githubusercontent.com/caijh/TopFreeProxies/master/sub/sub_merge_base64.txt)

### 节点来源
- [clashnode](https://github.com/imyaoxp/clashnode), 节点数量: `35`


## 仓库声明
订阅节点仅作学习交流使用，只是对网络上节点的优选排序，用于查找资料，学习知识，不做任何违法行为。所有资源均来自互联网，仅供大家交流学习使用，出现违法问题概不负责。

