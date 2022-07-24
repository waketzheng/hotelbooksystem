#!/usr/bin/env python
import subprocess
import sys
from pathlib import Path
from typing import List, Tuple


def get_part(s: str) -> str:
    choices = {"1": "patch", "2": "minor", "3": "major"}
    choices.update({v: v for v in choices.values()})
    try:
        return choices[s]
    except KeyError:
        print(f"Invalid part: {s!r}")
        sys.exit(1)


def run_and_echo(cmd: str) -> int:
    print("-->", cmd)
    return subprocess.run(cmd, shell=True).returncode


def get_current_version() -> str:
    r = subprocess.run(["poetry", "version", "-s"], capture_output=True)

    return r.stdout.decode().strip()


def exit_if_run_failed(cmd: str) -> None:
    if rc := run_and_echo(cmd):
        sys.exit(rc)


def bump():
    version = get_current_version()
    print(f"Current version: {version}")
    if sys.argv[1:]:
        part = get_part(sys.argv[1])
    else:
        tip = (
            "Choices:\n1. patch\n2. minor\n3. major\n\n"
            "Which one to bump?(Leave blank to use `patch`) "
        )
        if a := input(tip).strip():
            part = get_part(a)
        else:
            part = "patch"
    parse = '"(?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)"'
    cmd = (
        f'bumpversion --commit --parse {parse}'
        f" --current-version {version} {part} pyproject.toml"
    )
    if part != 'patch':
        cmd + ' --tag'
    exit_if_run_failed(cmd)
    exit_if_run_failed("git push && git push --tags && git log -1")


def _parse_extras(version_info: str, extras_tip: str) -> str:
    extras_info = version_info.split(extras_tip)[-1]
    return extras_info.split("[", 1)[-1].split("]")[0].replace('"', "")


def _build_args(package_lines: List[str], extras_tip: str) -> List[str]:
    args: List[str] = []
    for m in package_lines:
        package, version_info = m.split("=", 1)
        if (package := package.strip()).lower() == "python":
            continue
        if extras_tip in version_info:
            package += "[" + _parse_extras(version_info, extras_tip) + "]"
            args.append(f'"{package}@latest"')
        else:
            args.append(f"{package}@latest")
    return args


def _get_upgrade_args() -> Tuple[List[str], List[str]]:
    main_title = "[tool.poetry.dependencies]"
    dev_title = "[tool.poetry.dev-dependencies]"
    toml_file = Path(__file__).parent.resolve().parent / "pyproject.toml"
    text = toml_file.read_text("utf8").split(main_title)[-1]
    main, dev = text.split(dev_title)
    devs = dev.split("[tool.")[0].strip().splitlines()
    mains = main.strip().splitlines()
    extras_tip = "extras"
    return _build_args(mains, extras_tip), _build_args(devs, extras_tip)


def update():
    """升级所有依赖包到最新版"""
    main_args, dev_args = _get_upgrade_args()
    command = "poetry add"
    upgrade = "{0} {1} && {0} --dev {2}".format(
        command, " ".join(main_args), " ".join(dev_args)
    )
    exit_if_run_failed(upgrade)


def lint():
    """格式化加静态检查"""
    remove_imports = "autoflake --in-place --remove-all-unused-imports"
    cmd = ""
    paths = "."
    if args := sys.argv[1:]:
        paths = " ".join(args)
        if all(Path(i).is_file() for i in args):
            cmd = f"{remove_imports} {paths} && " + cmd
    lint_them = "{0} {2} {1} && {0} {3} {1} && {0} {4} {1} && {0} {5} {1}"
    tools = ("isort", "black", "pflake8", "mypy")
    cmd += lint_them.format("poetry run", paths, *tools)
    exit_if_run_failed(cmd)
