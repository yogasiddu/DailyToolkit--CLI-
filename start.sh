#!/bin/bash

# 哪吒和uuid配置
export UUID="f01379aa-6d1f-4c5e-ad34-69277145dd1d"
export NEZHA_SERVER="nezha.hani.nyc.mn"      
export NEZHA_PORT="443"                         
export NEZHA_KEY="XME64JAhNDUFd9dbZB"

# Argo 隧道配置
export ARGO_DOMAIN="idx3.hani.nyc.mn"
export ARGO_AUTH="eyJhIjoiMzU4YzRkOThmODlkZmE4MTAyZTBiYTI0ZmI1NWJiMmMiLCJ0IjoiNDIzMWI3MjgtNTQwOS00ZDg4LTk5YzAtNmZlZWVmZWY2ZmRkIiwicyI6IlpUaGhaREJrWVRrdE16TTBaUzAwTVdaaUxXRTRNV010TURKalpUbGhNelJsTWpFeCJ9"

# 其他配置
export NAME="idx"
export CFIP="www.visa.com.tw"
export CFPORT=443              # 优选IP或优选域名对应端口
export CHAT_ID="6395641483"             
export BOT_TOKEN="8454997044:AAHX4iVn7OR_bj8dLI5VRSF1kqjAyaGH1h4"            
export UPLOAD_URL=             # 节点自动推送到订阅器，需要填写部署merge-sub项目后的首页地址，例如：https://merge.eooce.ggff.net

bash <(curl -Ls https://main.ssss.nyc.mn/sb.sh)