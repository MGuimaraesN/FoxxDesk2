# FoxxDesk Brand Changelog

## Summary

- Objetivo: rebrand controlado e amplo de FoxxDesk para FoxxDesk.
- Escopo alterado: marca visível, binário principal, empacotamento, instaladores, serviços, application IDs, deep links, UI, traduções, documentação e GitHub Actions.
- Não alterado: rede, NAT traversal, rendezvous/relay, criptografia, autenticação, permissões, protocolo, IPC, drivers, captura, clipboard, transferência de arquivos, FFI e dependências upstream.
- Licença: `LICENCE` permanece intacto; `NOTICE.md` preserva a origem, os copyrights e a AGPL-3.0.
- Identidade aplicada: `FoxxDesk`, `foxxdesk`, `FoxxDesk Remote Desktop`, `com.foxxdesk.client` e `rustdesk://`.

## Inventory and Classification

A auditoria inicial e final usou `rg`, `git grep` e `find` para `FoxxDesk/foxxdesk/FOXXDESK`, `carriez`, `hbb`, `flutter_hbb`, `librustdesk` e nomes de arquivos.

| Classe | Decisão |
|---|---|
| Marca/UI, títulos, notificações, About, 2FA | ALTERAR para FoxxDesk |
| Binário, pacotes, serviços, desktop entries, bundles e artefatos | ALTERAR para foxxdesk/FoxxDesk |
| `librustdesk`, símbolos FFI, generated bridges e `flutter_hbb` | MANTER |
| Drivers `rustdesk_idd`, `RustDeskIddDriver`, impressora e topmost helper | MANTER |
| URLs, chaves e servidores upstream reais | MANTER |
| Chaves de tradução e config/IPC persistidas | MANTER; alterar somente valor exibido |
| `rustdesk://` legado | MANTER de forma aditiva onde o sistema aceita múltiplos schemes |

## Changed Files

