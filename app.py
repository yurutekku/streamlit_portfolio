import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import time
import openpyxl

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

# コード表示
code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')


st.header('レッスン４：データ入力と表示')

# テキスト入力
name = st.text_input('あなたの名前を入力してください')
if name:
    st.write(f'こんにちは、{name}さん！')


# 数値入力
age = st.number_input('あなたの年齢を入力してください', min_value=0, max_value=120, value=30)
st.write(f'あなたは{age}歳です。')


# 日付入力
date = st.date_input('日付を選択してください')
st.write(f'選択された日付：{date}')


# データフレームの表示
data = {
    '名前': ['太郎', '花子', '一郎'],
    '年齢': [25, 30, 35],
    '都市': ['東京', '大阪', '福岡'],
}

df = pd.DataFrame(data)

st.subheader('データフレームの表示')
st.dataframe(df)


# 表の表示
st.subheader('表の表示')
st.table(df)


st.header('レッスン５：折れ線グラフ(plotly,go)の作成')

# サンプルデータの作成
data = {
    '月': ['1月', '2月', '3月', '4月', '5月', '6月'],
    '売上': [100, 120, 140, 180, 200, 210],
    '利益': [20, 25, 30, 40, 50, 55]
}

df = pd.DataFrame(data)

st.write('サンプルデータ')
st.dataframe(df)


# 基本的な折れ線グラフの作成
fig = go.Figure()
fig.add_trace(go.Scatter(x=df['月'],
                         y=df['売上'],
                         mode='lines+markers',
                         name='売上'))
fig.add_trace(go.Scatter(x=df['月'],
                         y=df['利益'],
                         mode='lines+markers',
                         name='利益'))

fig.update_layout(title='月別売上と利益',
                  xaxis_title='月',
                  yaxis_title='金額（万円）')
st.plotly_chart(fig)


# カスタマイズされた折れ線グラフの作成
fig = go.Figure()
fig.add_trace(go.Scatter(
                x=df['月'],
                y=df['売上'],
                mode='lines+markers',
                name='売上',
                line=dict(color='blue',
                          width=2)))
fig.add_trace(go.Scatter(
                x=df['月'],
                y=df['利益'],
                mode='lines+markers',
                name='利益',
                line=dict(color='red',
                          width=2)))

fig.update_layout(
        title='月別売上と利益の推移',
        xaxis_title='月',
        yaxis_title='金額（万円）',
        font=dict(family="Meiryo",
                  size=12),
        legend=dict(orientation="h",
                    yanchor="bottom",
                    y=1.02,
                    xanchor="right",
                    x=1),
        hovermode="x unified"
        )

fig.update_xaxes(tickangle=45)
fig.update_yaxes(zeroline=True,
                 zerolinewidth=2,
                 zerolinecolor='lightgray')

st.plotly_chart(fig)


st.header('レッスン６：棒グラフ(plotly,go)の作成')

# サンプルデータの作成
data = {
    '製品': ['A', 'B', 'C', 'D', 'E'],
    '売上': [300, 400, 200, 600, 500],
    '利益': [30, 60, 20, 100, 80]
}

df = pd.DataFrame(data)

st.write('サンプルデータ：')
st.dataframe(df)


# 基本的な棒グラフの作成
fig = go.Figure()
fig.add_trace(go.Bar(x=df['製品'],
                     y=df['売上'],
                     name='売上'))
fig.add_trace(go.Bar(x=df['製品'],
                     y=df['利益'],
                     name='利益'))

fig.update_layout(title='製品別の売上と利益',
                  xaxis_title='製品',
                  yaxis_title='金額（万円）',
                  barmode='group')
st.plotly_chart(fig)


# カスタマイズされた棒グラフの作成
fig = go.Figure()
fig.add_trace(go.Bar(
                x=df['製品'],
                y=df['売上'],
                name='売上',
                marker_color='blue'))
fig.add_trace(go.Bar(
                x=df['製品'],
                y=df['利益'],
                name='利益',
                marker_color='red'))

fig.update_layout(
        title='製品別の売上と利益比較',
        xaxis_title='製品',
        yaxis_title='金額（万円）',
        barmode='group',
        font=dict(family="Meiryo",
                  size=12),
        legend=dict(orientation="h",
                    yanchor="bottom",
                    y=1.02,
                    xanchor="right",
                    x=1),
        hovermode="x unified"
        )

fig.update_traces(texttemplate='%{y}',
                  textposition='outside')
