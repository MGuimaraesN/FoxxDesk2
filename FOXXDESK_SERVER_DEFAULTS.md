# FoxxDesk Server Defaults

Valores aplicados pelo `scripts/apply_foxxdesk_brand.py`.

- HBBS / ID server: `foxxdesk.mguimaraesn.dev`
- HBBR / Relay server: `foxxdesk.mguimaraesn.dev`
- Public key: `6WbpsDtYMwUca74qNvNaBfV4pUIGzyXnX1Q8V8fZ8YA=`

Observação: o cliente RustDesk/FoxxDesk usa `RENDEZVOUS_SERVERS`, `RENDEZVOUS_PORT` e `RS_PUB_KEY` em `libs/hbb_common/src/config.rs`. O relay é anunciado/selecionado pelo servidor; não substitua URLs/downloads upstream por domínios fictícios.
