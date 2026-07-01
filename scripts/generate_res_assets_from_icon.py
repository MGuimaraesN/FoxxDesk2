#!/usr/bin/env python3
"""
Generate brand image assets under ./res from res/icon.png.

Versao v2:
- Corrige SVGs com viewBox deslocado, como res/scalable.svg e res/rustdesk-banner.svg.
- Mantem logo-header.svg e design.svg excluidos.
- Usa res/icon.png como fonte unica.
- Gera PNG, SVG wrapper com PNG embutido e ICO.
"""

from __future__ import annotations

import argparse
import base64
import datetime as dt
import io
import shutil
from pathlib import Path

from PIL import Image

SCRIPT_VERSION = "icon-assets-v2-fix-svg-viewbox-2026-06-30"

PNG_ASSETS = [
    {"path": "res/32x32.png", "size": (32, 32)},
    {"path": "res/64x64.png", "size": (64, 64)},
    {"path": "res/128x128.png", "size": (128, 128)},
    {"path": "res/128x128@2x.png", "size": (256, 256)},
    {"path": "res/FoxxDesk.png", "size": (1600, 1600)},
    {"path": "res/mac-icon.png", "size": (1024, 1024)},
    {"path": "res/mac-tray-dark-x2.png", "size": (60, 60)},
    {"path": "res/mac-tray-light-x2.png", "size": (48, 48)},
]

SVG_ASSETS = [
    {"path": "res/FoxxDesk.svg", "width": 128, "height": 128, "viewBox": "0 0 96 95.999999"},
    {"path": "res/logo.svg", "width": 26, "height": 26, "viewBox": "0 0 96 95.999999"},
    {"path": "res/scalable.svg", "width": 32, "height": 32, "viewBox": "66.993 897.484 32 32.000001"},
]

