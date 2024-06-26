# 機械学習/データ分析の数学
:::note info
このドキュメントはQiitaのMarkdown形式に則っています。
:::
## 主成分分析
主成分分析（PCA）とは、多次元データの情報を損なわずに低次元空間に縮約する統計的な解析手法です。
:::note 
具体的には、複数の説明変数を、より少ない指標や合成変数に要約します。この要約は「次元の縮約」と呼ばれます。
:::
なぜ主成分分析を行うのでしょうか？それは、主成分分析に以下の３つのメリットがあるからです。
- データの可視化：<br>
高次元データを低次元空間に投影することで、データの構造や傾向を視覚的に理解しやすくなります。
- 次元削減：<br>
データの次元を削減することで、データ処理や機械学習の計算量を削減することができます。
- 特徴量抽出：<br>
データの重要な特徴を抽出することで、データ分析や機械学習のパフォーマンスを向上させることができます。