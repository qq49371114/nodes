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

    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDAwMi1DTiIsImFkZCI6IjUubWFtYW1hamQuc2l0ZSIsInBvcnQiOiIyMzYwNSIsInR5cGUiOiJub25lIiwiaWQiOiJhYTRhNDBlYS0zZGIwLTNiODQtYTYwOC1jMDJmZjVhNjkxZDciLCJhaWQiOiIyIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiI1Lm1hbWFtYWpkLnNpdGUiLCJ0bHMiOiIifQ==
    trojan://ttfang@5.10.245.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=%2525252FTelegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#05-0019-RELAY
    trojan://ttfang@139.180.154.158:443?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=%2525252FTelegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#05-0020-US
    trojan://ttfang@103.169.142.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=%2525252FTelegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#05-0021-RELAY
    trojan://ttfang@91.206.71.216:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=%2525252FTelegram%252525E9%252525A6%25252583%252525E5%2525259A%2525259A%252525E9%252525A6%25252583%252525E5%2525259A%252525A6#05-0028-RELAY
    trojan://ttfang@66.81.247.216:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=%2525252FTelegram%252525E9%252525A6%25252583%252525E5%2525259A%2525259A%252525E9%252525A6%25252583%252525E5%2525259A%252525A6#05-0031-RELAY
    trojan://ttfang@20.235.105.146:443?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=%2525252F#05-0036-IN
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpmNzVkM2YyNi0wMzhlLTRmNTMtYjgxYi1hZTJlMDVlYmVmMzM@36.234.120.74:10075#05-0037-TW
    trojan://13253e6e-a1f7-4090-801f-a8dc2b083bef@104.21.78.206:2083?allowInsecure=1&sni=inVIncibLE.fAfA20.shoP&ws=1&wspath=%2525252FtrxSsuyYmFFPA4woIq%2525252FNzguNDYuNTYuNDI%2525253D#05-0038-RELAY
    trojan://bpb-trojan@162.159.153.2:443?allowInsecure=1&sni=zamim340.ggff.net&ws=1&wspath=%2525252Ftr#05-0040-RELAY
    trojan://a94fafdb-10d6-46c2-be8a-5c2e8358fbb0@172.67.187.28:443?allowInsecure=1&sni=dddDdDdDDFfFf.iran2035.dPdNS.ORG&ws=1&wspath=%2525252Fxa846InEcmjyiKVby2Lp#05-0041-RELAY
    trojan://ttfang@45.12.30.216:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=%2525252FTelegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#05-0042-RELAY
    trojan://ttfang@45.131.208.216:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=%2525252FTelegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#05-0043-RELAY
    trojan://ttfang@92.243.75.216:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=%2525252FTelegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#05-0044-RELAY
    trojan://ttfang@94.247.142.216:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=%2525252FTelegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#05-0045-RELAY
    ss://YWVzLTEyOC1nY206MDE3MjFlNDMtNTM4OS00Zjk3LWIyMWMtOTAwYWJiMmJkYTll@awes35lesl.blhao0o.dpdns.org:12017#06-0050-CN
    ss://YWVzLTEyOC1nY206MDE3MjFlNDMtNTM4OS00Zjk3LWIyMWMtOTAwYWJiMmJkYTll@awes35lesl.blhao0o.dpdns.org:12020#06-0051-CN
    ss://YWVzLTEyOC1nY206MDE3MjFlNDMtNTM4OS00Zjk3LWIyMWMtOTAwYWJiMmJkYTll@awes35lesl.blhao0o.dpdns.org:12030#06-0052-CN
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@51.15.23.63:989#06-0063-NL
    trojan://tg-fq521free@194.76.18.129:443?allowInsecure=1&sni=torjan.xn--xhq44j.eu.org&ws=1&wspath=%2525252F#06-0083-KZ
    trojan://ttfang@86.38.214.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=%2525252FTelegramU0001F1E8U0001F1F3#06-0087-RELAY
    trojan://tg-fq521free@45.67.215.95:443?allowInsecure=1&sni=torjan.xn--xhq44j.eu.org&ws=1&wspath=%2525252F#06-0111-RU
    trojan://tg-fq521free@198.62.62.67:443?allowInsecure=1&sni=torjan.xn--xhq44j.eu.org&ws=1&wspath=%2525252F#06-0136-US
    trojan://ttfang@ttfang.fange.me:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=%2525252FTelegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#06-0137-RELAY
    trojan://tg-fq521free@216.24.57.30:443?allowInsecure=1&sni=torjan.xn--xhq44j.eu.org&ws=1&wspath=%2525252F#06-0138-US
    ss://YWVzLTI1Ni1jZmI6WG44aktkbURNMDBJZU8lMjUyNSUyNTIzJTI1MjQlMjUyM2ZKQU10c0VBRVVPcEgvWVdZdFlxREZuVDBTVg@103.186.154.28:38388#06-0141-VN
    ss://YWVzLTI1Ni1jZmI6WG44aktkbURNMDBJZU8lMjUyNSUyNTIzJTI1MjQlMjUyM2ZKQU10c0VBRVVPcEgvWVdZdFlxREZuVDBTVg@103.186.154.36:38388#06-0142-VN
    ss://YWVzLTI1Ni1jZmI6WG44aktkbURNMDBJZU8lMjUyNSUyNTIzJTI1MjQlMjUyM2ZKQU10c0VBRVVPcEgvWVdZdFlxREZuVDBTVg@103.186.154.32:38388#06-0143-VN
    ss://YWVzLTI1Ni1jZmI6WG44aktkbURNMDBJZU8lMjUyNSUyNTIzJTI1MjQlMjUyM2ZKQU10c0VBRVVPcEgvWVdZdFlxREZuVDBTVg@103.186.154.20:38388#06-0144-VN
    ss://YWVzLTI1Ni1jZmI6WG44aktkbURNMDBJZU8lMjUyNSUyNTIzJTI1MjQlMjUyM2ZKQU10c0VBRVVPcEgvWVdZdFlxREZuVDBTVg@103.186.154.37:38388#06-0145-VN
    ss://YWVzLTI1Ni1jZmI6WG44aktkbURNMDBJZU8lMjUyNSUyNTIzJTI1MjQlMjUyM2ZKQU10c0VBRVVPcEgvWVdZdFlxREZuVDBTVg@103.186.154.24:38388#06-0146-VN
    ss://YWVzLTI1Ni1jZmI6WG44aktkbURNMDBJZU8lMjUyNSUyNTIzJTI1MjQlMjUyM2ZKQU10c0VBRVVPcEgvWVdZdFlxREZuVDBTVg@103.186.155.21:38388#06-0147-VN
    trojan://ttfang@45.40.153.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0151-US
    trojan://ttfang@45.40.149.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0152-US
    trojan://ttfang@45.131.210.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0153-RELAY
    trojan://ttfang@50.62.88.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0154-US
    trojan://ttfang@45.40.146.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0155-US
    trojan://ttfang@50.62.172.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0156-US
    trojan://ttfang@45.40.150.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0157-US
    trojan://ttfang@69.84.182.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0158-US
    trojan://ttfang@45.40.151.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0159-US
    trojan://ttfang@72.167.243.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0160-US
    trojan://ttfang@66.81.247.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0161-RELAY
    trojan://ttfang@45.135.235.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0162-RELAY
    trojan://ttfang@50.62.91.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0163-US
    trojan://ttfang@45.40.152.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0164-US
    trojan://ttfang@72.167.242.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0165-US
    trojan://ttfang@45.40.154.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0166-US
    trojan://ttfang@63.141.128.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0167-US
    trojan://ttfang@45.40.155.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0168-US
    trojan://ttfang@45.149.12.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0169-RELAY
    trojan://ttfang@45.67.215.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0170-RU
    trojan://ttfang@45.85.119.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0171-RELAY
    trojan://ttfang@50.62.198.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0172-US
    trojan://ttfang@31.43.179.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0173-RELAY
    


</details>

### 所有节点
合并节点总数: `61`
[节点链接](https://raw.githubusercontent.com/caijh/TopFreeProxies/master/sub/sub_merge_base64.txt)

### 节点来源
- [clashnode](https://github.com/imyaoxp/clashnode), 节点数量: `61`


## 仓库声明
订阅节点仅作学习交流使用，只是对网络上节点的优选排序，用于查找资料，学习知识，不做任何违法行为。所有资源均来自互联网，仅供大家交流学习使用，出现违法问题概不负责。