| Arquivo | Tipo | Alteração | Motivo | Risco |
|---|---|---|---|---|
| `github/workflows/fdroid.yml` | Rebrand (M) | Identidade de marca/empacotamento foi alinhada a FoxxDesk. | Identidade FoxxDesk controlada | Baixo |
| `.github/workflows/flutter-build.yml` | GitHub Actions (M) | Nomes exibidos, staging e artefatos foram alinhados a FoxxDesk; ações/downloads upstream foram mantidos. | Identidade FoxxDesk controlada | Médio |
| `.github/workflows/flutter-ci.yml` | GitHub Actions (M) | Nomes exibidos, staging e artefatos foram alinhados a FoxxDesk; ações/downloads upstream foram mantidos. | Identidade FoxxDesk controlada | Médio |
| `.github/workflows/flutter-nightly.yml` | GitHub Actions (M) | Nomes exibidos, staging e artefatos foram alinhados a FoxxDesk; ações/downloads upstream foram mantidos. | Identidade FoxxDesk controlada | Médio |
| `.github/workflows/flutter-tag.yml` | GitHub Actions (M) | Nomes exibidos, staging e artefatos foram alinhados a FoxxDesk; ações/downloads upstream foram mantidos. | Identidade FoxxDesk controlada | Médio |
| `.github/workflows/playground.yml` | GitHub Actions (M) | Nomes exibidos, staging e artefatos foram alinhados a FoxxDesk; ações/downloads upstream foram mantidos. | Identidade FoxxDesk controlada | Médio |
| `Cargo.lock` | Cargo (M) | Package/binário e metadados foram migrados; lib principal permaneceu librustdesk. | Identidade FoxxDesk controlada | Médio |
| `Cargo.toml` | Cargo (M) | Package/binário e metadados foram migrados; lib principal permaneceu librustdesk. | Identidade FoxxDesk controlada | Médio |
| `Dockerfile` | Build container (M) | Diretório de checkout/build foi alinhado ao slug foxxdesk. | Identidade FoxxDesk controlada | Baixo |
| `README.md` | Documentação (M) | Identidade FoxxDesk, origem FoxxDesk, AGPL e pendências oficiais foram documentadas. | Identidade FoxxDesk controlada | Baixo |
| `appimage/AppImageBuilder-aarch64.yml` | Linux package (M) | Manifesto, ID, caminhos e artefatos foram migrados para FoxxDesk. | Identidade FoxxDesk controlada | Médio |
| `appimage/AppImageBuilder-x86_64.yml` | Linux package (M) | Manifesto, ID, caminhos e artefatos foram migrados para FoxxDesk. | Identidade FoxxDesk controlada | Médio |
| `build.py` | Empacotamento (M) | Pacotes, serviços, desktop entries, paths e artefatos foram migrados para FoxxDesk. | Identidade FoxxDesk controlada | Médio |
| `entrypoint.sh` | Build container (M) | Diretório de checkout/build foi alinhado ao slug foxxdesk. | Identidade FoxxDesk controlada | Baixo |
| `fastlane/metadata/android/en-US/full_description.txt` | Store metadata (M) | Descrição visível passou a FoxxDesk e links upstream foram explicitados. | Identidade FoxxDesk controlada | Baixo |
| `fastlane/metadata/android/fr-FR/full_description.txt` | Store metadata (M) | Descrição visível passou a FoxxDesk e links upstream foram explicitados. | Identidade FoxxDesk controlada | Baixo |
| `fastlane/metadata/android/nl-NL/full_description.txt` | Store metadata (M) | Descrição visível passou a FoxxDesk e links upstream foram explicitados. | Identidade FoxxDesk controlada | Baixo |
| `fastlane/metadata/android/zh-CN/full_description.txt` | Store metadata (M) | Descrição visível passou a FoxxDesk e links upstream foram explicitados. | Identidade FoxxDesk controlada | Baixo |
| `flatpak/com.foxxdesk.client.metainfo.xml` | Linux package (D) | Manifesto, ID, caminhos e artefatos foram migrados para FoxxDesk. | Identidade FoxxDesk controlada | Médio |
| `flatpak/foxxdesk.json` | Linux package (D) | Manifesto, ID, caminhos e artefatos foram migrados para FoxxDesk. | Identidade FoxxDesk controlada | Médio |
| `flutter/android/app/build.gradle` | Android (M) | Application ID, labels, notificações, WakeLock e deep link foram ajustados sem renomear pacote Kotlin/FFI. | Identidade FoxxDesk controlada | Médio |
| `flutter/android/app/src/main/AndroidManifest.xml` | Android (M) | Application ID, labels, notificações, WakeLock e deep link foram ajustados sem renomear pacote Kotlin/FFI. | Identidade FoxxDesk controlada | Médio |
| `flutter/android/app/src/main/kotlin/com/carriez/flutter_hbb/BootReceiver.kt` | Android (M) | Application ID, labels, notificações, WakeLock e deep link foram ajustados sem renomear pacote Kotlin/FFI. | Identidade FoxxDesk controlada | Médio |
| `flutter/android/app/src/main/kotlin/com/carriez/flutter_hbb/MainService.kt` | Android (M) | Application ID, labels, notificações, WakeLock e deep link foram ajustados sem renomear pacote Kotlin/FFI. | Identidade FoxxDesk controlada | Médio |
| `flutter/android/app/src/main/res/values/strings.xml` | Android (M) | Application ID, labels, notificações, WakeLock e deep link foram ajustados sem renomear pacote Kotlin/FFI. | Identidade FoxxDesk controlada | Médio |
| `flutter/ios/Runner.xcodeproj/project.pbxproj` | iOS (M) | Display name, produto, bundle ID, scheme e perfil pendente foram ajustados; FFI e Firebase upstream foram preservados. | Identidade FoxxDesk controlada | Médio |
| `flutter/ios/Runner.xcodeproj/xcshareddata/xcschemes/Runner.xcscheme` | iOS (M) | Display name, produto, bundle ID, scheme e perfil pendente foram ajustados; FFI e Firebase upstream foram preservados. | Identidade FoxxDesk controlada | Médio |
| `flutter/ios/Runner/Info.plist` | iOS (M) | Display name, produto, bundle ID, scheme e perfil pendente foram ajustados; FFI e Firebase upstream foram preservados. | Identidade FoxxDesk controlada | Médio |
| `flutter/ios/exportOptions.plist` | iOS (M) | Display name, produto, bundle ID, scheme e perfil pendente foram ajustados; FFI e Firebase upstream foram preservados. | Identidade FoxxDesk controlada | Médio |
| `flutter/lib/common.dart` | Flutter UI (M) | Textos, títulos e tratamento compatível de deep links foram ajustados sem renomear flutter_hbb. | Identidade FoxxDesk controlada | Baixo |
| `flutter/lib/desktop/pages/desktop_home_page.dart` | Flutter UI (M) | Textos, títulos e tratamento compatível de deep links foram ajustados sem renomear flutter_hbb. | Identidade FoxxDesk controlada | Baixo |
| `flutter/lib/desktop/pages/desktop_setting_page.dart` | Flutter UI (M) | Textos, títulos e tratamento compatível de deep links foram ajustados sem renomear flutter_hbb. | Identidade FoxxDesk controlada | Baixo |
| `flutter/lib/desktop/widgets/tabbar_widget.dart` | Flutter UI (M) | Textos, títulos e tratamento compatível de deep links foram ajustados sem renomear flutter_hbb. | Identidade FoxxDesk controlada | Baixo |
| `flutter/lib/mobile/pages/home_page.dart` | Flutter UI (M) | Textos, títulos e tratamento compatível de deep links foram ajustados sem renomear flutter_hbb. | Identidade FoxxDesk controlada | Baixo |
| `flutter/lib/mobile/pages/settings_page.dart` | Flutter UI (M) | Textos, títulos e tratamento compatível de deep links foram ajustados sem renomear flutter_hbb. | Identidade FoxxDesk controlada | Baixo |
| `flutter/lib/web/bridge.dart` | Flutter UI (M) | Textos, títulos e tratamento compatível de deep links foram ajustados sem renomear flutter_hbb. | Identidade FoxxDesk controlada | Baixo |
| `flutter/linux/CMakeLists.txt` | Linux (M) | Binário, application ID, título e ícone empacotado foram ajustados; canais/FFI foram preservados. | Identidade FoxxDesk controlada | Médio |
| `flutter/linux/my_application.cc` | Linux (M) | Binário, application ID, título e ícone empacotado foram ajustados; canais/FFI foram preservados. | Identidade FoxxDesk controlada | Médio |
| `flutter/macos/Runner.xcodeproj/project.pbxproj` | macOS (M) | Produto, bundle ID, app bundle, scheme e logs visíveis foram ajustados; canais e librustdesk foram preservados. | Identidade FoxxDesk controlada | Médio |
| `flutter/macos/Runner.xcodeproj/xcshareddata/xcschemes/Runner.xcscheme` | macOS (M) | Produto, bundle ID, app bundle, scheme e logs visíveis foram ajustados; canais e librustdesk foram preservados. | Identidade FoxxDesk controlada | Médio |
| `flutter/macos/Runner/Base.lproj/MainMenu.xib` | macOS (M) | Produto, bundle ID, app bundle, scheme e logs visíveis foram ajustados; canais e librustdesk foram preservados. | Identidade FoxxDesk controlada | Médio |
| `flutter/macos/Runner/Configs/AppInfo.xcconfig` | macOS (M) | Produto, bundle ID, app bundle, scheme e logs visíveis foram ajustados; canais e librustdesk foram preservados. | Identidade FoxxDesk controlada | Médio |
| `flutter/macos/Runner/Info.plist` | macOS (M) | Produto, bundle ID, app bundle, scheme e logs visíveis foram ajustados; canais e librustdesk foram preservados. | Identidade FoxxDesk controlada | Médio |
| `flutter/macos/Runner/MainFlutterWindow.swift` | macOS (M) | Produto, bundle ID, app bundle, scheme e logs visíveis foram ajustados; canais e librustdesk foram preservados. | Identidade FoxxDesk controlada | Médio |
| `flutter/pubspec.yaml` | Rebrand (M) | Identidade de marca/empacotamento foi alinhada a FoxxDesk. | Identidade FoxxDesk controlada | Baixo |
| `flutter/windows/CMakeLists.txt` | Windows (M) | Binário e metadados de versão/produto foram ajustados; DLL e símbolos FFI foram preservados. | Identidade FoxxDesk controlada | Médio |
| `flutter/windows/runner/Runner.rc` | Windows (M) | Binário e metadados de versão/produto foram ajustados; DLL e símbolos FFI foram preservados. | Identidade FoxxDesk controlada | Médio |
| `flutter/windows/runner/main.cpp` | Windows (M) | Binário e metadados de versão/produto foram ajustados; DLL e símbolos FFI foram preservados. | Identidade FoxxDesk controlada | Médio |
| `libs/hbb_common/src/config.rs` | Rebrand (M) | Identidade de marca/empacotamento foi alinhada a FoxxDesk. | Identidade FoxxDesk controlada | Baixo |
| `libs/hbb_common/src/platform/mod.rs` | Rebrand (M) | Identidade de marca/empacotamento foi alinhada a FoxxDesk. | Identidade FoxxDesk controlada | Baixo |
| `libs/portable/Cargo.lock` | Windows installer (M) | MSI/portable, metadados e marcadores foram migrados; driver/topmost upstream foi preservado. | Identidade FoxxDesk controlada | Médio |
| `libs/portable/Cargo.toml` | Windows installer (M) | MSI/portable, metadados e marcadores foram migrados; driver/topmost upstream foi preservado. | Identidade FoxxDesk controlada | Médio |
| `libs/portable/generate.py` | Windows installer (M) | MSI/portable, metadados e marcadores foram migrados; driver/topmost upstream foi preservado. | Identidade FoxxDesk controlada | Médio |
| `libs/portable/src/bin_reader.rs` | Windows installer (M) | MSI/portable, metadados e marcadores foram migrados; driver/topmost upstream foi preservado. | Identidade FoxxDesk controlada | Médio |
| `libs/portable/src/main.rs` | Windows installer (M) | MSI/portable, metadados e marcadores foram migrados; driver/topmost upstream foi preservado. | Identidade FoxxDesk controlada | Médio |
| `res/DEBIAN/postinst` | Empacotamento (M) | Pacotes, serviços, desktop entries, paths e artefatos foram migrados para FoxxDesk. | Identidade FoxxDesk controlada | Médio |
| `res/DEBIAN/postrm` | Empacotamento (M) | Pacotes, serviços, desktop entries, paths e artefatos foram migrados para FoxxDesk. | Identidade FoxxDesk controlada | Médio |
| `res/DEBIAN/preinst` | Empacotamento (M) | Pacotes, serviços, desktop entries, paths e artefatos foram migrados para FoxxDesk. | Identidade FoxxDesk controlada | Médio |
| `res/DEBIAN/prerm` | Empacotamento (M) | Pacotes, serviços, desktop entries, paths e artefatos foram migrados para FoxxDesk. | Identidade FoxxDesk controlada | Médio |
| `res/PKGBUILD` | Empacotamento (M) | Pacotes, serviços, desktop entries, paths e artefatos foram migrados para FoxxDesk. | Identidade FoxxDesk controlada | Médio |
| `res/msi/Package/Components/FoxxDesk.wxs` | Windows installer (D) | MSI/portable, metadados e marcadores foram migrados; driver/topmost upstream foi preservado. | Identidade FoxxDesk controlada | Médio |
| `res/msi/Package/Language/Package.en-us.wxl` | Windows installer (M) | MSI/portable, metadados e marcadores foram migrados; driver/topmost upstream foi preservado. | Identidade FoxxDesk controlada | Médio |
| `res/msi/README.md` | Windows installer (M) | MSI/portable, metadados e marcadores foram migrados; driver/topmost upstream foi preservado. | Identidade FoxxDesk controlada | Médio |
| `res/msi/preprocess.py` | Windows installer (M) | MSI/portable, metadados e marcadores foram migrados; driver/topmost upstream foi preservado. | Identidade FoxxDesk controlada | Médio |
| `res/osx-dist.sh` | Empacotamento (M) | Pacotes, serviços, desktop entries, paths e artefatos foram migrados para FoxxDesk. | Identidade FoxxDesk controlada | Médio |
| `res/pacman_install` | Empacotamento (M) | Pacotes, serviços, desktop entries, paths e artefatos foram migrados para FoxxDesk. | Identidade FoxxDesk controlada | Médio |
| `res/pam.d/foxxdesk.debian` | Empacotamento (D) | Pacotes, serviços, desktop entries, paths e artefatos foram migrados para FoxxDesk. | Identidade FoxxDesk controlada | Médio |
| `res/pam.d/foxxdesk.suse` | Empacotamento (D) | Pacotes, serviços, desktop entries, paths e artefatos foram migrados para FoxxDesk. | Identidade FoxxDesk controlada | Médio |
| `res/rpm-flutter-suse.spec` | Empacotamento (M) | Pacotes, serviços, desktop entries, paths e artefatos foram migrados para FoxxDesk. | Identidade FoxxDesk controlada | Médio |
| `res/rpm-flutter.spec` | Empacotamento (M) | Pacotes, serviços, desktop entries, paths e artefatos foram migrados para FoxxDesk. | Identidade FoxxDesk controlada | Médio |
| `res/rpm-suse.spec` | Empacotamento (M) | Pacotes, serviços, desktop entries, paths e artefatos foram migrados para FoxxDesk. | Identidade FoxxDesk controlada | Médio |
| `res/rpm.spec` | Empacotamento (M) | Pacotes, serviços, desktop entries, paths e artefatos foram migrados para FoxxDesk. | Identidade FoxxDesk controlada | Médio |
| `res/foxxdesk-link.desktop` | Empacotamento (D) | Pacotes, serviços, desktop entries, paths e artefatos foram migrados para FoxxDesk. | Identidade FoxxDesk controlada | Médio |
| `res/foxxdesk.desktop` | Empacotamento (D) | Pacotes, serviços, desktop entries, paths e artefatos foram migrados para FoxxDesk. | Identidade FoxxDesk controlada | Médio |
| `res/foxxdesk.service` | Empacotamento (D) | Pacotes, serviços, desktop entries, paths e artefatos foram migrados para FoxxDesk. | Identidade FoxxDesk controlada | Médio |
| `src/auth_2fa.rs` | Rust / UI (M) | Marca visível ou nome de binário foi ajustado sem alterar rede, segurança, protocolo ou drivers. | Identidade FoxxDesk controlada | Baixo |
| `src/clipboard.rs` | Rust / UI (M) | Marca visível ou nome de binário foi ajustado sem alterar rede, segurança, protocolo ou drivers. | Identidade FoxxDesk controlada | Baixo |
| `src/common.rs` | Rust / UI (M) | Marca visível ou nome de binário foi ajustado sem alterar rede, segurança, protocolo ou drivers. | Identidade FoxxDesk controlada | Baixo |
| `src/core_main.rs` | Rust / UI (M) | Marca visível ou nome de binário foi ajustado sem alterar rede, segurança, protocolo ou drivers. | Identidade FoxxDesk controlada | Baixo |
| `src/custom_server.rs` | Rust / UI (M) | Marca visível ou nome de binário foi ajustado sem alterar rede, segurança, protocolo ou drivers. | Identidade FoxxDesk controlada | Baixo |
| `src/flutter_ffi.rs` | Plataforma / update (M) | Paths, bundles e nomes de artefato visíveis foram migrados com compatibilidade técnica preservada. | Identidade FoxxDesk controlada | Médio |
| `src/ipc/auth.rs` | Rust / UI (M) | Marca visível ou nome de binário foi ajustado sem alterar rede, segurança, protocolo ou drivers. | Identidade FoxxDesk controlada | Baixo |
| `src/lang.rs` | Rust / UI (M) | Marca visível ou nome de binário foi ajustado sem alterar rede, segurança, protocolo ou drivers. | Identidade FoxxDesk controlada | Baixo |
| `src/lang/ar.rs` | UI / tradução (M) | Valores exibidos de marca foram alterados; chaves de tradução e placeholders foram preservados. | Identidade FoxxDesk controlada | Baixo |
| `src/lang/be.rs` | UI / tradução (M) | Valores exibidos de marca foram alterados; chaves de tradução e placeholders foram preservados. | Identidade FoxxDesk controlada | Baixo |
| `src/lang/bg.rs` | UI / tradução (M) | Valores exibidos de marca foram alterados; chaves de tradução e placeholders foram preservados. | Identidade FoxxDesk controlada | Baixo |
| `src/lang/ca.rs` | UI / tradução (M) | Valores exibidos de marca foram alterados; chaves de tradução e placeholders foram preservados. | Identidade FoxxDesk controlada | Baixo |
| `src/lang/cn.rs` | UI / tradução (M) | Valores exibidos de marca foram alterados; chaves de tradução e placeholders foram preservados. | Identidade FoxxDesk controlada | Baixo |
| `src/lang/cs.rs` | UI / tradução (M) | Valores exibidos de marca foram alterados; chaves de tradução e placeholders foram preservados. | Identidade FoxxDesk controlada | Baixo |
| `src/lang/da.rs` | UI / tradução (M) | Valores exibidos de marca foram alterados; chaves de tradução e placeholders foram preservados. | Identidade FoxxDesk controlada | Baixo |
| `src/lang/de.rs` | UI / tradução (M) | Valores exibidos de marca foram alterados; chaves de tradução e placeholders foram preservados. | Identidade FoxxDesk controlada | Baixo |
| `src/lang/el.rs` | UI / tradução (M) | Valores exibidos de marca foram alterados; chaves de tradução e placeholders foram preservados. | Identidade FoxxDesk controlada | Baixo |
| `src/lang/en.rs` | UI / tradução (M) | Valores exibidos de marca foram alterados; chaves de tradução e placeholders foram preservados. | Identidade FoxxDesk controlada | Baixo |
| `src/lang/eo.rs` | UI / tradução (M) | Valores exibidos de marca foram alterados; chaves de tradução e placeholders foram preservados. | Identidade FoxxDesk controlada | Baixo |
| `src/lang/es.rs` | UI / tradução (M) | Valores exibidos de marca foram alterados; chaves de tradução e placeholders foram preservados. | Identidade FoxxDesk controlada | Baixo |
| `src/lang/et.rs` | UI / tradução (M) | Valores exibidos de marca foram alterados; chaves de tradução e placeholders foram preservados. | Identidade FoxxDesk controlada | Baixo |
| `src/lang/eu.rs` | UI / tradução (M) | Valores exibidos de marca foram alterados; chaves de tradução e placeholders foram preservados. | Identidade FoxxDesk controlada | Baixo |
| `src/lang/fa.rs` | UI / tradução (M) | Valores exibidos de marca foram alterados; chaves de tradução e placeholders foram preservados. | Identidade FoxxDesk controlada | Baixo |
| `src/lang/fi.rs` | UI / tradução (M) | Valores exibidos de marca foram alterados; chaves de tradução e placeholders foram preservados. | Identidade FoxxDesk controlada | Baixo |
| `src/lang/fr.rs` | UI / tradução (M) | Valores exibidos de marca foram alterados; chaves de tradução e placeholders foram preservados. | Identidade FoxxDesk controlada | Baixo |
| `src/lang/ge.rs` | UI / tradução (M) | Valores exibidos de marca foram alterados; chaves de tradução e placeholders foram preservados. | Identidade FoxxDesk controlada | Baixo |
| `src/lang/gu.rs` | UI / tradução (M) | Valores exibidos de marca foram alterados; chaves de tradução e placeholders foram preservados. | Identidade FoxxDesk controlada | Baixo |
| `src/lang/he.rs` | UI / tradução (M) | Valores exibidos de marca foram alterados; chaves de tradução e placeholders foram preservados. | Identidade FoxxDesk controlada | Baixo |
| `src/lang/hi.rs` | UI / tradução (M) | Valores exibidos de marca foram alterados; chaves de tradução e placeholders foram preservados. | Identidade FoxxDesk controlada | Baixo |
| `src/lang/hr.rs` | UI / tradução (M) | Valores exibidos de marca foram alterados; chaves de tradução e placeholders foram preservados. | Identidade FoxxDesk controlada | Baixo |
| `src/lang/hu.rs` | UI / tradução (M) | Valores exibidos de marca foram alterados; chaves de tradução e placeholders foram preservados. | Identidade FoxxDesk controlada | Baixo |
| `src/lang/id.rs` | UI / tradução (M) | Valores exibidos de marca foram alterados; chaves de tradução e placeholders foram preservados. | Identidade FoxxDesk controlada | Baixo |
| `src/lang/it.rs` | UI / tradução (M) | Valores exibidos de marca foram alterados; chaves de tradução e placeholders foram preservados. | Identidade FoxxDesk controlada | Baixo |
| `src/lang/ja.rs` | UI / tradução (M) | Valores exibidos de marca foram alterados; chaves de tradução e placeholders foram preservados. | Identidade FoxxDesk controlada | Baixo |
| `src/lang/ko.rs` | UI / tradução (M) | Valores exibidos de marca foram alterados; chaves de tradução e placeholders foram preservados. | Identidade FoxxDesk controlada | Baixo |
| `src/lang/kz.rs` | UI / tradução (M) | Valores exibidos de marca foram alterados; chaves de tradução e placeholders foram preservados. | Identidade FoxxDesk controlada | Baixo |
| `src/lang/lt.rs` | UI / tradução (M) | Valores exibidos de marca foram alterados; chaves de tradução e placeholders foram preservados. | Identidade FoxxDesk controlada | Baixo |
| `src/lang/lv.rs` | UI / tradução (M) | Valores exibidos de marca foram alterados; chaves de tradução e placeholders foram preservados. | Identidade FoxxDesk controlada | Baixo |
| `src/lang/ml.rs` | UI / tradução (M) | Valores exibidos de marca foram alterados; chaves de tradução e placeholders foram preservados. | Identidade FoxxDesk controlada | Baixo |
| `src/lang/nb.rs` | UI / tradução (M) | Valores exibidos de marca foram alterados; chaves de tradução e placeholders foram preservados. | Identidade FoxxDesk controlada | Baixo |
| `src/lang/nl.rs` | UI / tradução (M) | Valores exibidos de marca foram alterados; chaves de tradução e placeholders foram preservados. | Identidade FoxxDesk controlada | Baixo |
| `src/lang/pl.rs` | UI / tradução (M) | Valores exibidos de marca foram alterados; chaves de tradução e placeholders foram preservados. | Identidade FoxxDesk controlada | Baixo |
| `src/lang/pt_PT.rs` | UI / tradução (M) | Valores exibidos de marca foram alterados; chaves de tradução e placeholders foram preservados. | Identidade FoxxDesk controlada | Baixo |
| `src/lang/ptbr.rs` | UI / tradução (M) | Valores exibidos de marca foram alterados; chaves de tradução e placeholders foram preservados. | Identidade FoxxDesk controlada | Baixo |
| `src/lang/ro.rs` | UI / tradução (M) | Valores exibidos de marca foram alterados; chaves de tradução e placeholders foram preservados. | Identidade FoxxDesk controlada | Baixo |
| `src/lang/ru.rs` | UI / tradução (M) | Valores exibidos de marca foram alterados; chaves de tradução e placeholders foram preservados. | Identidade FoxxDesk controlada | Baixo |
| `src/lang/sc.rs` | UI / tradução (M) | Valores exibidos de marca foram alterados; chaves de tradução e placeholders foram preservados. | Identidade FoxxDesk controlada | Baixo |
| `src/lang/sk.rs` | UI / tradução (M) | Valores exibidos de marca foram alterados; chaves de tradução e placeholders foram preservados. | Identidade FoxxDesk controlada | Baixo |
| `src/lang/sl.rs` | UI / tradução (M) | Valores exibidos de marca foram alterados; chaves de tradução e placeholders foram preservados. | Identidade FoxxDesk controlada | Baixo |
| `src/lang/sq.rs` | UI / tradução (M) | Valores exibidos de marca foram alterados; chaves de tradução e placeholders foram preservados. | Identidade FoxxDesk controlada | Baixo |
| `src/lang/sr.rs` | UI / tradução (M) | Valores exibidos de marca foram alterados; chaves de tradução e placeholders foram preservados. | Identidade FoxxDesk controlada | Baixo |
| `src/lang/sv.rs` | UI / tradução (M) | Valores exibidos de marca foram alterados; chaves de tradução e placeholders foram preservados. | Identidade FoxxDesk controlada | Baixo |
| `src/lang/ta.rs` | UI / tradução (M) | Valores exibidos de marca foram alterados; chaves de tradução e placeholders foram preservados. | Identidade FoxxDesk controlada | Baixo |
| `src/lang/th.rs` | UI / tradução (M) | Valores exibidos de marca foram alterados; chaves de tradução e placeholders foram preservados. | Identidade FoxxDesk controlada | Baixo |
| `src/lang/tr.rs` | UI / tradução (M) | Valores exibidos de marca foram alterados; chaves de tradução e placeholders foram preservados. | Identidade FoxxDesk controlada | Baixo |
| `src/lang/tw.rs` | UI / tradução (M) | Valores exibidos de marca foram alterados; chaves de tradução e placeholders foram preservados. | Identidade FoxxDesk controlada | Baixo |
| `src/lang/uk.rs` | UI / tradução (M) | Valores exibidos de marca foram alterados; chaves de tradução e placeholders foram preservados. | Identidade FoxxDesk controlada | Baixo |
| `src/lang/vi.rs` | UI / tradução (M) | Valores exibidos de marca foram alterados; chaves de tradução e placeholders foram preservados. | Identidade FoxxDesk controlada | Baixo |
| `src/main.rs` | Rust / UI (M) | Marca visível ou nome de binário foi ajustado sem alterar rede, segurança, protocolo ou drivers. | Identidade FoxxDesk controlada | Baixo |
| `src/naming.rs` | Rust / UI (M) | Marca visível ou nome de binário foi ajustado sem alterar rede, segurança, protocolo ou drivers. | Identidade FoxxDesk controlada | Baixo |
| `src/platform/linux.rs` | Plataforma / update (M) | Paths, bundles e nomes de artefato visíveis foram migrados com compatibilidade técnica preservada. | Identidade FoxxDesk controlada | Médio |
| `src/platform/macos.rs` | Plataforma / update (M) | Paths, bundles e nomes de artefato visíveis foram migrados com compatibilidade técnica preservada. | Identidade FoxxDesk controlada | Médio |
| `src/platform/privileges_scripts/agent.plist` | Plataforma / update (M) | Paths, bundles e nomes de artefato visíveis foram migrados com compatibilidade técnica preservada. | Identidade FoxxDesk controlada | Médio |
| `src/platform/privileges_scripts/daemon.plist` | Plataforma / update (M) | Paths, bundles e nomes de artefato visíveis foram migrados com compatibilidade técnica preservada. | Identidade FoxxDesk controlada | Médio |
| `src/platform/privileges_scripts/install.scpt` | Plataforma / update (M) | Paths, bundles e nomes de artefato visíveis foram migrados com compatibilidade técnica preservada. | Identidade FoxxDesk controlada | Médio |
| `src/platform/privileges_scripts/uninstall.scpt` | Plataforma / update (M) | Paths, bundles e nomes de artefato visíveis foram migrados com compatibilidade técnica preservada. | Identidade FoxxDesk controlada | Médio |
| `src/platform/privileges_scripts/update.scpt` | Plataforma / update (M) | Paths, bundles e nomes de artefato visíveis foram migrados com compatibilidade técnica preservada. | Identidade FoxxDesk controlada | Médio |
| `src/platform/windows.rs` | Plataforma / update (M) | Paths, bundles e nomes de artefato visíveis foram migrados com compatibilidade técnica preservada. | Identidade FoxxDesk controlada | Médio |
| `src/plugin/callback_ext.rs` | Rust / UI (M) | Marca visível ou nome de binário foi ajustado sem alterar rede, segurança, protocolo ou drivers. | Identidade FoxxDesk controlada | Baixo |
| `src/plugin/manager.rs` | Rust / UI (M) | Marca visível ou nome de binário foi ajustado sem alterar rede, segurança, protocolo ou drivers. | Identidade FoxxDesk controlada | Baixo |
| `src/plugin/mod.rs` | Rust / UI (M) | Marca visível ou nome de binário foi ajustado sem alterar rede, segurança, protocolo ou drivers. | Identidade FoxxDesk controlada | Baixo |
| `src/rendezvous_mediator.rs` | Rust / UI (M) | Marca visível ou nome de binário foi ajustado sem alterar rede, segurança, protocolo ou drivers. | Identidade FoxxDesk controlada | Baixo |
| `src/server/dbus.rs` | Rust / UI (M) | Marca visível ou nome de binário foi ajustado sem alterar rede, segurança, protocolo ou drivers. | Identidade FoxxDesk controlada | Baixo |
| `src/server/uinput.rs` | Rust / UI (M) | Marca visível ou nome de binário foi ajustado sem alterar rede, segurança, protocolo ou drivers. | Identidade FoxxDesk controlada | Baixo |
| `src/ui.rs` | Rust / UI (M) | Marca visível ou nome de binário foi ajustado sem alterar rede, segurança, protocolo ou drivers. | Identidade FoxxDesk controlada | Baixo |
| `src/ui_session_interface.rs` | Rust / UI (M) | Marca visível ou nome de binário foi ajustado sem alterar rede, segurança, protocolo ou drivers. | Identidade FoxxDesk controlada | Baixo |
| `src/updater.rs` | Plataforma / update (M) | Paths, bundles e nomes de artefato visíveis foram migrados com compatibilidade técnica preservada. | Identidade FoxxDesk controlada | Médio |
| `src/whiteboard/linux.rs` | Rust / UI (M) | Marca visível ou nome de binário foi ajustado sem alterar rede, segurança, protocolo ou drivers. | Identidade FoxxDesk controlada | Baixo |
| `src/whiteboard/macos.rs` | Rust / UI (M) | Marca visível ou nome de binário foi ajustado sem alterar rede, segurança, protocolo ou drivers. | Identidade FoxxDesk controlada | Baixo |
| `src/whiteboard/windows.rs` | Rust / UI (M) | Marca visível ou nome de binário foi ajustado sem alterar rede, segurança, protocolo ou drivers. | Identidade FoxxDesk controlada | Baixo |
| `.github/workflows/foxxdesk-build.yml` | GitHub Actions (??) | Nomes exibidos, staging e artefatos foram alinhados a FoxxDesk; ações/downloads upstream foram mantidos. | Identidade FoxxDesk controlada | Médio |
| `NOTICE.md` | Documentação (??) | Identidade FoxxDesk, origem FoxxDesk, AGPL e pendências oficiais foram documentadas. | Identidade FoxxDesk controlada | Baixo |
| `flatpak/com.foxxdesk.client.metainfo.xml` | Linux package (??) | Manifesto, ID, caminhos e artefatos foram migrados para FoxxDesk. | Identidade FoxxDesk controlada | Médio |
| `flatpak/foxxdesk.json` | Linux package (??) | Manifesto, ID, caminhos e artefatos foram migrados para FoxxDesk. | Identidade FoxxDesk controlada | Médio |
| `res/foxxdesk-link.desktop` | Empacotamento (??) | Pacotes, serviços, desktop entries, paths e artefatos foram migrados para FoxxDesk. | Identidade FoxxDesk controlada | Médio |
| `res/foxxdesk.desktop` | Empacotamento (??) | Pacotes, serviços, desktop entries, paths e artefatos foram migrados para FoxxDesk. | Identidade FoxxDesk controlada | Médio |
| `res/foxxdesk.service` | Empacotamento (??) | Pacotes, serviços, desktop entries, paths e artefatos foram migrados para FoxxDesk. | Identidade FoxxDesk controlada | Médio |
| `res/msi/Package/Components/FoxxDesk.wxs` | Windows installer (??) | MSI/portable, metadados e marcadores foram migrados; driver/topmost upstream foi preservado. | Identidade FoxxDesk controlada | Médio |
| `res/pam.d/foxxdesk.debian` | Empacotamento (??) | Pacotes, serviços, desktop entries, paths e artefatos foram migrados para FoxxDesk. | Identidade FoxxDesk controlada | Médio |
| `res/pam.d/foxxdesk.suse` | Empacotamento (??) | Pacotes, serviços, desktop entries, paths e artefatos foram migrados para FoxxDesk. | Identidade FoxxDesk controlada | Médio |
| `BRAND_CHANGELOG.md` | Relatório (novo) | Inventário exato, referências mantidas, assets, validações e pendências. | Rastreabilidade | Baixo |

