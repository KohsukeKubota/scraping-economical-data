# seleniumを用いたスクレイピングにより経済指標ダッシュボード（日本経済新聞）から経済指標データのcsvを自動取得する
seleniumはブラウザ操作を自動化するツールで、様々な言語に対応しています。

[経済指標ダッシュボード](https://vdata.nikkei.com/economicdashboard/macro/)は、日本経済の動向を把握するのに役に立つ経済指標が一覧できるサイトです。今回はここから対応するcsvデータをseleniumを用いて自動取得します。

## 必要なライブラリ
```bash
pip install urllib
pip install selenium
```
