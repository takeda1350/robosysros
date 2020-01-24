# robosysros
## 概要
入力した数値をPublishして、別ノードでSubscribeし、入力された数値の二乗した数値を表示する

## インストール方法
`catkin_ws/src/`内で下記コマンドを実行

```
$git clone https://github.com/takeda1350/robosys.git
```

## 実行方法
端末１
`$ roscre`
端末２
`$ rosrun mypkg count.py`
端末３
`$ rosrun mypkg twice.py`
## デモ動画
https://youtu.be/z8k4U-Ns4HM
## LICENSE
This repository is licensed under the GPLv3 license, see COPYING
