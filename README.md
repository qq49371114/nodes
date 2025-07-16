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
高速节点数量: `57`
<details>
  <summary>展开复制节点</summary>

    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMDAxLUpQIiwiYWRkIjoianAtMS5hbmV3c3RhcnQuY3lvdSIsInBvcnQiOiI1MDYxIiwidHlwZSI6Im5vbmUiLCJpZCI6IjZhZDIyM2RiLWIwMWQtM2E1ZS05ZTAwLTMzZDY3MTMxYWI3ZCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6ImpwLTEuYW5ld3N0YXJ0LmN5b3UiLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMDAyLU5PV0hFUkUiLCJhZGQiOiJqcDYtMS5hbmV3c3RhcnQuY3lvdSIsInBvcnQiOiI1MDYxIiwidHlwZSI6Im5vbmUiLCJpZCI6IjZhZDIyM2RiLWIwMWQtM2E1ZS05ZTAwLTMzZDY3MTMxYWI3ZCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6ImpwNi0xLmFuZXdzdGFydC5jeW91IiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMDA0LU5PV0hFUkUiLCJhZGQiOiJ1czYtMS5hbmV3c3RhcnQuY3lvdSIsInBvcnQiOiI1MDYxIiwidHlwZSI6Im5vbmUiLCJpZCI6IjZhZDIyM2RiLWIwMWQtM2E1ZS05ZTAwLTMzZDY3MTMxYWI3ZCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6InVzNi0xLmFuZXdzdGFydC5jeW91IiwidGxzIjoidGxzIn0=
    trojan://7d8886cb-ff8e-3ef1-83fa-683558e78e2d@gz0slb.aliyuncdn.smp-paymentservices-apple.com:56323?allowInsecure=1&sni=edge.steam-dns.top.comcast.net#04-005-NOWHERE
    trojan://7d8886cb-ff8e-3ef1-83fa-683558e78e2d@gz0slb.aliyuncdn.smp-paymentservices-apple.com:56432?allowInsecure=1&sni=fastly.cdn.steampipe.steamcontent.com#04-006-NOWHERE
    trojan://7d8886cb-ff8e-3ef1-83fa-683558e78e2d@push04.endpoint.smp-paymentservices-apple.com:23452?allowInsecure=1&sni=www.microsoft365.com#04-007-CN
    trojan://7d8886cb-ff8e-3ef1-83fa-683558e78e2d@push04.endpoint.smp-paymentservices-apple.com:23453?allowInsecure=1&sni=origin-a.akamaihd.net#04-008-CN
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTA4LVJFTEFZIiwiYWRkIjoiczEuY24tZGIudG9wIiwicG9ydCI6IjgwODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiYmQ1NGRlNDMtNWVlYS0zOGM1LTkyNmItZDMzNWY4MGY4NzZiIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9kYWJhaS5pbjE3Mi42Ny4xMDIuMjIzIiwiaG9zdCI6InMxLmNuLWRiLnRvcCIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTA5LVJFTEFZIiwiYWRkIjoiczMuY24tZGIudG9wIiwicG9ydCI6IjIwODYiLCJ0eXBlIjoibm9uZSIsImlkIjoiYmQ1NGRlNDMtNWVlYS0zOGM1LTkyNmItZDMzNWY4MGY4NzZiIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9kYWJhaS5pbjEwNC4yNS4yMC41OCIsImhvc3QiOiJzMy5jbi1kYi50b3AiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTEwLVJFTEFZIiwiYWRkIjoiczQuZGItbGluazAxLnRvcCIsInBvcnQiOiIyMDg2IiwidHlwZSI6Im5vbmUiLCJpZCI6ImJkNTRkZTQzLTVlZWEtMzhjNS05MjZiLWQzMzVmODBmODc2YiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvZGFiYWkuaW4xMDQuMTYuMTk0LjIxNCIsImhvc3QiOiJzNC5kYi1saW5rMDEudG9wIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTExLVJFTEFZIiwiYWRkIjoiczEuZGItbGluazAyLnRvcCIsInBvcnQiOiIyMDgyIiwidHlwZSI6Im5vbmUiLCJpZCI6ImJkNTRkZTQzLTVlZWEtMzhjNS05MjZiLWQzMzVmODBmODc2YiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvZGFiYWkuaW4xNzIuNjQuMi4yIiwiaG9zdCI6InMxLmRiLWxpbmswMi50b3AiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTEyLVJFTEFZIiwiYWRkIjoiczUuY24tZGIudG9wIiwicG9ydCI6IjgwODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiYmQ1NGRlNDMtNWVlYS0zOGM1LTkyNmItZDMzNWY4MGY4NzZiIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9kYWJhaS5pbjE3Mi42NC41NS4xMDIiLCJob3N0IjoiczUuY24tZGIudG9wIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTEzLVJFTEFZIiwiYWRkIjoiczQuZGItbGluazAyLnRvcCIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiJiZDU0ZGU0My01ZWVhLTM4YzUtOTI2Yi1kMzM1ZjgwZjg3NmIiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2RhYmFpLmluMTA0LjIxLjEwNy4yMTkiLCJob3N0IjoiczQuZGItbGluazAyLnRvcCIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTE0LU5PV0hFUkUiLCJhZGQiOiIxMi5tYW1hbWFqZC5zaXRlIiwicG9ydCI6IjIzNjEyIiwidHlwZSI6Im5vbmUiLCJpZCI6Ijk3Zjk3Y2VhLTBlZDctM2U0Yi1hNjEyLTFiZDRlYTA4NjQ5ZSIsImFpZCI6IjIiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6IjEyLm1hbWFtYWpkLnNpdGUiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTE1LUNOIiwiYWRkIjoiMTcubWFtYW1hamQuc2l0ZSIsInBvcnQiOiIyMzYxNyIsInR5cGUiOiJub25lIiwiaWQiOiI5N2Y5N2NlYS0wZWQ3LTNlNGItYTYxMi0xYmQ0ZWEwODY0OWUiLCJhaWQiOiIyIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIxNy5tYW1hbWFqZC5zaXRlIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTE2LUNOIiwiYWRkIjoiMTEubWFtYW1hamQuc2l0ZSIsInBvcnQiOiIyMzYxMSIsInR5cGUiOiJub25lIiwiaWQiOiI5N2Y5N2NlYS0wZWQ3LTNlNGItYTYxMi0xYmQ0ZWEwODY0OWUiLCJhaWQiOiIyIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIxMS5tYW1hbWFqZC5zaXRlIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTE3LUNOIiwiYWRkIjoiMTkubWFtYW1hamQuc2l0ZSIsInBvcnQiOiIyMzYxOSIsInR5cGUiOiJub25lIiwiaWQiOiI5N2Y5N2NlYS0wZWQ3LTNlNGItYTYxMi0xYmQ0ZWEwODY0OWUiLCJhaWQiOiIyIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIxOS5tYW1hbWFqZC5zaXRlIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTE4LUNOIiwiYWRkIjoiMTYubWFtYW1hamQuc2l0ZSIsInBvcnQiOiIyMzYxNiIsInR5cGUiOiJub25lIiwiaWQiOiI5N2Y5N2NlYS0wZWQ3LTNlNGItYTYxMi0xYmQ0ZWEwODY0OWUiLCJhaWQiOiIyIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIxNi5tYW1hbWFqZC5zaXRlIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTE5LUNOIiwiYWRkIjoiMTgubWFtYW1hamQuc2l0ZSIsInBvcnQiOiIyMzYxOCIsInR5cGUiOiJub25lIiwiaWQiOiI5N2Y5N2NlYS0wZWQ3LTNlNGItYTYxMi0xYmQ0ZWEwODY0OWUiLCJhaWQiOiIyIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIxOC5tYW1hbWFqZC5zaXRlIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTIwLUNOIiwiYWRkIjoiMTUubWFtYW1hamQuc2l0ZSIsInBvcnQiOiIyMzYxNSIsInR5cGUiOiJub25lIiwiaWQiOiI5N2Y5N2NlYS0wZWQ3LTNlNGItYTYxMi0xYmQ0ZWEwODY0OWUiLCJhaWQiOiIyIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIxNS5tYW1hbWFqZC5zaXRlIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTIxLU5PV0hFUkUiLCJhZGQiOiI1Lm1hbWFtYWpkLnNpdGUiLCJwb3J0IjoiMjM2MDUiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTdmOTdjZWEtMGVkNy0zZTRiLWE2MTItMWJkNGVhMDg2NDllIiwiYWlkIjoiMiIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiNS5tYW1hbWFqZC5zaXRlIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTIyLUNOIiwiYWRkIjoiMTMubWFtYW1hamQuc2l0ZSIsInBvcnQiOiIyMzYxMyIsInR5cGUiOiJub25lIiwiaWQiOiI5N2Y5N2NlYS0wZWQ3LTNlNGItYTYxMi0xYmQ0ZWEwODY0OWUiLCJhaWQiOiIyIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIxMy5tYW1hbWFqZC5zaXRlIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTIzLUNOIiwiYWRkIjoiMTQubWFtYW1hamQuc2l0ZSIsInBvcnQiOiIyMzYxNCIsInR5cGUiOiJub25lIiwiaWQiOiI5N2Y5N2NlYS0wZWQ3LTNlNGItYTYxMi0xYmQ0ZWEwODY0OWUiLCJhaWQiOiIyIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIxNC5tYW1hbWFqZC5zaXRlIiwidGxzIjoiIn0=
    ss://YWVzLTI1Ni1nY206YXRqZ3NKWG1jdg@103.15.91.171:52327#05-141-VN
    trojan://ttfang@139.180.154.158:443?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=%2525252F#05-153-SG
    trojan://ttfang@13.228.155.72:443?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=%2525252F#05-170-SG
    trojan://ttfang@13.233.5.49:443?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=%2525252F#05-171-IN
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMjAzLVJFTEFZIiwiYWRkIjoiMTc1MDE1ODc0MS50ZW5jZW50YXBwLmNuIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI2OWZlOTdjNy04YTFjLTRhYjAtYjRmZC1jMTcwNDJiNDkyOTEiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIxNzUwMTU4NzQxLnRlbmNlbnRhcHAuY24iLCJ0bHMiOiJ0bHMifQ==
    trojan://trojan@109.234.211.66:8443?allowInsecure=1&sni=store.timimi.dpdns.org&ws=1&wspath=%2525252F#09-457-RELAY
    vmess://eyJ2IjoiMiIsInBzIjoiMDktNTEzLVJVIiwiYWRkIjoiNDUuNTkyMTY4OC54eXoiLCJwb3J0IjoiMTg0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiNzFhN2RiMTQtMWI2Zi01YWVjLTllNWQtOWJkNWY4YmVhYmFiIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiNDUuNTkyMTY4OC54eXoiLCJ0bHMiOiJ0bHMifQ==
    trojan://tg-fq521free@198.62.62.67:443?allowInsecure=1&sni=torjan.xn--xhq44j.eu.org&ws=1&wspath=%2525252F#09-598-US
    ss://YWVzLTI1Ni1nY206VEclMjUzQSUyNTQwRW5rZWx0ZV9ub3RpZiUyNTI2JTI1MjZURyUyNTNBJTI1NDBOb3RpZl9DaGF0@152.53.2.128:34045#14-611-AT
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@185.153.197.5:989#14-612-MD
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpjNDA2NDFjMWY4OWU3YWNi@147.45.178.200:57456#14-617-DE
    ss://YWVzLTI1Ni1nY206aVVCMDkyM1JCQQ@154.3.8.151:30067#14-618-US
    vmess://eyJ2IjoiMiIsInBzIjoiMTQtNjE5LU5MIiwiYWRkIjoiODMuMTQ5Ljg0LjE0NSIsInBvcnQiOiIxNTcwOSIsInR5cGUiOiJub25lIiwiaWQiOiI0YWMzOWU4YS02ZDVjLTQ4YmItYjBkMC1mNjMzYzgyOTExM2UiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6IiUyNTI1MkYiLCJob3N0IjoidG9yamFuLnhuLS14aHE0NGouZXUub3JnIiwidGxzIjoiIn0=
    trojan://7367d04e-4c59-4dff-a50e-12e730a09891@155.117.228.70:26193?allowInsecure=1#14-620-HK
    ss://YWVzLTI1Ni1jZmI6cXdlclJFV1ElMjU0MCUyNTQw@p222.panda001.net:15098#14-622-KR
    vmess://eyJ2IjoiMiIsInBzIjoiMTQtNjIzLUhLIiwiYWRkIjoidjcuaGVkdWlhbi5saW5rIiwicG9ydCI6IjMwODA3IiwidHlwZSI6Im5vbmUiLCJpZCI6ImNiYjNmODc3LWQxZmItMzQ0Yy04N2E5LWQxNTNiZmZkNTQ4NCIsImFpZCI6IjIiLCJuZXQiOiJ3cyIsInBhdGgiOiIvb29vbyIsImhvc3QiOiJ2Ny5oZWR1aWFuLmxpbmsiLCJ0bHMiOiIifQ==
    trojan://Aimer@206.238.236.219:2083?allowInsecure=1&sni=amepo.ambercc.filegear-sg.me#23-625-SG
    trojan://Aimer@108.165.152.225:2083?allowInsecure=1&sni=amepo.ambercc.filegear-sg.me#23-633-RELAY
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpxc2NhdkY1VXZpSUwtOFYtRTRyYUJB@194.87.71.228:2222#23-636-DE
    trojan://f282b878-8711-45a1-8c69-5564172123c1@172.67.181.173:443?allowInsecure=1&sni=vpn.stupidworld.web.id&ws=1&wspath=%2525252F#23-645-RELAY
    ss://YWVzLTEyOC1nY206c2hhZG93c29ja3M@173.244.56.6:443#23-648-USss%2F%2FY2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpiMFRLeG5IQVllZUZZeXpUQU1YbjBG%40h110vpnnl.outlinekeys.net52571%2323-634-NL
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpZVFEwWg@83.147.18.163:8388#23-652-ES
    trojan://telegram-id-directvpn@3.78.31.242:22223?allowInsecure=1&sni=trojan.burgerip.co.uk#23-654-DE
    trojan://telegram-id-privatevpns@3.78.31.242:22222?allowInsecure=1&sni=trojan.burgerip.co.uk#23-655-DE
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo0YTJyZml4b3BoZGpmZmE4S1ZBNEFh@45.87.175.199:8080#23-662-LT
    ss://YWVzLTI1Ni1jZmI6WG44aktkbURNMDBJZU8lMjUyNSUyNTIzJTI1MjQlMjUyM2ZKQU10c0VBRVVPcEgvWVdZdFlxREZuVDBTVg@103.186.154.35:38388#23-669-VN
    vmess://eyJ2IjoiMiIsInBzIjoiMjMtNjcwLVNFIiwiYWRkIjoiMTY5LjE1MC4yMDguODMiLCJwb3J0IjoiMTgwMDAiLCJ0eXBlIjoibm9uZSIsImlkIjoiZjhjOGRjM2QtMGQzNy00NmIwLThiMzQtYTcyMzI4ODJmY2ZlIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6InRyb2phbi5idXJnZXJpcC5jby51ayIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoiMjMtNjg0LUNIIiwiYWRkIjoiMTg2LjE5MC4yMTUuMTkzIiwicG9ydCI6IjIyMzI0IiwidHlwZSI6Im5vbmUiLCJpZCI6IjA0NjIxYmFlLWFiMzYtMTFlYy1iOTA5LTAyNDJhYzEyMDAwMiIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiJ0cm9qYW4uYnVyZ2VyaXAuY28udWsiLCJ0bHMiOiIifQ==
    trojan://ceaea123-1b4b-469b-8358-bcd5f5529305@uk.liangyuandian.top:443?allowInsecure=1#23-689-SG
    trojan://51c44c4e-f8c2-4419-a52b-b4b7bd915078@ap.liangyuandian.top:443?allowInsecure=1#23-690-SG
    ss://YWVzLTI1Ni1jZmI6WG44aktkbURNMDBJZU8lMjUyNSUyNTIzJTI1MjQlMjUyM2ZKQU10c0VBRVVPcEgvWVdZdFlxREZuVDBTVg@103.186.154.19:38388#23-704-VN
    ss://YWVzLTI1Ni1jZmI6THAyN3JxeUpxNzJiWnNxWA@217.30.10.18:9045#23-705-PL
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@103.163.218.2:989#23-706-VN
    


</details>

### 所有节点
合并节点总数: `166`
[节点链接](https://raw.githubusercontent.com/caijh/TopFreeProxies/master/sub/sub_merge_base64.txt)

### 节点来源
- [clashnode](https://github.com/imyaoxp/clashnode), 节点数量: `166`


## 仓库声明
订阅节点仅作学习交流使用，只是对网络上节点的优选排序，用于查找资料，学习知识，不做任何违法行为。所有资源均来自互联网，仅供大家交流学习使用，出现违法问题概不负责。

