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
高速节点数量: `10`
<details>
  <summary>展开复制节点</summary>

    trojan://d0d08cddacc3190ea81b1b792e1b5fde@143.110.155.169:443?allowInsecure=1&sni=t.hongkong6.qzz.io&ws=1&wspath=%2525252F#05-0038-RELAY
    ss://MjAyMi1ibGFrZTMtYWVzLTI1Ni1nY206bXRNa3AlMjUyQjFGdHRrU0xtRE9GOWJsbk5NTGlnY0NSYWNwclFTM3J5MG5mM28lMjUzRCUyNTNBSkIxdWVUQ0tOSUdNYmh6V05qcyUyNTJCMEZuWmpaWE8zVXlYY1poSUoyOHZpZkElMjUzRA@pop.plus.3123.0tk8a3a1q4t94dler.com:4059#06-0050-CN
    trojan://f282b878-8711-45a1-8c69-5564172123c1@172.67.181.173:443?allowInsecure=1&sni=vpn.stupidworld.web.id&ws=1&wspath=%2525252F#07-0163-RELAY
    trojan://trojan@109.234.211.66:8443?allowInsecure=1&sni=store.timimi.dpdns.org&ws=1&wspath=%2525252F#07-0174-RELAY
    trojan://ZU)0ryc$VSrG@104.17.148.22:443?allowInsecure=1&sni=uk2WbO0iKx3IyI4i9WjdYU6Y-O28ET7o.pagEs.DeV&ws=1&wspath=%2525252F#07-0207-RELAY
    vmess://eyJ2IjoiMiIsInBzIjoiMDgtMDIxOS1DTiIsImFkZCI6IjQ3LjEwNC4xODYuMTMzIiwicG9ydCI6IjUwMDAyIiwidHlwZSI6Im5vbmUiLCJpZCI6IjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    ss://YWVzLTI1Ni1jZmI6ZjhmN2FDemNQS2JzRjhwMw@156.146.40.194:989#16-0232-SK
    vmess://eyJ2IjoiMiIsInBzIjoiMTYtMDIzNC1ISyIsImFkZCI6ImVkOTdhZThlLXQwNDlzMC10NG54dmMtMXAxYi5oa3QudGNwYmJyLm5ldCIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiIyNzliODU4OC02MTZiLTExZWQtYThiZi1mMjNjOTFjZmJiYzkiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiJlZDk3YWU4ZS10MDQ5czAtdDRueHZjLTFwMWIuaGt0LnRjcGJici5uZXQiLCJ0bHMiOiIifQ==
    trojan://d0d08cddacc3190ea81b1b792e1b5fde@157.230.32.243:443?allowInsecure=1&sni=www.baidu.com#16-0235-SG
    


</details>

### 所有节点
合并节点总数: `11`
[节点链接](https://raw.githubusercontent.com/caijh/TopFreeProxies/master/sub/sub_merge_base64.txt)

### 节点来源
- [clashnode](https://github.com/imyaoxp/clashnode), 节点数量: `11`


## 仓库声明
订阅节点仅作学习交流使用，只是对网络上节点的优选排序，用于查找资料，学习知识，不做任何违法行为。所有资源均来自互联网，仅供大家交流学习使用，出现违法问题概不负责。

