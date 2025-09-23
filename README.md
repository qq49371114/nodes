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
高速节点数量: `46`
<details>
  <summary>展开复制节点</summary>

    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@185.213.23.226:989#05-0002-NO
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDAxMC1NWSIsImFkZCI6IjIxMS4yNS4yNDYuMTMxIiwicG9ydCI6IjM0NzgxIiwidHlwZSI6Im5vbmUiLCJpZCI6IjdkZDIwMDdiLTBjZDAtNGJhYy1hOGRmLTM0NDhiNTk1NDVmZCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvYXJraSIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    trojan://wb6368@92.243.75.49:2087?allowInsecure=1&sni=hsdgbuys.pages.dev&ws=1&wspath=%2525252F#05-0011-RELAY
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDEyMy1SRUxBWSIsImFkZCI6Imtsby45ODY5ODYuc2hvcCIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYjc1Yzk3MzEtNDA4ZC00YWE2LThhZTktMzg1NzIwNTExM2ExIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9udmp4Nmo3a2JEUUlRTVp2YmVWQTkiLCJob3N0Ijoia2xvLjk4Njk4Ni5zaG9wIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDEyNC1ISyIsImFkZCI6IjQ3LjIzOS4xMjguMTk0IiwicG9ydCI6IjU4MDU2IiwidHlwZSI6Im5vbmUiLCJpZCI6IjBkNWE1MDkxLWM5MjMtNGZiNi05ZGZkLTk1ZWNmZDYwY2RlZSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvYXJraSIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDEyNS1ISyIsImFkZCI6IjQ3LjIzOS4xMjguMTk0IiwicG9ydCI6IjMwMjQ0IiwidHlwZSI6Im5vbmUiLCJpZCI6ImIzNzhlYWEwLTg0OGYtNDNiYi1iMDYyLTAyNDRmOWUwNzBjNiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvYXJraSIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDEzMC1ISyIsImFkZCI6IjY5N2RjNTUxLXQxaTlzMC10bTUzY20tMW9sOTcuaGszLnA1cHYuY29tIiwicG9ydCI6IjgwIiwidHlwZSI6Im5vbmUiLCJpZCI6IjkzZmI2OWZjLTc3Y2YtMTFlZS04NWVlLWYyM2M5MTM2OWYyZCIsImFpZCI6IjIiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6IjY5N2RjNTUxLXQxaTlzMC10bTUzY20tMW9sOTcuaGszLnA1cHYuY29tIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDEzMy1TQyIsImFkZCI6IjE1NC4yMDEuODAuMjE0IiwicG9ydCI6IjExMTU5IiwidHlwZSI6Im5vbmUiLCJpZCI6ImQ5MjAyZmRkLTU2NzktNDNhNy1hOTMzLTBkMDc2MDViYWIzYyIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvYXJraSIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDEzNC1ISyIsImFkZCI6IjguMjE3LjE3MS4xOTMiLCJwb3J0IjoiMzYzMDAiLCJ0eXBlIjoibm9uZSIsImlkIjoiNjc4Y2RiMTQtMjJhNi00ZmIyLWEwNDAtYjM1M2VjYjk4OWNlIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9hcmtpIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDEzNi1ISyIsImFkZCI6IjguMjE3LjIyMC4zMCIsInBvcnQiOiIzMTEyMyIsInR5cGUiOiJub25lIiwiaWQiOiIxMmY3MTY0Yi1lM2UxLTQyNjQtODZjYy02ODAyODkwMmNkMTkiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2Fya2kiLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDEzNy1ISyIsImFkZCI6IjguMjE3LjIyMC4zMCIsInBvcnQiOiIzOTY0OCIsInR5cGUiOiJub25lIiwiaWQiOiIyYzI1ODNiNi1lY2UwLTRkM2QtYTdmNS1jZjM3YzRhNmZhOGQiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2Fya2kiLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDEzOC1ISyIsImFkZCI6IjQ3LjIzOS44MS4xMTMiLCJwb3J0IjoiMjk3NjAiLCJ0eXBlIjoibm9uZSIsImlkIjoiZmQyOTg3Y2MtYjI1Zi00OTY2LTg0NmEtYjBkNjVkM2MxZTRiIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9hcmtpIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDEzOS1ISyIsImFkZCI6IjQ3Ljc2LjE1Ny4yMzQiLCJwb3J0IjoiMTQ0NzkiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTA2MDZjMTQtY2JhNC00M2ZmLTk1ODYtOWVkZDhiZWYyMWE0IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9hcmtpIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDE0MC1ISyIsImFkZCI6IjguMjE4LjguODQiLCJwb3J0IjoiMjMzMjYiLCJ0eXBlIjoibm9uZSIsImlkIjoiODcxZDA0ZGYtZmM1OC00NzBhLWJhY2EtZGFhZTI4ODY5MTY0IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9hcmtpIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoiMDYtMDAyNS1KUCIsImFkZCI6IjMxLjU3LjE3Mi4yMzUiLCJwb3J0IjoiNTE4OTciLCJ0eXBlIjoibm9uZSIsImlkIjoiMmIyODFjNTYtM2ZjMi00NDljLWFiMzktYTdkYTVhMDIyNDA0IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiMDYtMDAyNy1HQiIsImFkZCI6IjE3Mi4xOTIuMjYuMTYxIiwicG9ydCI6IjI2OTMxIiwidHlwZSI6Im5vbmUiLCJpZCI6ImVhN2IwMTczLWEyN2MtNGVhMS1hMTU2LWNkNjBjMjFlMzUzNiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@51.15.17.169:989#06-0038-NL
    vmess://eyJ2IjoiMiIsInBzIjoiMDYtMDA1MC1KUCIsImFkZCI6IjE1OC4xMDEuMTMwLjIzOCIsInBvcnQiOiIyMzk3MiIsInR5cGUiOiJub25lIiwiaWQiOiJhMTJmMWFhMi05NmMyLTRlYjItZjMzMi1mYTdkN2FmMjY1YTQiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiMDYtMDA1Ny1NWSIsImFkZCI6IjM4LjU0Ljk4LjExMCIsInBvcnQiOiIyMDUyIiwidHlwZSI6Im5vbmUiLCJpZCI6IjY2NWQ5YjhmLTE1M2QtNDkwNy1hZGFjLWRlMTJhZmQ5Yzg1MSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6InRscyJ9
    trojan://tunnel-astrovpn_official928@206.206.126.109:8441?allowInsecure=1&sni=zula.ir.AstroVPN-official.AstroVPN-official.workers.dev.AstroVPN_Official.org.AstroVPN.com.AstroVPN_Official.xyz.AstroVPN_Official.AstroVPN_Official.AstroVPN_Official.AstroVPN_Official.AstroVPN_Official.AstroVPN_Official.AstroVPN_Official.AstroVPN_Official.monster.AstroVPN_OfficialJoinTelegram-------------AstroVPN_Official----------Join.ir#06-0064-SG
    vmess://eyJ2IjoiMiIsInBzIjoiMDYtMDA2NS1VUyIsImFkZCI6IjE1NC42NC4yMjguMjM2IiwicG9ydCI6IjE1NDkxIiwidHlwZSI6Im5vbmUiLCJpZCI6IjM4OWI1MmJhLWQ5MzYtNDgwMC04N2E2LTFlOTc2NWUzNTA3OSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    ss://YWVzLTI1Ni1jZmI6WG44aktkbURNMDBJZU8lMjUyNSUyNTIzJTI1MjQlMjUyM2ZKQU10c0VBRVVPcEgvWVdZdFlxREZuVDBTVg@103.186.155.16:38388#06-0080-VN
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@154.90.63.177:989#08-0081-KR
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@154.90.62.168:989#08-0083-KR
    ss://YWVzLTI1Ni1jZmI6WG44aktkbURNMDBJZU8lMjUyNSUyNTIzJTI1MjQlMjUyM2ZKQU10c0VBRVVPcEgvWVdZdFlxREZuVDBTVg@103.186.154.152:38388#08-0085-VN
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpwNzhuYUNmMkVmT2xSU0xUWDB3RlZ4@pupas-shirting-unsung.freesocks.work:443#08-0086-US
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@154.223.16.212:989#08-0148-CO
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpRQ1hEeHVEbFRUTUQ3anRnSFVqSW9q@45.87.175.180:8080#23-0114-LT
    vmess://eyJ2IjoiMiIsInBzIjoiMjMtMDExNS1DQSIsImFkZCI6IjE1LjIzNS41MC4xNzIiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjAzZmNjNjE4LWI5M2QtNjc5Ni02YWVkLThhMzhjOTc1ZDU4MSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvbGlua3Z3cyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    trojan://NISHIKUITAN222@172.67.148.85:443?allowInsecure=1#23-0119-RELAY
    trojan://telegram-id-directvpn@13.36.206.216:22223?allowInsecure=1&sni=trojan.burgerip.co.uk#23-0152-FR
    ss://YWVzLTEyOC1nY206c2hhZG93c29ja3M@212.102.53.194:443#23-0153-GB
    ss://YWVzLTEyOC1nY206c2hhZG93c29ja3M@212.102.53.80:443#23-0154-GB
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpvWklvQTY5UTh5aGNRVjhrYTNQYTNB@103.104.247.47:8080#23-0155-NL
    ss://YWVzLTEyOC1nY206c2hhZG93c29ja3M@212.102.53.198:443#23-0157-GB
    ss://YWVzLTEyOC1nY206c2hhZG93c29ja3M@212.102.53.81:443#23-0162-GB
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpjdklJODVUclc2bjBPR3lmcEhWUzF1@45.87.175.185:8080#23-0163-LT
    ss://YWVzLTEyOC1nY206c2hhZG93c29ja3M@156.146.62.163:443#23-0164-CH
    ss://YWVzLTEyOC1nY206c2hhZG93c29ja3M@149.34.244.82:443#23-0165-NL
    ss://YWVzLTEyOC1nY206c2hhZG93c29ja3M@149.34.244.68:443#23-0167-NL
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTplVWg0bFNwaTduT1lqMHZTcnFMVWgw@95.163.176.37:8506#23-0169-AT
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpjdklJODVUclc2bjBPR3lmcEhWUzF1@45.87.175.164:8080#23-0170-LT
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpvWklvQTY5UTh5aGNRVjhrYTNQYTNB@45.87.175.92:8080#23-0171-LT
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpvWklvQTY5UTh5aGNRVjhrYTNQYTNB@45.87.175.65:8080#23-0172-LT
    trojan://telegram-id-privatevpns@13.36.206.216:22222?allowInsecure=1&sni=trojan.burgerip.co.uk#23-0175-FR
    


</details>

### 所有节点
合并节点总数: `147`
[节点链接](https://raw.githubusercontent.com/caijh/TopFreeProxies/master/sub/sub_merge_base64.txt)

### 节点来源
- [clashnode](https://github.com/imyaoxp/clashnode), 节点数量: `147`


## 仓库声明
订阅节点仅作学习交流使用，只是对网络上节点的优选排序，用于查找资料，学习知识，不做任何违法行为。所有资源均来自互联网，仅供大家交流学习使用，出现违法问题概不负责。

