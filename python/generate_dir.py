from pathlib import Path


def main():
    Path(tgt_dir := f"./python/ABC_{input()}").mkdir()
    for problem in ["a", "b"]:
        Path(f"{tgt_dir}/{problem}.py").touch(exist_ok=False)


if __name__ == "__main__":
    main()
