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

    ssr://eWQtMDUucGFvZnVubGluay5jb206MTA5MTphdXRoX2FlczEyOF9zaGExOmNoYWNoYTIwLWlldGY6cGxhaW46WW5oemJuVmpjbWRyTm1obWFYTm8vP2dyb3VwPVUxTlNVSEp2ZG1sa1pYSSZyZW1hcmtzPU1EVXRNREF3TlMxRFRnJm9iZnNwYXJhbT1ORFUyTnpJeU1qSTFORFV1YldsamNtOXpiMlowTG1OdmJRJnByb3RvcGFyYW09TWpJeU5UUTFPbFJKZGxNeVF3
    ss://Y2hhY2hhMjAtaWV0Zjphc2QxMjM0NTY@103.149.182.191:8388#05-0006-HK
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDAwOC1SRUxBWSIsImFkZCI6IjczRTQyMDE5LWM4MjAtQTY2YS0wMTFFLWYxMTkzNzIzMmVjMS44OTg5MDYwNC5YWXoiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImMyNjMzNTYwLTVhY2ItNGRkMy05YzIyLTlhNmMyZmQyMTJlMiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvMnVSc000WjRZOE81T3NiSmtBIiwiaG9zdCI6IjczRTQyMDE5LWM4MjAtQTY2YS0wMTFFLWYxMTkzNzIzMmVjMS44OTg5MDYwNC5YWXoiLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDAwOS1SRUxBWSIsImFkZCI6ImhoaGp1ODkuODkwNjAzLnh5eiIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiZGMyZjU1NTctNmZjNC00ZmY3LTk4OWEtYzJjZjk4YzA4MDI5IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9ReGgzMW5uYWFaeVlVSXU3MTM3IiwiaG9zdCI6ImhoaGp1ODkuODkwNjAzLnh5eiIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDAxMC1SRUxBWSIsImFkZCI6InMxLmRiLWxpbmsuaW4iLCJwb3J0IjoiODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiMDAzZWYyMDYtNDZiNi0zNzAxLWFiNzctYjAzZGViZTc1MTFmIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9kYWJhaS5pbjNlNDRhNmYyNGY0ZjQwZGJkMWExYjNhMzRjMzQwYWY3IiwiaG9zdCI6InMxLmRiLWxpbmsuaW4iLCJ0bHMiOiIifQ==
    trojan://c2633560-5acb-4dd3-9c22-9a6c2fd212e2@ddddccvggyyu.457.pp.ua:443?allowInsecure=1&sni=ddDdCcVggYYU.457.PP.uA&ws=1&wspath=%2525252F0eGw4mEUlhltSk3Y8O5OsbJkA#05-0011-RELAY
    ss://YWVzLTI1Ni1nY206YTRWdHFSd2hqNmdXYkh3TDRKdDI2dw@ss.80808.sbs:20#05-0099-RU
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDExNC1ISyIsImFkZCI6IjQ3Ljg2LjE2LjEyNyIsInBvcnQiOiIyMDUyMSIsInR5cGUiOiJub25lIiwiaWQiOiIyMmFiMWRjOS1jYTEzLTRiNWUtYTJkYy00ZGJjNTFkNWUxMTEiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDExNS1VUyIsImFkZCI6IjQzLjE2Mi4xMTQuMTM3IiwicG9ydCI6IjU5Njc0IiwidHlwZSI6Im5vbmUiLCJpZCI6IjZhNGNlNWI5LTBkNjAtNGEyMS1hOGZlLTg5Nzc5ODAxOTUwMCIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    trojan://wb6368@92.243.75.49:2087?allowInsecure=1&sni=hsdgbuys.pages.dev&ws=1&wspath=%2525252F#06-0015-RELAY
    ss://cmM0LW1kNToxNGZGUHJiZXpFM0hEWnpzTU9yNg@23.251.121.242:8080#06-0016-US
    trojan://9e76767d-4bfa-4f04-a800-42e2f63afed2@fr.viefast.net:443?allowInsecure=1&sni=csapp.catch.net.tw#08-0022-FR
    ss://YWVzLTI1Ni1jZmI6WG44aktkbURNMDBJZU8lMjUyNSUyNTIzJTI1MjQlMjUyM2ZKQU10c0VBRVVPcEgvWVdZdFlxREZuVDBTVg@103.186.155.36:38388#08-0023-VN
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@154.90.63.177:989#08-0024-KR
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@51.15.17.169:989#08-0026-NL
    ss://YWVzLTI1Ni1jZmI6WG44aktkbURNMDBJZU8lMjUyNSUyNTIzJTI1MjQlMjUyM2ZKQU10c0VBRVVPcEgvWVdZdFlxREZuVDBTVg@103.186.154.26:38388#08-0027-VN
    ss://YWVzLTI1Ni1jZmI6WG44aktkbURNMDBJZU8lMjUyNSUyNTIzJTI1MjQlMjUyM2ZKQU10c0VBRVVPcEgvWVdZdFlxREZuVDBTVg@103.186.155.145:38388#08-0028-VN
    ss://YWVzLTI1Ni1jZmI6WG44aktkbURNMDBJZU8lMjUyNSUyNTIzJTI1MjQlMjUyM2ZKQU10c0VBRVVPcEgvWVdZdFlxREZuVDBTVg@103.186.155.135:38388#08-0029-VN
    ss://YWVzLTI1Ni1jZmI6WG44aktkbURNMDBJZU8lMjUyNSUyNTIzJTI1MjQlMjUyM2ZKQU10c0VBRVVPcEgvWVdZdFlxREZuVDBTVg@103.186.155.133:38388#08-0030-VN
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@38.165.233.93:989#08-0034-PY
    vmess://eyJ2IjoiMiIsInBzIjoiMDgtMDAzNS1VUyIsImFkZCI6InZjLmZseS5kZXYiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjM1Mzc5MjE5LTY1MzUtNGYyZS1hNGZlLTNlNDRmNjFlMGVlZSIsImFpZCI6IjMyIiwibmV0Ijoid3MiLCJwYXRoIjoiL3ZjIiwiaG9zdCI6InZjLmZseS5kZXYiLCJ0bHMiOiJ0bHMifQ==
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@171.22.254.17:989#08-0036-MT
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@38.54.57.90:989#08-0037-BR
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@46.183.184.60:989#08-0118-HR
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@192.71.166.100:989#08-0119-GR
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpOazlhc2dsRHpIemprdFZ6VGt2aGFB@arxfw2b78fi2q9hzylhn.freesocks.work:443#08-0120-VN
    vmess://eyJ2IjoiMiIsInBzIjoiMDgtMDEyMS1DQSIsImFkZCI6IjIzLjE2Mi4yMDAuMjI3IiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiIwM2ZjYzYxOC1iOTNkLTY3OTYtNmFlZC04YTM4Yzk3NWQ1ODEiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2xpbmt2d3MiLCJob3N0IjoiIiwidGxzIjoidGxzIn0=
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@185.123.101.241:989#08-0122-TR
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpmOGY3YUN6Y1BLYnNGOHAz@181.119.30.20:990#08-0123-CO
    ss://YWVzLTEyOC1nY206c2hhZG93c29ja3M@156.146.62.163:443#08-0124-CH
    ss://YWVzLTEyOC1nY206c2hhZG93c29ja3M@212.102.53.81:443#08-0125-GB
    ss://YWVzLTEyOC1nY206c2hhZG93c29ja3M@149.22.87.204:443#08-0126-JPss%2F%2FMjAyMi1ibGFrZTMtYWVzLTI1Ni1nY206N1lHRWNiR2M3M2NBMkFPZVM1aTlPL1o5bkJ3ZVBSY0RPY3dtejhpRllUTSUyNTNEJTI1M0FWdlhIdG5LMlZ5Qk80S0Nxc2hrdFJjJTI1MkJsWC9VWTJqRHpUJTI1MkJ3UGhzSS9BN00lMjUzRA%40cadacorp1yl7nz9xw6mt3vk8qd5rp2gj4bs1jcorcad.outline360bot.com80%2305-0007-CA
    ss://YWVzLTI1Ni1nY206MGE5MTRlOWEtM2UzYi00NzBmLWEyNjctN2VhNzA4M2M0NWJi@77.110.110.240:443#23-0038-AT
    ss://YWVzLTI1Ni1nY206MTAyYWQzZGEtMmQ1NS00OWQ2LWI4YzgtMmQ3ZTA0ZGYzM2Nh@77.110.110.240:443#23-0041-AT
    ss://YWVzLTI1Ni1nY206M2Y0MGJmM2QtMmYxZS00ZjQzLWJmNTQtZTVmZTc0MmEzYjRl@77.110.110.240:443#23-0042-AT
    ss://YWVzLTI1Ni1nY206ZDcwZWY4YjUtNjA0OC00YzBkLWJlNGQtZmM2MDM5OWIwZjQ1@77.110.110.240:443#23-0043-AT
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpqaWZ1UjJOVE0wWXQ@62.133.62.109:443#23-0044-FR
    vmess://eyJ2IjoiMiIsInBzIjoiMjMtMDA0Ny1ERSIsImFkZCI6IjU3LjEyOS4yNC4xMjUiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjAzZmNjNjE4LWI5M2QtNjc5Ni02YWVkLThhMzhjOTc1ZDU4MSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvbGlua3Z3cz9lZD0yMDQ4QEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTiIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    ss://YWVzLTEyOC1nY206MTAwODY@160.16.123.124:10087#23-0049-JP
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpQdEh2NGJPNGpQdEJzSFdTbDFuNVFk@45.95.232.236:4248#23-0053-CH
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@104.192.226.106:989#23-0055-US
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo5dHFoTWRJclRrZ1E0NlB2aHlBdE1I@92.112.126.90:443#23-0072-NL
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo5bGNDdnpOeHBOc25JTnlhWWZ6Yzhl@212.113.106.76:29149#23-0073-AT
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo5ZFZMYWNjR0JxRng@62.60.233.21:443#23-0074-TR
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpVS3Z5aXhLUmRUU3cyOFFwODdrZUVS@macintosh.outlinekeys.net:19609#23-0076-NL
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo0YTJyZml4b3BoZGpmZmE4S1ZBNEFh@45.87.175.171:8080#23-0087-LT
    


</details>

### 所有节点
合并节点总数: `41`
[节点链接](https://raw.githubusercontent.com/caijh/TopFreeProxies/master/sub/sub_merge_base64.txt)

### 节点来源
- [clashnode](https://github.com/imyaoxp/clashnode), 节点数量: `41`


## 仓库声明
订阅节点仅作学习交流使用，只是对网络上节点的优选排序，用于查找资料，学习知识，不做任何违法行为。所有资源均来自互联网，仅供大家交流学习使用，出现违法问题概不负责。

