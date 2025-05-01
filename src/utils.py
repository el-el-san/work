import os
import json
import csv
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

def read_text_file(file_path: str) -> Optional[str]:
    """
    指定されたパスのテキストファイルを読み込みます。

    Args:
        file_path: 読み込むファイルのパス。

    Returns:
        ファイルの内容を文字列として返します。
        ファイルが存在しない場合や読み込みエラーが発生した場合はNoneを返します。
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except IOError as e:
        print(f"Error reading file {file_path}: {e}")
        return None

def write_text_file(file_path: str, content: str, overwrite: bool = False) -> bool:
    """
    指定されたパスにテキストファイルを書き込みます。

    Args:
        file_path: 書き込むファイルのパス。
        content: 書き込む文字列の内容。
        overwrite: Trueの場合、既存のファイルを上書きします。
                   Falseの場合、ファイルが既に存在すると書き込みません。

    Returns:
        書き込みが成功した場合はTrue、失敗した場合はFalseを返します。
    """
    if not overwrite and os.path.exists(file_path):
        print(f"Error: File already exists at {file_path} and overwrite is false.")
        return False

    try:
        # ディレクトリが存在しない場合は作成
        dir_name = os.path.dirname(file_path)
        if dir_name and not os.path.exists(dir_name):
            os.makedirs(dir_name)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except IOError as e:
        print(f"Error writing file {file_path}: {e}")
        return False

def safe_get_from_dict(data: Dict[Any, Any], key: Any, default: Any = None) -> Any:
    """
    辞書からキーを使って安全に値を取得します。キーが存在しない場合はデフォルト値を返します。

    Args:
        data: データを取得する辞書。
        key: 取得したい値のキー。
        default: キーが存在しない場合に返すデフォルト値。デフォルトはNone。

    Returns:
        指定されたキーに対応する値、またはデフォルト値。
    """
    return data.get(key, default)

def format_datetime(dt: datetime, fmt: str = '%Y-%m-%d %H:%M:%S') -> str:
    """
    datetimeオブジェクトを指定されたフォーマットの文字列に変換します。

    Args:
        dt: フォーマットするdatetimeオブジェクト。
        fmt: フォーマット文字列（strftime形式）。デフォルトは '%Y-%m-%d %H:%M:%S'。

    Returns:
        フォーマットされた日付/時刻文字列。
    """
    try:
        return dt.strftime(fmt)
    except ValueError as e:
        print(f"Error formatting datetime with format '{fmt}': {e}")
        # エラー時はデフォルトのフォーマット、または元のdatetimeオブジェクトを文字列化して返すなど考慮
        # ここではエラーメッセージ付きで元のdatetimeオブジェクトの__str__表現を返す例
        return f"Error: {e} - Original: {dt}"
    except TypeError as e:
         print(f"Error: Input is not a datetime object: {e}")
         return str(dt) # 入力がdatetimeでない場合、元の入力の文字列表現を返す

def parse_csv_file(file_path: str, delimiter: str = ',', has_header: bool = True) -> Optional[List[Dict[str, str]]]:
    """
    CSVファイルを読み込み、リスト形式の辞書として解析します。

    Args:
        file_path: 読み込むCSVファイルのパス。
        delimiter: 列の区切り文字。デフォルトはカンマ。
        has_header: ファイルにヘッダー行があるか。Trueの場合、ヘッダーをキーとして使用します。

    Returns:
        CSVの内容を表す辞書のリスト。読み込みエラーや解析エラーが発生した場合はNoneを返します。
        has_headerがFalseの場合、キーは'col1', 'col2', ... となります。
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            if has_header:
                reader = csv.DictReader(f, delimiter=delimiter)
                return list(reader)
            else:
                reader = csv.reader(f, delimiter=delimiter)
                data = []
                for row in reader:
                    # ヘッダーがない場合、列番号をキーとする辞書を作成
                    row_dict = {f'col{i+1}': value for i, value in enumerate(row)}
                    data.append(row_dict)
                return data

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except csv.Error as e:
        print(f"Error parsing CSV file {file_path}: {e}")
        return None
    except IOError as e:
        print(f"Error reading file {file_path}: {e}")
        return None

def is_valid_email(email: str) -> bool:
    """
    簡単な正規表現を使ってメールアドレスの形式が有効かチェックします。
    (注意: このチェックは厳密ではありません。完全なバリデーションにはより複雑な正規表現やライブラリが必要です。)

    Args:
        email: チェックするメールアドレス文字列。

    Returns:
        形式が有効と思われる場合はTrue、そうでない場合はFalse。
    """
    import re
    # RFC 5322に完全には準拠しない、一般的なメールアドレス形式のチェック
    email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    return bool(email_regex.match(email))

# 必要に応じて他のヘルパー関数を追加してください
# 例: JSONファイルの読み書き、リストの重複削除、特定要素のフィルタリングなど