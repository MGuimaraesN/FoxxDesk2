#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
apply_foxxdesk_rebrand_standalone_v9.py

Versão standalone sem ZIP/payload embutido.

O que mudou em relação ao v7/v8:
- Não existe _PAYLOAD_B64.
- Não carrega ZIP de referência, nem espelha arquivos inteiros.
- Por padrão aplica somente correções críticas/build em arquivos seguros.
- Use --profile full para rebrand textual na allowlist completa.
- Preserva URLs/dependências upstream de rustdesk-org e nomes internos sensíveis.
- Corrige Cargo.lock de forma cirúrgica para builds com --locked.
- Mantém --dry-run, --apply, backup automático e relatório.

Importante:
- Esta versão é mais limpa e auditável, mas não cria arquivos textuais grandes a
  partir do ZIP antigo. Quando precisa renomear um arquivo, ela copia o arquivo
  antigo para o novo nome e aplica as regras no conteúdo.
"""
from __future__ import annotations

import argparse
import codecs
import datetime as _dt
import hashlib
import re
import shutil
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

SCRIPT_VERSION = "v9-standalone-safe-no-payload-2026-07-01"
APP_DISPLAY_NAME = "FoxxDesk"
APP_SLUG = "foxxdesk"
APP_SLUG_UPPER = "FOXXDESK"
DEFAULT_SERVER = "foxxdesk.mguimaraesn.dev"
DEFAULT_KEY = "6WbpsDtYMwUca74qNvNaBfV4pUIGzyXnX1Q8V8fZ8YA="
DEFAULT_MAINTAINER_EMAIL = "mateus@mguimaraesn.dev"

BINARY_EXTS = {
    ".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".icns", ".exe", ".dll",
    ".so", ".dylib", ".bin", ".zip", ".tar", ".gz", ".pdf", ".ttf", ".otf",
    ".woff", ".woff2", ".7z", ".xz", ".a", ".lib", ".mp4", ".mov", ".apk", ".dmg"
}

SKIP_DIRS = {
    ".git", ".github/cache", ".rebrand_backup", "target", "build", "dist", "node_modules",
    "flutter/build", "flutter/.dart_tool", "flutter/.pub-cache", "flutter/ephemeral",
}

ALLOWED_FILES: List[str] = [
    '.github/FUNDING.yml',
    '.github/ISSUE_TEMPLATE/bug_report.yaml',
    '.github/workflows/bridge.yml',
    '.github/workflows/fdroid.yml',
    '.github/workflows/flutter-build.yml',
    '.github/workflows/flutter-ci.yml',
    '.github/workflows/flutter-nightly.yml',
    '.github/workflows/flutter-tag.yml',
    '.github/workflows/foxxdesk-build.yml',
    '.github/workflows/playground.yml',
    '.gitignore',
    'AGENTS.md',
    'BRAND_CHANGELOG.md',
    'Cargo.toml',
    'Cargo.lock',
    'Dockerfile',
    'FOXXDESK_MAX_SAFE_BRAND_REPORT.md',
    'FOXXDESK_SERVER_DEFAULTS.md',
    'NOTICE.md',
    'README.md',
    'appimage/AppImageBuilder-aarch64.yml',
    'appimage/AppImageBuilder-x86_64.yml',
    'build.py',
    'docs/CONTRIBUTING-DE.md',
    'docs/CONTRIBUTING-FR.md',
    'docs/CONTRIBUTING-ID.md',
    'docs/CONTRIBUTING-IT.md',
    'docs/CONTRIBUTING-JP.md',
    'docs/CONTRIBUTING-KR.md',
    'docs/CONTRIBUTING-NL.md',
    'docs/CONTRIBUTING-NO.md',
    'docs/CONTRIBUTING-PL.md',
    'docs/CONTRIBUTING-RO.md',
    'docs/CONTRIBUTING-RU.md',
    'docs/CONTRIBUTING-TR.md',
    'docs/CONTRIBUTING-ZH.md',
    'docs/CONTRIBUTING.md',
    'docs/README-AR.md',
    'docs/README-CS.md',
    'docs/README-DA.md',
    'docs/README-DE.md',
    'docs/README-EO.md',
    'docs/README-ES.md',
    'docs/README-FA.md',
    'docs/README-FI.md',
    'docs/README-FR.md',
    'docs/README-GR.md',
    'docs/README-HU.md',
    'docs/README-ID.md',
    'docs/README-IT.md',
    'docs/README-JP.md',
    'docs/README-KR.md',
    'docs/README-ML.md',
    'docs/README-NL.md',
    'docs/README-NO.md',
    'docs/README-PL.md',
    'docs/README-PTBR.md',
    'docs/README-RO.md',
    'docs/README-RU.md',
    'docs/README-TR.md',
    'docs/README-UA.md',
    'docs/README-VN.md',
    'docs/README-ZH.md',
    'docs/SECURITY-DE.md',
    'docs/SECURITY-FR.md',
    'docs/SECURITY-IT.md',
    'docs/SECURITY-JP.md',
    'docs/SECURITY-KR.md',
    'docs/SECURITY-NL.md',
    'docs/SECURITY-NO.md',
    'docs/SECURITY-PL.md',
    'docs/SECURITY-RO.md',
    'docs/SECURITY-TR.md',
    'docs/SECURITY.md',
    'entrypoint.sh',
    'fastlane/metadata/android/en-US/full_description.txt',
    'fastlane/metadata/android/fr-FR/full_description.txt',
    'fastlane/metadata/android/nl-NL/full_description.txt',
    'fastlane/metadata/android/zh-CN/full_description.txt',
    'flatpak/com.foxxdesk.client.metainfo.xml',
    'flatpak/foxxdesk.json',
    'flutter/.gitignore',
    'flutter/android/app/build.gradle',
    'flutter/android/app/src/main/AndroidManifest.xml',
    'flutter/android/app/src/main/kotlin/com/carriez/flutter_hbb/BootReceiver.kt',
    'flutter/android/app/src/main/kotlin/com/carriez/flutter_hbb/FloatingWindowService.kt',
    'flutter/android/app/src/main/kotlin/com/carriez/flutter_hbb/MainService.kt',
    'flutter/android/app/src/main/res/values/strings.xml',
    'flutter/build_android_deps.sh',
    'flutter/build_fdroid.sh',
    'flutter/build_ios.sh',
    'flutter/ios/Runner.xcodeproj/project.pbxproj',
    'flutter/ios/Runner.xcodeproj/xcshareddata/xcschemes/Runner.xcscheme',
    'flutter/ios/Runner/GoogleService-Info.plist',
    'flutter/ios/Runner/Info.plist',
    'flutter/ios/exportOptions.plist',
    'flutter/lib/common.dart',
    'flutter/lib/common/widgets/dialog.dart',
    'flutter/lib/common/widgets/login.dart',
    'flutter/lib/common/widgets/toolbar.dart',
    'flutter/lib/consts.dart',
    'flutter/lib/desktop/pages/desktop_setting_page.dart',
    'flutter/lib/mobile/pages/settings_page.dart',
    'flutter/lib/models/group_model.dart',
    'flutter/lib/models/model.dart',
    'flutter/lib/models/native_model.dart',
    'flutter/lib/plugin/manager.dart',
    'flutter/lib/plugin/widgets/desc_ui.dart',
    'flutter/lib/utils/multi_window_manager.dart',
    'flutter/lib/utils/platform_channel.dart',
    'flutter/linux/CMakeLists.txt',
    'flutter/linux/main.cc',
    'flutter/linux/my_application.cc',
    'flutter/macos/Runner.xcodeproj/project.pbxproj',
    'flutter/macos/Runner.xcodeproj/xcshareddata/xcschemes/Runner.xcscheme',
    'flutter/macos/Runner/Base.lproj/MainMenu.xib',
    'flutter/macos/Runner/Configs/AppInfo.xcconfig',
    'flutter/macos/Runner/Info.plist',
    'flutter/macos/Runner/MainFlutterWindow.swift',
    'flutter/pubspec.yaml',
    'flutter/windows/CMakeLists.txt',
    'flutter/windows/runner/Runner.rc',
    'flutter/windows/runner/main.cpp',
    'libs/clipboard/README.md',
    'libs/clipboard/src/lib.rs',
    'libs/clipboard/src/platform/unix/fuse/mod.rs',
    'libs/clipboard/src/platform/unix/macos/README.md',
    'libs/clipboard/src/platform/unix/macos/pasteboard_context.rs',
    'libs/enigo/src/linux/xdo.rs',
    'libs/hbb_common/src/config.rs',
    'libs/hbb_common/src/fs.rs',
    'libs/hbb_common/src/platform/linux.rs',
    'libs/hbb_common/src/platform/mod.rs',
    'libs/portable/Cargo.lock',
    'libs/portable/Cargo.toml',
    'libs/portable/generate.py',
    'libs/portable/src/bin_reader.rs',
    'libs/portable/src/main.rs',
    'libs/remote_printer/src/lib.rs',
    'libs/remote_printer/src/setup/driver.rs',
    'libs/scrap/examples/capture_mag.rs',
    'libs/scrap/src/dxgi/mag.rs',
    'libs/virtual_display/dylib/src/lib.rs',
    'libs/virtual_display/dylib/src/win10/IddController.c',
    'res/DEBIAN/postinst',
    'res/DEBIAN/postrm',
    'res/DEBIAN/preinst',
    'res/DEBIAN/prerm',
    'res/PKGBUILD',
    'res/foxxdesk-link.desktop',
    'res/foxxdesk.desktop',
    'res/foxxdesk.service',
    'res/msi/CustomActions/RemotePrinter.cpp',
    'res/msi/Package/Components/FoxxDesk.wxs',
    'res/msi/Package/Language/Package.en-us.wxl',
    'res/msi/Package/Language/WixExt_en-us.wxl',
    'res/msi/README.md',
    'res/msi/preprocess.py',
    'res/osx-dist.sh',
    'res/pacman_install',
    'res/pam.d/foxxdesk.debian',
    'res/pam.d/foxxdesk.suse',
    'res/rpm-flutter-suse.spec',
    'res/rpm-flutter.spec',
    'res/rpm-suse.spec',
    'res/rpm.spec',
    'scripts/apply_foxxdesk_brand.py',
    'scripts/apply_foxxdesk_brand_DEFINITIVE.py',
    'scripts/apply_foxxdesk_brand_SAFE.py',
    'scripts/apply_foxxdesk_brand_with_fixes.py',
    'scripts/fix_foxxdesk_windows_flutter_build.py',
    'scripts/fix_generated_bridge_compat.py',
    'src/client.rs',
    'src/client/io_loop.rs',
    'src/clipboard.rs',
    'src/common.rs',
    'src/core_main.rs',
    'src/custom_server.rs',
    'src/flutter.rs',
    'src/hbbs_http/account.rs',
    'src/ipc.rs',
    'src/ipc/auth.rs',
    'src/ipc/fs.rs',
    'src/lang.rs',
    'src/lang/ar.rs',
    'src/lang/be.rs',
    'src/lang/bg.rs',
    'src/lang/ca.rs',
    'src/lang/cn.rs',
    'src/lang/cs.rs',
    'src/lang/da.rs',
    'src/lang/de.rs',
    'src/lang/el.rs',
    'src/lang/en.rs',
    'src/lang/eo.rs',
    'src/lang/es.rs',
    'src/lang/et.rs',
    'src/lang/eu.rs',
    'src/lang/fa.rs',
    'src/lang/fi.rs',
    'src/lang/fr.rs',
    'src/lang/ge.rs',
    'src/lang/he.rs',
    'src/lang/hi.rs',
    'src/lang/hr.rs',
    'src/lang/hu.rs',
    'src/lang/id.rs',
    'src/lang/it.rs',
    'src/lang/ja.rs',
    'src/lang/ko.rs',
    'src/lang/kz.rs',
    'src/lang/lt.rs',
    'src/lang/lv.rs',
    'src/lang/nb.rs',
    'src/lang/nl.rs',
    'src/lang/pl.rs',
    'src/lang/pt_PT.rs',
    'src/lang/ptbr.rs',
    'src/lang/ro.rs',
    'src/lang/ru.rs',
    'src/lang/sc.rs',
    'src/lang/sk.rs',
    'src/lang/sl.rs',
    'src/lang/sq.rs',
    'src/lang/sr.rs',
    'src/lang/sv.rs',
    'src/lang/ta.rs',
    'src/lang/th.rs',
    'src/lang/tr.rs',
    'src/lang/tw.rs',
    'src/lang/uk.rs',
    'src/main.rs',
    'src/naming.rs',
    'src/platform/delegate.rs',
    'src/platform/gtk_sudo.rs',
    'src/platform/linux.rs',
    'src/platform/linux_desktop_manager.rs',
    'src/platform/macos.rs',
    'src/platform/privileges_scripts/agent.plist',
    'src/platform/privileges_scripts/daemon.plist',
    'src/platform/privileges_scripts/install.scpt',
    'src/platform/privileges_scripts/uninstall.scpt',
    'src/platform/privileges_scripts/update.scpt',
    'src/platform/windows.cc',
    'src/platform/windows.rs',
    'src/platform/windows/acl.rs',
    'src/platform/windows_delete_test_cert.cc',
    'src/plugin/callback_msg.rs',
    'src/plugin/errno.rs',
    'src/plugin/manager.rs',
    'src/plugin/plugins.rs',
    'src/privacy_mode/win_topmost_window.rs',
    'src/rendezvous_mediator.rs',
    'src/server/clipboard_service.rs',
    'src/server/connection.rs',
    'src/server/dbus.rs',
    'src/server/input_service.rs',
    'src/server/terminal_service.rs',
    'src/ui_cm_interface.rs',
    'src/ui_session_interface.rs',
    'src/virtual_display_manager.rs',
]

SAFE_CORE_FILES: List[str] = [
    "Cargo.toml",
    "Cargo.lock",
    "libs/portable/Cargo.toml",
    "libs/portable/Cargo.lock",
    "build.py",
    "libs/hbb_common/src/config.rs",
    "FOXXDESK_SERVER_DEFAULTS.md",
    "res/pacman_install",
    "res/PKGBUILD",
    "res/DEBIAN/postinst",
    "res/DEBIAN/postrm",
    "res/DEBIAN/preinst",
    "res/DEBIAN/prerm",
    "res/rpm-flutter-suse.spec",
    "res/rpm-flutter.spec",
    "res/rpm-suse.spec",
    "res/rpm.spec",
    "res/foxxdesk-link.desktop",
    "res/foxxdesk.desktop",
    "res/foxxdesk.service",
    "res/pam.d/foxxdesk.debian",
    "res/pam.d/foxxdesk.suse",
    "flatpak/com.foxxdesk.client.metainfo.xml",
    "flatpak/foxxdesk.json",
    "res/msi/Package/Components/FoxxDesk.wxs",
]

# Cópias seguras: não apaga o arquivo antigo por padrão.
FILE_RENAMES: Dict[str, str] = {
    ".github/workflows/rustdesk-build.yml": ".github/workflows/foxxdesk-build.yml",
    "flatpak/com.rustdesk.RustDesk.metainfo.xml": "flatpak/com.foxxdesk.client.metainfo.xml",
    "flatpak/rustdesk.json": "flatpak/foxxdesk.json",
    "res/rustdesk-link.desktop": "res/foxxdesk-link.desktop",
    "res/rustdesk.desktop": "res/foxxdesk.desktop",
    "res/rustdesk.service": "res/foxxdesk.service",
    "res/pam.d/rustdesk.debian": "res/pam.d/foxxdesk.debian",
    "res/pam.d/rustdesk.suse": "res/pam.d/foxxdesk.suse",
    "res/msi/Package/Components/RustDesk.wxs": "res/msi/Package/Components/FoxxDesk.wxs",
}

# Nomes/URLs que devem continuar como upstream ou API interna.
PROTECT_PATTERNS: Sequence[str] = (
    r"https?://[^\s\)\]\}\>\"']*rustdesk[^\s\)\]\}\>\"']*",
    r"git\+https?://[^\s\)\]\}\>\"']*rustdesk[^\s\)\]\}\>\"']*",
    r"github\.com/rustdesk-org",
    r"github\.com/rustdesk/[^\s\)\]\}\>\"']*",
    r"rustdesk-org",
    r"rustdesk/rustdesk",
    r"librustdesk",
    r"is_rustdesk(?:_[A-Za-z0-9_]+)?",
    r"try_kill_rustdesk_main_window_process",
    r"RustDeskTempTopMostWindow",
    r"RustDeskInterval",
    r"DeleteRustDeskTestCert",
)


def die(msg: str, code: int = 2) -> None:
    print(f"ERRO: {msg}", file=sys.stderr)
    raise SystemExit(code)


def normalize_lf(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n")


def dominant_newline(text: str) -> str:
    crlf = text.count("\r\n")
    lf = text.count("\n") - crlf
    cr = text.count("\r") - crlf
    if crlf >= lf and crlf >= cr and crlf > 0:
        return "\r\n"
    if cr > lf and cr > 0:
        return "\r"
    return "\n"


def convert_newlines(text: str, newline: str) -> str:
    return normalize_lf(text).replace("\n", newline)


def has_bad_control_chars(text: str) -> bool:
    sample = text[:4096]
    if not sample:
        return False
    bad = 0
    for ch in sample:
        o = ord(ch)
        if ch in "\n\r\t":
            continue
        if o < 32:
            bad += 1
    return (bad / max(1, len(sample))) > 0.03


def decode_file(data: bytes, path: Path) -> Tuple[Optional[str], Optional[str], bool]:
    if path.suffix.lower() in BINARY_EXTS:
        return None, None, True
    if data.startswith(codecs.BOM_UTF8):
        try:
            return data.decode("utf-8-sig"), "utf-8-sig", False
        except UnicodeDecodeError:
            return None, None, True
    if data.startswith(codecs.BOM_UTF16_LE) or data.startswith(codecs.BOM_UTF16_BE):
        try:
            text = data.decode("utf-16")
            return (text, "utf-16", False) if not has_bad_control_chars(text) else (None, None, True)
        except UnicodeDecodeError:
            return None, None, True
    if b"\x00" in data[:4096]:
        return None, None, True
    for enc in ("utf-8", "cp1252", "latin-1"):
        try:
            text = data.decode(enc)
            if not has_bad_control_chars(text):
                return text, enc, False
        except UnicodeDecodeError:
            pass
    return None, None, True


def encode_text(text: str, enc: Optional[str]) -> bytes:
    try:
        return text.encode(enc or "utf-8", errors="strict")
    except UnicodeEncodeError:
        return text.encode("utf-8")


def safe_cli_value(name: str, value: Optional[str]) -> Optional[str]:
    if value is None:
        return None
    value = value.strip()
    if "\n" in value or "\r" in value:
        die(f"{name} não pode conter quebra de linha.")
    return value or None


def normalize_homepage(value: Optional[str]) -> Optional[str]:
    if not value:
        return None
    value = value.strip().rstrip("/")
    if not value:
        return None
    if not re.match(r"^[A-Za-z][A-Za-z0-9+.-]*://", value):
        value = "https://" + value
    if any(ch in value for ch in (" ", "\t", "\n", "\r")):
        die("--homepage/--server inválido para Homepage: não pode conter espaços ou quebras.")
    return value


def redact_value(value: Optional[str], label: str = "valor") -> str:
    if not value:
        return "(não informado)"
    digest = hashlib.sha256(value.encode("utf-8", errors="ignore")).hexdigest()[:10]
    if label == "key":
        return f"<key ocultada; len={len(value)}; sha256={digest}>"
    return value


def copy_backup(target: Path, backup_root: Path, rel: str) -> None:
    src = target / rel
    dst = backup_root / rel
    dst.parent.mkdir(parents=True, exist_ok=True)
    if src.exists() and not dst.exists():
        shutil.copy2(src, dst)


def is_skipped_path(rel: str) -> bool:
    rel_norm = rel.replace("\\", "/").lstrip("/")
    parts = rel_norm.split("/")
    for skip in SKIP_DIRS:
        if rel_norm == skip or rel_norm.startswith(skip.rstrip("/") + "/"):
            return True
    return any(part in {".git", "target", "node_modules", ".rebrand_backup"} for part in parts)


def iter_scan_files(target: Path, max_size: int) -> Iterable[str]:
    for p in target.rglob("*"):
        if not p.is_file():
            continue
        rel = p.relative_to(target).as_posix()
        if is_skipped_path(rel):
            continue
        try:
            if p.stat().st_size > max_size:
                continue
        except OSError:
            continue
        yield rel


def protect_text(text: str) -> Tuple[str, Dict[str, str]]:
    tokens: Dict[str, str] = {}
    protected = text

    def repl(match: re.Match[str]) -> str:
        token = f"@@FOXXDESK_PROTECT_{len(tokens)}@@"
        tokens[token] = match.group(0)
        return token

    for pattern in PROTECT_PATTERNS:
        protected = re.sub(pattern, repl, protected)
    return protected, tokens


def restore_text(text: str, tokens: Dict[str, str]) -> str:
    for token, original in tokens.items():
        text = text.replace(token, original)
    return text


def safe_brand_replacements(text: str) -> str:
    """Rebrand por limites de palavra, evitando trocar nomes dentro de identificadores."""
    protected, tokens = protect_text(text)
    replacements = [
        (r"com\.rustdesk\.RustDesk", "com.foxxdesk.client"),
        (r"com\.rustdesk", "com.foxxdesk"),
        (r"org\.rustdesk", "org.foxxdesk"),
        (r"(?<![A-Za-z0-9_])RUSTDESK(?![A-Za-z0-9_])", APP_SLUG_UPPER),
        (r"(?<![A-Za-z0-9_])RustDesk(?![A-Za-z0-9_])", APP_DISPLAY_NAME),
        (r"(?<![A-Za-z0-9_])rustdesk(?![A-Za-z0-9_])", APP_SLUG),
        (r"(?<![A-Za-z0-9_])rust_desk(?![A-Za-z0-9_])", "foxx_desk"),
        (r"(?<![A-Za-z0-9_])rust-desk(?![A-Za-z0-9_])", "foxx-desk"),
    ]
    for pattern, repl in replacements:
        protected = re.sub(pattern, repl, protected)
    return restore_text(protected, tokens)


def patch_cargo_toml(rel: str, text: str) -> str:
    if rel == "Cargo.toml":
        text = re.sub(r'(?m)^name\s*=\s*"rustdesk"\s*$', 'name = "foxxdesk"', text, count=1)
        text = re.sub(r'(?m)^authors\s*=\s*\["rustdesk <info@rustdesk\.com>"\]\s*$', 'authors = ["FoxxDesk / MGN"]', text, count=1)
        text = re.sub(r'(?m)^description\s*=\s*"RustDesk Remote Desktop"\s*$', 'description = "FoxxDesk Remote Desktop"', text, count=1)
        text = re.sub(r'(?m)^default-run\s*=\s*"rustdesk"\s*$', 'default-run = "foxxdesk"', text, count=1)
        return text
    if rel == "libs/portable/Cargo.toml":
        text = re.sub(r'(?m)^name\s*=\s*"rustdesk-portable-packer"\s*$', 'name = "foxxdesk-portable-packer"', text, count=1)
        text = re.sub(r'(?m)^description\s*=\s*"RustDesk Remote Desktop"\s*$', 'description = "FoxxDesk Remote Desktop"', text, count=1)
        text = re.sub(r'(?m)^ProductName\s*=\s*"RustDesk"\s*$', 'ProductName = "FoxxDesk"', text, count=1)
        text = re.sub(r'(?m)^OriginalFilename\s*=\s*"rustdesk\.exe"\s*$', 'OriginalFilename = "foxxdesk.exe"', text, count=1)
        text = re.sub(r'(?m)^FileDescription\s*=\s*"RustDesk Remote Desktop"\s*$', 'FileDescription = "FoxxDesk Remote Desktop"', text, count=1)
        text = text.replace("Purslane Ltd. and RustDesk contributors", "Purslane Ltd. and FoxxDesk/MGN contributors")
        return text
    return text


def patch_cargo_lock(rel: str, text: str) -> str:
    if rel not in {"Cargo.lock", "libs/portable/Cargo.lock"}:
        return text
    text = re.sub(
        r'(?m)^(\[\[package\]\]\nname = ")rustdesk("$)',
        r'\1foxxdesk\2',
        text,
        count=1 if rel == "Cargo.lock" else 0,
    )
    text = re.sub(
        r'(?m)^(\[\[package\]\]\nname = ")rustdesk-portable-packer("$)',
        r'\1foxxdesk-portable-packer\2',
        text,
        count=1,
    )
    return text


def patch_build_py(rel: str, text: str, args: argparse.Namespace) -> str:
    if rel != "build.py":
        return text
    # Mantém URLs upstream/dependências; altera apenas metadados e nomes locais.
    text = re.sub(r'(?m)^APP_DISPLAY_NAME\s*=.*$', 'APP_DISPLAY_NAME = os.environ.get("APP_DISPLAY_NAME", "FoxxDesk")', text)
    text = re.sub(r'(?m)^APP_SLUG\s*=.*$', 'APP_SLUG = os.environ.get("APP_SLUG", "foxxdesk")', text)
    text = re.sub(r'(?m)^UPSTREAM_SLUG\s*=.*$', 'UPSTREAM_SLUG = "foxxdesk"', text)
    if "APP_DISPLAY_NAME = os.environ.get" not in text:
        insert = (
            'APP_DISPLAY_NAME = os.environ.get("APP_DISPLAY_NAME", "FoxxDesk")\n'
            'APP_SLUG = os.environ.get("APP_SLUG", "foxxdesk")\n'
            'APP_EXE = APP_SLUG + (".exe" if windows else "")\n'
            'UPSTREAM_SLUG = "foxxdesk"\n'
        )
        pos = text.find("skip_cargo = False")
        if pos != -1:
            before = text[:pos]
            after = text[pos:]
            if "APP_SLUG" not in before:
                text = before + insert + after
    homepage = normalize_homepage(args.homepage or args.server)
    if homepage:
        text = re.sub(r'(?m)^Homepage:\s*https?://rustdesk\.com\s*$', f'Homepage: {homepage}', text)
        text = re.sub(r'(?m)^Homepage:\s*https?://foxxdesk[^\s]*\s*$', f'Homepage: {homepage}', text)
    if args.maintainer_email:
        text = text.replace("rustdesk <info@rustdesk.com>", f"FoxxDesk / MGN <{args.maintainer_email}>")
        text = text.replace("TODO_FOXXDESK_MAINTAINER_EMAIL", args.maintainer_email)
        text = text.replace(DEFAULT_MAINTAINER_EMAIL, args.maintainer_email)
    return text


def patch_config_rs(rel: str, text: str, args: argparse.Namespace) -> str:
    if rel != "libs/hbb_common/src/config.rs":
        return text
    if args.server:
        text = re.sub(r'RwLock::new\("[^"]*"\.to_owned\(\)\)', f'RwLock::new("{args.server}".to_owned())', text, count=1)
        text = re.sub(r'pub const RENDEZVOUS_SERVERS: &\[&str\] = &\["[^"]*"\];', f'pub const RENDEZVOUS_SERVERS: &[&str] = &["{args.server}"];', text, count=1)
    if args.key:
        text = re.sub(r'pub const RS_PUB_KEY: &str = "[^"]*";', f'pub const RS_PUB_KEY: &str = "{args.key}";', text, count=1)
    return text


def patch_server_defaults(rel: str, text: str, args: argparse.Namespace) -> str:
    if rel != "FOXXDESK_SERVER_DEFAULTS.md":
        return text
    server = args.server or DEFAULT_SERVER
    relay = args.relay or server
    key = args.key or DEFAULT_KEY
    text = re.sub(r'(?m)^- HBBS / ID server: `[^`]*`$', f'- HBBS / ID server: `{server}`', text)
    text = re.sub(r'(?m)^- HBBR / Relay server: `[^`]*`$', f'- HBBR / Relay server: `{relay}`', text)
    text = re.sub(r'(?m)^- Public key: `[^`]*`$', f'- Public key: `{key}`', text)
    return text


def patch_package_scripts(rel: str, text: str, args: argparse.Namespace) -> str:
    if rel in {"res/rpm-flutter-suse.spec", "res/rpm-flutter.spec", "res/rpm-suse.spec", "res/rpm.spec"}:
        email = args.maintainer_email or DEFAULT_MAINTAINER_EMAIL
        text = text.replace("TODO_FOXXDESK_MAINTAINER_EMAIL", email)
        text = text.replace("rustdesk <info@rustdesk.com>", f"FoxxDesk / MGN <{email}>")
    return text


def patch_text(rel: str, text: str, args: argparse.Namespace) -> str:
    text = normalize_lf(text)
    text = patch_cargo_lock(rel, text)
    text = patch_cargo_toml(rel, text)
    text = patch_build_py(rel, text, args)
    text = patch_config_rs(rel, text, args)
    text = patch_server_defaults(rel, text, args)
    text = patch_package_scripts(rel, text, args)
    if args.profile == "full":
        text = safe_brand_replacements(text)
    # Reforços pontuais após patches específicos.
    text = text.replace("/usr/share/rustdesk/files/", "/usr/share/foxxdesk/files/")
    text = text.replace("/usr/share/rustdesk/", "/usr/share/foxxdesk/")
    text = text.replace("/etc/systemd/system/rustdesk.service", "/etc/systemd/system/foxxdesk.service")
    text = text.replace("rustdesk.service", "foxxdesk.service")
    text = text.replace("rustdesk.desktop", "foxxdesk.desktop")
    text = text.replace("rustdesk-link.desktop", "foxxdesk-link.desktop")
    return text


def line_for_first_diff(old: str, new: str) -> int:
    old_lines = old.splitlines()
    new_lines = new.splitlines()
    for i, (a, b) in enumerate(zip(old_lines, new_lines), start=1):
        if a != b:
            return i
    return min(len(old_lines), len(new_lines)) + 1


def md_escape(s: str) -> str:
    return str(s).replace("|", "\\|").replace("\n", "\\n")


def apply_file_renames(target: Path, args: argparse.Namespace, report: Dict[str, Any], backup_root: Optional[Path]) -> None:
    for src_rel, dst_rel in FILE_RENAMES.items():
        src = target / src_rel
        dst = target / dst_rel
        if dst.exists():
            continue
        if not src.exists():
            continue
        report["renamed_files"].append(f"{src_rel} -> {dst_rel}")
        report["changes"].append({"file": dst_rel, "line": 1, "status": "criado" if args.apply else "criaria", "action": "copiar arquivo renomeado", "message": f"origem: {src_rel}"})
        if args.apply:
            if backup_root is not None:
                copy_backup(target, backup_root, src_rel)
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)


def process_one_file(target: Path, rel: str, args: argparse.Namespace, report: Dict[str, Any], backup_root: Optional[Path]) -> None:
    if is_skipped_path(rel):
        report["ignored_files"].append(rel)
        return
    path = target / rel
    report["analyzed_files"].append(rel)
    if not path.exists():
        if rel in ALLOWED_FILES:
            report["missing_files"].append(rel)
        return
    if not path.is_file():
        report["pending"].append({"file": rel, "message": "caminho existe, mas não é arquivo"})
        return
    try:
        data = path.read_bytes()
    except OSError as exc:
        report["pending"].append({"file": rel, "message": f"falha ao ler: {exc}"})
        return
    if len(data) > args.max_size:
        report["ignored_files"].append(rel)
        return
    text, enc, isbin = decode_file(data, path)
    if isbin or text is None:
        report["ignored_files"].append(rel)
        return
    old_norm = normalize_lf(text)
    new_norm = patch_text(rel, old_norm, args)
    if new_norm == old_norm:
        report["already_applied_files"].append(rel)
        return
    report["changed_files"].append(rel)
    report["changes"].append({
        "file": rel,
        "line": line_for_first_diff(old_norm, new_norm),
        "status": "alterado" if args.apply else "alteraria",
        "action": "aplicar regras standalone de rebrand",
        "message": "conteúdo textual mudou por regra segura; sem payload/ZIP",
    })
    if args.apply:
        if backup_root is not None:
            copy_backup(target, backup_root, rel)
        newline = dominant_newline(text)
        path.write_bytes(encode_text(convert_newlines(new_norm, newline), enc))


def build_report(report: Dict[str, Any], args: argparse.Namespace, target: Path) -> str:
    now = _dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = ["# Relatório de rebrand FoxxDesk", ""]
    lines += [
        f"- Data/hora: `{now}`",
        f"- Modo: `{'apply' if args.apply else 'dry-run'}`",
        f"- Projeto alvo: `{target}`",
        "- Script: `apply_foxxdesk_rebrand_standalone_v9.py`",
        f"- Versão do script: `{SCRIPT_VERSION}`",
        "- Payload/ZIP embutido: `não`",
        f"- Perfil: `{args.profile}`",
        "- Estratégia: `safe = correções críticas; full = allowlist completa + proteção de upstream`",
        "",
        "## Valores dinâmicos",
        "",
        f"- server: `{redact_value(args.server)}`",
        f"- relay: `{redact_value(args.relay)}`",
        f"- key: `{redact_value(args.key, 'key')}`",
        f"- maintainer-email: `{redact_value(args.maintainer_email)}`",
        f"- homepage: `{redact_value(normalize_homepage(args.homepage or args.server))}`",
        "",
        "## Resumo",
        "",
        f"- Arquivos permitidos na allowlist: `{len(ALLOWED_FILES)}`",
        f"- Arquivos analisados: `{len(set(report['analyzed_files']))}`",
        f"- Arquivos alterados: `{len(set(report['changed_files']))}`",
        f"- Arquivos já aplicados/sem mudança: `{len(set(report['already_applied_files']))}`",
        f"- Arquivos esperados não encontrados: `{len(set(report['missing_files']))}`",
        f"- Arquivos ignorados: `{len(set(report['ignored_files']))}`",
        f"- Renomeações/cópias criadas: `{len(report['renamed_files'])}`",
        f"- Pendências: `{len(report['pending'])}`",
    ]
    if report.get("backup_dir"):
        lines.append(f"- Backup: `{report['backup_dir']}`")
    lines.append("")

    def section(title: str, items: Iterable[Any]) -> None:
        lines.append(f"## {title}")
        lines.append("")
        unique = sorted({str(x) for x in items})
        if not unique:
            lines.append("Nenhum.")
        else:
            for item in unique:
                lines.append(f"- `{item}`")
        lines.append("")

    section("Arquivos alterados", report["changed_files"])
    section("Arquivos renomeados/copiados", report["renamed_files"])
    section("Arquivos esperados que não foram encontrados", report["missing_files"])
    section("Arquivos ignorados", report["ignored_files"])

    lines += ["## Alterações", ""]
    if not report["changes"]:
        lines.append("Nenhuma alteração avaliada.")
    else:
        lines.append("| Status | Arquivo | Linha | Ação | Mensagem |")
        lines.append("|---|---|---:|---|---|")
        for c in report["changes"]:
            lines.append(f"| {c.get('status')} | `{c.get('file')}` | {c.get('line') or ''} | {md_escape(c.get('action',''))} | {md_escape(c.get('message',''))} |")

    lines += ["", "## Pendências", ""]
    if not report["pending"]:
        lines.append("Nenhuma.")
    else:
        for p in report["pending"]:
            lines.append(f"- `{p.get('file')}`: {p.get('message')}")
    lines.append("")
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Aplica rebrand FoxxDesk standalone, sem ZIP/payload embutido.")
    p.add_argument("--target", default="./", help="Pasta raiz do projeto alvo. Padrão: ./")
    mode = p.add_mutually_exclusive_group(required=True)
    mode.add_argument("--dry-run", action="store_true", help="Mostra o que seria alterado sem salvar arquivos do projeto, exceto relatório.")
    mode.add_argument("--apply", action="store_true", help="Aplica as alterações.")
    p.add_argument("--yes", action="store_true", help="Confirma automaticamente o modo --apply.")
    p.add_argument("--server", default=None, help="Domínio/IP do servidor FoxxDesk; usado em config.rs e FOXXDESK_SERVER_DEFAULTS.md.")
    p.add_argument("--relay", default=None, help="Domínio/IP do relay FoxxDesk; usado em FOXXDESK_SERVER_DEFAULTS.md.")
    p.add_argument("--key", default=None, help="Chave pública; usada em config.rs e FOXXDESK_SERVER_DEFAULTS.md.")
    p.add_argument("--maintainer-email", default=None, help="E-mail do mantenedor em metadados de pacote.")
    p.add_argument("--homepage", default=None, help="Homepage pública para metadados. Se omitido, usa --server.")
    p.add_argument("--profile", choices=["safe", "full"], default="safe", help="safe: só correções críticas/build; full: allowlist completa com rebrand textual. Padrão: safe.")
    p.add_argument("--scan-all", action="store_true", help="Opcional: varre todos os arquivos textuais fora das pastas ignoradas. Recomendado só com --profile full.")
    p.add_argument("--max-size", type=int, default=2_000_000, help="Tamanho máximo por arquivo textual analisado. Padrão: 2MB.")
    p.add_argument("--remove-old-renamed", action="store_true", help="Depois de copiar arquivos renomeados, remove os antigos. Use só após conferir o dry-run.")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    args.server = safe_cli_value("--server", args.server)
    args.relay = safe_cli_value("--relay", args.relay)
    args.key = safe_cli_value("--key", args.key)
    args.maintainer_email = safe_cli_value("--maintainer-email", args.maintainer_email)
    args.homepage = safe_cli_value("--homepage", args.homepage)

    target = Path(args.target).expanduser().resolve()
    if not target.exists():
        die(f"--target não existe: {target}")
    if not target.is_dir():
        die(f"--target não é uma pasta: {target}")
    if args.apply and not args.yes:
        resp = input(f"Aplicar alterações em '{target}'? Digite 'SIM' para confirmar: ").strip()
        if resp != "SIM":
            die("aplicação cancelada pelo usuário", code=1)

    report: Dict[str, Any] = {
        "analyzed_files": [], "missing_files": [], "changed_files": [], "already_applied_files": [],
        "ignored_files": [], "pending": [], "changes": [], "renamed_files": [], "backup_dir": "",
    }

    backup_root: Optional[Path] = None
    if args.apply:
        stamp = _dt.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_root = target / ".rebrand_backup" / stamp
        backup_root.mkdir(parents=True, exist_ok=False)
        report["backup_dir"] = str(backup_root)

    apply_file_renames(target, args, report, backup_root)

    if args.scan_all:
        candidates = sorted(set(iter_scan_files(target, args.max_size)))
    elif args.profile == "full":
        candidates = sorted(set(ALLOWED_FILES) | set(FILE_RENAMES.values()) | set(FILE_RENAMES.keys()))
    else:
        # Em safe mode, não mexe nos arquivos antigos se o destino novo já existe.
        # O apply_file_renames já copia o antigo para o novo quando necessário.
        candidates = sorted(set(SAFE_CORE_FILES) | set(FILE_RENAMES.values()))

    for rel in candidates:
        process_one_file(target, rel, args, report, backup_root)

    if args.apply and args.remove_old_renamed:
        for src_rel, dst_rel in FILE_RENAMES.items():
            src = target / src_rel
            dst = target / dst_rel
            if src.exists() and dst.exists():
                if backup_root is not None:
                    copy_backup(target, backup_root, src_rel)
                src.unlink()
                report["changes"].append({"file": src_rel, "line": 1, "status": "removido", "action": "remover arquivo antigo após renomeação", "message": f"substituído por {dst_rel}"})

    report_md = build_report(report, args, target)
    report_path = target / "rebrand_report.md"
    report_path.write_text(report_md, encoding="utf-8", newline="\n")

    changed = len(set(report["changed_files"]))
    pending = len(report["pending"])
    missing = len(set(report["missing_files"]))
    print(f"Script: {SCRIPT_VERSION}")
    print(f"Relatório gerado em: {report_path}")
    print(f"Modo: {'apply' if args.apply else 'dry-run'} | arquivos alterados: {changed} | pendências: {pending} | não encontrados: {missing}")
    if args.dry_run:
        print("Dry-run concluído: nenhum arquivo do projeto foi salvo, exceto o relatório.")
    return 0 if pending == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())