def secure_archive(nom: str, mode: int, add: str) -> tuple[True | False, str]:
    try:
        n: str = f"ex3/{nom}"
        with open(n) as f:
            content = f.read()
        if mode == 0:
            return [True, content]
        elif mode == 1:
            if not add:
                raise 
            trans_lines: list[str] = []
            for line in content.split('\n'):
                if line:
                    trans_lines.append(line + add)
                else:
                    trans_lines.append(line)

            trans_content: str = '\n'.join(trans_lines)
            name = f"ex3/new_{nom}"

    except FileNotFoundError:
        return [False,
                f"[Errno 2] No such file or directory: '{nom}'"]
    except PermissionError:
        return [False,
                f"[Errno 13] Permission denied: '{nom}'"]


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")
    print()

    print("Using 'secure_archive' to read from a nonexistent file:")
    secure_archive("/not/existing/file", 0)
    print()

    print("Using 'secure_archive'to read from an inaccessible file:")
    secure_archive("/etc/master.passwd", 0)
    print()

    print("Using 'secure_archive'to read from an regular file:")
    secure_archive("text.txt", 0)
    print()

    print("Using 'secure_archive'to write previous content to a new file:")
    secure_archive("text.txt", 1)
