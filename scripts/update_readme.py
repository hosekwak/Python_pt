"""programmers/ 폴더의 풀이 파일을 스캔해서
README.md의 풀이 기록 표를 자동으로 다시 생성하는 스크립트.

각 풀이 파일(.py) 맨 위에는 아래 형식의 메타데이터 주석이 있어야 합니다:

    # 번호: 12345
    # 문제: 두 수의 합
    # 난이도: Lv.1
    # 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12345
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
SOURCES = {
    "programmers": "프로그래머스",
}
START_MARK = "<!-- SOLUTIONS_TABLE_START -->"
END_MARK = "<!-- SOLUTIONS_TABLE_END -->"

FIELD_PATTERN = re.compile(r"^#\s*(번호|문제|난이도|링크)\s*:\s*(.+?)\s*$")


def parse_metadata(py_file: Path) -> dict:
    meta = {}
    with py_file.open(encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if not line.startswith("#"):
                break
            m = FIELD_PATTERN.match(line)
            if m:
                meta[m.group(1)] = m.group(2)
    return meta


def collect_rows() -> list[dict]:
    rows = []
    for folder, source_name in SOURCES.items():
        folder_path = ROOT / folder
        if not folder_path.exists():
            continue
        for py_file in sorted(folder_path.rglob("*.py")):
            meta = parse_metadata(py_file)
            rel_path = py_file.relative_to(ROOT).as_posix()
            title = meta.get("문제", py_file.stem)
            link = meta.get("링크")
            title_cell = f"[{title}]({link})" if link else title
            rows.append({
                "번호": meta.get("번호", ""),
                "문제": title_cell,
                "출처": source_name,
                "난이도": meta.get("난이도", ""),
                "풀이": f"[코드]({rel_path})",
                "_sort_source": folder,
                "_sort_num": int(meta["번호"]) if meta.get("번호", "").isdigit() else 0,
            })
    rows.sort(key=lambda r: (r["_sort_source"], r["_sort_num"]))
    return rows


def build_table(rows: list[dict]) -> str:
    if not rows:
        return "아직 등록된 풀이가 없습니다."
    header = "| 번호 | 문제 | 출처 | 난이도 | 풀이 |\n|---|---|---|---|---|"
    lines = [
        f"| {r['번호']} | {r['문제']} | {r['출처']} | {r['난이도']} | {r['풀이']} |"
        for r in rows
    ]
    return "\n".join([header, *lines])


def update_readme(table: str) -> None:
    content = README.read_text(encoding="utf-8")
    if START_MARK not in content or END_MARK not in content:
        raise SystemExit(f"README.md에 {START_MARK} / {END_MARK} 마커가 없습니다.")
    before, rest = content.split(START_MARK, 1)
    _, after = rest.split(END_MARK, 1)
    new_content = f"{before}{START_MARK}\n{table}\n{END_MARK}{after}"
    README.write_text(new_content, encoding="utf-8")


def main() -> None:
    rows = collect_rows()
    table = build_table(rows)
    update_readme(table)
    print(f"README.md 갱신 완료 ({len(rows)}개 풀이)")


if __name__ == "__main__":
    main()
