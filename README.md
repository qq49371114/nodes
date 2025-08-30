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
高速节点数量: `35`
<details>
  <summary>展开复制节点</summary>

    trojan://ttfang@193.9.49.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=%2525252FTelegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#05-0002-RELAY
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
    vmess://eyJ2IjoiMiIsInBzIjoiMDgtMDA2My1SRUxBWSIsImFkZCI6InB1YmcuYWMiLCJwb3J0IjoiODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiNTZjODUyYzItOTUxNy00YzEzLWFlMTgtYmYwYmVlNDE3MDZhIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9wcm9maWxlL3RlbGVncmFtQHNzcnN1YiIsImhvc3QiOiJwdWJnLmFjIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDgtMDA2NC1SRUxBWSIsImFkZCI6ImI2MmE5NDhjLWZhYTItNGU4YS1iZjhhLTNmZjMxMjFjODc1YS5hc291bC1hdmEudG9wIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI1ZjcyNmZlMy1kODJlLTRkYTUtYTcxMS04YWYwY2JiMmI2ODIiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2F6dW1hc2UucmVuIiwiaG9zdCI6ImI2MmE5NDhjLWZhYTItNGU4YS1iZjhhLTNmZjMxMjFjODc1YS5hc291bC1hdmEudG9wIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDgtMDA2NS1DTiIsImFkZCI6InY0LmhlZHVpYW4ubGluayIsInBvcnQiOiIzMDgwNCIsInR5cGUiOiJub25lIiwiaWQiOiJjYmIzZjg3Ny1kMWZiLTM0NGMtODdhOS1kMTUzYmZmZDU0ODQiLCJhaWQiOiIyIiwibmV0Ijoid3MiLCJwYXRoIjoiL29vb28iLCJob3N0IjoidjQuaGVkdWlhbi5saW5rIiwidGxzIjoiIn0=
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo5dHFoTWRJclRrZ1E0NlB2aHlBdE1I@switcher-nick-croquet.freesocks.work:443#08-0066-NL
    vmess://eyJ2IjoiMiIsInBzIjoiMDgtMDA2OC1ISyIsImFkZCI6ImhrdC5nb3RvY2hpbmF0b3duLm5ldCIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiI5M2ZiNjlmYy03N2NmLTExZWUtODVlZS1mMjNjOTEzNjlmMmQiLCJhaWQiOiIyIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiJoa3QuZ290b2NoaW5hdG93bi5uZXQiLCJ0bHMiOiIifQ==
    ss://YWVzLTI1Ni1jZmI6cXdlclJFV1ElMjU0MCUyNTQw@p141.panda001.net:4652#08-0069-KR
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@46.183.184.60:989#08-0070-HR
    vmess://eyJ2IjoiMiIsInBzIjoiMDgtMDA3MS1SRUxBWSIsImFkZCI6InRlc3QzLmZsaGEucnUiLCJwb3J0IjoiODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiOWE4MTM0MGQtZjgxYi00Yzc2LThhYmItZjRkMzA1YzUzNWMwIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii85YTgxMzQwZC1mODFiLTRjNzYtOGFiYi1mNGQzMDVjNTM1YzAtdm1lc3MiLCJob3N0IjoidGVzdDMuZmxoYS5ydSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoiMDgtMDA3Mi1DTiIsImFkZCI6IjQ3LjEwNC4xODYuMTMzIiwicG9ydCI6IjUwMDAyIiwidHlwZSI6Im5vbmUiLCJpZCI6IjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoiMDgtMDA3My1DTiIsImFkZCI6InYzNi5oZWR1aWFuLmxpbmsiLCJwb3J0IjoiMzA4MzYiLCJ0eXBlIjoibm9uZSIsImlkIjoiY2JiM2Y4NzctZDFmYi0zNDRjLTg3YTktZDE1M2JmZmQ1NDg0IiwiYWlkIjoiMiIsIm5ldCI6IndzIiwicGF0aCI6Ii9vb29vIiwiaG9zdCI6InYzNi5oZWR1aWFuLmxpbmsiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiMDgtMDA3NC1DTiIsImFkZCI6InYyNC5oZWR1aWFuLmxpbmsiLCJwb3J0IjoiMzA4MjQiLCJ0eXBlIjoibm9uZSIsImlkIjoiY2JiM2Y4NzctZDFmYi0zNDRjLTg3YTktZDE1M2JmZmQ1NDg0IiwiYWlkIjoiMiIsIm5ldCI6IndzIiwicGF0aCI6Ii9vb29vIiwiaG9zdCI6InYyNC5oZWR1aWFuLmxpbmsiLCJ0bHMiOiIifQ==
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpxWHZPN3pZVTdLZWFCME1kN0RRTG93@51.195.119.47:1080#08-0075-FR
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpRQ1hEeHVEbFRUTUQ3anRnSFVqSW9q@193.29.139.227:8080#08-0077-NL
    ss://YWVzLTI1Ni1jZmI6YW1hem9uc2tyMDU@43.203.207.149:443#08-0078-KR
    trojan://28c79056-ccfd-4cc1-93d4-c337cc782e65@89.221.224.94:80?allowInsecure=1&sni=is2-t.sshmax.xyz#08-0080-IS
    ss://YWVzLTI1Ni1jZmI6YW1hem9uc2tyMDU@43.201.47.36:443#08-0081-KRtrojan%2F%2Ftg-fq521free%40198.62.62.67443%3FallowInsecure%3D1%26sni%3Dtorjan.xn--xhq44j.eu.org%26ws%3D1%26wspath%3D%25252F%2306-0057-US
    trojan://c73406e2-1d3a-4724-a691-4d0b7f36cee9@95.164.46.235:443?allowInsecure=1#08-0082-IT
    vmess://eyJ2IjoiMiIsInBzIjoiMDgtMDA4My1SRUxBWSIsImFkZCI6IjEwNC4yMS4yMzcuMTI0IiwicG9ydCI6IjgwIiwidHlwZSI6Im5vbmUiLCJpZCI6ImQzMWMzOWUwLWU2MTQtMTFlZS1iMzMzLTIwNWM2ZDVmNWQ3OCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvP2VkPTIwNDgiLCJob3N0IjoiIiwidGxzIjoiIn0=
    trojan://pjdnqv@15.181.201.80:443?allowInsecure=1&sni=aws-us-dallas-1.f1rocketnode.com#08-0084-US
    trojan://e254ed63-33df-4ca8-a980-7d0d9f510a93@aafrtpfxr.phl01i9zjfegelp.5xfsur8v62.gosdk.xyz:27408?allowInsecure=1&sni=q08m.vgraxiw73s.hasyaf.cn#08-0085-NOWHERE
    trojan://ttfang@166.62.104.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0086-US
    vmess://eyJ2IjoiMiIsInBzIjoiMDgtMDA4Ny1VUyIsImFkZCI6IjM4LjM4LjE4MS4yNTAiLCJwb3J0IjoiMzcwMDIiLCJ0eXBlIjoibm9uZSIsImlkIjoiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwiYWlkIjoiNjQiLCJuZXQiOiJ3cyIsInBhdGgiOiIvcGF0aC8xNTM0MjgxMzMzMDIiLCJob3N0IjoiIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDgtMDA4OC1CRyIsImFkZCI6Ijk1LjE2NC44LjEwNiIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiJjMWViZThjNy1iZGQ5LTRhY2EtYTJmNy0wMWJlYTc5Mjc5YjMiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL3ZtZXNzIiwiaG9zdCI6IiIsInRscyI6IiJ9
    


</details>

### 所有节点
合并节点总数: `28`
[节点链接](https://raw.githubusercontent.com/caijh/TopFreeProxies/master/sub/sub_merge_base64.txt)

### 节点来源
- [clashnode](https://github.com/imyaoxp/clashnode), 节点数量: `28`


## 仓库声明
订阅节点仅作学习交流使用，只是对网络上节点的优选排序，用于查找资料，学习知识，不做任何违法行为。所有资源均来自互联网，仅供大家交流学习使用，出现违法问题概不负责。

