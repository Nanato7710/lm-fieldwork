# Chat template primer

このページは、言語処理100本ノックの問94、95を読む前の10分の足場です。

チャット画面では、会話をroleとcontentの組として扱います。

```text
[
  {role: "user", content: "短く説明して"},
  {role: "assistant", content: "何を説明しますか"},
  {role: "user", content: "tokenについて"}
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

## 固定したtoy templateを追う

この教材の観察コードでは、各messageを次の規則で直列化します。

```text
<|role|>
content
```

すべてのmessageを並べた後、次のassistant応答を始めるために`<|assistant|>`を末尾へ加えます。
これは観察用に作った規則であり、実在するpretrained modelのtemplateではありません。

まず、上のmessagesへ規則を手作業で適用し、できあがる文字列を`work/week04/paper_notes.md`へ予想として書きます。
次に、以下を実行して直列化した文字列とtoken IDsを確認します。

```bash
uv run python course/week04/starter/chat_template_observation.py
```

問94、95では、生成結果ではなく、messages、template適用後の文字列、token IDsの関係を確認します。
外部モデルのdownloadや生成の再現はCoreの条件ではありません。
