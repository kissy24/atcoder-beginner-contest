# Atcoder ABC 解答置き場

## 概要

- AtcoderのABC過去問の解答コードを置いてます。
- [過去問集](https://kenkoooo.com/atcoder/#/table/)

## 2021年の着手状況

### 現状

- Atcoderで頑張りたいとかはあまりない(ABCの実施日・時間が厳しい…)
- お仕事でコードあまり書けてない時にAとBだけウォームアップのために解いてます。

### 今後

- 引き続きPythonかGoの訓練用に利用する
- 2022年はD問題中心に進めたい
- テストコードも書く

## その他

### generate_folder ツールについて

以下のような感じで、フォルダとファイルが生成されます。

- D問題以上は解かないため、生成してません。
- lang オプションを利用すると任意の拡張子に変更できます。

```shell
$ go run generate_folder.go    
035

>>> ABC_035 ---a.py
             |-b.py
             |-c.py
             --d.py
```
