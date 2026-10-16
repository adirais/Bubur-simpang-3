import datetime, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
src = (root / "src/index.src.html").read_text()
logo = pathlib.Path("/tmp/claude-0/trace/logo-path.txt")
d = logo.read_text() if logo.exists() else (root / "assets/logo.svg").read_text().split(' d="')[1].split('"')[0]
build = datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S")
(root / "index.html").write_text(src.replace("{{LOGO}}", d).replace("{{BUILD}}", build))
print("built", build, (root / "index.html").stat().st_size // 1024, "KB")
