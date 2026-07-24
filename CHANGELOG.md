# Changelog

Semua perubahan yang mencolok pada proyek ini akan didokumentasikan di dalam file ini.

Format pencatatan berpedoman pada [Keep a Changelog](https://keepachangelog.com/id-ID/1.0.0/), 
dan proyek ini mematuhi standar [Semantic Versioning](https://semver.org/lang/id/).

## [0.1.0] - 2026-07-24

### Ditambahkan
- Inisialisasi awal (*initial release*) paket `opticargo-shared`.
- Pembuatan struktur *file* konfigurasi inti (`pyproject.toml`, `README.md`, `.gitignore`).
- Pendefinisian `enums.py` lintas domain (seperti `UserRole`, `ShipStatus`, `VoyageStatus`).
- Implementasi 13 model Pydantic yang selaras 1:1 dengan struktur tabel *database* PostgreSQL (sesuai Bagian 14 Dokumen Perancangan Sistem), termasuk entitas `User`, `Ship`, `Voyage`, dan `Port`.
- Pembuatan skema API (*Pagination* dan *Error Response*) di dalam direktori `api/`.
- Pendefinisian awal model *state agent* (`BaseAgentState`, `GraphAnalysisInput`) di dalam direktori `agent_state/` untuk integrasi LangGraph.
- Penetapan standar *testing* menggunakan `pytest` untuk memastikan validitas model.
- Pendefinisian nilai konstan di dalam `constants.py`.