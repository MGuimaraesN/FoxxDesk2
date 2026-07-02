# Relatório de rebrand FoxxDesk

- Data/hora: `2026-07-02 07:20:26`
- Modo: `apply`
- Projeto alvo: `/home/mateus/_Projects/FoxxDesk2`
- Script: `apply_foxxdesk_rebrand_all_files_no_zip_v22.py`
- Versão do script: `v22-windows-appdata-driver-cleanup-2026-07-02`
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

- Arquivos permitidos na allowlist: `265`
- Arquivos analisados: `282`
- Arquivos alterados: `5`
- Arquivos já aplicados/sem mudança: `268`
- Arquivos esperados não encontrados: `4`
- Arquivos ignorados: `4`
- Renomeações/cópias criadas: `0`
- Pendências: `0`
- Backup: `/home/mateus/_Projects/FoxxDesk2/.rebrand_backup/20260702_072024`

## Arquivos alterados

- `.github/workflows/flutter-build.yml`
- `libs/hbb_common/src/config.rs`
- `libs/portable/src/main.rs`
- `res/job.py`
- `src/platform/windows.rs`

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
| alterado | `.github/workflows/flutter-build.yml` | 284 | aplicar regras standalone de rebrand | conteúdo textual mudou por regra segura; sem payload/ZIP |
| alterado | `libs/hbb_common/src/config.rs` | 802 | aplicar regras standalone de rebrand | conteúdo textual mudou por regra segura; sem payload/ZIP |
| alterado | `libs/portable/src/main.rs` | 20 | aplicar regras standalone de rebrand | conteúdo textual mudou por regra segura; sem payload/ZIP |
| alterado | `res/job.py` | 208 | aplicar regras standalone de rebrand | conteúdo textual mudou por regra segura; sem payload/ZIP |
| alterado | `src/platform/windows.rs` | 1231 | aplicar regras standalone de rebrand | conteúdo textual mudou por regra segura; sem payload/ZIP |

## Pendências

Nenhuma.
