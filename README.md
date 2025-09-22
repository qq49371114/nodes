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

    trojan://02XtoczO7V@creativecommons.org:443?allowInsecure=1&sni=mooshali.arshiacomplus.dpdns.org&ws=1&wspath=%2525252Fhishhhh123#05-0001-RELAY
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@51.15.23.63:989#05-0005-NL
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDAwNi1ISyIsImFkZCI6IjY5N2RjNTUxLXQxaTlzMC10bTUzY20tMW9sOTcuaGszLnA1cHYuY29tIiwicG9ydCI6IjgwIiwidHlwZSI6Im5vbmUiLCJpZCI6IjkzZmI2OWZjLTc3Y2YtMTFlZS04NWVlLWYyM2M5MTM2OWYyZCIsImFpZCI6IjIiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6IjY5N2RjNTUxLXQxaTlzMC10bTUzY20tMW9sOTcuaGszLnA1cHYuY29tIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDAwNy1SRUxBWSIsImFkZCI6ImRkZHZ2Ym4uOTMxLnBwLnVhIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI0MTc0Yjk1ZC0xMTVlLTRkMzktYWRkNi0xZjhkYjk1YmI4NjAiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLzZXZTNVOURmMVdHeGdGbm9GUHcxIiwiaG9zdCI6ImRkZHZ2Ym4uOTMxLnBwLnVhIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDAxMi1TQyIsImFkZCI6IjE1NC4yMDEuODAuMjE0IiwicG9ydCI6IjExMTU5IiwidHlwZSI6Im5vbmUiLCJpZCI6ImQ5MjAyZmRkLTU2NzktNDNhNy1hOTMzLTBkMDc2MDViYWIzYyIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvYXJraSIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDAxMy1ISyIsImFkZCI6IjQ3LjI0Mi4xODMuMTE0IiwicG9ydCI6IjU5NjM1IiwidHlwZSI6Im5vbmUiLCJpZCI6ImZkNzM5YWQxLWVjZjctNGMyNy05ZGM4LWVlY2U0ODBlNGIwZCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvYXJraSIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDAxNC1ISyIsImFkZCI6IjguMjE3LjE3MS4xOTMiLCJwb3J0IjoiMzYzMDAiLCJ0eXBlIjoibm9uZSIsImlkIjoiNjc4Y2RiMTQtMjJhNi00ZmIyLWEwNDAtYjM1M2VjYjk4OWNlIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9hcmtpIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDAxNS1ISyIsImFkZCI6IjguMjE3LjE3MS4xOTMiLCJwb3J0IjoiNTUwOTYiLCJ0eXBlIjoibm9uZSIsImlkIjoiMmI0ZDMxNTctZWQ3Zi00NmMyLWJjNGEtNWJiOGMxZjgxZTQwIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9hcmtpIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDAxNi1ISyIsImFkZCI6IjQ3LjIzOS4zMC4yNTEiLCJwb3J0IjoiMjcyMDAiLCJ0eXBlIjoibm9uZSIsImlkIjoiNjI4YzUxYzAtOTBkYi00MGUxLThhZWEtMGQ5N2FlMDgxYmJhIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9hcmtpIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDAxNy1ISyIsImFkZCI6IjguMjE3LjIyMC4zMCIsInBvcnQiOiIzMTEyMyIsInR5cGUiOiJub25lIiwiaWQiOiIxMmY3MTY0Yi1lM2UxLTQyNjQtODZjYy02ODAyODkwMmNkMTkiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2Fya2kiLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDAxOC1ISyIsImFkZCI6IjQ3LjI0Mi4xNTkuMjQ5IiwicG9ydCI6IjIyNjg2IiwidHlwZSI6Im5vbmUiLCJpZCI6IjI2OTQwY2I1LTk5OWYtNDk2OS1iZjZhLTA2NDcxZjM0MjI1OSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvYXJraSIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDAxOS1ISyIsImFkZCI6IjQ3Ljc2LjE1Ny4yMzQiLCJwb3J0IjoiNTUxMjUiLCJ0eXBlIjoibm9uZSIsImlkIjoiODcyMjdiZDktMTUwNi00ZDQ4LWJkNmItMGI4MGE4YzJhYWU3IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9hcmtpIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDAyMC1ISyIsImFkZCI6IjguMjE3LjIyMC4zMCIsInBvcnQiOiIzOTY0OCIsInR5cGUiOiJub25lIiwiaWQiOiIyYzI1ODNiNi1lY2UwLTRkM2QtYTdmNS1jZjM3YzRhNmZhOGQiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2Fya2kiLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDAyMS1ISyIsImFkZCI6IjQ3LjIzOS44MS4xMTMiLCJwb3J0IjoiMjk3NjAiLCJ0eXBlIjoibm9uZSIsImlkIjoiZmQyOTg3Y2MtYjI1Zi00OTY2LTg0NmEtYjBkNjVkM2MxZTRiIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9hcmtpIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDAyMi1ISyIsImFkZCI6IjQ3Ljc2LjE1Ny4yMzQiLCJwb3J0IjoiMTQ0NzkiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTA2MDZjMTQtY2JhNC00M2ZmLTk1ODYtOWVkZDhiZWYyMWE0IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9hcmtpIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDAyMy1ISyIsImFkZCI6IjguMjE4LjguODQiLCJwb3J0IjoiMjMzMjYiLCJ0eXBlIjoibm9uZSIsImlkIjoiODcxZDA0ZGYtZmM1OC00NzBhLWJhY2EtZGFhZTI4ODY5MTY0IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9hcmtpIiwiaG9zdCI6IiIsInRscyI6IiJ9
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpRQ1hEeHVEbFRUTUQ3anRnSFVqSW9q@45.158.171.146:8080#05-0133-FR
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNToxUld3WGh3ZkFCNWdBRW96VTRHMlBn@45.158.171.146:8080#05-0134-FR
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo0YTJyZml4b3BoZGpmZmE4S1ZBNEFh@45.158.171.146:8080#05-0135-FR
    vmess://eyJ2IjoiMiIsInBzIjoiMDYtMDAyNS1DTiIsImFkZCI6InY4LmhlZHVpYW4ubGluayIsInBvcnQiOiIzMDgwOCIsInR5cGUiOiJub25lIiwiaWQiOiJjYmIzZjg3Ny1kMWZiLTM0NGMtODdhOS1kMTUzYmZmZDU0ODQiLCJhaWQiOiIyIiwibmV0Ijoid3MiLCJwYXRoIjoiL29vb28iLCJob3N0IjoidjguaGVkdWlhbi5saW5rIiwidGxzIjoiIn0=
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@185.213.23.226:989#08-0040-NO
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpwNzhuYUNmMkVmT2xSU0xUWDB3RlZ4@pupas-shirting-unsung.freesocks.work:443#08-0041-US
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@154.90.62.168:989#08-0042-KR
    vmess://eyJ2IjoiMiIsInBzIjoiMDgtMDA0My1ISyIsImFkZCI6ImhrdC5nb3RvY2hpbmF0b3duLm5ldCIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiI5M2ZiNjlmYy03N2NmLTExZWUtODVlZS1mMjNjOTEzNjlmMmQiLCJhaWQiOiIyIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiJoa3QuZ290b2NoaW5hdG93bi5uZXQiLCJ0bHMiOiIifQ==
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@154.90.63.177:989#08-0044-KR
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@51.15.17.169:989#08-0045-NL
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpOazlhc2dsRHpIemprdFZ6VGt2aGFB@arxfw2b78fi2q9hzylhn.freesocks.work:443#08-0046-VN
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@38.165.233.93:989#08-0047-PY
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@154.223.16.212:989#08-0048-CO
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@37.235.49.168:989#08-0049-IS
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@156.146.40.194:989#08-0050-SK
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@185.153.197.5:989#08-0143-MD
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpRQ1hEeHVEbFRUTUQ3anRnSFVqSW9q@151.242.251.153:8080#08-0144-AE
    ss://YWVzLTI1Ni1nY206YTdmMDgyYzEtMGQxMi00NjA5LWI2YmYtZTc2MGI2NjhjZjIz@77.110.110.240:443#23-0052-AT
    ss://YWVzLTI1Ni1nY206MTAyYWQzZGEtMmQ1NS00OWQ2LWI4YzgtMmQ3ZTA0ZGYzM2Nh@77.110.110.240:443#23-0054-AT
    ss://YWVzLTI1Ni1nY206M2Y0MGJmM2QtMmYxZS00ZjQzLWJmNTQtZTVmZTc0MmEzYjRl@77.110.110.240:443#23-0055-AT
    ss://YWVzLTI1Ni1nY206ZDcwZWY4YjUtNjA0OC00YzBkLWJlNGQtZmM2MDM5OWIwZjQ1@77.110.110.240:443#23-0056-AT
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpqaWZ1UjJOVE0wWXQ@62.133.62.109:443#23-0057-FR
    vmess://eyJ2IjoiMiIsInBzIjoiMjMtMDA2MC1ERSIsImFkZCI6IjU3LjEyOS4yNC4xMjUiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjAzZmNjNjE4LWI5M2QtNjc5Ni02YWVkLThhMzhjOTc1ZDU4MSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvbGlua3Z3cz9lZD0yMDQ4QEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTiIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    ss://YWVzLTEyOC1nY206MTAwODY@160.16.123.124:10087#23-0062-JP
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpQdEh2NGJPNGpQdEJzSFdTbDFuNVFk@45.95.232.236:4248#23-0066-CH
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@104.192.226.106:989#23-0068-USss%2F%2FYWVzLTI1Ni1nY206MGE5MTRlOWEtM2UzYi00NzBmLWEyNjctN2VhNzA4M2M0NWJi%4077.110.110.240443%2323-0051-AT
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo5dHFoTWRJclRrZ1E0NlB2aHlBdE1I@92.112.126.90:443#23-0085-NL
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo5bGNDdnpOeHBOc25JTnlhWWZ6Yzhl@212.113.106.76:29149#23-0086-AT
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo5ZFZMYWNjR0JxRng@62.60.233.21:443#23-0087-TR
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpVS3Z5aXhLUmRUU3cyOFFwODdrZUVS@macintosh.outlinekeys.net:19609#23-0089-NL
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo0YTJyZml4b3BoZGpmZmE4S1ZBNEFh@45.87.175.171:8080#23-0100-LT
    


</details>

### 所有节点
合并节点总数: `49`
[节点链接](https://raw.githubusercontent.com/caijh/TopFreeProxies/master/sub/sub_merge_base64.txt)

### 节点来源
- [clashnode](https://github.com/imyaoxp/clashnode), 节点数量: `49`


## 仓库声明
订阅节点仅作学习交流使用，只是对网络上节点的优选排序，用于查找资料，学习知识，不做任何违法行为。所有资源均来自互联网，仅供大家交流学习使用，出现违法问题概不负责。

