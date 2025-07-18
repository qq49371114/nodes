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

    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMDAxLUpQIiwiYWRkIjoianAtMS5hbmV3c3RhcnQuY3lvdSIsInBvcnQiOiI1MDYxIiwidHlwZSI6Im5vbmUiLCJpZCI6ImIyODhiNTY0LTUyY2ItM2QyNC1hNjBkLWQ3MmQ4ZDZkNjliMCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6ImpwLTEuYW5ld3N0YXJ0LmN5b3UiLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMDA0LU5PV0hFUkUiLCJhZGQiOiJ1czYtMS5hbmV3c3RhcnQuY3lvdSIsInBvcnQiOiI1MDYxIiwidHlwZSI6Im5vbmUiLCJpZCI6ImIyODhiNTY0LTUyY2ItM2QyNC1hNjBkLWQ3MmQ4ZDZkNjliMCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6InVzNi0xLmFuZXdzdGFydC5jeW91IiwidGxzIjoidGxzIn0=
    trojan://88f13c80-9015-3d6e-94be-6129b54b0cfd@gz0slb.aliyuncdn.smp-paymentservices-apple.com:56323?allowInsecure=1&sni=steampipe-partner.akamaized.net#04-005-NOWHERE
    trojan://88f13c80-9015-3d6e-94be-6129b54b0cfd@gz0slb.aliyuncdn.smp-paymentservices-apple.com:56432?allowInsecure=1&sni=steampipe.akamaized.net#04-006-NOWHERE
    trojan://88f13c80-9015-3d6e-94be-6129b54b0cfd@push04.endpoint.smp-paymentservices-apple.com:23452?allowInsecure=1&sni=edge.steam-dns.top.comcast.net#04-007-CN
    trojan://88f13c80-9015-3d6e-94be-6129b54b0cfd@push04.endpoint.smp-paymentservices-apple.com:23453?allowInsecure=1&sni=upos-hz-mirrorakam.akamaized.net#04-008-CN
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTA4LVJFTEFZIiwiYWRkIjoiczMuZGItbGluazAxLnRvcCIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiJkYWE0MjM0MS0zN2Q1LTM2NzgtOWE5Yi01OTliZTEyMDlhYTEiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2RhYmFpLmluMTA0LjI0LjE1OS4xMjMiLCJob3N0IjoiczMuZGItbGluazAxLnRvcCIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTA5LVJFTEFZIiwiYWRkIjoiczIuZGItbGluazAyLnRvcCIsInBvcnQiOiI4ODgwIiwidHlwZSI6Im5vbmUiLCJpZCI6ImRhYTQyMzQxLTM3ZDUtMzY3OC05YTliLTU5OWJlMTIwOWFhMSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvZGFiYWkuaW4xMDQuMjAuNTIuMTI3IiwiaG9zdCI6InMyLmRiLWxpbmswMi50b3AiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTEwLVJFTEFZIiwiYWRkIjoiczQuZGItbGluazAxLnRvcCIsInBvcnQiOiIyMDk1IiwidHlwZSI6Im5vbmUiLCJpZCI6ImRhYTQyMzQxLTM3ZDUtMzY3OC05YTliLTU5OWJlMTIwOWFhMSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvZGFiYWkuaW4xMDQuMjAuOTMuMTI0IiwiaG9zdCI6InM0LmRiLWxpbmswMS50b3AiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTExLVJFTEFZIiwiYWRkIjoiczMuY24tZGIudG9wIiwicG9ydCI6IjgwIiwidHlwZSI6Im5vbmUiLCJpZCI6ImRhYTQyMzQxLTM3ZDUtMzY3OC05YTliLTU5OWJlMTIwOWFhMSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvZGFiYWkuaW4xNzIuNjcuMTAwLjEyNiIsImhvc3QiOiJzMy5jbi1kYi50b3AiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTEyLVJFTEFZIiwiYWRkIjoiczIuZGItbGluazAxLnRvcCIsInBvcnQiOiIyMDg2IiwidHlwZSI6Im5vbmUiLCJpZCI6ImRhYTQyMzQxLTM3ZDUtMzY3OC05YTliLTU5OWJlMTIwOWFhMSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvZGFiYWkuaW4xNzIuNjQuNTkuNzQiLCJob3N0IjoiczIuZGItbGluazAxLnRvcCIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTEzLVJFTEFZIiwiYWRkIjoiczUuY24tZGIudG9wIiwicG9ydCI6IjgwIiwidHlwZSI6Im5vbmUiLCJpZCI6ImRhYTQyMzQxLTM3ZDUtMzY3OC05YTliLTU5OWJlMTIwOWFhMSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvZGFiYWkuaW4xNzIuNjQuMTQuMTcwIiwiaG9zdCI6InM1LmNuLWRiLnRvcCIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTE0LVJFTEFZIiwiYWRkIjoiczIuY24tZGIudG9wIiwicG9ydCI6IjIwODIiLCJ0eXBlIjoibm9uZSIsImlkIjoiZGFhNDIzNDEtMzdkNS0zNjc4LTlhOWItNTk5YmUxMjA5YWExIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9kYWJhaS5pbjEwNC4xNi4yOS4xOTQiLCJob3N0IjoiczIuY24tZGIudG9wIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTE1LU5PV0hFUkUiLCJhZGQiOiIxMi5tYW1hbWFqZC5zaXRlIiwicG9ydCI6IjIzNjEyIiwidHlwZSI6Im5vbmUiLCJpZCI6IjgwZTNkNmM5LTlkM2EtM2QyMS04MTdmLTQ2MTcxYTE5OTZjMiIsImFpZCI6IjIiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6IjEyLm1hbWFtYWpkLnNpdGUiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTE2LUNOIiwiYWRkIjoiMTcubWFtYW1hamQuc2l0ZSIsInBvcnQiOiIyMzYxNyIsInR5cGUiOiJub25lIiwiaWQiOiI4MGUzZDZjOS05ZDNhLTNkMjEtODE3Zi00NjE3MWExOTk2YzIiLCJhaWQiOiIyIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIxNy5tYW1hbWFqZC5zaXRlIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTE3LUNOIiwiYWRkIjoiMTEubWFtYW1hamQuc2l0ZSIsInBvcnQiOiIyMzYxMSIsInR5cGUiOiJub25lIiwiaWQiOiI4MGUzZDZjOS05ZDNhLTNkMjEtODE3Zi00NjE3MWExOTk2YzIiLCJhaWQiOiIyIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIxMS5tYW1hbWFqZC5zaXRlIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTE4LUNOIiwiYWRkIjoiMTkubWFtYW1hamQuc2l0ZSIsInBvcnQiOiIyMzYxOSIsInR5cGUiOiJub25lIiwiaWQiOiI4MGUzZDZjOS05ZDNhLTNkMjEtODE3Zi00NjE3MWExOTk2YzIiLCJhaWQiOiIyIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIxOS5tYW1hbWFqZC5zaXRlIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTE5LUNOIiwiYWRkIjoiMTYubWFtYW1hamQuc2l0ZSIsInBvcnQiOiIyMzYxNiIsInR5cGUiOiJub25lIiwiaWQiOiI4MGUzZDZjOS05ZDNhLTNkMjEtODE3Zi00NjE3MWExOTk2YzIiLCJhaWQiOiIyIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIxNi5tYW1hbWFqZC5zaXRlIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTIwLUNOIiwiYWRkIjoiMTgubWFtYW1hamQuc2l0ZSIsInBvcnQiOiIyMzYxOCIsInR5cGUiOiJub25lIiwiaWQiOiI4MGUzZDZjOS05ZDNhLTNkMjEtODE3Zi00NjE3MWExOTk2YzIiLCJhaWQiOiIyIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIxOC5tYW1hbWFqZC5zaXRlIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTIxLUNOIiwiYWRkIjoiMTUubWFtYW1hamQuc2l0ZSIsInBvcnQiOiIyMzYxNSIsInR5cGUiOiJub25lIiwiaWQiOiI4MGUzZDZjOS05ZDNhLTNkMjEtODE3Zi00NjE3MWExOTk2YzIiLCJhaWQiOiIyIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIxNS5tYW1hbWFqZC5zaXRlIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTIyLU5PV0hFUkUiLCJhZGQiOiI1Lm1hbWFtYWpkLnNpdGUiLCJwb3J0IjoiMjM2MDUiLCJ0eXBlIjoibm9uZSIsImlkIjoiODBlM2Q2YzktOWQzYS0zZDIxLTgxN2YtNDYxNzFhMTk5NmMyIiwiYWlkIjoiMiIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiNS5tYW1hbWFqZC5zaXRlIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTIzLUNOIiwiYWRkIjoiMTMubWFtYW1hamQuc2l0ZSIsInBvcnQiOiIyMzYxMyIsInR5cGUiOiJub25lIiwiaWQiOiI4MGUzZDZjOS05ZDNhLTNkMjEtODE3Zi00NjE3MWExOTk2YzIiLCJhaWQiOiIyIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIxMy5tYW1hbWFqZC5zaXRlIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDQtMTI0LUNOIiwiYWRkIjoiMTQubWFtYW1hamQuc2l0ZSIsInBvcnQiOiIyMzYxNCIsInR5cGUiOiJub25lIiwiaWQiOiI4MGUzZDZjOS05ZDNhLTNkMjEtODE3Zi00NjE3MWExOTk2YzIiLCJhaWQiOiIyIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIxNC5tYW1hbWFqZC5zaXRlIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMTg2LUNOIiwiYWRkIjoiMTgzLjIzNi45Ny4xMDEiLCJwb3J0IjoiMzc3NzciLCJ0eXBlIjoibm9uZSIsImlkIjoiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwiYWlkIjoiNjQiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIxNC5tYW1hbWFqZC5zaXRlIiwidGxzIjoiIn0=
    trojan://d0298536-d670-4045-bbb1-ddd5ea68683e@www.digitalocean.com:443?allowInsecure=1&sni=azadnet-5vk.pages.dev&ws=1&wspath=%2525252Fazadnet-5vk.pages.dev%2525252F%2525253Fed%2525253D2560#05-317-RELAY
    trojan://74260628090146500@stirring-parakeet.shiner427.skin:443?allowInsecure=1#09-359-NL
    trojan://trojan@91.193.58.0:443?allowInsecure=1&sni=wahaha.yingyangkuaixian.dpdns.org&ws=1&wspath=%2525252F#09-365-RELAY
    vmess://eyJ2IjoiMiIsInBzIjoiMDktMzg2LVJVIiwiYWRkIjoid3d3LmxseGxseGwuY2xpY2siLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjI0NmJiZTIxLTE0NTAtNDYxMC1iMTk0LTliMWUwZGJjNWRhMSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvMjQ2YmJlMjEtMTQ1MC00NjEwLWIxOTQtOWIxZTBkYmM1ZGExIiwiaG9zdCI6Ind3dy5sbHhsbHhsLmNsaWNrIiwidGxzIjoidGxzIn0=
    ss://YWVzLTI1Ni1nY206aVVCMDkyM1JCQQ@154.3.8.151:30067#14-435-US
    ss://YWVzLTI1Ni1nY206VEclMjUzQSUyNTQwRW5rZWx0ZV9ub3RpZiUyNTI2JTI1MjZURyUyNTNBJTI1NDBOb3RpZl9DaGF0@152.53.2.128:34045#14-436-AT
    trojan://trojan@109.234.211.66:8443?allowInsecure=1&sni=store.timimi.dpdns.org&ws=1&wspath=%2525252F#14-437-RELAY
    trojan://tg-fq521free@194.76.18.129:443?allowInsecure=1&sni=torjan.xn--xhq44j.eu.org&ws=1&wspath=%2525252F#14-438-KZ
    trojan://tg-fq521free@45.67.215.95:443?allowInsecure=1&sni=torjan.xn--xhq44j.eu.org&ws=1&wspath=%2525252F#14-439-RU
    trojan://tg-fq521free@198.62.62.67:443?allowInsecure=1&sni=torjan.xn--xhq44j.eu.org&ws=1&wspath=%2525252F#14-440-US
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@154.223.21.221:989#23-443-HK
    trojan://telegram-id-v2rayvpnchannel@18.197.77.20:22223?allowInsecure=1&sni=trojan.burgerip.co.uk#23-461-DE
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTptU1FpdVQ1alIxN255V2djWE9QclRX@77.105.166.12:8594#23-491-FR
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpjdklJODVUclc2bjBPR3lmcEhWUzF1@45.87.175.178:8080#23-492-LT
    ss://YWVzLTI1Ni1jZmI6THAyN3JxeUpxNzJiWnNxWA@217.30.10.18:9045#23-493-PL
    trojan://telegram-id-privatevpns@18.197.77.20:22222?allowInsecure=1&sni=trojan.burgerip.co.uk#23-497-DE
    ss://YWVzLTI1Ni1jZmI6WG44aktkbURNMDBJZU8lMjUyNSUyNTIzJTI1MjQlMjUyM2ZKQU10c0VBRVVPcEgvWVdZdFlxREZuVDBTVg@103.186.154.29:38388#23-503-VN
    ss://YWVzLTI1Ni1nY206T0lHR1lHUjAwMlNSR0czMw@156.231.104.13:18003#23-506-JP
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpjNDA2NDFjMWY4OWU3YWNi@147.45.178.200:57456#23-518-DE
    


</details>

### 所有节点
合并节点总数: `144`
[节点链接](https://raw.githubusercontent.com/caijh/TopFreeProxies/master/sub/sub_merge_base64.txt)

### 节点来源
- [clashnode](https://github.com/imyaoxp/clashnode), 节点数量: `144`


## 仓库声明
订阅节点仅作学习交流使用，只是对网络上节点的优选排序，用于查找资料，学习知识，不做任何违法行为。所有资源均来自互联网，仅供大家交流学习使用，出现违法问题概不负责。

