# Relatório de rebrand FoxxDesk

- Data/hora: `2026-07-01 09:19:26`
- Modo: `apply`
- Projeto alvo: `/home/mateus/_Projects/FoxxDesk2`
- Script: `apply_foxxdesk_rebrand_all_files_no_zip_v13.py`
- Versão do script: `v13-build-safe-patch-only-no-zip-2026-07-01`
- Payload/ZIP/manifesto externo: `não`
- Espelhamento/substituição de arquivo inteiro por referência antiga: `não`
- Perfil: `full`
- Estratégia: `patch-only; não espelha arquivos inteiros; full = TODOS os arquivos da allowlist + proteção de upstream`
- Observação: se aparecerem apenas ~13 arquivos, você provavelmente executou a v9 safe ou usou --profile safe.

## Valores dinâmicos

- server: `foxxdesk.mguimaraesn.dev`
- relay: `foxxdesk.mguimaraesn.dev`
- key: `<key ocultada; len=44; sha256=a58bc137d7>`
- maintainer-email: `mateus@mguimaraesn.dev`
- homepage: `https://foxxdesk.mguimaraesn.dev`

## Resumo

- Arquivos permitidos na allowlist: `261`
- Arquivos analisados: `270`
- Arquivos alterados: `7`
- Arquivos já aplicados/sem mudança: `250`
- Arquivos esperados não encontrados: `8`
- Arquivos ignorados: `4`
- Renomeações/cópias criadas: `0`
- Pendências: `1`
- Backup: `/home/mateus/_Projects/FoxxDesk2/.rebrand_backup/20260701_091924`

## Arquivos alterados

- `.github/workflows/bridge.yml`
- `.github/workflows/flutter-build.yml`
- `.github/workflows/playground.yml`
- `res/DEBIAN/postinst`
- `res/PKGBUILD`
- `res/rpm-flutter-suse.spec`
- `res/rpm-flutter.spec`

## Arquivos renomeados/copiados

Nenhum.

## Arquivos esperados que não foram encontrados

- `BRAND_CHANGELOG.md`
- `FOXXDESK_MAX_SAFE_BRAND_REPORT.md`
- `FOXXDESK_SERVER_DEFAULTS.md`
- `NOTICE.md`
- `libs/hbb_common/src/config.rs`
- `libs/hbb_common/src/fs.rs`
- `libs/hbb_common/src/platform/linux.rs`
- `libs/hbb_common/src/platform/mod.rs`

## Arquivos ignorados

- `scripts/apply_foxxdesk_brand.py (opcional ausente)`
- `scripts/apply_foxxdesk_brand_DEFINITIVE.py (opcional ausente)`
- `scripts/apply_foxxdesk_brand_SAFE.py (opcional ausente)`
- `scripts/apply_foxxdesk_brand_with_fixes.py (opcional ausente)`

## Alterações

| Status | Arquivo | Linha | Ação | Mensagem |
|---|---|---:|---|---|
| alterado | `.github/workflows/bridge.yml` | 89 | aplicar regras standalone de rebrand | conteúdo textual mudou por regra segura; sem payload/ZIP |
| alterado | `.github/workflows/flutter-build.yml` | 180 | aplicar regras standalone de rebrand | conteúdo textual mudou por regra segura; sem payload/ZIP |
| alterado | `.github/workflows/playground.yml` | 151 | aplicar regras standalone de rebrand | conteúdo textual mudou por regra segura; sem payload/ZIP |
| alterado | `res/DEBIAN/postinst` | 8 | aplicar regras standalone de rebrand | conteúdo textual mudou por regra segura; sem payload/ZIP |
| alterado | `res/PKGBUILD` | 29 | aplicar regras standalone de rebrand | conteúdo textual mudou por regra segura; sem payload/ZIP |
| alterado | `res/rpm-flutter-suse.spec` | 62 | aplicar regras standalone de rebrand | conteúdo textual mudou por regra segura; sem payload/ZIP |
| alterado | `res/rpm-flutter.spec` | 62 | aplicar regras standalone de rebrand | conteúdo textual mudou por regra segura; sem payload/ZIP |

## Pendências

- `libs/hbb_common/Cargo.toml`: submódulo ausente; rode `git submodule update --init --recursive` ou garanta `submodules: recursive` no checkout do workflow
