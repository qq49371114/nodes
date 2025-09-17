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
高速节点数量: `44`
<details>
  <summary>展开复制节点</summary>

    trojan://1b26d982-fd68-44f4-bf6d-22fe17a9249a@sg005.421421.xyz:20230?allowInsecure=1&sni=www.alibaba.com&ws=1&wspath=%2525252F#05-0002-SG
    ssr://eWQtMDUucGFvZnVubGluay5jb206MTA4MTphdXRoX2FlczEyOF9zaGExOmNoYWNoYTIwLWlldGY6cGxhaW46WW5oemJuVmpjbWRyTm1obWFYTm8vP2dyb3VwPVUxTlNVSEp2ZG1sa1pYSSZyZW1hcmtzPU1EVXRNREF3TXkxRFRnJm9iZnNwYXJhbT1ORFUyTnpJeU1qSTFORFV1YldsamNtOXpiMlowTG1OdmJRJnByb3RvcGFyYW09TWpJeU5UUTFPbFJKZGxNeVF3
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@51.15.17.169:989#05-0004-NL
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDAwNS1DQSIsImFkZCI6ImthbXBvbmcub3JnIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiIwM2ZjYzYxOC1iOTNkLTY3OTYtNmFlZC04YTM4Yzk3NWQ1ODEiLCJhaWQiOiIxIiwibmV0Ijoid3MiLCJwYXRoIjoiL2xpbmt2d3MiLCJob3N0Ijoia2FtcG9uZy5vcmciLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDAwOC1GUiIsImFkZCI6IjU3LjEyOC4xODkuMjQwIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiIwM2ZjYzYxOC1iOTNkLTY3OTYtNmFlZC04YTM4Yzk3NWQ1ODEiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2xpbmt2d3MiLCJob3N0IjoiIiwidGxzIjoidGxzIn0=
    ssr://eWQtMDcucGFvZnVubGluay5jb206NTk1NjphdXRoX2FlczEyOF9zaGExOmNoYWNoYTIwLWlldGY6cGxhaW46WW5oemJuVmpjbWRyTm1obWFYTm8vP2dyb3VwPVUxTlNVSEp2ZG1sa1pYSSZyZW1hcmtzPU1EVXRNREF4T0MxRFRnJm9iZnNwYXJhbT1ORFUyTnpJeU1qSTFORFV1YldsamNtOXpiMlowTG1OdmJRJnByb3RvcGFyYW09TWpJeU5UUTFPbFJKZGxNeVF3
    trojan://4174b95d-115e-4d39-add6-1f8db95bb860@172.67.153.179:443?allowInsecure=1&sni=qqqqqqqqqqa.www890604.dpdns.org&ws=1&wspath=%2525252FuzJNzgkkYWRWGxgFnoFPw1#05-0019-RELAY
    trojan://c2633560-5acb-4dd3-9c22-9a6c2fd212e2@ddddccvggyyu.457.pp.ua:443?allowInsecure=1&sni=ddDdCcVggYYU.457.PP.uA&ws=1&wspath=%2525252F0eGw4mEUlhltSk3Y8O5OsbJkA#05-0020-RELAY
    trojan://trojan@azadnet-9ya.pages.dev:443?allowInsecure=1&sni=azadnet-9ya.pages.dev&ws=1&wspath=%2525252F#05-0025-RELAY
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo3THQyc3FVdTl3c0E0bEFnUGNYZGpC@95.81.106.102:8443#05-0026-RU
    trojan://9e76767d-4bfa-4f04-a800-42e2f63afed2@es.viefast.net:443?allowInsecure=1&sni=csapp.catch.net.tw#05-0110-ES
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDExMS1GUiIsImFkZCI6IjU3LjEyOC4xODkuMjUzIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiIwM2ZjYzYxOC1iOTNkLTY3OTYtNmFlZC04YTM4Yzk3NWQ1ODEiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2xpbmt2d3MiLCJob3N0IjoiIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDExNy1ERSIsImFkZCI6IjkxLjk4LjgzLjExNCIsInBvcnQiOiI4NTg1IiwidHlwZSI6Im5vbmUiLCJpZCI6IjllYzFlYmQwLTM0ZTItNDBiMC1hNjgxLTNjYjBjMmQ1MTk1MyIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL2xpbmt2d3MiLCJob3N0IjoiIiwidGxzIjoiIn0=
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNToxMDI4MjZjMC04YWQzLTQ0MTctODg0My02ZGEwZjVjODBjZmU@gw.liangyuandianwan.com:35603#06-0029-CN
    vmess://eyJ2IjoiMiIsInBzIjoiMDYtMDAzMS1ISyIsImFkZCI6IjFlNDI2MDQ2LXQwZmRzMC10MTJjbmotMW9sOTcuaGsucDVwdi5jb20iLCJwb3J0IjoiODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTNmYjY5ZmMtNzdjZi0xMWVlLTg1ZWUtZjIzYzkxMzY5ZjJkIiwiYWlkIjoiMiIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiMWU0MjYwNDYtdDBmZHMwLXQxMmNuai0xb2w5Ny5oay5wNXB2LmNvbSIsInRscyI6IiJ9
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@38.165.233.93:989#06-0037-PY
    trojan://9e76767d-4bfa-4f04-a800-42e2f63afed2@de.viefast.net:443?allowInsecure=1&sni=csapp.catch.net.tw#06-0038-DE
    ss://YWVzLTI1Ni1jZmI6WG44aktkbURNMDBJZU8lMjUyNSUyNTIzJTI1MjQlMjUyM2ZKQU10c0VBRVVPcEgvWVdZdFlxREZuVDBTVg@103.186.155.213:38388#06-0045-VN
    ss://YWVzLTI1Ni1jZmI6WG44aktkbURNMDBJZU8lMjUyNSUyNTIzJTI1MjQlMjUyM2ZKQU10c0VBRVVPcEgvWVdZdFlxREZuVDBTVg@103.186.155.101:38388#06-0046-VN
    ss://YWVzLTI1Ni1jZmI6WG44aktkbURNMDBJZU8lMjUyNSUyNTIzJTI1MjQlMjUyM2ZKQU10c0VBRVVPcEgvWVdZdFlxREZuVDBTVg@103.186.155.119:38388#06-0047-VN
    ss://YWVzLTI1Ni1jZmI6WG44aktkbURNMDBJZU8lMjUyNSUyNTIzJTI1MjQlMjUyM2ZKQU10c0VBRVVPcEgvWVdZdFlxREZuVDBTVg@103.186.155.71:38388#06-0048-VN
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@154.223.20.79:989#06-0119-TW
    ss://YWVzLTI1Ni1jZmI6WG44aktkbURNMDBJZU8lMjUyNSUyNTIzJTI1MjQlMjUyM2ZKQU10c0VBRVVPcEgvWVdZdFlxREZuVDBTVg@103.186.155.116:38388#08-0050-VN
    vmess://eyJ2IjoiMiIsInBzIjoiMDgtMDA1MS1DTiIsImFkZCI6IjE4My4yNDAuMTgwLjQ3IiwicG9ydCI6IjUyNTEyIiwidHlwZSI6Im5vbmUiLCJpZCI6IjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsImFpZCI6IjY0IiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiMDgtMDEyMC1VUyIsImFkZCI6InZjLmZseS5kZXYiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjM1Mzc5MjE5LTY1MzUtNGYyZS1hNGZlLTNlNDRmNjFlMGVlZSIsImFpZCI6IjMyIiwibmV0Ijoid3MiLCJwYXRoIjoiL3ZjIiwiaG9zdCI6InZjLmZseS5kZXYiLCJ0bHMiOiJ0bHMifQ==
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@185.153.197.5:989#08-0121-MD
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@192.71.166.100:989#08-0122-GR
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@46.183.184.60:989#08-0123-HR
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@38.54.57.90:989#08-0124-BR
    ss://YWVzLTI1Ni1nY206MGE5MTRlOWEtM2UzYi00NzBmLWEyNjctN2VhNzA4M2M0NWJi@77.110.110.240:443#23-0052-AT
    ss://YWVzLTI1Ni1nY206YTdmMDgyYzEtMGQxMi00NjA5LWI2YmYtZTc2MGI2NjhjZjIz@77.110.110.240:443#23-0053-AT
    ss://YWVzLTI1Ni1nY206MTAyYWQzZGEtMmQ1NS00OWQ2LWI4YzgtMmQ3ZTA0ZGYzM2Nh@77.110.110.240:443#23-0055-AT
    ss://YWVzLTI1Ni1nY206ZDcwZWY4YjUtNjA0OC00YzBkLWJlNGQtZmM2MDM5OWIwZjQ1@77.110.110.240:443#23-0057-AT
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpqaWZ1UjJOVE0wWXQ@62.133.62.109:443#23-0058-FR
    vmess://eyJ2IjoiMiIsInBzIjoiMjMtMDA2MS1ERSIsImFkZCI6IjU3LjEyOS4yNC4xMjUiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjAzZmNjNjE4LWI5M2QtNjc5Ni02YWVkLThhMzhjOTc1ZDU4MSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvbGlua3Z3cz9lZD0yMDQ4QEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTi0tQEhpQnllVlBOTiIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    ss://YWVzLTEyOC1nY206MTAwODY@160.16.123.124:10087#23-0063-JP
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpQdEh2NGJPNGpQdEJzSFdTbDFuNVFk@45.95.232.236:4248#23-0067-CH
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@104.192.226.106:989#23-0069-USss%2F%2FYWVzLTI1Ni1nY206M2Y0MGJmM2QtMmYxZS00ZjQzLWJmNTQtZTVmZTc0MmEzYjRl%4077.110.110.240443%2323-0056-AT
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo5dHFoTWRJclRrZ1E0NlB2aHlBdE1I@92.112.126.90:443#23-0086-NL
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo5bGNDdnpOeHBOc25JTnlhWWZ6Yzhl@212.113.106.76:29149#23-0087-AT
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo5ZFZMYWNjR0JxRng@62.60.233.21:443#23-0088-TR
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpVS3Z5aXhLUmRUU3cyOFFwODdrZUVS@macintosh.outlinekeys.net:19609#23-0090-NL
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo0YTJyZml4b3BoZGpmZmE4S1ZBNEFh@45.87.175.171:8080#23-0101-LT
    


</details>

### 所有节点
合并节点总数: `45`
[节点链接](https://raw.githubusercontent.com/caijh/TopFreeProxies/master/sub/sub_merge_base64.txt)

### 节点来源
- [clashnode](https://github.com/imyaoxp/clashnode), 节点数量: `45`


## 仓库声明
订阅节点仅作学习交流使用，只是对网络上节点的优选排序，用于查找资料，学习知识，不做任何违法行为。所有资源均来自互联网，仅供大家交流学习使用，出现违法问题概不负责。

