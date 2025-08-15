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
高速节点数量: `71`
<details>
  <summary>展开复制节点</summary>

    trojan://tg-fq521free@45.67.215.95:443?allowInsecure=1&sni=torjan.xn--xhq44j.eu.org&ws=1&wspath=%2525252F#05-0015-RU
    trojan://Aimer@47.79.38.17:443?allowInsecure=1&sni=torjan.xn--xhq44j.eu.org&ws=1&wspath=%2525252F#05-0016-US
    ss://cmM0LW1kNToxNGZGUHJiZXpFM0hEWnpzTU9yNg@23.251.121.242:8080#05-0037-UStrojan%2F%2F0F22D008-24D4-4DFE-947B-8D2FD64CD24C%40www.visa.com.sg2053%3FallowInsecure%3D1%26sni%3Dt.hongkong6.qzz.io%26ws%3D1%26wspath%3D%25252F%2305-0010-RELAY
    vmess://eyJ2IjoiMiIsInBzIjoiMDUtMDA0Ni1DTiIsImFkZCI6InYzNy5oZWR1aWFuLmxpbmsiLCJwb3J0IjoiMzA4MzciLCJ0eXBlIjoibm9uZSIsImlkIjoiY2JiM2Y4NzctZDFmYi0zNDRjLTg3YTktZDE1M2JmZmQ1NDg0IiwiYWlkIjoiMiIsIm5ldCI6IndzIiwicGF0aCI6Ii9vb29vIiwiaG9zdCI6InYzNy5oZWR1aWFuLmxpbmsiLCJ0bHMiOiIifQ==
    trojan://Aimer@188.164.159.18:443?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0054-RELAY
    trojan://Aimer@188.164.159.107:2096?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0055-RELAY
    trojan://Aimer@188.164.159.138:2083?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0056-RELAY
    trojan://Aimer@188.164.159.91:2083?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0057-RELAY
    trojan://Aimer@188.164.159.43:2083?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0058-RELAY
    trojan://Aimer@188.164.159.98:2083?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0059-RELAY
    trojan://Aimer@188.164.159.55:2096?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0060-RELAY
    trojan://Aimer@154.211.8.227:2087?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0095-RELAY
    trojan://Aimer@154.211.8.150:2096?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0096-RELAY
    trojan://Aimer@34.85.77.183:8080?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0099-GOOGLE
    trojan://Aimer@103.116.7.67:2083?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0101-RELAY
    trojan://Aimer@115.22.115.218:50000?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0102-KR
    trojan://Aimer@175.210.186.14:12562?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0103-KR
    trojan://Aimer@211.224.100.145:50000?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0104-KR
    trojan://Aimer@211.57.146.108:50000?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0105-KR
    trojan://Aimer@222.105.100.2:12483?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0106-KR
    trojan://Aimer@59.16.25.39:12288?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0107-KR
    trojan://Aimer@210.222.78.191:10240?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0108-KR
    trojan://Aimer@121.167.146.253:12902?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0109-KR
    trojan://Aimer@220.72.106.154:12127?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0110-KR
    trojan://Aimer@175.212.51.220:21301?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0111-KR
    trojan://Aimer@31.43.179.27:443?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0117-RELAY
    trojan://Aimer@86.38.214.186:443?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0125-RELAY
    trojan://Aimer@5.182.85.255:2096?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0173-RELAY
    trojan://Aimer@46.254.92.142:2087?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0174-RELAY
    trojan://Aimer@77.232.140.114:2053?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0175-RELAY
    trojan://Aimer@46.254.93.251:2087?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0176-RELAY
    trojan://Aimer@176.124.223.40:2053?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0177-RELAY
    trojan://Aimer@5.182.84.50:2096?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0178-RELAY
    trojan://Aimer@45.67.215.217:2087?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0179-RU
    trojan://Aimer@46.254.93.211:2053?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0180-RELAY
    trojan://Aimer@154.197.64.219:2083?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0182-RELAY
    trojan://Aimer@154.197.64.104:8443?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0183-RELAY
    trojan://Aimer@154.197.64.233:443?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0184-RELAY
    trojan://Aimer@154.197.64.196:2087?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0185-RELAY
    trojan://Aimer@92.243.74.23:2096?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0187-RELAY
    trojan://Aimer@92.243.74.3:8443?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0188-RELAY
    trojan://Aimer@27.50.49.37:2053?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0189-RELAY
    trojan://Aimer@27.50.49.136:443?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0190-RELAY
    trojan://Aimer@92.243.74.239:8443?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0191-RELAY
    trojan://Aimer@74.176.199.245:443?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0234-JP
    trojan://Aimer@154.17.10.113:12266?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0253-US
    trojan://Aimer@154.23.172.19:11000?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0255-US
    trojan://Aimer@154.26.182.37:443?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0256-US
    trojan://Aimer@67.226.221.102:80?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0259-US
    trojan://Aimer@lynn.ns.cloudflare.com:443?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0260-RELAY
    trojan://Aimer@172.64.35.66:443?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0261-RELAY
    trojan://Aimer@135.84.64.36:2083?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0264-US
    trojan://Aimer@162.159.44.230:2053?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0265-RELAY
    trojan://Aimer@104.19.60.99:2087?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0266-RELAY
    trojan://Aimer@199.34.228.187:443?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0267-US
    trojan://Aimer@161.145.150.29:2083?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0268-US
    trojan://Aimer@kip.ns.cloudflare.com:443?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0269-RELAY
    trojan://Aimer@107.173.111.232:20082?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0270-US
    trojan://Aimer@108.165.152.78:2083?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0271-RELAY
    trojan://Aimer@192.210.207.89:20080?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0272-US
    trojan://Aimer@108.165.152.1:2087?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0273-RELAY
    trojan://Aimer@199.34.228.71:8443?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0274-US
    trojan://Aimer@155.46.213.38:2083?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0275-RELAY
    trojan://Aimer@199.34.228.50:2053?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0276-US
    trojan://Aimer@108.165.152.202:2083?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0277-RELAY
    trojan://Aimer@162.120.94.232:8443?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0278-RELAY
    trojan://Aimer@108.165.152.175:2096?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0280-RELAY
    trojan://Aimer@167.68.5.248:2087?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0281-RELAY
    trojan://Aimer@108.165.152.59:2087?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0282-RELAY
    trojan://Aimer@172.67.77.127:443?allowInsecure=1&sni=epgb.aimercc.dpdns.org&ws=1&wspath=%2525252F%2525253Fed%2525253D2560#06-0283-RELAY
    


</details>

### 所有节点
合并节点总数: `353`
[节点链接](https://raw.githubusercontent.com/caijh/TopFreeProxies/master/sub/sub_merge_base64.txt)

### 节点来源
- [clashnode](https://github.com/imyaoxp/clashnode), 节点数量: `353`


## 仓库声明
订阅节点仅作学习交流使用，只是对网络上节点的优选排序，用于查找资料，学习知识，不做任何违法行为。所有资源均来自互联网，仅供大家交流学习使用，出现违法问题概不负责。

