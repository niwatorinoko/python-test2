import os
import zipfile
from datetime import datetime, timedelta

# 作業ディレクトリと条件の設定
current_dir = os.getcwd()
backup_folder = os.path.join(current_dir, "backup")
file_extensions = ('.py', '.ipynb')  # 対象ファイル拡張子
exclude_folder = 'backup'
exclude_prefix = 'backup'

# 2週間前の日付を計算
two_weeks_ago = datetime.now() - timedelta(weeks=2)

# 日付の表示
print(f"N_Days_Before: {two_weeks_ago}")
print(f"Current Time: {datetime.now()}")

# 対象ファイルを収集
files_to_archive = []

for root, dirs, files in os.walk(current_dir):
    # 'backup' フォルダをスキップ
    if exclude_folder in root:
        continue
    
    for file in files:
        # 対象外ファイルをスキップ
        if file.startswith(exclude_prefix):
            continue
        
        # 対象ファイルかつ最近2週間以内に変更されたファイルを確認
        if file.endswith(file_extensions):
            file_path = os.path.join(root, file)
            file_mtime = datetime.fromtimestamp(os.path.getmtime(file_path))
            
            if file_mtime > two_weeks_ago:
                relative_path = os.path.relpath(file_path, current_dir)
                files_to_archive.append(relative_path)

# 圧縮前に対象ファイルを表示
# if files_to_archive:
#     print("\nFiles to be archived:")
#     for file in files_to_archive:
#         print(f"  {file}")
# else:
#     print("\nNo files to archive.")
#     exit()

# 'backup' フォルダを作成
if not os.path.exists(backup_folder):
    os.makedirs(backup_folder)

# 圧縮ファイルの名前を生成
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
zip_filename = f"test02_Q3_{timestamp}.zip"
zip_filepath = os.path.join(backup_folder, zip_filename)

# ファイルをZIPに圧縮
with zipfile.ZipFile(zip_filepath, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for file in files_to_archive:
        zipf.write(file)
        print(f"{file} -> archive succeeds.")

print(f"\n==> Compressed file saved as {zip_filepath}")
