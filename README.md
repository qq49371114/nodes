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

    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpZeDJzRjRYUkhlN3JTOE5nNmVsbTdC@83.172.138.149:8443#05-0000-DE
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@51.15.17.169:989#05-0005-NL
    ss://cmM0LW1kNToxNGZGUHJiZXpFM0hEWnpzTU9yNg@23.251.121.242:8080#05-0006-US
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDAwOC1SRUxBWSIsImFkZCI6Imtsby45ODY5ODYuc2hvcCIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYjc1Yzk3MzEtNDA4ZC00YWE2LThhZTktMzg1NzIwNTExM2ExIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9udmp4Nmo3a2JEUUlRTVp2YmVWQTkiLCJob3N0Ijoia2xvLjk4Njk4Ni5zaG9wIiwidGxzIjoidGxzIn0=
    ss://YWVzLTI1Ni1nY206YTRWdHFSd2hqNmdXYkh3TDRKdDI2dw@ss.80808.sbs:20#05-0010-RU
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDAxMi1SRUxBWSIsImFkZCI6InFxcXFxcXFxcXFxcWFhYWEud3d3ODkwNjA0LmRwZG5zLm9yZyIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiNDE3NGI5NWQtMTE1ZS00ZDM5LWFkZDYtMWY4ZGI5NWJiODYwIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii82V2UzVTlEZjFXR3hnRm5vRlB3MSIsImhvc3QiOiJxcXFxcXFxcXFxcXFhYWFhLnd3dzg5MDYwNC5kcGRucy5vcmciLCJ0bHMiOiJ0bHMifQ==
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpqSEg4S2dmZDZJWHB2eDJzdkNWRzFI@5.188.181.41:8443#05-0113-ES
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpRY3N1a242cVNIbEtpVG5oMDhhOUNi@94.237.105.27:8443#05-0115-FI
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpEOEZDQzVDMC00QUI2LTQ5NzgtQkFDNy01NUIzMUQ2N0Q3NkU@freed.themars.top:31101#06-0024-CN
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpEOEZDQzVDMC00QUI2LTQ5NzgtQkFDNy01NUIzMUQ2N0Q3NkU@freed.themars.top:31102#06-0025-CN
    vmess://eyJ2IjoiMiIsInBzIjoiMDYtMDAyNi1DTiIsImFkZCI6InhkZC5kYXNodWFpLmN5b3UiLCJwb3J0IjoiNDUwNzMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYzJmZjQ2ZTMtMTE3Zi00NTc1LWI4ZDItMzhkZDcwNmUxNWJmIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoieGRkLmRhc2h1YWkuY3lvdSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoiMDYtMDAzMS1KUCIsImFkZCI6Imd2OWdxLWcwNS5qcDAxLW5uLXZtMC5lbnRyeS5mcjA1MjguYXJ0IiwicG9ydCI6IjIxNTg1IiwidHlwZSI6Im5vbmUiLCJpZCI6ImJiNjM0NjVmLTY1ZjgtMzI1Ny1iNmIzLTkzYWVhNjBjMTRiMyIsImFpZCI6IjEiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6Imd2OWdxLWcwNS5qcDAxLW5uLXZtMC5lbnRyeS5mcjA1MjguYXJ0IiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDYtMDAzMi1KUCIsImFkZCI6ImtrNXdoLWcwNS5qcDAxLW5uLXZtMC5lbnRyeS5mcjA1MjguYXJ0IiwicG9ydCI6IjIxNTg1IiwidHlwZSI6Im5vbmUiLCJpZCI6ImQ4OWFiZjM0LTRjYzgtMzU3My04NzZjLWUxOTNjNmNiMWE4YiIsImFpZCI6IjEiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6ImtrNXdoLWcwNS5qcDAxLW5uLXZtMC5lbnRyeS5mcjA1MjguYXJ0IiwidGxzIjoidGxzIn0=
    trojan://XWnVX2ASHl@5.255.103.217:37757?allowInsecure=1&sni=moshali.arshiacomplus.dpdns.org&ws=1&wspath=%2525252Fmoshaliplus#06-0033-NL
    trojan://9e76767d-4bfa-4f04-a800-42e2f63afed2@de.viefast.net:443?allowInsecure=1&sni=csapp.catch.net.tw#06-0043-DE
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@154.90.63.177:989#08-0049-KR
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@38.54.57.90:989#08-0050-BR
    ss://YWVzLTI1Ni1jZmI6WG44aktkbURNMDBJZU8lMjUyNSUyNTIzJTI1MjQlMjUyM2ZKQU10c0VBRVVPcEgvWVdZdFlxREZuVDBTVg@103.186.155.145:38388#08-0051-VN
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@46.183.184.60:989#08-0052-HR
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@192.71.166.100:989#08-0053-GR
    ss://YWVzLTEyOC1nY206c2hhZG93c29ja3M@156.146.38.167:443#08-0118-USss%2F%2FYWVzLTI1Ni1nY206ZDcwZWY4YjUtNjA0OC00YzBkLWJlNGQtZmM2MDM5OWIwZjQ1%4077.110.110.240443%2323-0059-AT
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpvWklvQTY5UTh5aGNRVjhrYTNQYTNB@103.104.247.49:8080#08-0119-NL
    ss://YWVzLTI1Ni1nY206MGE5MTRlOWEtM2UzYi00NzBmLWEyNjctN2VhNzA4M2M0NWJi@77.110.110.240:443#23-0054-AT
    ss://YWVzLTI1Ni1nY206YTdmMDgyYzEtMGQxMi00NjA5LWI2YmYtZTc2MGI2NjhjZjIz@77.110.110.240:443#23-0055-AT
    ss://YWVzLTI1Ni1nY206MTAyYWQzZGEtMmQ1NS00OWQ2LWI4YzgtMmQ3ZTA0ZGYzM2Nh@77.110.110.240:443#23-0057-AT
    ss://YWVzLTI1Ni1nY206M2Y0MGJmM2QtMmYxZS00ZjQzLWJmNTQtZTVmZTc0MmEzYjRl@77.110.110.240:443#23-0058-AT
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpqaWZ1UjJOVE0wWXQ@62.133.62.109:443#23-0060-FR
    vmess://eyJ2IjoiMiIsInBzIjoiMjMtMDA2My1ERSIsImFkZCI6IjU3LjEyOS4yNC4xMjUiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjAzZmNjNjE4LWI5M2QtNjc5Ni02YWVkLThhMzhjOTc1ZDU4MSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvbGlua3Z3cz9lZD0yMDQ4QEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTiIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpQdEh2NGJPNGpQdEJzSFdTbDFuNVFk@45.95.232.236:4248#23-0069-CH
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@104.192.226.106:989#23-0071-US
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo5dHFoTWRJclRrZ1E0NlB2aHlBdE1I@92.112.126.90:443#23-0088-NL
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo5bGNDdnpOeHBOc25JTnlhWWZ6Yzhl@212.113.106.76:29149#23-0089-AT
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo5ZFZMYWNjR0JxRng@62.60.233.21:443#23-0090-TR
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpVS3Z5aXhLUmRUU3cyOFFwODdrZUVS@macintosh.outlinekeys.net:19609#23-0092-NL
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo0YTJyZml4b3BoZGpmZmE4S1ZBNEFh@45.87.175.171:8080#23-0103-LT
    


</details>

### 所有节点
合并节点总数: `38`
[节点链接](https://raw.githubusercontent.com/caijh/TopFreeProxies/master/sub/sub_merge_base64.txt)

### 节点来源
- [clashnode](https://github.com/imyaoxp/clashnode), 节点数量: `38`


## 仓库声明
订阅节点仅作学习交流使用，只是对网络上节点的优选排序，用于查找资料，学习知识，不做任何违法行为。所有资源均来自互联网，仅供大家交流学习使用，出现违法问题概不负责。

