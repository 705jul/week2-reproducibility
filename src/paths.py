# src/paths.py

from pathlib import Path


def get_project_root(current_path: Path | None = None) -> Path:
    """
    현재 실행 위치를 기준으로 프로젝트 루트 경로를 반환한다.

    Notebook이 notebooks/ 폴더 안에서 실행되면
    부모 폴더를 프로젝트 루트로 본다.

    프로젝트 루트에서 실행되면
    현재 폴더를 프로젝트 루트로 본다.
    """
    if current_path is None:
        current_path = Path.cwd()

    current_path = Path(current_path).resolve()

    if current_path.name == "notebooks":
        return current_path.parent

    return current_path


def get_project_dirs(base_dir: Path | None = None) -> dict:
    """
    프로젝트에서 자주 사용하는 폴더 경로를 딕셔너리로 반환한다.

    반환되는 key:
    - base
    - raw
    - clean
    - feature
    - outputs
    - reports
    - notebooks
    - src
    """
    if base_dir is None:
        base_dir = get_project_root()

    base_dir = Path(base_dir).resolve()

    dirs = {
        "base": base_dir,
        "raw": base_dir / "data" / "raw",
        "clean": base_dir / "data" / "clean",
        "feature": base_dir / "data" / "feature",
        "outputs": base_dir / "outputs",
        "reports": base_dir / "reports" / "week2",
        "notebooks": base_dir / "notebooks",
        "src": base_dir / "src",
    }

    for path in dirs.values():
        path.mkdir(parents=True, exist_ok=True)

    return dirs
