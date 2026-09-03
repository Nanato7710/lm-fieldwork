# Chat template primer

このページは、言語処理100本ノックの問94、95を読む前の10分の足場です。

チャット画面では、会話をroleとcontentの組として扱います。

```text
[
  {role: "user", content: "短く説明して"},
  {role: "assistant", content: "何を説明しますか"}
]
```

モデルへ渡す前に、chat templateがこの構造をモデル固有の文字列へ直列化します。
直列化した文字列をtokenizerがtoken IDsへ変え、それからモデルへ渡します。

```text
messages
  ↓ chat template
role境界や制御記号を含む文字列
  ↓ tokenizer
token IDs
  ↓ model
```

chat templateは入力形式を整える規則であり、post-trainingそのものではありません。
同じmessagesでもtemplateが違えばtoken列が変わり、想定外のtemplateはモデルの応答を悪化させることがあります。

問94、95では、生成結果だけでなく、messagesがどの文字列とtoken列へ変わったかを確認します。
モデルのdownloadや生成の再現が難しい場合は、問題文と出力例からこのdata flowを追えばCoreとして十分です。
