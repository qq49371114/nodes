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
高速节点数量: `27`
<details>
  <summary>展开复制节点</summary>

    trojan://f282b878-8711-45a1-8c69-5564172123c1@104.21.72.109:443?allowInsecure=1&sni=vpn.stupidworld.web.id&ws=1&wspath=%2525252FStupid-World%2525252F103.106.228.126-2053#05-0001-RELAY
    ss://YWVzLTI1Ni1jZmI6YW1hem9uc2tyMDU@18.195.55.29:443#05-0003-DE
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDAxNC1SRUxBWSIsImFkZCI6Ind3dy5zcGVlZHRlc3QubmV0IiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJiN2FjZjQ0Zi0zYzNhLTQzMGMtOGVkMC1mYjY0Y2NjOWExM2EiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2xpbmt2a3dzcyIsImhvc3QiOiJ3d3cuc3BlZWR0ZXN0Lm5ldCIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDAxNy1SRUxBWSIsImFkZCI6IjE3Mi42Ni4zLjIxMSIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiJiZDhmNGMzYS1iNTVhLTRhNTUtYTRiZS1kMmVhZDRhNGM2NmEiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2luZGV4Lmh0bWwiLCJob3N0IjoiIiwidGxzIjoiIn0=
    trojan://tg-fq521free@194.76.18.129:443?allowInsecure=1&sni=torjan.xn--xhq44j.eu.org&ws=1&wspath=%2525252F#06-0026-KZ
    trojan://ttfang@86.38.214.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=%2525252FTelegramU0001F1E8U0001F1F3#06-0029-RELAY
    trojan://tg-fq521free@45.67.215.95:443?allowInsecure=1&sni=torjan.xn--xhq44j.eu.org&ws=1&wspath=%2525252F#06-0042-RU
    trojan://tg-fq521free@216.24.57.30:443?allowInsecure=1&sni=torjan.xn--xhq44j.eu.org&ws=1&wspath=%2525252F#06-0052-US
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpOazlhc2dsRHpIemprdFZ6VGt2aGFB@arxfw2b78fi2q9hzylhn.freesocks.work:443#08-0055-VN
    vmess://eyJ2IjoiMiIsInBzIjoiMDgtMDA1Ni1SRUxBWSIsImFkZCI6ImI2MmE5NDhjLWZhYTItNGU4YS1iZjhhLTNmZjMxMjFjODc1YS5hc291bC1hdmEudG9wIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI1ZjcyNmZlMy1kODJlLTRkYTUtYTcxMS04YWYwY2JiMmI2ODIiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2F6dW1hc2UucmVuIiwiaG9zdCI6ImI2MmE5NDhjLWZhYTItNGU4YS1iZjhhLTNmZjMxMjFjODc1YS5hc291bC1hdmEudG9wIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDgtMDA1Ny1DTiIsImFkZCI6InYzNi5oZWR1aWFuLmxpbmsiLCJwb3J0IjoiMzA4MzYiLCJ0eXBlIjoibm9uZSIsImlkIjoiY2JiM2Y4NzctZDFmYi0zNDRjLTg3YTktZDE1M2JmZmQ1NDg0IiwiYWlkIjoiMiIsIm5ldCI6IndzIiwicGF0aCI6Ii9vb29vIiwiaG9zdCI6InYzNi5oZWR1aWFuLmxpbmsiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiMDgtMDA1OC1DTiIsImFkZCI6InY0LmhlZHVpYW4ubGluayIsInBvcnQiOiIzMDgwNCIsInR5cGUiOiJub25lIiwiaWQiOiJjYmIzZjg3Ny1kMWZiLTM0NGMtODdhOS1kMTUzYmZmZDU0ODQiLCJhaWQiOiIyIiwibmV0Ijoid3MiLCJwYXRoIjoiL29vb28iLCJob3N0IjoidjQuaGVkdWlhbi5saW5rIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDgtMDA1OS1SRUxBWSIsImFkZCI6InB1YmcuYWMiLCJwb3J0IjoiODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiNTZjODUyYzItOTUxNy00YzEzLWFlMTgtYmYwYmVlNDE3MDZhIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9wcm9maWxlL3RlbGVncmFtQHNzcnN1YiIsImhvc3QiOiJwdWJnLmFjIiwidGxzIjoiIn0=
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo5dHFoTWRJclRrZ1E0NlB2aHlBdE1I@switcher-nick-croquet.freesocks.work:443#08-0061-NL
    vmess://eyJ2IjoiMiIsInBzIjoiMDgtMDA2Mi1ISyIsImFkZCI6ImhrdC5nb3RvY2hpbmF0b3duLm5ldCIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiI5M2ZiNjlmYy03N2NmLTExZWUtODVlZS1mMjNjOTEzNjlmMmQiLCJhaWQiOiIyIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiJoa3QuZ290b2NoaW5hdG93bi5uZXQiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiMDgtMDA2My1SRUxBWSIsImFkZCI6InRlc3QzLmZsaGEucnUiLCJwb3J0IjoiODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiOWE4MTM0MGQtZjgxYi00Yzc2LThhYmItZjRkMzA1YzUzNWMwIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii85YTgxMzQwZC1mODFiLTRjNzYtOGFiYi1mNGQzMDVjNTM1YzAtdm1lc3MiLCJob3N0IjoidGVzdDMuZmxoYS5ydSIsInRscyI6IiJ9
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@46.183.184.60:989#08-0066-HR
    vmess://eyJ2IjoiMiIsInBzIjoiMDgtMDA2Ny1VUyIsImFkZCI6InZjLmZseS5kZXYiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjM1Mzc5MjE5LTY1MzUtNGYyZS1hNGZlLTNlNDRmNjFlMGVlZSIsImFpZCI6IjMyIiwibmV0Ijoid3MiLCJwYXRoIjoiL3ZjIiwiaG9zdCI6InZjLmZseS5kZXYiLCJ0bHMiOiJ0bHMifQ==
    ss://YWVzLTEyOC1nY206c2hhZG93c29ja3M@uk-dc1.yangon.club:443#08-0068-GB
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpvWklvQTY5UTh5aGNRVjhrYTNQYTNB@45.87.175.35:8080#08-0069-LT
    ss://YWVzLTEyOC1nY206WWMyQ3RySXo4TA@103.124.107.178:16899#08-0070-US
    ss://YWVzLTI1Ni1jZmI6YW1hem9uc2tyMDU@3.38.162.154:443#08-0071-KRtrojan%2F%2Ftg-fq521free%40198.62.62.67443%3FallowInsecure%3D1%26sni%3Dtorjan.xn--xhq44j.eu.org%26ws%3D1%26wspath%3D%25252F%2306-0051-US
    trojan://dba20dcb635e430fa4d3bfc303a149d2@104.16.192.157:443?allowInsecure=1&sni=jobscareerfortoday.com#08-0073-RELAY
    vmess://eyJ2IjoiMiIsInBzIjoiMDgtMDA3NS1SRUxBWSIsImFkZCI6IjE4NS4xNDYuMTczLjEyOSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiZjU4NGRlMTUtMjAzNC00MTcwLWE3MjMtZjQ4YzJiYWU1ZTBmIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9hZnJobXMxNnYuYmVzdHhyYXkuYnV6ei9saW5rd3MiLCJob3N0IjoiIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDgtMDA3Ni1DQSIsImFkZCI6IjE0Mi45My4xNDQuOTkiLCJwb3J0IjoiMzM4OSIsInR5cGUiOiJub25lIiwiaWQiOiI5YzA1MGE4Ni1kNjEyLTQ4ZjEtZWMzMi1lNTczZGYwOGExYjciLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiMDgtMDA3Ny1DTiIsImFkZCI6ImpwNWcueG4tLXZocTcwaHh5YXQ1MGg2d2suY29tIiwicG9ydCI6IjgwIiwidHlwZSI6Im5vbmUiLCJpZCI6IjVmNjRlMjVlLTQ5MGQtNDkyOS1iOTAxLWE1YWRjNjkwN2VjYyIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6ImpwNWcueG4tLXZocTcwaHh5YXQ1MGg2d2suY29tIiwidGxzIjoiIn0=
    


</details>

### 所有节点
合并节点总数: `26`
[节点链接](https://raw.githubusercontent.com/caijh/TopFreeProxies/master/sub/sub_merge_base64.txt)

### 节点来源
- [clashnode](https://github.com/imyaoxp/clashnode), 节点数量: `26`


## 仓库声明
订阅节点仅作学习交流使用，只是对网络上节点的优选排序，用于查找资料，学习知识，不做任何违法行为。所有资源均来自互联网，仅供大家交流学习使用，出现违法问题概不负责。