fig.update_yaxes(range=[0,
                        max(df['売上'].max(),
                            df['利益'].max()) * 1.1])

st.plotly_chart(fig)


# サンプルデータの作成
data = {
    '商品': ['A', 'B', 'C', 'D', 'E'],
    '売上': [300, 200, 180, 150, 120],
}

df = pd.DataFrame(data)
st.write('サンプルデータ：')
st.dataframe(df)


# 基本的な円グラフの作成
fig = go.Figure(data=[go.Pie(labels=df['商品'],
                             values=df['売上'])])
fig.update_layout(title='商品別売上比率')
st.plotly_chart(fig)


# カスタマイズされた円グラフの作成
colors = ['gold',
          'mediumturquoise',
          'darkorange',
          'lightgreen',
          'lightcoral']

fig = go.Figure(data=[go.Pie(labels=df['商品'],
                             values=df['売上'],
                             hole=.3,
                             marker=dict(colors=colors,
                                         line=dict(color='#000000',
                                                   width=2)))])

fig.update_traces(textposition='inside',
                  textinfo='percent+label',
                  hoverinfo='label+value+percent',
                  textfont_size=14)

fig.update_layout(
        title='商品別売上比率（詳細版）',
        font=dict(family="Meiryo",
                  size=12),
        legend=dict(orientation="h",
                    yanchor="bottom",
                    y=1.02,
                    xanchor="right",
                    x=1),
        annotations=[dict(text='総売上',
                          x=0.5,
                          y=0.5,
                          font_size=20,
                          showarrow=False)])

st.plotly_chart(fig)


# レッスン８：キャッシュを使用したパフォーマンス最適化
st.header('レッスン８：キャッシュを使用したパフォーマンス最適化')


def generate_large_dataset():
    # 大きなデータセットを生成（約10秒かかる）
    data = pd.DataFrame(np.random.randn(1000000, 5),
                        columns=['A', 'B', 'C', 'D', 'E'])
    return data


@st.cache_data
def load_data_cached():
    return generate_large_dataset()


def load_data_uncached():
    return generate_large_dataset()


st.subheader("キャッシュなしの場合")
start_time = time.time()
data_uncached = load_data_uncached()
end_time = time.time()
st.write(f"データ読み込み時間：{end_time - start_time: .2f} 秒")
st.write(data_uncached.head())


st.subheader("キャッシュありの場合")
start_time = time.time()
data_cached = load_data_cached()
end_time = time.time()
st.write(f"データ読み込み時間：{end_time - start_time: .2f} 秒")
st.write(data_cached.head())

st.write("キャッシュありの場合、２回目以降の読み込みは非常に高速になります・")


# 大規模データセットの処理
@st.cache_resource
def load_large_dataset():
    return pd.DataFrame(
        np.random.randn(1000000, 5),
        columns=['A', 'B', 'C', 'D', 'E']
    )


st.subheader("大規模データセットの処理")
start_time = time.time()
large_data = load_large_dataset()
end_time = time.time()
st.write(f"データ読み込み時間：{end_time - start_time: .2f} 秒")
st.write(f"データセットの形状：{large_data.shape}")
st.write(large_data.head())


# キャッシュの無効化
@st.cache_data(ttl=10)
def get_current_time():
    return pd.Timestamp.now()


st.subheader("キャッシュの無効化")
st.write("現在時刻（10秒ごとに更新）:")
st.write(get_current_time())


# レッスン９：セッション状態の管理
st.header('レッスン９：セッション状態の管理')

if 'count' not in st.session_state:
    st.session_state.count = 0


st.write(f"現在のカウント：{st.session_state.count}")


if st.button('カウントアップ'):
    st.session_state.count += 1
    st.rerun()


# フォーム入力の保持
st.subheader("フォーム入力の保持")

if 'user_name' not in st.session_state:
    st.session_state.user_name = ""

if 'user_email' not in st.session_state:
    st.session_state.user_email = ""

user_name = st.text_input("ユーザ名", value=st.session_state.user_name)
user_email = st.text_input("メールアドレス", value=st.session_state.user_email)

if st.button('ユーザー情報を保存'):
    st.session_state.user_name = user_name
    st.session_state.user_email = user_email
    st.success("ユーザー情報が保存されました！")

st.write(f"セッションに保存されたユーザー名：{st.session_state.user_name}")
st.write(f"セッションに保存されたメールアドレス：{st.session_state.user_email}")


# データフレームの状態管理
st.subheader("データフレームの状態管理")

if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame(columns=['商品', '価格'])

