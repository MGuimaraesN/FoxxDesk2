# Relatório de rebrand FoxxDesk

- Data/hora: `2026-07-02 11:41:57`
- Modo: `apply`
- Projeto alvo: `/home/mateus/_Projects/FoxxDesk2`
- Script: `apply_foxxdesk_rebrand_all_files_no_zip_v22.py`
- Versão do script: `v24-on-demand-elevation-and-printer-brand-cleanup-2026-07-02`
- Payload/ZIP/manifesto externo: `não`
- Espelhamento/substituição de arquivo inteiro por referência antiga: `não`
- Perfil: `full`
- Estratégia: `patch-only; não espelha arquivos inteiros; full = TODOS os arquivos da allowlist + proteção de upstream + fixes Flutter Windows/bridge + portable packer path guard v17 + chmod executável completo + MSI duplicate guard v18 + embedded server/relay/key defaults ocultos + artefatos limpos v20 + ajustes seguros de driver/impressora v21 + AppData Local FoxxDesk e limpeza final de driver v22`
- Observação: se aparecerem apenas ~13 arquivos, você provavelmente executou a v9 safe ou usou --profile safe.

## Valores dinâmicos

- server: `foxxdesk.mguimaraesn.dev`
- relay: `foxxdesk.mguimaraesn.dev`
- key: `<key ocultada; len=44; sha256=a58bc137d7>`
- maintainer-email: `mateus@mguimaraesn.dev`
- homepage: `https://foxxdesk.mguimaraesn.dev`

## Resumo

- Arquivos permitidos na allowlist: `267`
- Arquivos analisados: `284`
- Arquivos alterados: `5`
- Arquivos já aplicados/sem mudança: `270`
- Arquivos esperados não encontrados: `4`
- Arquivos ignorados: `4`
- Renomeações/cópias criadas: `0`
- Pendências: `0`
- Backup: `/home/mateus/_Projects/FoxxDesk2/.rebrand_backup/20260702_114156`

## Arquivos alterados

- `.github/workflows/flutter-build.yml`
- `flutter/windows/runner/runner.exe.manifest`
- `res/manifest.xml`
- `src/core_main.rs`
- `src/server/connection.rs`

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
| alterado | `.github/workflows/flutter-build.yml` | 270 | aplicar regras standalone de rebrand | conteúdo textual mudou por regra segura; sem payload/ZIP |
| alterado | `flutter/windows/runner/runner.exe.manifest` | 20 | aplicar regras standalone de rebrand | conteúdo textual mudou por regra segura; sem payload/ZIP |
| alterado | `res/manifest.xml` | 36 | aplicar regras standalone de rebrand | conteúdo textual mudou por regra segura; sem payload/ZIP |
| alterado | `src/core_main.rs` | 144 | aplicar regras standalone de rebrand | conteúdo textual mudou por regra segura; sem payload/ZIP |
| alterado | `src/server/connection.rs` | 5146 | aplicar regras standalone de rebrand | conteúdo textual mudou por regra segura; sem payload/ZIP |

## Pendências

Nenhuma.
