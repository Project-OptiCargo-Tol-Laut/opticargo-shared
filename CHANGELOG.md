# Changelog

Semua perubahan yang mencolok pada proyek ini akan didokumentasikan di dalam file ini.

Format pencatatan berpedoman pada [Keep a Changelog](https://keepachangelog.com/id-ID/1.0.0/), 
dan proyek ini mematuhi standar [Semantic Versioning](https://semver.org/lang/id/).

## [1.0.0] - 2026-07-29

### Ditambahkan

- Kontrak final PRD v3.0 untuk seluruh 17 entity family, termasuk variant
  `Base/Create/Update/Read` dan `CargoCapacity` bertipe.
- Enum lifecycle final, booking transition matrix, API/error/pagination/export,
  event envelope dan typed payload, agent state, ML, serta dataset provenance.
- Validator canonical untuk waktu UTC-aware, kapasitas, interval tanggal, status
  payment/document/notification/recommendation, skor, dan abstention.
- JSON Schema current dan snapshot immutable v1.0.0 serta compatibility checker.
- Metadata typed package, examples, dan quality pipeline Python 3.11+.

### Diubah

- `UserRole.operator` dimigrasikan ke nilai wire `operator_kapal`; alias Python
  sementara dipertahankan.
- Error field canonical berubah dari `error_code` ke `code`; alias input/property
  lama dipertahankan, sementara `trace_id` kini wajib.
- Semua model kontrak kini mewarisi strict `ContractModel` dan menolak field asing.

### Dihapus

- Percobaan ORM/SQLModel pada route; persistence tetap dimiliki gateway.

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
