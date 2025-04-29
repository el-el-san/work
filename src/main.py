"""
このスクリプトは「Hello, World!」というメッセージを標準出力に表示します。
これはPythonの基本的な機能を示すシンプルな例です。
"""

import sys

def main():
    """
    スクリプトのメインエントリーポイントです。
    標準出力に「Hello, World!」を表示します。
    基本的なエラーハンドリングを含みます。
    """
    try:
        # 「Hello, World!」メッセージを標準出力に表示
        print("Hello, World!")
    except Exception as e:
        # 標準出力への書き込み中にエラーが発生した場合の処理
        # 標準エラー出力にエラーメッセージを出力するのが一般的
        print(f"エラーが発生しました: {e}", file=sys.stderr)
        # エラーを示すために非ゼロの終了コードで終了
        sys.exit(1)

if __name__ == "__main__":
    # スクリプトが直接実行された場合にmain関数を呼び出す
    main()