## Kept FoxxDesk/Internal References

| Arquivo/padrão | Referência mantida | Motivo |
|---|---|---|
| `Cargo.toml`, `src/main.rs`, `src/service.rs`, projetos Flutter nativos | `librustdesk` | ABI/FFI carregada por Android, iOS, macOS, Linux e Windows. Renomear exigiria refactor integral de símbolos, loaders e bridges. |
| `flutter/pubspec.yaml`, `flutter/lib/**`, `flutter/android/**` | `flutter_hbb`, `package:flutter_hbb`, pacote Kotlin `com.carriez.flutter_hbb` | Identificadores internos compartilhados por imports, classes nativas e plugins; o application ID público foi alterado separadamente. |
| `flutter/lib/generated_bridge*.dart`, `src/bridge_generated*.rs` | nomes gerados | Arquivos gerados não foram editados. |
| `src/virtual_display_manager.rs`, `src/privacy_mode/**`, `libs/virtual_display/**`, MSI/workflows | `rustdesk_idd`, `RustDeskIddDriver`, `rustdesk_virtual_displays`, `RuntimeBroker_rustdesk.exe`, `RustDeskPrinterDriver` | Contratos de drivers/helpers upstream e nomes externos reais. |
| `src/server/dbus.rs`, platform channels Dart/C++/Swift, IPC/config | `org.rustdesk.rustdesk/*`, `RUSTDESK_APPNAME`, nomes de canais e estruturas | Contratos internos entre lados nativo/Dart e compatibilidade persistida. |
| `Cargo.toml`, `Cargo.lock`, `.github/workflows/**`, `flutter/pubspec.yaml`, `res/vcpkg/**` | `rustdesk-org/*`, `foxxdesk/*`, engines, actions e patches | Dependências/downloads upstream reais; trocar criaria URLs inexistentes ou quebraria o build. |
| `libs/hbb_common/src/config.rs`, `src/common.rs`, UI Flutter/Sciter, Fastlane, Flatpak, README/docs | `rustdesk.com`, GitHub FoxxDesk e docs | Servidores, documentação e projeto original reais; nenhum domínio/backend FoxxDesk foi inventado. |
| `libs/hbb_common/src/config.rs` | rendezvous `rs-ny.rustdesk.com` e `RS_PUB_KEY` | Infraestrutura e chave pública funcionais; não existem valores FoxxDesk oficiais fornecidos. |
| `src/lang/*.rs`, Flutter UI e Android Kotlin | chaves como `About FoxxDesk`, `Show FoxxDesk`, `verify_foxxdesk_password_tip` | Chaves são API interna; somente seus valores exibidos foram alterados. |
| `src/custom_server.rs`, deep-link handlers e manifests | nomes/prefixos legados `foxxdesk-*` e `rustdesk://` | Compatibilidade de arquivos/links existentes; FoxxDesk é o padrão novo. |
| `docs/README*.md`, `docs/CONTRIBUTING*.md`, `docs/SECURITY*.md` | documentação FoxxDesk herdada | Traduções/documentos upstream mantidos como material de origem; o README principal identifica claramente o fork. |
| `flutter/ios/Runner/GoogleService-Info.plist` | bundle/projeto Firebase FoxxDesk | Credencial de backend real; não foi falsificada. Deve ser substituída por configuração FoxxDesk oficial antes de habilitar Firebase em produção. |
| `.github/workflows/third-party-RustDeskTempTopMostWindow.yml` | nome do workflow/repositório helper | Projeto third-party upstream e nome de artefato técnico. |
| `res/msi/Package/License.rtf`, `LICENCE` | FoxxDesk/Purslane e textos legais | Avisos legais e copyrights originais preservados. |
| `res/foxxdesk-banner.svg` | nome/conteúdo FoxxDesk | Asset upstream mantido porque não foi fornecida arte oficial FoxxDesk. |

