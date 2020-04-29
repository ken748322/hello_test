# ローカルリポジトリ
git init                            # ローカルリポジトリの初期化
git add hello.html                  # ローカルリポジトリにファイルを追加
git commit -m "add new file"        # commit: ファイルの追加や変更の履歴をリポジトリに保存すること

# リモートリポジトリの準備
# origin: リモートリポジトリのURLが入っている
# master: メインブランチ
git remote add origin https://github.com//awesome.git
git push origin master      # リモードリポジトリに反映させる

# branchの使い方
git branch          # branchの確認
git branch sub1     # branch "sub1"を作る
git checkout sub1   # branch "sub1"にアクセス

git merge sub1              # 現在のローカルリポジトリにbranchを融合させる
git push origin maseter     # 忘れずに
