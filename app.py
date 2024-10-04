import streamlit as st

# タイトルの設定
st.title('StreamlitによるApp')

# ヘッダーテキストの設定
st.header('レッスン３：テキスト要素の追加')

# 通常のテキスト
st.write('これは通常のテキストです。')

# Markdown形式のテキスト
st.markdown('これは **太字** で、*イタリック* です。')

# LaTeX形式の数式
st.latex(r'\sqrt{x^2 + y^2} = z')

# 情報メッセージ（青色）
st.info('データの読み込みが完了しました。')

# 警告メッセージ（黄色）
st.warning('ファイルのサイズが大きいため、処理に時間がかかる可能性があります。')

# エラーメッセージ（赤色）
st.error('ファイルの形式が正しくありません。CSVファイルをアップロードしてください。')

# 成功メッセージ（緑色）
st.success('グラフの作成が完了しました。')


code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')
