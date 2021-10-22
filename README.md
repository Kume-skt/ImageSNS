# ImageSNS
 
Slackに画像を投げるだけのプログラム

## 必要な物
slackbotのアクセストークン
Bot Token Scopes の　files:write

## めも
slackのカスタムインテグレーションでは、画像を直接生成して投稿するのは、できない  
貴重なbot枠を１つ使うことになるがいた仕方無いと思うことにした。

認証に手間がかかった。先人たちは、params にトークンとか入れていた。  
認証できないかった。

## 参考ページ
[slack API](https://api.slack.com/methods/files.upload)