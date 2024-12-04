import json
import csv
from pathlib import Path

# ファイルパス
data_folder = Path("python-test2/Test2/2023_fall_test02_questions/data")
grades_json_path = data_folder / "grades.json"
grades_new_json_path = data_folder / "grades_new.json"
grades_new_csv_path = data_folder / "grades_new.csv"
credits_all_txt_path = data_folder / "credits_all.txt"

# JSONデータを読み込む
with open(grades_json_path, "r", encoding="utf-8") as f:
    grades_data = json.load(f)

# 全科目を credits_all.txt から取得
with open(credits_all_txt_path, "r", encoding="utf-8") as f:
    all_courses = sorted([line.split(":")[0].strip() for line in f if line.strip()])

# 学生データを正規化
normalized_data = []
for student_id, grades in sorted(grades_data.items()):
    student_grades = {course: grades.get(course, "") for course in all_courses}
    normalized_data.append({
        "studentID": student_id,
        "grades": student_grades
    })

# 新しいJSONファイルに保存
with open(grades_new_json_path, "w", encoding="utf-8") as f:
    json.dump(normalized_data, f, indent=4, ensure_ascii=False)

# CSV形式に変換
csv_headers = ["StudentID"] + all_courses
csv_rows = []
for student in normalized_data:
    row = [student["studentID"]] + [student["grades"][course] for course in all_courses]
    csv_rows.append(row)

# CSVファイルを保存
with open(grades_new_csv_path, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(csv_headers)
    writer.writerows(csv_rows)

print(f"正規化されたJSONファイルを保存しました: {grades_new_json_path}")
print(f"正規化されたCSVファイルを保存しました: {grades_new_csv_path}")
