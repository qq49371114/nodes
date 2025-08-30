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
高速节点数量: `34`
<details>
  <summary>展开复制节点</summary>

    trojan://ttfang@185.193.30.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=%2525252FTelegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#05-0003-RELAY
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDAwNC1SRUxBWSIsImFkZCI6ImxpbnV4LmRvIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiIyZmJlNDFkYi0wNzk3LTQ0ZjYtYTNlYi05YzY4MGU1ZjA5Y2UiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLzJmYmU0MWRiLTA3OTctNDRmNi1hM2ViLTljNjgwZTVmMDljZS12bSIsImhvc3QiOiJsaW51eC5kbyIsInRscyI6InRscyJ9
    trojan://ttfang@86.38.214.216:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=%2525252F%2525252FTelegram#05-0005-RELAY
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDAyMS1FUyIsImFkZCI6IjE4NS4yMzYuMjYuMTExIiwicG9ydCI6IjMyMDIwIiwidHlwZSI6Im5vbmUiLCJpZCI6Ijc4YjRmYjU3LTM5ZDctNGU5ZC1kZDM4LWM5YTM4MzIyYmNiMiIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiJTI1MjUyRiUyNTI1MkZUZWxlZ3JhbSIsImhvc3QiOiJ0dGZhbmcuZmFuZ2UubWUiLCJ0bHMiOiIifQ==
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpxc2NhdkY1VXZpSUwtOFYtRTRyYUJB@91.84.104.133:2222#05-0024-NL
    trojan://tg-fq521free@194.76.18.129:443?allowInsecure=1&sni=torjan.xn--xhq44j.eu.org&ws=1&wspath=%2525252F#06-0032-KZ
    trojan://ttfang@86.38.214.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=%2525252FTelegramU0001F1E8U0001F1F3#06-0035-RELAY
    trojan://tg-fq521free@45.67.215.95:443?allowInsecure=1&sni=torjan.xn--xhq44j.eu.org&ws=1&wspath=%2525252F#06-0048-RU
    trojan://tg-fq521free@216.24.57.30:443?allowInsecure=1&sni=torjan.xn--xhq44j.eu.org&ws=1&wspath=%2525252F#06-0058-US
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpOazlhc2dsRHpIemprdFZ6VGt2aGFB@arxfw2b78fi2q9hzylhn.freesocks.work:443#08-0062-VN
    vmess://eyJ2IjoiMiIsInBzIjoiMDgtMDA2My1DTiIsImFkZCI6InY0LmhlZHVpYW4ubGluayIsInBvcnQiOiIzMDgwNCIsInR5cGUiOiJub25lIiwiaWQiOiJjYmIzZjg3Ny1kMWZiLTM0NGMtODdhOS1kMTUzYmZmZDU0ODQiLCJhaWQiOiIyIiwibmV0Ijoid3MiLCJwYXRoIjoiL29vb28iLCJob3N0IjoidjQuaGVkdWlhbi5saW5rIiwidGxzIjoiIn0=
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo5dHFoTWRJclRrZ1E0NlB2aHlBdE1I@switcher-nick-croquet.freesocks.work:443#08-0064-NL
    vmess://eyJ2IjoiMiIsInBzIjoiMDgtMDA2NS1SRUxBWSIsImFkZCI6ImI2MmE5NDhjLWZhYTItNGU4YS1iZjhhLTNmZjMxMjFjODc1YS5hc291bC1hdmEudG9wIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI1ZjcyNmZlMy1kODJlLTRkYTUtYTcxMS04YWYwY2JiMmI2ODIiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2F6dW1hc2UucmVuIiwiaG9zdCI6ImI2MmE5NDhjLWZhYTItNGU4YS1iZjhhLTNmZjMxMjFjODc1YS5hc291bC1hdmEudG9wIiwidGxzIjoidGxzIn0=
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@46.183.184.60:989#08-0067-HR
    vmess://eyJ2IjoiMiIsInBzIjoiMDgtMDA2OC1DTiIsImFkZCI6InYzNi5oZWR1aWFuLmxpbmsiLCJwb3J0IjoiMzA4MzYiLCJ0eXBlIjoibm9uZSIsImlkIjoiY2JiM2Y4NzctZDFmYi0zNDRjLTg3YTktZDE1M2JmZmQ1NDg0IiwiYWlkIjoiMiIsIm5ldCI6IndzIiwicGF0aCI6Ii9vb29vIiwiaG9zdCI6InYzNi5oZWR1aWFuLmxpbmsiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiMDgtMDA2OS1DTiIsImFkZCI6InY4LmhlZHVpYW4ubGluayIsInBvcnQiOiIzMDgwOCIsInR5cGUiOiJub25lIiwiaWQiOiJjYmIzZjg3Ny1kMWZiLTM0NGMtODdhOS1kMTUzYmZmZDU0ODQiLCJhaWQiOiIyIiwibmV0Ijoid3MiLCJwYXRoIjoiL29vb28iLCJob3N0IjoidjguaGVkdWlhbi5saW5rIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDgtMDA3MC1DTiIsImFkZCI6IjQ3LjEwNC4xODYuMTMzIiwicG9ydCI6IjUwMDAyIiwidHlwZSI6Im5vbmUiLCJpZCI6IjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoiMDgtMDA3MS1DTiIsImFkZCI6InYzNS5oZWR1aWFuLmxpbmsiLCJwb3J0IjoiMzA4MzUiLCJ0eXBlIjoibm9uZSIsImlkIjoiY2JiM2Y4NzctZDFmYi0zNDRjLTg3YTktZDE1M2JmZmQ1NDg0IiwiYWlkIjoiMiIsIm5ldCI6IndzIiwicGF0aCI6Ii9vb29vIiwiaG9zdCI6InYzNS5oZWR1aWFuLmxpbmsiLCJ0bHMiOiIifQ==
    ss://YWVzLTI1Ni1jZmI6cXdlclJFV1ElMjU0MCUyNTQw@p141.panda001.net:4652#08-0072-KR
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@38.165.233.93:989#08-0073-PY
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpKSWhONnJCS2thRWJvTE5YVlN2NXJx@ca225.vpnbook.com:80#08-0074-CAtrojan%2F%2Fttfang%40193.9.49.1942096%3FallowInsecure%3D1%26sni%3Dttfang.fange.me%26ws%3D1%26wspath%3D%25252FTelegram%2525F0%25259F%252587%2525A8%2525F0%25259F%252587%2525B3%2305-0002-RELAY
    vmess://eyJ2IjoiMiIsInBzIjoiMDgtMDA3NS1OT1dIRVJFIiwiYWRkIjoiMmMyMjI3ZTEtc3V0ajQwLXQ5MDdjci0xYzFtci5jdS5wbGViYWkubmV0IiwicG9ydCI6IjUyMjkiLCJ0eXBlIjoibm9uZSIsImlkIjoiYTEyNjQwZDAtZTJhZC0xMWVmLThmNWItZjIzYzkxM2M4ZDJiIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvb29vbyIsImhvc3QiOiJ2MzUuaGVkdWlhbi5saW5rIiwidGxzIjoiIn0=
    trojan://e254ed63-33df-4ca8-a980-7d0d9f510a93@aafrtpfxr.krl01i9zjfegelp.5xfsur8v62.gosdk.xyz:46668?allowInsecure=1&sni=q08m.vgraxiw73s.hasyaf.cn#08-0076-NOWHERE
    vmess://eyJ2IjoiMiIsInBzIjoiMDgtMDA3Ny1KUCIsImFkZCI6IjE1Mi42OS4xOTcuNjAiLCJwb3J0IjoiMTA2OSIsInR5cGUiOiJub25lIiwiaWQiOiJhYzhlMjZmZS04MTUwLTRiNjAtYWU2NC04MmZjNzdlYmEyY2YiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiMDgtMDA3OS1OT1dIRVJFIiwiYWRkIjoiNWE0dTA0LmEzYjV3eS54eXoiLCJwb3J0IjoiMzY4MjEiLCJ0eXBlIjoibm9uZSIsImlkIjoiMzAxNmJlMDYtMmY5MS00YjhmLTllNmEtYmQ1NWYyYzU1NjEwIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiNWE0dTA0LmEzYjV3eS54eXoiLCJ0bHMiOiJ0bHMifQ==
    ss://YWVzLTI1Ni1jZmI6cXdlclJFV1ElMjU0MCUyNTQw@p232.panda004.net:51472#08-0080-KRtrojan%2F%2Ftg-fq521free%40198.62.62.67443%3FallowInsecure%3D1%26sni%3Dtorjan.xn--xhq44j.eu.org%26ws%3D1%26wspath%3D%25252F%2306-0057-US
    vmess://eyJ2IjoiMiIsInBzIjoiMDgtMDA4MS1SRUxBWSIsImFkZCI6IjE3Mi42Ny4yMjkuMzkiLCJwb3J0IjoiMjA4NiIsInR5cGUiOiJub25lIiwiaWQiOiI1OGZlMTU0Mi01MjkwLTQwYWQtODE1YS03NzcwN2E4MWFmZTUiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL0lPZWJoTE1obDFDVGJGSGJMOTVteWZSWDIiLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDgtMDA4Mi1SRUxBWSIsImFkZCI6IjE5NS44NS41OS4yMSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiMDNmY2M2MTgtYjkzZC02Nzk2LTZhZWQtOGEzOGM5NzVkNTgxIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9uaW5hLmJvbmQvbGlua3Z3cyIsImhvc3QiOiIiLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiMDgtMDA4NC1GUiIsImFkZCI6IjQ1LjkyLjIxOC4yNDkiLCJwb3J0IjoiMjk5MjgiLCJ0eXBlIjoibm9uZSIsImlkIjoiY2ViMjUxZDQtMjc3ZC00ZjQzLWIzODEtYzUxMDMxNzJhOTkwIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9jZWIyNTFkNCIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    trojan://58b489f2-58f3-41f2-bc5c-76bba7618468@94.131.117.240:443?allowInsecure=1#08-0086-ES
    vmess://eyJ2IjoiMiIsInBzIjoiMDgtMDA4OC1SRUxBWSIsImFkZCI6IjEwNC4xOS40My45NCIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiI1ZDgxNWRjNi1hNzk1LTQ0ZmYtYWViNi03ZWUxNmE3YTFjNTciLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL25lZWRheT9lZD0yMDQ4IiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoiMDgtMDA4OS1SRUxBWSIsImFkZCI6InJhazFkaW5nLjg5MDYwMDA0Lnh5eiIsInBvcnQiOiIyMDgzIiwidHlwZSI6Im5vbmUiLCJpZCI6Ijc1ZDk2MzY1LTEyMjktNGZjNC1kYmRhLTg1NTcxN2Y4NzZjZiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6InJhazFkaW5nLjg5MDYwMDA0Lnh5eiIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoiMDgtMDA5MC1SRUxBWSIsImFkZCI6IjEwNC4xNi40MC4xNTQiLCJwb3J0IjoiMjA4MiIsInR5cGUiOiJub25lIiwiaWQiOiIzN2Q4Yzk5Mi02MTcwLTQwZTktODlkZC1lOWEyNjQ3MjIzZjgiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzP2VkPTIwNDgiLCJob3N0IjoiIiwidGxzIjoiIn0=
    


</details>

### 所有节点
合并节点总数: `38`
[节点链接](https://raw.githubusercontent.com/caijh/TopFreeProxies/master/sub/sub_merge_base64.txt)

### 节点来源
- [clashnode](https://github.com/imyaoxp/clashnode), 节点数量: `38`


## 仓库声明
订阅节点仅作学习交流使用，只是对网络上节点的优选排序，用于查找资料，学习知识，不做任何违法行为。所有资源均来自互联网，仅供大家交流学习使用，出现违法问题概不负责。

