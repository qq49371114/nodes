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
高速节点数量: `56`
<details>
  <summary>展开复制节点</summary>

    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMDAxLUpQIiwiYWRkIjoianAtMS5hbmV3c3RhcnQuY3lvdSIsInBvcnQiOiI1MDYxIiwidHlwZSI6Im5vbmUiLCJpZCI6IjhmMWM4OWIwLTE4ZjEtMzM0NS1iMjZjLTIwNzYzYzhkODhhNiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6ImpwLTEuYW5ld3N0YXJ0LmN5b3UiLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMDA0LU5PV0hFUkUiLCJhZGQiOiJ1czYtMS5hbmV3c3RhcnQuY3lvdSIsInBvcnQiOiI1MDYxIiwidHlwZSI6Im5vbmUiLCJpZCI6IjhmMWM4OWIwLTE4ZjEtMzM0NS1iMjZjLTIwNzYzYzhkODhhNiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6InVzNi0xLmFuZXdzdGFydC5jeW91IiwidGxzIjoidGxzIn0=
    trojan://44384381-9f1a-3e76-89c9-161d3a88a02f@gz0slb.aliyuncdn.smp-paymentservices-apple.com:56323?allowInsecure=1&sni=edge.steam-dns.top.comcast.net#04-005-NOWHERE
    trojan://44384381-9f1a-3e76-89c9-161d3a88a02f@gz0slb.aliyuncdn.smp-paymentservices-apple.com:56432?allowInsecure=1&sni=fastly.cdn.steampipe.steamcontent.com#04-006-NOWHERE
    trojan://44384381-9f1a-3e76-89c9-161d3a88a02f@push04.endpoint.smp-paymentservices-apple.com:23452?allowInsecure=1&sni=www.microsoft365.com#04-007-CN
    trojan://44384381-9f1a-3e76-89c9-161d3a88a02f@push04.endpoint.smp-paymentservices-apple.com:23453?allowInsecure=1&sni=origin-a.akamaihd.net#04-008-CN
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTA4LVJFTEFZIiwiYWRkIjoiczIuY24tZGIudG9wIiwicG9ydCI6IjIwOTUiLCJ0eXBlIjoibm9uZSIsImlkIjoiMGU4OGRiYjktOWNmMy0zZjBiLThhNGEtNDA2Njg4MDBmZGI0IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9kYWJhaS5pbjEwNC4yNS4yMy4zOSIsImhvc3QiOiJzMi5jbi1kYi50b3AiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTA5LVJFTEFZIiwiYWRkIjoiczIuZGItbGluazAyLnRvcCIsInBvcnQiOiIyMDg2IiwidHlwZSI6Im5vbmUiLCJpZCI6IjBlODhkYmI5LTljZjMtM2YwYi04YTRhLTQwNjY4ODAwZmRiNCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvZGFiYWkuaW4xMDQuMjAuMTg4LjcyIiwiaG9zdCI6InMyLmRiLWxpbmswMi50b3AiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTEwLVJFTEFZIiwiYWRkIjoiczQuZGItbGluazAxLnRvcCIsInBvcnQiOiIyMDk1IiwidHlwZSI6Im5vbmUiLCJpZCI6IjBlODhkYmI5LTljZjMtM2YwYi04YTRhLTQwNjY4ODAwZmRiNCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvZGFiYWkuaW4xMDQuMjUuMjE3LjE1NCIsImhvc3QiOiJzNC5kYi1saW5rMDEudG9wIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTExLVJFTEFZIiwiYWRkIjoiczEuZGItbGluazAxLnRvcCIsInBvcnQiOiI4ODgwIiwidHlwZSI6Im5vbmUiLCJpZCI6IjBlODhkYmI5LTljZjMtM2YwYi04YTRhLTQwNjY4ODAwZmRiNCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvZGFiYWkuaW4xMDQuMTYuMTQzLjQiLCJob3N0IjoiczEuZGItbGluazAxLnRvcCIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTEyLVJFTEFZIiwiYWRkIjoiczUuY24tZGIudG9wIiwicG9ydCI6IjIwODYiLCJ0eXBlIjoibm9uZSIsImlkIjoiMGU4OGRiYjktOWNmMy0zZjBiLThhNGEtNDA2Njg4MDBmZGI0IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9kYWJhaS5pbjE3Mi42NC4zNS45NCIsImhvc3QiOiJzNS5jbi1kYi50b3AiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTEzLVJFTEFZIiwiYWRkIjoiczQuZGItbGluazAyLnRvcCIsInBvcnQiOiIyMDUyIiwidHlwZSI6Im5vbmUiLCJpZCI6IjBlODhkYmI5LTljZjMtM2YwYi04YTRhLTQwNjY4ODAwZmRiNCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvZGFiYWkuaW4xNzIuNjQuMzcuMTcyIiwiaG9zdCI6InM0LmRiLWxpbmswMi50b3AiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTE0LVJFTEFZIiwiYWRkIjoiczUuY24tZGIudG9wIiwicG9ydCI6IjIwNTIiLCJ0eXBlIjoibm9uZSIsImlkIjoiMGU4OGRiYjktOWNmMy0zZjBiLThhNGEtNDA2Njg4MDBmZGI0IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9kYWJhaS5pbjE3Mi42Ny4xMDkuMiIsImhvc3QiOiJzNS5jbi1kYi50b3AiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTE1LU5PV0hFUkUiLCJhZGQiOiIxMi5tYW1hbWFqZC5zaXRlIiwicG9ydCI6IjIzNjEyIiwidHlwZSI6Im5vbmUiLCJpZCI6IjFhN2ZiYWEwLTg1MmItMzRhMC1iMjhlLWVlNGU0NjQzMWQ1NSIsImFpZCI6IjIiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6IjEyLm1hbWFtYWpkLnNpdGUiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTE2LUNOIiwiYWRkIjoiMTcubWFtYW1hamQuc2l0ZSIsInBvcnQiOiIyMzYxNyIsInR5cGUiOiJub25lIiwiaWQiOiIxYTdmYmFhMC04NTJiLTM0YTAtYjI4ZS1lZTRlNDY0MzFkNTUiLCJhaWQiOiIyIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIxNy5tYW1hbWFqZC5zaXRlIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTE3LUNOIiwiYWRkIjoiMTEubWFtYW1hamQuc2l0ZSIsInBvcnQiOiIyMzYxMSIsInR5cGUiOiJub25lIiwiaWQiOiIxYTdmYmFhMC04NTJiLTM0YTAtYjI4ZS1lZTRlNDY0MzFkNTUiLCJhaWQiOiIyIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIxMS5tYW1hbWFqZC5zaXRlIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTE4LUNOIiwiYWRkIjoiMTkubWFtYW1hamQuc2l0ZSIsInBvcnQiOiIyMzYxOSIsInR5cGUiOiJub25lIiwiaWQiOiIxYTdmYmFhMC04NTJiLTM0YTAtYjI4ZS1lZTRlNDY0MzFkNTUiLCJhaWQiOiIyIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIxOS5tYW1hbWFqZC5zaXRlIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTE5LUNOIiwiYWRkIjoiMTYubWFtYW1hamQuc2l0ZSIsInBvcnQiOiIyMzYxNiIsInR5cGUiOiJub25lIiwiaWQiOiIxYTdmYmFhMC04NTJiLTM0YTAtYjI4ZS1lZTRlNDY0MzFkNTUiLCJhaWQiOiIyIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIxNi5tYW1hbWFqZC5zaXRlIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTIwLUNOIiwiYWRkIjoiMTgubWFtYW1hamQuc2l0ZSIsInBvcnQiOiIyMzYxOCIsInR5cGUiOiJub25lIiwiaWQiOiIxYTdmYmFhMC04NTJiLTM0YTAtYjI4ZS1lZTRlNDY0MzFkNTUiLCJhaWQiOiIyIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIxOC5tYW1hbWFqZC5zaXRlIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTIxLU5PV0hFUkUiLCJhZGQiOiIxNS5tYW1hbWFqZC5zaXRlIiwicG9ydCI6IjIzNjE1IiwidHlwZSI6Im5vbmUiLCJpZCI6IjFhN2ZiYWEwLTg1MmItMzRhMC1iMjhlLWVlNGU0NjQzMWQ1NSIsImFpZCI6IjIiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6IjE1Lm1hbWFtYWpkLnNpdGUiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTIyLU5PV0hFUkUiLCJhZGQiOiI1Lm1hbWFtYWpkLnNpdGUiLCJwb3J0IjoiMjM2MDUiLCJ0eXBlIjoibm9uZSIsImlkIjoiMWE3ZmJhYTAtODUyYi0zNGEwLWIyOGUtZWU0ZTQ2NDMxZDU1IiwiYWlkIjoiMiIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiNS5tYW1hbWFqZC5zaXRlIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTIzLUNOIiwiYWRkIjoiMTMubWFtYW1hamQuc2l0ZSIsInBvcnQiOiIyMzYxMyIsInR5cGUiOiJub25lIiwiaWQiOiIxYTdmYmFhMC04NTJiLTM0YTAtYjI4ZS1lZTRlNDY0MzFkNTUiLCJhaWQiOiIyIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIxMy5tYW1hbWFqZC5zaXRlIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTI0LUNOIiwiYWRkIjoiMTQubWFtYW1hamQuc2l0ZSIsInBvcnQiOiIyMzYxNCIsInR5cGUiOiJub25lIiwiaWQiOiIxYTdmYmFhMC04NTJiLTM0YTAtYjI4ZS1lZTRlNDY0MzFkNTUiLCJhaWQiOiIyIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIxNC5tYW1hbWFqZC5zaXRlIiwidGxzIjoiIn0=
    trojan://tg-fq521free@216.24.57.30:443?allowInsecure=1&sni=torjan.xn--xhq44j.eu.org&ws=1&wspath=%2525252F#05-136-US
    trojan://tg-fq521free@45.67.215.95:443?allowInsecure=1&sni=torjan.xn--xhq44j.eu.org&ws=1&wspath=%2525252F#05-137-RU
    trojan://Aimer@112.162.240.23:18077?allowInsecure=1&sni=epgz.aimercc.filegear-sg.me&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#05-151-KR
    trojan://Aimer@119.194.220.146:50000?allowInsecure=1&sni=epgz.aimercc.filegear-sg.me&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#05-153-KR
    trojan://Aimer@14.50.215.31:12411?allowInsecure=1&sni=epgz.aimercc.filegear-sg.me&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#05-154-KR
    trojan://Aimer@211.57.29.229:31017?allowInsecure=1&sni=epgz.aimercc.filegear-sg.me&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#05-155-KR
    trojan://Aimer@38.47.116.206:443?allowInsecure=1&sni=epgz.aimercc.filegear-sg.me&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#05-156-US
    trojan://Aimer@45.156.24.225:443?allowInsecure=1&sni=epgz.aimercc.filegear-sg.me&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#05-157-US
    trojan://Aimer@77.232.140.114:2053?allowInsecure=1&sni=epgz.aimercc.filegear-sg.me&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#05-164-RELAY
    trojan://Aimer@theo.ns.cloudflare.com:443?allowInsecure=1&sni=epgz.aimercc.filegear-sg.me&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#05-165-RELAY
    trojan://Aimer@49.51.179.33:443?allowInsecure=1&sni=epgz.aimercc.filegear-sg.me&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#05-166-US
    trojan://Aimer@108.165.152.225:2083?allowInsecure=1&sni=epgz.aimercc.filegear-sg.me&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#05-168-RELAY
    trojan://Aimer@103.76.85.91:30002?allowInsecure=1&sni=epgz.aimercc.filegear-sg.me&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#05-169-JP
    trojan://Aimer@188.164.159.248:2053?allowInsecure=1&sni=epgz.aimercc.filegear-sg.me&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#05-170-RELAY
    trojan://Aimer@121.140.226.21:12245?allowInsecure=1&sni=epgz.aimercc.filegear-sg.me&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#05-171-KR
    trojan://Aimer@154.197.64.166:2053?allowInsecure=1&sni=epgz.aimercc.filegear-sg.me&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#05-172-RELAY
    trojan://Aimer@188.164.159.25:2053?allowInsecure=1&sni=epgz.aimercc.filegear-sg.me&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#05-173-RELAY
    trojan://Aimer@27.50.49.61:2096?allowInsecure=1&sni=epgz.aimercc.filegear-sg.me&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#05-174-RELAY
    trojan://Aimer@77.232.140.101:2053?allowInsecure=1&sni=epgz.aimercc.filegear-sg.me&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#05-175-RELAY
    trojan://74260628090146500@stirring-parakeet.shiner427.skin:443?allowInsecure=1#09-289-NOWHERE
    trojan://Aimer@92.243.74.180:8443?allowInsecure=1&sni=tyep.esslh.filegear-sg.me&ws=1&wspath=%2525252F#09-399-RELAY
    vmess://eyJ2IjoiMiIsInBzIjoiMTQtNTQ3LUNOIiwiYWRkIjoidjQuaGVkdWlhbi5saW5rIiwicG9ydCI6IjMwODA0IiwidHlwZSI6Im5vbmUiLCJpZCI6ImNiYjNmODc3LWQxZmItMzQ0Yy04N2E5LWQxNTNiZmZkNTQ4NCIsImFpZCI6IjIiLCJuZXQiOiJ3cyIsInBhdGgiOiIvb29vbyIsImhvc3QiOiJ2NC5oZWR1aWFuLmxpbmsiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiMTQtNTQ5LVJFTEFZIiwiYWRkIjoiYjYyYTk0OGMtZmFhMi00ZThhLWJmOGEtM2ZmMzEyMWM4NzVhLmFzb3VsLWF2YS50b3AiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjVmNzI2ZmUzLWQ4MmUtNGRhNS1hNzExLThhZjBjYmIyYjY4MiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvYXp1bWFzZS5yZW4iLCJob3N0IjoiYjYyYTk0OGMtZmFhMi00ZThhLWJmOGEtM2ZmMzEyMWM4NzVhLmFzb3VsLWF2YS50b3AiLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiMTQtNTUwLUNOIiwiYWRkIjoidjI5LmhlZHVpYW4ubGluayIsInBvcnQiOiIzMDgyOSIsInR5cGUiOiJub25lIiwiaWQiOiJjYmIzZjg3Ny1kMWZiLTM0NGMtODdhOS1kMTUzYmZmZDU0ODQiLCJhaWQiOiIyIiwibmV0Ijoid3MiLCJwYXRoIjoiL29vb28iLCJob3N0IjoidjI5LmhlZHVpYW4ubGluayIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoiMTQtNTUxLUNOIiwiYWRkIjoidjI0LmhlZHVpYW4ubGluayIsInBvcnQiOiIzMDgyNCIsInR5cGUiOiJub25lIiwiaWQiOiJjYmIzZjg3Ny1kMWZiLTM0NGMtODdhOS1kMTUzYmZmZDU0ODQiLCJhaWQiOiIyIiwibmV0Ijoid3MiLCJwYXRoIjoiL29vb28iLCJob3N0IjoidjI0LmhlZHVpYW4ubGluayIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoiMTQtNTUyLUNOIiwiYWRkIjoidjguaGVkdWlhbi5saW5rIiwicG9ydCI6IjMwODA4IiwidHlwZSI6Im5vbmUiLCJpZCI6ImNiYjNmODc3LWQxZmItMzQ0Yy04N2E5LWQxNTNiZmZkNTQ4NCIsImFpZCI6IjIiLCJuZXQiOiJ3cyIsInBhdGgiOiIvb29vbyIsImhvc3QiOiJ2OC5oZWR1aWFuLmxpbmsiLCJ0bHMiOiIifQ==
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@38.54.57.90:989#14-553-BR
    trojan://trojan@91.193.58.0:443?allowInsecure=1&sni=wahaha.yingyangkuaixian.dpdns.org&ws=1&wspath=%2525252F#14-554-RELAY
    ss://YWVzLTI1Ni1nY206R2p2M3QwV0RZMTdIVWFrdyUyNTJCMkRwZUElMjUzRCUyNTNE@iepl.huli168.com:17273#14-555-NOWHERE
    ss://YWVzLTI1Ni1jZmI6cXdlclJFV1ElMjU0MCUyNTQw@p141.panda001.net:4652#14-557-KR
    vmess://eyJ2IjoiMiIsInBzIjoiMTQtNTU4LUNOIiwiYWRkIjoiNDcuMTA0LjE4Ni4xMzMiLCJwb3J0IjoiNTAwMDIiLCJ0eXBlIjoibm9uZSIsImlkIjoiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@37.19.203.147:989#14-559-BG
    


</details>

### 所有节点
合并节点总数: `137`
[节点链接](https://raw.githubusercontent.com/caijh/TopFreeProxies/master/sub/sub_merge_base64.txt)

### 节点来源
- [clashnode](https://github.com/imyaoxp/clashnode), 节点数量: `137`


## 仓库声明
订阅节点仅作学习交流使用，只是对网络上节点的优选排序，用于查找资料，学习知识，不做任何违法行为。所有资源均来自互联网，仅供大家交流学习使用，出现违法问题概不负责。

