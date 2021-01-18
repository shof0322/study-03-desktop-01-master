import pandas as pd
import eel


### デスクトップアプリ作成課題
@eel.expose
def kimetsu_search(word, filename) -> object:
    # 検索対象取得
    df = pd.read_csv(f"./{filename}")
    source = list(df["name"])

    # 検索
    if word in source:
        print("『{}』はあります".format(word))
        eel.view_log_js(f'{word}はあります\n')
    else:
        print("『{}』はありません".format(word))
        eel.view_log_js(f'{word}はありません\n')
        # 追加
        # add_flg=input("追加登録しますか？(0:しない 1:する)　＞＞　")
        # if add_flg=="1":
        source.append(word)

    # CSV書き込み
    df = pd.DataFrame(source, columns=["name"])
    df.to_csv(f"./{filename}", encoding="utf_8-sig")
    print(source)