ICO_ASSETS = [
    {"path": "res/icon.ico", "render_size": (256, 256), "ico_sizes": [(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]},
    {"path": "res/tray-icon.ico", "render_size": (32, 32), "ico_sizes": [(16, 16), (24, 24), (32, 32)]},
]

EXCLUDED = {"res/logo-header.svg", "res/design.svg", "res/icon.png"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate PNG/SVG/ICO assets from res/icon.png")
    parser.add_argument("--target", default=".", help="Project root. Default: current directory")
    parser.add_argument("--source", default="res/icon.png", help="Path to source icon relative to target. Default: res/icon.png")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--dry-run", action="store_true", help="Show what would be generated")
    mode.add_argument("--apply", action="store_true", help="Generate/update files")
    parser.add_argument("--yes", action="store_true", help="Skip confirmation in --apply mode")
    return parser.parse_args()


def ensure_rgba(im: Image.Image) -> Image.Image:
    return im.convert("RGBA") if im.mode != "RGBA" else im


def resize_image(src: Image.Image, size: tuple[int, int]) -> Image.Image:
    return ensure_rgba(src).resize(size, Image.LANCZOS)


def png_bytes(src: Image.Image, size: tuple[int, int]) -> bytes:
    out = io.BytesIO()
    resize_image(src, size).save(out, format="PNG")
    return out.getvalue()


def parse_viewbox(viewbox: str) -> tuple[float, float, float, float]:
    parts = [float(x) for x in viewbox.replace(",", " ").split()]
    if len(parts) != 4:
        raise ValueError(f"viewBox invalido: {viewbox}")
    return parts[0], parts[1], parts[2], parts[3]


def fmt_num(value: float) -> str:
    if float(value).is_integer():
        return str(int(value))
    return f"{value:.6f}".rstrip("0").rstrip(".")


def svg_bytes(src: Image.Image, width: int, height: int, viewbox: str) -> bytes:
    min_x, min_y, vb_w, vb_h = parse_viewbox(viewbox)

    # A imagem precisa ficar dentro do proprio viewBox.
    # Isso corrige arquivos cujo viewBox nao começa em 0 0, como scalable.svg.
    render_w = max(1, round(vb_w))
    render_h = max(1, round(vb_h))
    png = png_bytes(src, (render_w, render_h))
    b64 = base64.b64encode(png).decode("ascii")

    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg"
     xmlns:xlink="http://www.w3.org/1999/xlink"
     width="{width}"
     height="{height}"
     viewBox="{viewbox}"
     version="1.1">
  <image x="{fmt_num(min_x)}"
         y="{fmt_num(min_y)}"
         width="{fmt_num(vb_w)}"
         height="{fmt_num(vb_h)}"
         preserveAspectRatio="xMidYMid meet"
         xlink:href="data:image/png;base64,{b64}" />
</svg>
'''
    return svg.encode("utf-8")


def ico_bytes(src: Image.Image, render_size: tuple[int, int], ico_sizes: list[tuple[int, int]]) -> bytes:
    out = io.BytesIO()
    resize_image(src, render_size).save(out, format="ICO", sizes=ico_sizes)
    return out.getvalue()


def backup_file(root: Path, rel: str, backup_root: Path) -> None:
    src = root / rel
    dst = backup_root / rel
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def write_if_changed(root: Path, rel: str, data: bytes, dry_run: bool, backup_root: Path, report: list[str]) -> str:
    if rel in EXCLUDED:
        report.append(f"- excluido por regra: `{rel}`")
        return "skipped"

    path = root / rel
    existed = path.exists()
    current = path.read_bytes() if existed else None

    if current == data:
        report.append(f"- ja esta atualizado: `{rel}`")
        return "unchanged"

    if dry_run:
        action = "sera atualizado" if existed else "sera criado"
        report.append(f"- {action}: `{rel}`")
        return "planned"

    if existed:
        backup_file(root, rel, backup_root)

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)

    if existed:
        report.append(f"- atualizado: `{rel}` (backup em `{backup_root}`)")
    else:
        report.append(f"- criado: `{rel}`")
    return "written"


def confirm() -> None:
    ans = input("Aplicar geracao de assets? [y/N]: ").strip().lower()
    if ans not in {"y", "yes", "s", "sim"}:
        raise SystemExit("Operacao cancelada.")


def generate(root: Path, source_rel: str, dry_run: bool) -> tuple[list[str], dict[str, int], Path]:
    src_path = root / source_rel
    if not src_path.exists():
        raise FileNotFoundError(f"Arquivo fonte nao encontrado: {src_path}")

    timestamp = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_root = root / ".icon_asset_backup" / timestamp

    report: list[str] = []
    stats = {"planned": 0, "written": 0, "unchanged": 0, "skipped": 0}

    with Image.open(src_path) as im:
        src = ensure_rgba(im)

        for item in PNG_ASSETS:
            data = png_bytes(src, item["size"])
            status = write_if_changed(root, item["path"], data, dry_run, backup_root, report)
            stats[status] += 1

        for item in SVG_ASSETS:
            data = svg_bytes(src, item["width"], item["height"], item["viewBox"])
            status = write_if_changed(root, item["path"], data, dry_run, backup_root, report)
            stats[status] += 1

        for item in ICO_ASSETS:
            data = ico_bytes(src, item["render_size"], item["ico_sizes"])
            status = write_if_changed(root, item["path"], data, dry_run, backup_root, report)
            stats[status] += 1

    return report, stats, backup_root


def main() -> None:
    args = parse_args()
    root = Path(args.target).resolve()

    if not root.exists() or not root.is_dir():
        raise SystemExit(f"Pasta alvo invalida: {root}")

    if args.apply and not args.yes:
        confirm()

    report, stats, backup_root = generate(root, args.source, args.dry_run)
    mode = "dry-run" if args.dry_run else "apply"
    report_path = root / "icon_assets_report.md"
    changed = stats["planned"] if args.dry_run else stats["written"]

    lines = [
        "# Relatorio de geracao de assets",
        "",
        f"- Script: `{SCRIPT_VERSION}`",
        f"- Modo: `{mode}`",
        f"- Projeto alvo: `{root}`",
        f"- Fonte: `{args.source}`",
        f"- Backup: `{backup_root if args.apply and stats['written'] else 'nao criado'}`",
        "",
        "## Observacoes",
        "",
        "- O arquivo `res/icon.png` e a fonte unica.",
        "- `res/logo-header.svg` e `res/design.svg` sao excluidos e nunca sao gerados.",
        "- `res/scalable.svg` e `res/rustdesk-banner.svg` preservam viewBox deslocado e posicionam a imagem dentro do viewBox.",
        "- Arquivos `.svg` sao gerados como SVG wrapper com PNG embutido em base64; nao sao vetores reais.",
        "",
        "## Resumo",
        "",
        f"- Arquivos alteraveis/criados no modo atual: `{changed}`",
        f"- Ja atualizados: `{stats['unchanged']}`",
        f"- Pulados/excluidos: `{stats['skipped']}`",
        "",
        "## Arquivos tratados",
        "",
    ]
    lines.extend(report)
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Modo: {mode} | arquivos alterados: {changed} | ja atualizados: {stats['unchanged']} | relatorio: {report_path}")


if __name__ == "__main__":
    main()