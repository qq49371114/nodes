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
高速节点数量: `54`
<details>
  <summary>展开复制节点</summary>

    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMDAxLUpQIiwiYWRkIjoianAtMS5hbmV3c3RhcnQuY3lvdSIsInBvcnQiOiI1MDYxIiwidHlwZSI6Im5vbmUiLCJpZCI6IjU1MDc0Y2JkLWUxNjYtMzJlZC1iOTBmLWM1ZDQ3YWE5YTdhMyIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6ImpwLTEuYW5ld3N0YXJ0LmN5b3UiLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMDA0LU5PV0hFUkUiLCJhZGQiOiJ1czYtMS5hbmV3c3RhcnQuY3lvdSIsInBvcnQiOiI1MDYxIiwidHlwZSI6Im5vbmUiLCJpZCI6IjU1MDc0Y2JkLWUxNjYtMzJlZC1iOTBmLWM1ZDQ3YWE5YTdhMyIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6InVzNi0xLmFuZXdzdGFydC5jeW91IiwidGxzIjoidGxzIn0=
    trojan://fff6303d-8960-3f8e-92fd-62113f7e44fa@gz0slb.aliyuncdn.smp-paymentservices-apple.com:56323?allowInsecure=1&sni=edge.steam-dns.top.comcast.net#04-005-NOWHERE
    trojan://fff6303d-8960-3f8e-92fd-62113f7e44fa@gz0slb.aliyuncdn.smp-paymentservices-apple.com:56432?allowInsecure=1&sni=fastly.cdn.steampipe.steamcontent.com#04-006-NOWHERE
    trojan://fff6303d-8960-3f8e-92fd-62113f7e44fa@push04.endpoint.smp-paymentservices-apple.com:23452?allowInsecure=1&sni=www.microsoft365.com#04-007-CN
    trojan://fff6303d-8960-3f8e-92fd-62113f7e44fa@push04.endpoint.smp-paymentservices-apple.com:23453?allowInsecure=1&sni=origin-a.akamaihd.net#04-008-CN
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTA4LVJFTEFZIiwiYWRkIjoiczUuZGItbGluazAyLnRvcCIsInBvcnQiOiIyMDg2IiwidHlwZSI6Im5vbmUiLCJpZCI6IjQxNzA2M2QxLTc2N2MtMzliNy1hOTkzLTdhNDhiOWU2NWI5NCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvZGFiYWkuaW4xMDQuMjAuNDYuMjEwIiwiaG9zdCI6InM1LmRiLWxpbmswMi50b3AiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTA5LVJFTEFZIiwiYWRkIjoiczEuZGItbGluazAyLnRvcCIsInBvcnQiOiIyMDg2IiwidHlwZSI6Im5vbmUiLCJpZCI6IjQxNzA2M2QxLTc2N2MtMzliNy1hOTkzLTdhNDhiOWU2NWI5NCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvZGFiYWkuaW4xMDQuMjAuNjkuMTQ0IiwiaG9zdCI6InMxLmRiLWxpbmswMi50b3AiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTEwLVJFTEFZIiwiYWRkIjoiczQuZGItbGluazAyLnRvcCIsInBvcnQiOiI4MDgwIiwidHlwZSI6Im5vbmUiLCJpZCI6IjQxNzA2M2QxLTc2N2MtMzliNy1hOTkzLTdhNDhiOWU2NWI5NCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvZGFiYWkuaW4xMDQuMjAuNDEuMTQ1IiwiaG9zdCI6InM0LmRiLWxpbmswMi50b3AiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTExLVJFTEFZIiwiYWRkIjoiczMuY24tZGIudG9wIiwicG9ydCI6IjIwODIiLCJ0eXBlIjoibm9uZSIsImlkIjoiNDE3MDYzZDEtNzY3Yy0zOWI3LWE5OTMtN2E0OGI5ZTY1Yjk0IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9kYWJhaS5pbjE3Mi42NC4zOC4yNDgiLCJob3N0IjoiczMuY24tZGIudG9wIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTEyLVJFTEFZIiwiYWRkIjoiczEuY24tZGIudG9wIiwicG9ydCI6Ijg4ODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiNDE3MDYzZDEtNzY3Yy0zOWI3LWE5OTMtN2E0OGI5ZTY1Yjk0IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9kYWJhaS5pbjE3Mi42Ny4xMTAuMTMzIiwiaG9zdCI6InMxLmNuLWRiLnRvcCIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTEzLVJFTEFZIiwiYWRkIjoiczEuZGItbGluazAxLnRvcCIsInBvcnQiOiI4MDgwIiwidHlwZSI6Im5vbmUiLCJpZCI6IjQxNzA2M2QxLTc2N2MtMzliNy1hOTkzLTdhNDhiOWU2NWI5NCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvZGFiYWkuaW4xMDQuMjAuNzcuMjE4IiwiaG9zdCI6InMxLmRiLWxpbmswMS50b3AiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTE0LVJFTEFZIiwiYWRkIjoiczMuZGItbGluazAxLnRvcCIsInBvcnQiOiI4ODgwIiwidHlwZSI6Im5vbmUiLCJpZCI6IjQxNzA2M2QxLTc2N2MtMzliNy1hOTkzLTdhNDhiOWU2NWI5NCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvZGFiYWkuaW4xMDQuMjEuMjM5LjEwMCIsImhvc3QiOiJzMy5kYi1saW5rMDEudG9wIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTE1LU5PV0hFUkUiLCJhZGQiOiIxMi5tYW1hbWFqZC5zaXRlIiwicG9ydCI6IjIzNjEyIiwidHlwZSI6Im5vbmUiLCJpZCI6ImM5ZGYyMjA3LTZjYjItM2RhMS1iNjUxLWNkYzdjOGFhZGMzYiIsImFpZCI6IjIiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6IjEyLm1hbWFtYWpkLnNpdGUiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTE2LUNOIiwiYWRkIjoiMTcubWFtYW1hamQuc2l0ZSIsInBvcnQiOiIyMzYxNyIsInR5cGUiOiJub25lIiwiaWQiOiJjOWRmMjIwNy02Y2IyLTNkYTEtYjY1MS1jZGM3YzhhYWRjM2IiLCJhaWQiOiIyIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIxNy5tYW1hbWFqZC5zaXRlIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTE3LUNOIiwiYWRkIjoiMTEubWFtYW1hamQuc2l0ZSIsInBvcnQiOiIyMzYxMSIsInR5cGUiOiJub25lIiwiaWQiOiJjOWRmMjIwNy02Y2IyLTNkYTEtYjY1MS1jZGM3YzhhYWRjM2IiLCJhaWQiOiIyIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIxMS5tYW1hbWFqZC5zaXRlIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTE4LUNOIiwiYWRkIjoiMTkubWFtYW1hamQuc2l0ZSIsInBvcnQiOiIyMzYxOSIsInR5cGUiOiJub25lIiwiaWQiOiJjOWRmMjIwNy02Y2IyLTNkYTEtYjY1MS1jZGM3YzhhYWRjM2IiLCJhaWQiOiIyIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIxOS5tYW1hbWFqZC5zaXRlIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTE5LUNOIiwiYWRkIjoiMTYubWFtYW1hamQuc2l0ZSIsInBvcnQiOiIyMzYxNiIsInR5cGUiOiJub25lIiwiaWQiOiJjOWRmMjIwNy02Y2IyLTNkYTEtYjY1MS1jZGM3YzhhYWRjM2IiLCJhaWQiOiIyIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIxNi5tYW1hbWFqZC5zaXRlIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTIwLUNOIiwiYWRkIjoiMTgubWFtYW1hamQuc2l0ZSIsInBvcnQiOiIyMzYxOCIsInR5cGUiOiJub25lIiwiaWQiOiJjOWRmMjIwNy02Y2IyLTNkYTEtYjY1MS1jZGM3YzhhYWRjM2IiLCJhaWQiOiIyIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIxOC5tYW1hbWFqZC5zaXRlIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTIxLUNOIiwiYWRkIjoiMTUubWFtYW1hamQuc2l0ZSIsInBvcnQiOiIyMzYxNSIsInR5cGUiOiJub25lIiwiaWQiOiJjOWRmMjIwNy02Y2IyLTNkYTEtYjY1MS1jZGM3YzhhYWRjM2IiLCJhaWQiOiIyIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIxNS5tYW1hbWFqZC5zaXRlIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTIyLU5PV0hFUkUiLCJhZGQiOiI1Lm1hbWFtYWpkLnNpdGUiLCJwb3J0IjoiMjM2MDUiLCJ0eXBlIjoibm9uZSIsImlkIjoiYzlkZjIyMDctNmNiMi0zZGExLWI2NTEtY2RjN2M4YWFkYzNiIiwiYWlkIjoiMiIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiNS5tYW1hbWFqZC5zaXRlIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTIzLUNOIiwiYWRkIjoiMTMubWFtYW1hamQuc2l0ZSIsInBvcnQiOiIyMzYxMyIsInR5cGUiOiJub25lIiwiaWQiOiJjOWRmMjIwNy02Y2IyLTNkYTEtYjY1MS1jZGM3YzhhYWRjM2IiLCJhaWQiOiIyIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIxMy5tYW1hbWFqZC5zaXRlIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTI0LUNOIiwiYWRkIjoiMTQubWFtYW1hamQuc2l0ZSIsInBvcnQiOiIyMzYxNCIsInR5cGUiOiJub25lIiwiaWQiOiJjOWRmMjIwNy02Y2IyLTNkYTEtYjY1MS1jZGM3YzhhYWRjM2IiLCJhaWQiOiIyIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIxNC5tYW1hbWFqZC5zaXRlIiwidGxzIjoiIn0=
    trojan://ttfang@20.235.105.146:443?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=%2525252F#05-125-IN
    trojan://ttfang@138.2.95.61:1111?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=%2525252F#05-126-SG
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMTI3LUNOIiwiYWRkIjoidjI1LmhlZHVpYW4ubGluayIsInBvcnQiOiIzMDgyNSIsInR5cGUiOiJub25lIiwiaWQiOiJjYmIzZjg3Ny1kMWZiLTM0NGMtODdhOS1kMTUzYmZmZDU0ODQiLCJhaWQiOiIyIiwibmV0Ijoid3MiLCJwYXRoIjoiL29vb28iLCJob3N0IjoidjI1LmhlZHVpYW4ubGluayIsInRscyI6IiJ9
    trojan://d0298536-d670-4045-bbb1-ddd5ea68683e@www.digitalocean.com:443?allowInsecure=1&sni=azadnet-5vk.pages.dev&ws=1&wspath=%2525252Fazadnet-5vk.pages.dev%2525252F%2525253Fed%2525253D2560#05-164-RELAY
    trojan://74260628090146500@stirring-parakeet.shiner427.skin:443?allowInsecure=1#09-284-NL
    trojan://Aimer@92.243.74.180:8443?allowInsecure=1&sni=tyep.esslh.filegear-sg.me&ws=1&wspath=%2525252F#09-392-RELAY
    ss://YWVzLTI1Ni1jZmI6WG44aktkbURNMDBJZU8lMjUyNSUyNTIzJTI1MjQlMjUyM2ZKQU10c0VBRVVPcEgvWVdZdFlxREZuVDBTVg@103.186.155.30:38388#14-539-VN
    vmess://eyJ2IjoiMiIsInBzIjoiMTQtNTQzLUNOIiwiYWRkIjoidjM2LmhlZHVpYW4ubGluayIsInBvcnQiOiIzMDgzNiIsInR5cGUiOiJub25lIiwiaWQiOiJjYmIzZjg3Ny1kMWZiLTM0NGMtODdhOS1kMTUzYmZmZDU0ODQiLCJhaWQiOiIyIiwibmV0Ijoid3MiLCJwYXRoIjoiL29vb28iLCJob3N0IjoidjM2LmhlZHVpYW4ubGluayIsInRscyI6IiJ9
    ss://YWVzLTI1Ni1nY206aVVCMDkyM1JCQQ@154.3.8.151:30067#14-544-US
    trojan://trojan@91.193.58.0:443?allowInsecure=1&sni=wahaha.yingyangkuaixian.dpdns.org&ws=1&wspath=%2525252F#14-546-RELAY
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo3anZISEY1U2FGb2I@78.153.131.96:443#23-564-LT
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTptU1FpdVQ1alIxN255V2djWE9QclRX@77.105.166.12:8594#23-565-FR
    trojan://wb6368@92.243.75.49:2087?allowInsecure=1&sni=hsdgbuys.pages.dev&ws=1&wspath=%2525252F#23-575-RELAY
    vmess://eyJ2IjoiMiIsInBzIjoiMjMtNTc4LVJFTEFZIiwiYWRkIjoiMTcyLjY3LjEzMS4yNyIsInBvcnQiOiIyMDUzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjM1MGUyYjAxLWQ0MTAtNDRhNi05MGJhLTY0ODNmMTA2Mjk3MiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTozNjBlMjFkMjE5NzdkYzEx@185.193.102.7:57456#23-579-FI
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpjdklJODVUclc2bjBPR3lmcEhWUzF1@45.87.175.183:8080#23-580-LT
    trojan://f282b878-8711-45a1-8c69-5564172123c1@aio.zipzap.biz.id:80?allowInsecure=1&sni=aio.zipzap.biz.id&ws=1&wspath=%2525252Faioproxybot%2525252F129.150.49.58-18650#23-582-RELAY
    vmess://eyJ2IjoiMiIsInBzIjoiMjMtNTgzLUNIIiwiYWRkIjoiMTg2LjE5MC4yMTUuMTkzIiwicG9ydCI6IjIyMzI0IiwidHlwZSI6Im5vbmUiLCJpZCI6IjA0NjIxYmFlLWFiMzYtMTFlYy1iOTA5LTAyNDJhYzEyMDAwMiIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiJTI1MjUyRmFpb3Byb3h5Ym90JTI1MjUyRjEyOS4xNTAuNDkuNTgtMTg2NTAiLCJob3N0IjoiYWlvLnppcHphcC5iaXouaWQiLCJ0bHMiOiIifQ==
    trojan://f282b878-8711-45a1-8c69-5564172123c1@aio.zipzap.biz.id:443?allowInsecure=1&sni=aio.zipzap.biz.id&ws=1&wspath=%2525252Faioproxybot%2525252F129.150.49.58-18650#23-585-RELAY
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo3OTA1YTMyYi0wMTJjLTQ3MTEtODllMi03M2I2NzEzZWNhNzU@pr.fastsoonlink.com:40030#23-586-PL
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo0YTJyZml4b3BoZGpmZmE4S1ZBNEFh@beesyar.org:8080#23-603-AE
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpqdnlIUGNQS2xkZk1MWFJHbUwwTmta@81.19.141.45:443#23-611-DE
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo0YTJyZml4b3BoZGpmZmE4S1ZBNEFh@45.87.175.164:8080#23-614-LT
    trojan://blue2024@104.19.172.92:443?allowInsecure=1&sni=td.promote.icu#23-617-RELAY
    trojan://bpb-trojan@104.19.177.234:443?allowInsecure=1&sni=bpb.my79801.com#23-618-RELAY
    trojan://bpb-trojan@104.18.126.124:443?allowInsecure=1&sni=bpb.my79801.com#23-619-RELAY
    trojan://bpb-trojan@104.16.143.191:443?allowInsecure=1&sni=bpb.my79801.com#23-620-RELAY
    trojan://bpb-trojan@104.16.196.91:443?allowInsecure=1&sni=bpb.my79801.com#23-621-RELAY
    trojan://bpb-trojan@190.93.245.14:443?allowInsecure=1&sni=bpb.my79801.com#23-622-RELAY
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpMUThoTGlYNjlWVWxjZmtmTTluZThT@h110vpnch.outlinekeys.net:4248#23-625-CH
    


</details>

### 所有节点
合并节点总数: `154`
[节点链接](https://raw.githubusercontent.com/caijh/TopFreeProxies/master/sub/sub_merge_base64.txt)

### 节点来源
- [clashnode](https://github.com/imyaoxp/clashnode), 节点数量: `154`


## 仓库声明
订阅节点仅作学习交流使用，只是对网络上节点的优选排序，用于查找资料，学习知识，不做任何违法行为。所有资源均来自互联网，仅供大家交流学习使用，出现违法问题概不负责。

