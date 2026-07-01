# Relatório de rebrand FoxxDesk

- Data/hora: `2026-07-01 14:51:45`
- Modo: `apply`
- Projeto alvo: `/home/mateus/_Projects/FoxxDesk2`
- Script: `apply_foxxdesk_rebrand_all_files_no_zip_v18.py`
- Versão do script: `v18-ci-executable-and-msi-duplicate-guard-no-zip-2026-07-01`
- Payload/ZIP/manifesto externo: `não`
- Espelhamento/substituição de arquivo inteiro por referência antiga: `não`
- Perfil: `full`
- Estratégia: `patch-only; não espelha arquivos inteiros; full = TODOS os arquivos da allowlist + proteção de upstream + fixes Flutter Windows/bridge + portable packer path guard v17 + chmod executável completo + MSI duplicate guard v18 completo + MSI duplicate guard v18`
- Observação: se aparecerem apenas ~13 arquivos, você provavelmente executou a v9 safe ou usou --profile safe.

## Valores dinâmicos

- server: `foxxdesk.mguimaraesn.dev`
- relay: `foxxdesk.mguimaraesn.dev`
- key: `<key ocultada; len=44; sha256=a58bc137d7>`
- maintainer-email: `mateus@mguimaraesn.dev`
- homepage: `https://foxxdesk.mguimaraesn.dev`

## Resumo

- Arquivos permitidos na allowlist: `262`
- Arquivos analisados: `279`
- Arquivos alterados: `13`
- Arquivos já aplicados/sem mudança: `261`
- Arquivos esperados não encontrados: `4`
- Arquivos ignorados: `4`
- Renomeações/cópias criadas: `0`
- Pendências: `0`
- Backup: `/home/mateus/_Projects/FoxxDesk2/.rebrand_backup/20260701_145143`

## Arquivos alterados

- `entrypoint.sh`
- `flutter/build_android.sh`
- `flutter/build_fdroid.sh`
- `flutter/build_ios.sh`
- `flutter/ios_arm64.sh`
- `flutter/ios_x64.sh`
- `flutter/ndk_arm.sh`
- `flutter/ndk_arm64.sh`
- `flutter/ndk_x64.sh`
- `flutter/ndk_x86.sh`
- `flutter/run.sh`
- `res/msi/Package/Components/RustDesk.wxs`
- `res/osx-dist.sh`

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
| removido | `res/msi/Package/Components/RustDesk.wxs` | 1 | remover arquivo antigo que duplica símbolos no MSI | res/msi/Package/Components/RustDesk.wxs não pode coexistir com res/msi/Package/Components/FoxxDesk.wxs; evita WIX0091/WIX0092 |
| chmod +x | `entrypoint.sh` | 1 | garantir bit executável no Git/CI | marca como executável; rode git add para registrar modo 100755 |
| chmod +x | `flutter/build_android.sh` | 1 | garantir bit executável no Git/CI | marca como executável; rode git add para registrar modo 100755 |
| chmod +x | `flutter/build_fdroid.sh` | 1 | garantir bit executável no Git/CI | marca como executável; rode git add para registrar modo 100755 |
| chmod +x | `flutter/build_ios.sh` | 1 | garantir bit executável no Git/CI | marca como executável; rode git add para registrar modo 100755 |
| chmod +x | `flutter/ios_arm64.sh` | 1 | garantir bit executável no Git/CI | marca como executável; rode git add para registrar modo 100755 |
| chmod +x | `flutter/ios_x64.sh` | 1 | garantir bit executável no Git/CI | marca como executável; rode git add para registrar modo 100755 |
| chmod +x | `flutter/ndk_arm.sh` | 1 | garantir bit executável no Git/CI | marca como executável; rode git add para registrar modo 100755 |
| chmod +x | `flutter/ndk_arm64.sh` | 1 | garantir bit executável no Git/CI | marca como executável; rode git add para registrar modo 100755 |
| chmod +x | `flutter/ndk_x64.sh` | 1 | garantir bit executável no Git/CI | marca como executável; rode git add para registrar modo 100755 |
| chmod +x | `flutter/ndk_x86.sh` | 1 | garantir bit executável no Git/CI | marca como executável; rode git add para registrar modo 100755 |
| chmod +x | `flutter/run.sh` | 1 | garantir bit executável no Git/CI | marca como executável; rode git add para registrar modo 100755 |
| chmod +x | `res/osx-dist.sh` | 1 | garantir bit executável no Git/CI | marca como executável; rode git add para registrar modo 100755 |

## Pendências

Nenhuma.
