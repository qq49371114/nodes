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

    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpmZTYzYzRiNC1jOWI4LTRhMWMtOGE3Yi1iY2Y0NzdiMDQ1OTM@118.170.222.48:10013#05-0000-TWtrojan%2F%2Ftg-fq521free%40198.62.62.67443%3FallowInsecure%3D1%26sni%3Dtorjan.xn--xhq44j.eu.org%26ws%3D1%26wspath%3D%25252F%2306-0054-US
    trojan://ttfang@198.12.144.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=%2525252FTelegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#05-0002-NOWHERE
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDAwOS1SRUxBWSIsImFkZCI6ImFpby51bmxpbWl0ZWQuYml6LmlkIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJmMjgyYjg3OC04NzExLTQ1YTEtOGM2OS01NTY0MTcyMTIzYzEiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2Fpb3Byb3h5Ym90LzEyOS4xNTAuNDkuNTgtMTg2NTAiLCJob3N0IjoiYWlvLnVubGltaXRlZC5iaXouaWQiLCJ0bHMiOiJ0bHMifQ==
    trojan://tg-fq521free@194.76.18.129:443?allowInsecure=1&sni=torjan.xn--xhq44j.eu.org&ws=1&wspath=%2525252F#06-0030-KZ
    trojan://ttfang@86.38.214.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=%2525252FTelegramU0001F1E8U0001F1F3#06-0033-RELAY
    trojan://tg-fq521free@45.67.215.95:443?allowInsecure=1&sni=torjan.xn--xhq44j.eu.org&ws=1&wspath=%2525252F#06-0046-RU
    trojan://tg-fq521free@216.24.57.30:443?allowInsecure=1&sni=torjan.xn--xhq44j.eu.org&ws=1&wspath=%2525252F#06-0055-US
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTptU1FpdVQ1alIxN255V2djWE9QclRX@77.105.166.12:8594#08-0057-FR
    trojan://ttfang@185.176.24.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0058-RELAY
    trojan://ttfang@198.71.232.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0059-US
    trojan://ttfang@192.0.63.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0060-US
    trojan://ttfang@212.183.88.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0061-AT
    trojan://ttfang@166.62.108.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0062-US
    trojan://ttfang@198.71.233.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0063-US
    trojan://ttfang@166.62.106.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0064-US
    trojan://ttfang@198.62.62.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0065-US
    trojan://ttfang@192.169.223.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0066-US
    trojan://ttfang@170.114.45.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0068-RELAY
    trojan://ttfang@195.85.59.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0069-RELAY
    trojan://ttfang@188.244.122.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0070-RELAY
    trojan://ttfang@185.193.29.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0071-RELAY
    trojan://ttfang@185.251.81.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0072-RELAY
    trojan://ttfang@194.76.18.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0073-KZ
    trojan://ttfang@198.177.57.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0074-RELAY
    trojan://ttfang@195.13.54.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0075-RELAY
    trojan://ttfang@199.181.197.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0076-RELAY
    trojan://ttfang@195.13.44.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0077-RELAY
    trojan://ttfang@185.251.83.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0078-RELAY
    trojan://ttfang@185.162.230.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0079-RELAY
    trojan://ttfang@195.13.55.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0080-RELAY
    trojan://ttfang@194.53.53.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0081-RELAY
    trojan://ttfang@176.124.223.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0082-RELAY
    trojan://ttfang@193.9.49.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0083-RELAY
    trojan://ttfang@195.13.45.194:2096?allowInsecure=1&sni=ttfang.fange.me&ws=1&wspath=Telegram%252525F0%2525259F%25252587%252525A8%252525F0%2525259F%25252587%252525B3#08-0084-RELAY
    


</details>

### 所有节点
合并节点总数: `37`
[节点链接](https://raw.githubusercontent.com/caijh/TopFreeProxies/master/sub/sub_merge_base64.txt)

### 节点来源
- [clashnode](https://github.com/imyaoxp/clashnode), 节点数量: `37`


## 仓库声明
订阅节点仅作学习交流使用，只是对网络上节点的优选排序，用于查找资料，学习知识，不做任何违法行为。所有资源均来自互联网，仅供大家交流学习使用，出现违法问题概不负责。