## Assets

| Arquivo | Status | Observação |
|---|---|---|
| `res/logo-header.svg`, `res/foxxdesk-banner.svg` | Mantido / REVISAR | Arte upstream; README marca explicitamente o logo como placeholder. |
| `res/icon.png`, `res/mac-icon.png`, `res/scalable.svg`, `res/{16x16,24x24,32x32,64x64,128x128,128x128@2x}.png` | Mantido / REVISAR | Ícones existentes continuam funcionais; referências de pacote agora usam o nome `foxxdesk`. |
| `flutter/windows/runner/resources/app_icon.ico`, `flutter/macos/Runner/AppIcon.icns` | Mantido / REVISAR | Sem arte FoxxDesk aprovada; nenhum bitmap foi falsificado. |
| `flutter/android/app/src/main/res/mipmap*/**`, `flutter/ios/Runner/Assets.xcassets/**` | Mantido / REVISAR | Launchers/splash existentes precisam de substituição manual coordenada por plataforma. |

## GitHub Actions

| Arquivo | Alteração |
|---|---|
| `.github/workflows/foxxdesk-build.yml` | Novo workflow manual `FoxxDesk Build`, tag padrão `foxxdesk-nightly`, chamada ao reusable build. |
| `.github/workflows/flutter-build.yml` | Reusable build renomeado; staging, executáveis, MSI/DMG/APK/DEB/RPM/AppImage/Flatpak e releases usam FoxxDesk. |
| `.github/workflows/flutter-nightly.yml`, `flutter-tag.yml`, `flutter-ci.yml` | Nomes exibidos e tag nightly alinhados. |
| `.github/workflows/playground.yml` | Artefatos e bundles de teste alinhados; dependências upstream preservadas. |
| `.github/workflows/fdroid.yml` | Workflow explicitamente marcado como compatibilidade/updater upstream até existir publicação FoxxDesk. |

