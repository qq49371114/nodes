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
高速节点数量: `39`
<details>
  <summary>展开复制节点</summary>

    trojan://ttfang@50.62.173.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=%2525252FTelegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#05-0000-RELAY
    trojan://ttfang@72.167.230.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=%2525252FTelegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#05-0002-US
    trojan://ttfang@102.132.188.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=%2525252FTelegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#05-0003-RELAY
    ss://YWVzLTEyOC1nY206MDE3MjFlNDMtNTM4OS00Zjk3LWIyMWMtOTAwYWJiMmJkYTll@awes35lesl.blhao0o.dpdns.org:12020#06-0030-CN
    trojan://tg-fq521free@194.76.18.129:443?allowInsecure=1&sni=torjan.xn--xhq44j.eu.org&ws=1&wspath=%2525252F#06-0053-KZ
    trojan://ttfang@86.38.214.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=%2525252FTelegramU0001F1E8U0001F1F3#06-0058-RELAY
    trojan://tg-fq521free@45.67.215.95:443?allowInsecure=1&sni=torjan.xn--xhq44j.eu.org&ws=1&wspath=%2525252F#06-0081-RU
    trojan://tg-fq521free@216.24.57.30:443?allowInsecure=1&sni=torjan.xn--xhq44j.eu.org&ws=1&wspath=%2525252F#06-0105-US
    trojan://tg-fq521free@198.62.62.67:443?allowInsecure=1&sni=torjan.xn--xhq44j.eu.org&ws=1&wspath=%2525252F#06-0107-US
    ss://YWVzLTI1Ni1jZmI6WG44aktkbURNMDBJZU8lMjUyNSUyNTIzJTI1MjQlMjUyM2ZKQU10c0VBRVVPcEgvWVdZdFlxREZuVDBTVg@103.186.154.36:38388#06-0109-VN
    ss://YWVzLTI1Ni1jZmI6WG44aktkbURNMDBJZU8lMjUyNSUyNTIzJTI1MjQlMjUyM2ZKQU10c0VBRVVPcEgvWVdZdFlxREZuVDBTVg@103.186.154.28:38388#06-0110-VN
    ss://YWVzLTI1Ni1jZmI6WG44aktkbURNMDBJZU8lMjUyNSUyNTIzJTI1MjQlMjUyM2ZKQU10c0VBRVVPcEgvWVdZdFlxREZuVDBTVg@103.186.154.20:38388#06-0111-VN
    ss://YWVzLTI1Ni1jZmI6WG44aktkbURNMDBJZU8lMjUyNSUyNTIzJTI1MjQlMjUyM2ZKQU10c0VBRVVPcEgvWVdZdFlxREZuVDBTVg@103.186.155.21:38388#06-0112-VN
    ss://YWVzLTI1Ni1jZmI6WG44aktkbURNMDBJZU8lMjUyNSUyNTIzJTI1MjQlMjUyM2ZKQU10c0VBRVVPcEgvWVdZdFlxREZuVDBTVg@103.186.154.32:38388#06-0113-VN
    vmess://eyJ2IjoiMiIsInBzIjoiMDgtMDExNi1FUyIsImFkZCI6InMzLmlweWFyLm9yZyIsInBvcnQiOiIzMjAyMCIsInR5cGUiOiJub25lIiwiaWQiOiI3OGI0ZmI1Ny0zOWQ3LTRlOWQtZGQzOC1jOWEzODMyMmJjYjIiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6IiUyNTI1MkYiLCJob3N0IjoidG9yamFuLnhuLS14aHE0NGouZXUub3JnIiwidGxzIjoiIn0=
    trojan://ttfang@50.62.175.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0117-US
    trojan://ttfang@66.81.247.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0118-RELAY
    trojan://ttfang@45.40.148.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0119-US
    trojan://ttfang@50.62.172.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0121-US
    trojan://ttfang@72.167.241.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0122-US
    trojan://ttfang@45.40.146.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0123-US
    trojan://ttfang@45.40.150.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0124-US
    trojan://ttfang@50.62.88.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0125-US
    trojan://ttfang@45.40.152.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0126-US
    trojan://ttfang@63.141.128.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0127-US
    trojan://ttfang@50.62.198.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0128-US
    trojan://ttfang@45.40.147.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0129-US
    trojan://ttfang@72.167.25.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0130-US
    trojan://ttfang@72.167.242.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0131-US
    trojan://ttfang@50.62.174.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0132-US
    trojan://ttfang@72.167.243.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0133-US
    trojan://ttfang@45.131.209.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0134-RELAY
    trojan://ttfang@45.153.7.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0135-RELAY
    trojan://ttfang@89.116.250.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0137-RELAY
    trojan://ttfang@5.175.141.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0138-RELAY
    trojan://ttfang@91.124.127.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0139-RELAY
    trojan://ttfang@77.232.140.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0140-RELAY
    trojan://ttfang@46.254.92.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0141-RELAY
    


</details>

### 所有节点
合并节点总数: `42`
[节点链接](https://raw.githubusercontent.com/caijh/TopFreeProxies/master/sub/sub_merge_base64.txt)

### 节点来源
- [clashnode](https://github.com/imyaoxp/clashnode), 节点数量: `42`


## 仓库声明
订阅节点仅作学习交流使用，只是对网络上节点的优选排序，用于查找资料，学习知识，不做任何违法行为。所有资源均来自互联网，仅供大家交流学习使用，出现违法问题概不负责。

