#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd -- "$SCRIPT_DIR/../.." && pwd)"

die() {
	printf 'error: %s\n' "$1" >&2
	exit 1
}

require_command() {
	command -v "$1" >/dev/null 2>&1 || die "required command not found: $1"
}

require_command bash
require_command makepkg
require_command shellcheck

cd "$ROOT_DIR"

shellcheck tools/sh/*.sh packaging/archlinux/pkgbuilds/common/*.sh packaging/archlinux/src/usr/bin/argvus-ai
bash -n tools/sh/*.sh packaging/archlinux/pkgbuilds/common/*.sh packaging/archlinux/src/usr/bin/argvus-ai

metadata() {
	bash -c '
		source "$1"
		printf "%s\n" "$pkgname" "$pkgver" "$pkgrel" "$pkgdesc"
		printf "%s\n" "${arch[*]}" "${license[*]}" "${depends[*]}"
		printf "%s\n" "${makedepends[*]}" "${options[*]}"
	' bash "$1"
}

ci_metadata="$(metadata packaging/archlinux/pkgbuilds/remote/PKGBUILD)"
local_metadata="$(metadata packaging/archlinux/pkgbuilds/local/PKGBUILD)"
[[ "$ci_metadata" == "$local_metadata" ]] || die \
	"CI and local PKGBUILD metadata is out of sync"

for pkgbuild_dir in packaging/archlinux/pkgbuilds/remote packaging/archlinux/pkgbuilds/local; do
	pkgbuild="$pkgbuild_dir/PKGBUILD"
	[[ -f "$pkgbuild" ]] || die "missing $pkgbuild"
	(
		cd "$pkgbuild_dir"
		makepkg -p PKGBUILD --printsrcinfo >/dev/null
	)
done

if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then git diff --check; fi
luac -p packaging/archlinux/src/usr/share/argvus/ai/hyprland.lua
stylua --check packaging/archlinux/src/usr/share/argvus/ai/hyprland.lua
python3 tests/test_launcher.py
if [ -d ../argvus-taskbar ]; then python3 tests/test_integration.py; fi
for desktop in packaging/archlinux/src/usr/share/applications/*.desktop; do
  desktop-file-validate "$desktop"
done
printf 'Validation OK\n'
