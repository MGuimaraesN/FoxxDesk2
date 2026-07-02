# Relatório de rebrand FoxxDesk

- Data/hora: `2026-07-01 20:59:35`
- Modo: `apply`
- Projeto alvo: `/home/mateus/_Projects/FoxxDesk2`
- Script: `apply_foxxdesk_rebrand_all_files_no_zip_v21.py`
- Versão do script: `v21-printer-driver-paths-case-safe-2026-07-01`
- Payload/ZIP/manifesto externo: `não`
- Espelhamento/substituição de arquivo inteiro por referência antiga: `não`
- Perfil: `full`
- Estratégia: `patch-only; não espelha arquivos inteiros; full = TODOS os arquivos da allowlist + proteção de upstream + fixes Flutter Windows/bridge + portable packer path guard v17 + chmod executável completo + MSI duplicate guard v18 + embedded server/relay/key defaults ocultos + artefatos limpos v20 + ajustes seguros de driver/impressora v21`
- Observação: se aparecerem apenas ~13 arquivos, você provavelmente executou a v9 safe ou usou --profile safe.

## Valores dinâmicos

- server: `foxxdesk.mguimaraesn.dev`
- relay: `foxxdesk.mguimaraesn.dev`
- key: `<key ocultada; len=44; sha256=a58bc137d7>`
- maintainer-email: `mateus@mguimaraesn.dev`
- homepage: `https://foxxdesk.mguimaraesn.dev`

## Resumo

- Arquivos permitidos na allowlist: `265`
- Arquivos analisados: `282`
- Arquivos alterados: `12`
- Arquivos já aplicados/sem mudança: `262`
- Arquivos esperados não encontrados: `4`
- Arquivos ignorados: `4`
- Renomeações/cópias criadas: `0`
- Pendências: `0`
- Backup: `/home/mateus/_Projects/FoxxDesk2/.rebrand_backup/20260701_205934`

## Arquivos alterados

- `.github/workflows/flutter-build.yml`
- `build.py`
- `libs/portable/src/main.rs`
- `libs/remote_printer/src/lib.rs`
- `res/job.py`
- `res/msi/CustomActions/CustomActions.cpp`
- `res/msi/CustomActions/RemotePrinter.cpp`
- `res/msi/Package/Components/FoxxDesk.wxs`
- `src/common.rs`
- `src/core_main.rs`
- `src/flutter_ffi.rs`
- `src/privacy_mode/win_topmost_window.rs`

## Arquivos renomeados/copiados

Nenhum.

## Arquivos esperados que não foram encontrados

- `BRAND_CHANGELOG.md`
- `FOXXDESK_MAX_SAFE_BRAND_REPORT.md`
- `FOXXDESK_SERVER_DEFAULTS.md`
- `NOTICE.md`

## Arquivos ignorados

- `scripts/apply_foxxdesk_brand.py (opcional ausente)`
- `scripts/apply_foxxdesk_brand_DEFINITIVE.py (opcional ausente)`
- `scripts/apply_foxxdesk_brand_SAFE.py (opcional ausente)`
- `scripts/apply_foxxdesk_brand_with_fixes.py (opcional ausente)`

## Alterações

| Status | Arquivo | Linha | Ação | Mensagem |
|---|---|---:|---|---|
| alterado | `.github/workflows/flutter-build.yml` | 54 | aplicar regras standalone de rebrand | conteúdo textual mudou por regra segura; sem payload/ZIP |
| alterado | `build.py` | 31 | aplicar regras standalone de rebrand | conteúdo textual mudou por regra segura; sem payload/ZIP |
| alterado | `libs/portable/src/main.rs` | 219 | aplicar regras standalone de rebrand | conteúdo textual mudou por regra segura; sem payload/ZIP |
| alterado | `libs/remote_printer/src/lib.rs` | 10 | aplicar regras standalone de rebrand | conteúdo textual mudou por regra segura; sem payload/ZIP |
| alterado | `res/job.py` | 208 | aplicar regras standalone de rebrand | conteúdo textual mudou por regra segura; sem payload/ZIP |
| alterado | `res/msi/CustomActions/CustomActions.cpp` | 209 | aplicar regras standalone de rebrand | conteúdo textual mudou por regra segura; sem payload/ZIP |
| alterado | `res/msi/CustomActions/RemotePrinter.cpp` | 21 | aplicar regras standalone de rebrand | conteúdo textual mudou por regra segura; sem payload/ZIP |
| alterado | `res/msi/Package/Components/FoxxDesk.wxs` | 25 | aplicar regras standalone de rebrand | conteúdo textual mudou por regra segura; sem payload/ZIP |
| alterado | `src/common.rs` | 2205 | aplicar regras standalone de rebrand | conteúdo textual mudou por regra segura; sem payload/ZIP |
| alterado | `src/core_main.rs` | 311 | aplicar regras standalone de rebrand | conteúdo textual mudou por regra segura; sem payload/ZIP |
| alterado | `src/flutter_ffi.rs` | 2809 | aplicar regras standalone de rebrand | conteúdo textual mudou por regra segura; sem payload/ZIP |
| alterado | `src/privacy_mode/win_topmost_window.rs` | 33 | aplicar regras standalone de rebrand | conteúdo textual mudou por regra segura; sem payload/ZIP |

## Pendências

Nenhuma.