## Validation

| Comando | Resultado |
|---|---|
| `git diff --check` | PASSOU. |
| `python3 -m py_compile build.py libs/portable/generate.py res/msi/preprocess.py` | PASSOU; caches gerados foram removidos. |
| `python3 build.py --help` | PASSOU. |
| `python3 res/msi/preprocess.py --help` | PASSOU. |
| Parse YAML de `.github/workflows/*.yml` com PyYAML | PASSOU. |
| Parse XML de manifests/plists/metainfo com `xml.etree.ElementTree` | PASSOU. |
| Parse de plists Apple com `plistlib` | PASSOU; `exportOptions.plist` também teve aspas XML inválidas corrigidas. |
| Parse de `flatpak/foxxdesk.json` com `json` | PASSOU. |
| `systemd-analyze verify --root=/tmp/foxxdesk-systemd-root ...` | Arquivo analisado; avisos somente para `network.target` e `pkill` ausentes no root sintético. |
| Parse de `Cargo.toml`, `Cargo.lock` e portable via `tomllib` | PASSOU; nomes package/lock consistentes e `librustdesk` preservada. |
| Verificação programática de chaves `src/lang/*.rs` | PASSOU; chaves preservadas, três overrides ingleses adicionados sem duplicatas. |
| Verificação de recursos renomeados | PASSOU; nomes antigos removidos e novos arquivos FoxxDesk presentes. |
| `cargo fmt --all -- --check` | NÃO EXECUTADO: `cargo: command not found`. |
| `cargo check --locked --features flutter --lib` | NÃO EXECUTADO: `cargo: command not found`. |
| `cargo check --locked --bins` | NÃO EXECUTADO: `cargo: command not found`. |
| `cd flutter && flutter pub get` | NÃO EXECUTADO: `flutter: command not found`. |
| `cd flutter && flutter analyze` | NÃO EXECUTADO: `flutter: command not found`. |
| Build Windows `python3 .\\build.py --portable --flutter ...` | NÃO EXECUTADO: ambiente atual não é Windows e não possui SDK Flutter/Rust. |
| `git grep -n -i foxxdesk` / `carriez` / `foxxdesk` | Executado; 2.095 / 38 / 1.710 ocorrências em arquivos rastreados (locks excluídos), classificadas nas tabelas acima. |
| `find . -iname '*foxxdesk*'` | Restaram somente o workflow third-party `RustDeskTempTopMostWindow` e `res/foxxdesk-banner.svg`. |