product = st.text_input("商品名を入力")
price = st.number_input("価格を入力", min_value=0)

if st.button('商品データを追加'):
    new_data = pd.DataFrame({'商品': [product], '価格': [price]})
    st.session_state.df = pd.concat(
                 [st.session_state.df, new_data],
                 ignore_index=True)

st.write("現在の商品データ：")
st.write(st.session_state.df)

if st.button('データをリセット'):
    st.session_state.df = pd.DataFrame(columns=['商品', '価格'])
    st.rerun()


# レッスン１０：ボタンとチェックボックス
st.header('レッスン１０：ボタンとチェックボックス')

if st.button('データを生成', key='generate_data'):
    random_data = pd.DataFrame(np.random.randn(20, 3), columns=['X', 'Y', 'Z'])
    st.write(random_data)

# チェックボックス
st.subheader('チェックボックス')

show_chart = st.checkbox('チャートを表示', key='show_chart')
if show_chart:
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['X', 'Y', 'Z'])
    fig = go.Figure()
    for column in chart_data.columns:
        fig.add_trace(
            go.Scatter(
                x=chart_data.index,
                y=chart_data[column],
                mode='lines',
                name=column
            )
        )
    st.plotly_chart(fig)


# ボタンを使った複数の操作
st.subheader('ボタンを使った複数の操作')

if 'counter' not in st.session_state:
    st.session_state.counter = 0

col1, col2, col3 = st.columns(3)

if col1.button('カウントアップ', key='count_up'):
    st.session_state.counter += 1

if col2.button('カウントダウン', key='count_down'):
    st.session_state.counter -= 1

if col3.button('リセット', key='reset_count'):
    st.session_state.counter = 0

st.write(f"現在のカウント：{st.session_state.counter}")


# チェックボックスを使った条件付き表示
st.subheader('チェックボックスを使った条件付き表示')

column_options = st.multiselect(
    '表示する列を選択してください',
    ['X', 'Y', 'Z'],
    ['X', 'Y', 'Z'],
    key='column_selection')

sample_data = pd.DataFrame(
    np.random.randn(10, 3),
    columns=['X', 'Y', 'Z']
    )

st.write(sample_data[column_options])


# レッスン１１：スライダーとセレクトボックス
st.header('レッスン１１：スライダーとセレクトボックス')

# スライダー
st.subheader('スライダー')

sample_size = st.slider(
    'サンプルサイズを選択',
    min_value=10,
    max_value=1000,
    value=100,
    step=10,
    key='sample_slider'
    )

data_sample1 = pd.DataFrame(
    np.random.randn(sample_size, 2),
    columns=['X', 'Y']
    )

fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=data_sample1['X'],
                          y=data_sample1['Y'],
                          mode='markers'))
st.plotly_chart(fig1)


# 範囲スライダー
st.subheader('範囲スライダー')

data_sample2 = pd.DataFrame(
    np.random.uniform(0, 100,
                      size=(1000, 2)),
    columns=['P', 'Q']
    )

range_values = st.slider(
    '値の範囲を選択',
    min_value=0.0,
    max_value=100.0,
    value=(25.0, 75.0),
    key='range_slider'
    )

filtered_data = data_sample2[(data_sample2['P'] >= range_values[0]) &
                             (data_sample2['P'] <= range_values[1])]

fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=filtered_data['P'],
                          y=filtered_data['Q'],
                          mode='markers'))
st.plotly_chart(fig2)


# セレクトボックス
st.subheader('セレクトボックス')

data_sample3 = pd.DataFrame(
    np.random.randn(200, 2),
    columns=['M', 'N']
    )

color_option = st.selectbox(
    'マーカーの色を選択',
    ['blue',
     'red',
     'green',
     'purple'],
    key='color_select')

fig3 = go.Figure()
fig3.add_trace(go.Scatter(x=data_sample3['M'],
                          y=data_sample3['N'],
                          mode='markers',
                          marker=dict(color=color_option)))
st.plotly_chart(fig3)


# マルチセレクトとスライダーの組み合わせ
st.subheader('マルチセレクトとスライダーの組み合わせ')

columns_to_plot = st.multiselect(
    'プロットする列を選択',
    ['A', 'B', 'C', 'D'],
    default=['A', 'B'],
    key='column_multiselect')

num_points = st.slider(
    'データポイント数',
    min_value=50,
    max_value=1000,
    value=200,
    step=50,
    key='points_slider'
    )

data_sample4 = pd.DataFrame(
    np.random.randn(num_points, 4),
    columns=['A', 'B', 'C', 'D']
    )

