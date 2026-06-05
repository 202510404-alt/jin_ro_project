import os
import ast
from pathlib import Path

def parse_python_file(file_path: Path):
    """파이썬 파일을 직접 열어서 구조(클래스, 함수, 메서드)를 실시간으로 해부합니다."""
    compact_symbols_info = []
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        tree = ast.parse(content)
        
        for node in tree.body:
            # 1. 클래스 정의 추적
            if isinstance(node, ast.ClassDef):
                base_names = [ast.unparse(b) for b in node.bases]
                class_sig = f"{node.name}({', '.join(base_names)})" if base_names else node.name
                compact_symbols_info.append(f"🧬 class {class_sig}")
                
                # 클래스 내부의 메서드들 추적
                for sub_node in node.body:
                    if isinstance(sub_node, ast.FunctionDef):
                        args_str = ast.unparse(sub_node.args).replace("\n", "").strip()
                        ret_str = f" -> {ast.unparse(sub_node.returns)}" if sub_node.returns else " -> Any"
                        compact_symbols_info.append(f"└─ def {sub_node.name}({args_str}){ret_str}")
                        
            # 2. 탑레벨 함수 정의 추적
            elif isinstance(node, ast.FunctionDef):
                args_str = ast.unparse(node.args).replace("\n", "").strip()
                ret_str = f" -> {ast.unparse(node.returns)}" if node.returns else " -> Any"
                compact_symbols_info.append(f"🎯 def {node.name}({args_str}){ret_str}")
                
    except Exception as e:
        compact_symbols_info.append(f"⚠️ [파싱 에러: {e}]")
        
    return compact_symbols_info

# 🔥 [수술 부위] 감시망(jjap_watcher.py)과 이름을 일치시키기 위해 예전 이름으로 복원했습니다!
def generate_ai_optimized_map():
    project_root = Path.cwd()
    output_file = project_root / "AI_CODEBASE_MAP.md"
    
    main_file = project_root / "main.py"
    src_dir = project_root / "src"
    
    EXCLUDE_KEYWORDS = [".venv", ".git", "__pycache__", "cline_tools"]
    
    target_files = []
    if main_file.exists():
        target_files.append(main_file)
        
    if src_dir.exists():
        for root, dirs, files in os.walk(src_dir):
            if any(k in root for k in EXCLUDE_KEYWORDS):
                continue
            for file in files:
                if file.endswith(".py"):
                    target_files.append(Path(root) / file)
                    
    target_files = sorted(target_files, key=lambda p: p.as_posix())

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# 🏗️ AI-OPTIMIZED ULTRA COMPACT CODEBASE MAP (DIRECT SOURCE SCAN)\n\n")
        f.write("> **[AI 프로토콜 매뉴얼]** 이 문서는 JSON 장부에 의존하지 않고, 하드디스크의 `main.py` 및 `src/` 내 모든 파이썬 소스코드를 직접 뒤져서 실시간 징집한 100% 무결점 인터페이스 지도입니다.\n\n")
        
        f.write("```markdown\n")
        f.write("project_root/\n")
        
        for file_path in target_files:
            rel_path = file_path.relative_to(project_root)
            parts = rel_path.parts
            
            indent = "│   " * (len(parts) - 1)
            file_name = parts[-1]
            
            symbols_info = parse_python_file(file_path)
            
            symbols_str = " | ".join(symbols_info)
            if symbols_str:
                f.write(f"{indent}├── {file_name} [{symbols_str}]\n")
            else:
                f.write(f"{indent}├── {file_name}\n")
                
        f.write("```\n")
    print(f"✅ [작업 완료] 외부 파일 의존성 없이 {len(target_files)}개의 코드를 전수조사하여 AI_CODEBASE_MAP.md를 강제 갱신했습니다!")

if __name__ == "__main__":
    # 🔥 여기도 함수 이름 싱크로율 패치
    generate_ai_optimized_map()