## Pending Manual Actions

- Substituir logos, ícones, splash screens e banner upstream por arte oficial FoxxDesk.
- Definir domínio/repositório/release/update server oficial FoxxDesk; `TODO_FOXXDESK_DOMAIN` permanece explícito.
- Definir e-mail oficial de maintainer para DEB/RPM.
- Fornecer Firebase `GoogleService-Info.plist` do bundle `com.foxxdesk.client`.
- Configurar provisioning profile iOS no lugar de `TODO_FOXXDESK_IOS_PROVISIONING_PROFILE`.
- Configurar Apple Team ID no lugar de `TODO_FOXXDESK_IOS_TEAM_ID`.
- Configurar assinatura/certificados oficiais Windows, macOS, Android e iOS.
- Rodar Cargo fmt/check e Flutter pub/analyze em ambiente com toolchains instaladas.
- Validar builds e instalação/desinstalação reais em Windows, macOS, Linux, Android e iOS.
- Decidir política final de migração de dados/configuração de instalações FoxxDesk anteriores.
- Revisar se o suporte aditivo a `rustdesk://` deve permanecer em distribuições que coexistam com FoxxDesk.

## Risks

| Risco | Impacto | Mitigação |
|---|---|---|
| Mudança de package/binário e paths | Scripts externos que chamam `foxxdesk` não encontrarão o novo executável. | Documentar migração e testar instaladores por SO. |
| Novos bundle/application IDs | Assinaturas, Firebase e stores exigem novas credenciais/perfis. | Concluir pendências oficiais antes do release. |
| Toolchains ausentes nesta validação | Erros de compilação específicos de plataforma podem permanecer. | Executar os comandos obrigatórios e Actions antes de publicar. |
| Deep link legado | Pode disputar `rustdesk://` com uma instalação FoxxDesk coexistente. | Remover o handler legado se coexistência for requisito prioritário. |
| Assets upstream | A UI ainda pode exibir arte FoxxDesk apesar dos nomes FoxxDesk. | Substituir somente com assets oficiais aprovados. |
