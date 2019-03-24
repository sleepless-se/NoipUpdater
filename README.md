# NoipUpdater
グローバルIPアドレスが変わっているかを確認して、Noip に登録しているIPアドレスを更新するスクリプトです。

## 動作環境
- Python 3.5+
- Selenium 3.141.0

## 設定
1.リポジトリをダウンロード

`git clone https://github.com/sleepless-se/NoipUpdater.git`

2.Seleniumをインストール

`cd NoipUpdater`

`pip3 install -r requirements.txt `

Chromeドライバーをここからダウンロード→ [chrome driver](https://sites.google.com/a/chromium.org/chromedriver/downloads). 下記のディレクトリに`chromedriver`を保存します。

Mac / Linux `open /usr/local/bin`

Windos `?`

（Windowsの保存場所が分かる方がいましたらプルリクエストをいただけると嬉しいです。）

3.Noip のログインアドレスとパスワードを設定

NoipUpdaterの`update_global_ip.py`を開きます。この行を編集します。

    email = "noip email"
    password = "noip password"

4.実行テスト

`python3 ./update_global_ip.py`

Chromeが起動し現在のIPアドレスをNoipに登録します。

5 .cronに設定 
    
1. cronを開いて `crontab -e`

1. この行を追加します。 `*/10 * * * * /path/to/python3 /path/to/NoipUpdater/update_global_ip.py`

*注意:パスは環境に合わせて設定してください。


---

# NoipUpdater
This script update global ip on Noip.
If ip had change with last ip address.
Login Noip then update global ip address.

## Environment
- Python 3.5+
- Selenium 3.141.0

## Settings
1.Clone repository

`git clone https://github.com/sleepless-se/NoipUpdater.git`

2.Install Selenium

`cd NoipUpdater`

`pip3 install -r requirements.txt `

Download [chrome driver](https://sites.google.com/a/chromium.org/chromedriver/downloads). Then save chromedrive at below

Mac / Linux `open /usr/local/bin`

Windos `?`

3.Set Noip login email and password

Open `update_global_ip.py` in NoipUpdater. Edit this line.

    email = "noip email"
    password = "noip password"

4.Run test

`python3 ./update_global_ip.py`

5 .Set on cron 
    
1. Open cron `crontab -e`

1. Add this line `*/10 * * * * /path/to/python3 /path/to/NoipUpdater/update_global_ip.py`

*Note:Please replace as your path.