fig4 = go.Figure()
for col in columns_to_plot:
    fig4.add_trace(
        go.Scatter(
            x=data_sample4.index,
            y=data_sample4[col],
            mode='lines+markers',
            name=col
        )
    )
st.plotly_chart(fig4)


# レッスン１２：ファイルアップローダー
st.header('レッスン１２：ファイルアップローダー')

# CSVファイルのアップロードと表示
st.subheader('CSVファイルのアップロードと表示')

uploaded_csv = st.file_uploader(
    "CSVファイルをアップロードしてください",
    type="csv",
    key="csv_uploader")

if uploaded_csv is not None:
    df_csv = pd.read_csv(uploaded_csv)
    st.write("アップロードされたCSVファイルの内容：")
    st.write(df_csv)

    st.write("データの基本統計：")
    st.write(df_csv.describe())

    # 数値列の選択
    numeric_columns = df_csv.select_dtypes(
        include=[np.number]).columns.tolist()
    selected_column = st.selectbox(
        "グラフ化する列を選択してください",
        numeric_columns,
        key="csv_column_select")

    # ヒストグラムの作成
    fig = go.Figure(data=[go.Histogram(x=df_csv[selected_column])])
    fig.update_layout(title=f"{selected_column}のヒストグラム")
    st.plotly_chart(fig)


# Excelファイルのアップロードと表示
st.subheader('Excelファイルのアップロードと表示')

uploaded_excel = st.file_uploader(
    "Excelファイルをアップロードしてください",
    type=["xlsx", "xls"],
    key="excel_uploader")

if uploaded_excel is not None:
    excel_file = openpyxl.load_workbook(uploaded_excel)
    sheet_names = excel_file.sheetnames

    st.write("シート名：")
    st.write(sheet_names)

    selected_sheet = st.radio(
        "分析するシートを選択してください",
        sheet_names,
        key="sheet_selector")

    df_excel = pd.read_excel(
        uploaded_excel,
        sheet_name=selected_sheet)
    st.write(f"選択されシート '{selected_sheet}' の内容：")
    st.write(df_excel)

    # 列の選択
    selected_columns = st.multiselect(
        "表示する列を選択してください",
        df_excel.columns.tolist(),
        key="excel_column_select")

    if selected_columns:
        st.write("選択された列のデータ：")
        st.write(df_excel[selected_columns])

        # 散布図の作成（２つの列が選択された場合）
        if len(selected_columns) == 2:
            fig = go.Figure(data=go.Scatter(x=df_excel[selected_columns[0]],
                                            y=df_excel[selected_columns[1]],
                                            mode='markers'))
            fig.update_layout(
                title=f"{selected_columns[0]} vs {selected_columns[1]} の散布図")
            st.plotly_chart(fig)


# レッスン１３：カラムとコンテナによるレイアウト
st.header("レッスン１３：カラムとコンテナによるレイアウト")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("列１")
    st.write("ここは１列目です。")
    st.button("ボタン１", key="button1")

with col2:
    st.subheader("列２")
    st.write("ここは２列目です。")
    st.checkbox("チェックボックス", key="checkbox1")

with col3:
    st.subheader("列３")
    st.write("ここは３列目です。")
    st.radio("ラジオボタン", ["選択肢１", "選択肢２", "選択肢３"], key="radio1")


# 異なる幅のカラム
st.subheader("異なる幅のカラム")

col_left, col_right = st.columns([2, 1])

with col_left:
    st.subheader("左側（幅広）")
    chart_data = pd.DataFrame(
                    np.random.randn(20, 3),
                    columns=["A", "B", "C"])
    selected_column = st.selectbox(
                     "データを選択",
                     ["A", "B", "C"],
                     key="data_select")
    st.line_chart(chart_data[selected_column])

with col_right:
    st.subheader("右側（幅狭）")
    st.write(f"選択されたデータ： {selected_column}")
    st.write(f"平均値： {chart_data[selected_column].mean():.2f}")
    st.write(f"最大値： {chart_data[selected_column].max():.2f}")
    st.write(f"最小値： {chart_data[selected_column].min():.2f}")

# コンテナの使用
st.subheader("コンテナの使用")

