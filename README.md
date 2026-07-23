# opticargo-shared

Package Python bersama berisi schema data (Pydantic models), tipe state
LangGraph, konstanta, dan util yang dipakai lintas service agar seluruh
komponen OptiCargo AI konsisten.

## Isi
- Pydantic models: Ship, Port, Commodity, Voyage, CargoListing, Booking,
  Recommendation, dll — selaras dengan skema database di Bagian 14 dokumen desain.
- Tipe state LangGraph yang dipertukarkan antar agent.
- Konstanta enum (status voyage, tipe komoditas, role user).
- Util umum: konversi satuan, validasi regulasi dasar.

## Tech Stack
- Python, Pydantic

## Dependensi Repo Lain
- Dipakai (di-`pip install` sebagai dependency) oleh: `opticargo-gateway-api`,
  `opticargo-agents`, `opticargo-rag-pipeline`, `opticargo-knowledge-graph`.

## Publish
Package di-versioning semver dan dipublish ke private index (lihat
`opticargo-infra` untuk konfigurasi registry), atau digunakan lewat git submodule
saat MVP untuk mempercepat iterasi.

## Instalasi
    pip install git+https://github.com/opticargo-ai/opticargo-shared.git@v0.1.0