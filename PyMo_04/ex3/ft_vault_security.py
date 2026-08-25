def secure_archive(nom: str, mode: int, add: str) -> tuple[bool, str]:
    try:
        n: str = nom
        with open(n) as f:
            content = f.read()
        if mode == 0:
            return (True, content)
        elif mode == 1:
            # if not add:
            #     raise
            trans_lines: list[str] = []
            for line in content.split('\n'):
                if line:
                    trans_lines.append(line + add)
                else:
                    trans_lines.append(line)

            trans_content: str = '\n'.join(trans_lines)
            name = f"ex3/new_{nom}"
            new_file = open(name, "w")
            new_file.write(trans_content)
            new_file.close()
            return (True, "Content successfully written to file")

        return (False, "Invalid mode")

    except FileNotFoundError:
        return (False,
                f"[Errno 2] No such file or directory: '{nom}'")
    except PermissionError:
        return (False,
                f"[Errno 13] Permission denied: '{nom}'")


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")
    print()

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", 0, ""))
    print()

    print("Using 'secure_archive'to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd", 0, ""))
    print()

    print("Using 'secure_archive'to read from an regular file:")
    print(secure_archive("text.txt", 0, ""))
    print()

    print("Using 'secure_archive'to write previous content to a new file:")
    print(secure_archive("text.txt", 1, "hola"))
