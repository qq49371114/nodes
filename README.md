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
高速节点数量: `31`
<details>
  <summary>展开复制节点</summary>

    trojan://ttfang@45.40.144.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=%2525252FTelegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#05-0002-RELAY
    ss://YWVzLTEyOC1nY206MDE3MjFlNDMtNTM4OS00Zjk3LWIyMWMtOTAwYWJiMmJkYTll@awes35lesl.blhao0o.dpdns.org:12031#06-0024-CN
    ss://YWVzLTEyOC1nY206MDE3MjFlNDMtNTM4OS00Zjk3LWIyMWMtOTAwYWJiMmJkYTll@awes35lesl.blhao0o.dpdns.org:12034#06-0025-CN
    ss://YWVzLTEyOC1nY206MDE3MjFlNDMtNTM4OS00Zjk3LWIyMWMtOTAwYWJiMmJkYTll@awes35lesl.blhao0o.dpdns.org:12014#06-0026-CN
    ss://YWVzLTEyOC1nY206MDE3MjFlNDMtNTM4OS00Zjk3LWIyMWMtOTAwYWJiMmJkYTll@awes35lesl.blhao0o.dpdns.org:12012#06-0027-CN
    trojan://ttfang@45.40.155.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0052-US
    trojan://ttfang@72.167.230.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0054-US
    trojan://ttfang@5.10.247.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0055-RELAY
    trojan://tg-fq521free@45.67.215.95:443?allowInsecure=1&sni=torjan.xn--xhq44j.eu.org&ws=1&wspath=%2525252F#08-0056-RU
    trojan://ttfang@46.254.92.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0057-RELAY
    trojan://ttfang@50.62.88.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0058-US
    trojan://ttfang@50.62.172.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0059-US
    trojan://ttfang@94.140.0.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0060-RELAY
    trojan://ttfang@89.116.250.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0061-RELAY
    trojan://ttfang@72.167.243.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0062-US
    trojan://ttfang@66.225.252.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0063-RELAY
    trojan://ttfang@45.40.153.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0064-US
    trojan://ttfang@45.40.151.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0065-US
    trojan://ttfang@45.142.120.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0066-RELAY
    trojan://ttfang@103.133.1.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0067-RELAY
    trojan://ttfang@50.62.91.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0068-US
    trojan://ttfang@50.62.174.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0069-US
    trojan://ttfang@45.131.7.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0070-RELAY
    trojan://ttfang@45.131.4.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0071-RELAY
    trojan://ttfang@45.40.147.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0072-US
    trojan://ttfang@92.60.74.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0073-RELAY
    trojan://ttfang@89.116.180.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0075-RELAY
    trojan://ttfang@77.37.33.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0076-RELAY
    trojan://ttfang@45.12.30.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0077-RELAY
    trojan://ttfang@103.169.142.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0078-RELAY
    


</details>

### 所有节点
合并节点总数: `32`
[节点链接](https://raw.githubusercontent.com/caijh/TopFreeProxies/master/sub/sub_merge_base64.txt)

### 节点来源
- [clashnode](https://github.com/imyaoxp/clashnode), 节点数量: `32`


## 仓库声明
订阅节点仅作学习交流使用，只是对网络上节点的优选排序，用于查找资料，学习知识，不做任何违法行为。所有资源均来自互联网，仅供大家交流学习使用，出现违法问题概不负责。

