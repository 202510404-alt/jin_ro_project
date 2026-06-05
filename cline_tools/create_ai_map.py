import os
import ast
from pathlib import Path

def parse_python_file(file_path: Path):
    """[형님 원본 100% 보존] 파이썬 소스코드를 직접 열어 실시간으로 라인 범위, 클래스/함, 전역 변수, 임포트를 징집합니다."""
    compact_symbols_info = []
    imports = []
    global_vars = []
    structural_symbols = []
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        tree = ast.parse(content)
        
        for node in tree.body:
            # 1. 외부 모듈 임포트 추적
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        imports.append(alias.name)
                else:
                    module_name = node.module or ""
                    for alias in node.names:
                        imports.append(f"{module_name}.{alias.name}" if module_name else alias.name)
            
            # 2. 탑레벨 중요 전역 변수/상수 추적
            elif isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        global_vars.append(target.id)
                        
            # 3. 클래스 정의 및 내부 구조 추적
            elif isinstance(node, ast.ClassDef):
                start = node.lineno
                end = getattr(node, "end_lineno", start)
                base_names = [ast.unparse(b) for b in node.bases]
                class_sig = f"{node.name}({', '.join(base_names)})" if base_names else node.name
                
                structural_symbols.append(f"🧬 class {class_sig} [L{start}-{end}]")
                
                for sub_node in node.body:
                    if isinstance(sub_node, ast.FunctionDef):
                        m_start = sub_node.lineno
                        m_end = getattr(sub_node, "end_lineno", m_start)
                        args_str = ast.unparse(sub_node.args).replace("\n", "").strip()
                        ret_str = f" -> {ast.unparse(sub_node.returns)}" if sub_node.returns else " -> Any"
                        structural_symbols.append(f"  └─ def {sub_node.name}({args_str}){ret_str} [L{m_start}-{m_end}]")
                        
            # 4. 탑레벨 함수 정의 추적
            elif isinstance(node, ast.FunctionDef):
                start = node.lineno
                end = getattr(node, "end_lineno", start)
                args_str = ast.unparse(node.args).replace("\n", "").strip()
                ret_str = f" -> {ast.unparse(node.returns)}" if node.returns else " -> Any"
                structural_symbols.append(f"🎯 def {node.name}({args_str}){ret_str} [L{start}-{end}]")
                
        meta_parts = []
        if imports:
            meta_parts.append(f"📦 imp: {', '.join(imports[:4])}" + ("..." if len(imports) > 4 else ""))
        if global_vars:
            meta_parts.append(f"💾 var: {', '.join(global_vars[:4])}" + ("..." if len(global_vars) > 4 else ""))
            
        if meta_parts:
            compact_symbols_info.append(f"💡 {' / '.join(meta_parts)}")
        compact_symbols_info.extend(structural_symbols)
                
    except Exception as e:
        compact_symbols_info.append(f"⚠️ [파싱 에러: {e}]")
        
    return compact_symbols_info

def generate_ai_optimized_map():
    """실시간으로 전 코드를 뒤져 라인 범위가 포함된 AI 최적화 초경량 지도를 생성합니다. (경로 추적 패치완료)"""
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
        f.write("# 🏗️ AI-OPTIMIZED ULTRA COMPACT CODEBASE MAP (INTELLIGENT SCAN)\n\n")
        f.write("> **[AI 프로토콜 매뉴얼]** 이 문서는 다른 AI 비서들의 경로 오해를 차단하기 위해 파일마다 **실제 하드디스크 상대 경로 `[📂 실제경로]`**를 강제 명시해 둔 특수 지도입니다.\n")
        f.write("> AI 비서는 절대 눈치로 경로를 추측하지 말고, 파일명 뒤에 박혀있는 `[📂 실제경로]` 규격을 그대로 복사하여 agent_navigator를 호출하십시오.\n\n")
        
        f.write("```markdown\n")
        f.write("project_root/\n")
        
        # 중간 폴더 출력을 추적하기 위한 집합(Set)
        printed_dirs = set()
        
        for file_path in target_files:
            rel_path = file_path.relative_to(project_root)
            parts = rel_path.parts
            
            # 🔥 [수정 포인트]: 파일이 위치한 부모 폴더 경로들을 트리 구조로 먼저 그려줍니다.
            for i in range(1, len(parts)):
                current_dir_parts = parts[:i]
                current_dir_path = Path(*current_dir_parts)
                
                if current_dir_path not in printed_dirs:
                    dir_indent = "│   " * (i - 1)
                    f.write(f"{dir_indent}├── {parts[i-1]}/\n")
                    printed_dirs.add(current_dir_path)
            
            # 최종 파일의 인덴트 및 이름 설정
            indent = "│   " * (len(parts) - 1)
            file_name = parts[-1]
            posix_rel_path = rel_path.as_posix() # 다른 AI 호환용 슬래시 통일
            
            # 형님의 오리지널 AST 실시간 파서 호출
            symbols_info = parse_python_file(file_path)
            symbols_str = " | ".join(symbols_info) if symbols_info else ""
            
            # 🔥 [핵심 수정]: 파일명 바로 뒤에 [📂 실제상대경로]를 무조건 박아버림!
            if symbols_str:
                f.write(f"{indent}├── {file_name} [📂 {posix_rel_path}] -> [{symbols_str}]\n")
            else:
                f.write(f"{indent}├── {file_name} [📂 {posix_rel_path}]\n")
                
        f.write("```\n")
    print(f"✅ [작업 완료] 형님의 AST 실시간 파서 유지! 다른 AI의 경로 오해를 막기 위해 디렉토리 트리와 [📂 실제상대경로] 가이드를 확실히 이식했습니다!")

if __name__ == "__main__":
    generate_ai_optimized_map()