with st.container():
    st.subheader("データ分析セクション")
    st.write("このコンテナ内にデータ分析関連の要素をグループ化します")

    data_container = st.container()

    data = pd.DataFrame({
        '名前': ['Alice', 'Bob', 'Charlie', 'David'],
        '年齢': [25, 30, 35, 40],
        '都市': ['東京', '大阪', '名古屋', '福岡'],
    })

    data_container.dataframe(data)

    analysis_type = st.radio(
        "分析タイプ",
        ["平均年齢", "都市別人数"],
        key="analysis_type")

    if analysis_type == "平均年齢":
        data_container.write(f"平均年齢：{data['年齢'].mean(): .1f}歳")
    else:
        data_container.write(data['都市'].value_counts())


# ネストされたレイアウト
st.subheader("ネストされたレイアウト")

col1, col2 = st.columns(2)

with col1:
    st.write("左側のカラム")
    with st.container():
        st.write("左側のコンテナ")
        slider_value = st.slider(
             "値の選択",
             0,
             100,
             50,
             key="nested_slider")

with col2:
    st.write("右側のカラム")
    with st.container():
        st.write("右側の上部コンテナ")
        option = st.selectbox(
            "オプションを選択",
            ["オプション１",
             "オプション２",
             "オプション３"],
            key="nested_select")

    with st.container():
        st.write("右側の下部コンテナ")
        if st.button(
                    "クリックしてください",
                    key="nested_button"):
            st.write("ボタンがクリックされました！")


# レッスン１４：エクスパンダーとサイドバーによるレイアウト
st.header("レッスン１４：エクスパンダーとサイドバーによるレイアウト")

st.subheader("エクスパンダーの使用例")

# １年分のデータを生成
sales_data = pd.DataFrame({
    '日付': pd.date_range(start='2023-01-01', end='2023-12-31'),
    '売上': np.random.randint(1000, 5000, 365),
    '商品': np.random.choice(['A', 'B', 'C'], 365)
})

with st.expander("データセットの詳細を表示"):
    st.dataframe(sales_data)

with st.expander("グラフを表示"):
    fig = go.Figure(
              data=go.Scatter(
                  x=sales_data['日付'],
                  y=sales_data['売上'],
                  mode='lines+markers'))
    fig.update_layout(title='日別売上推移')
    st.plotly_chart(fig)

with st.expander("統計情報"):
    st.write(f"総売上：{sales_data['売上'].sum(): ,}円")
    st.write(f"平均売上：{sales_data['売上'].mean(): .2f}円")
    st.write(f"最高売上：{sales_data['売上'].max(): ,}円")
    st.write(f"最低売上：{sales_data['売上'].min(): ,}円")


# サイドバーの使用例
st.subheader("サイドバーの使用例")

st.sidebar.title("データ分析ツール")

analysis_option = st.sidebar.radio(
    "分析オプション",
    ("データ概要", "売上分析", "商品別分析")
)

date_range = st.sidebar.date_input(
   "日付範囲",
   value=(sales_data['日付'].min().date(),
          sales_data['日付'].max().date())
)

filtered_data = sales_data[
    (sales_data['日付'].dt.date >= date_range[0]) &
    (sales_data['日付'].dt.date <= date_range[1])]

if filtered_data.empty:
    st.sidebar.info(
        "選択された日付範囲にデータがありません。別の範囲を選択してください")
else:
    if analysis_option == "データ概要":
        st.write("選択された分析オプション： データ概要")
        st.dataframe(filtered_data)
    elif analysis_option == "売上分析":
        st.write("選択された分析オプション： 売上分析")
        st.line_chart(filtered_data.set_index('日付')['売上'])
    else:
        st.write("選択された分析オプション： 商品別分析")
        product_sales = filtered_data.groupby('商品')['売上'].sum().reset_index()
        st.bar_chart(product_sales.set_index('商品'))


# 高度なエクスパンダーの使用例
st.subheader("高度なエクスパンダーの使用例")

with st.expander("カスタム分析"):
    selected_product = st.selectbox("分析する商品を選択", sales_data['商品'].unique())
    product_data = filtered_data[filtered_data['商品'] == selected_product]

    if product_data.empty:
        st.info("選択された日付範囲との商品の組み合わせにデータがありません。")
    else:
        st.write(f"商品 {selected_product} の分析")
        st.line_chart(product_data.set_index('日付')['売上'])

        if st.checkbox("詳細統計を表示"):
            st.write(product_data['売上'].describe())


# レッスン１７：Streamlit Cloud アプリケーションのメンテナンスと管理
st.header("レッスン１７：Streamlit Cloud アプリケーションのメンテナンスと管理")
st.write("Streamlit Cloud にアプリ公開後に修正した内容が自動的に反映されるかを確認します（本文が表示されたら成功！！）")
