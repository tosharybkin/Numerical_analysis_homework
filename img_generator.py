import subprocess

def main():
    k = 0.5
    c = 0.1

    for _ in range(20):
        subprocess.run(
            [
                "python",
                "source.py",
                "--save",
                "--k",
                f"{k}",
                "--c",
                f"{c}"
            ]
        )

        k += 0.5
        c += 0.1

if __name__ == "__main__":
    main()
