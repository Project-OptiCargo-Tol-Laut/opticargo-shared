# OptiCargo Shared (`opticargo-shared`)

**Versi:** 0.1.0
**Tipe:** Python Package (Library)
**Repositori:** `opticargo-ai/opticargo-shared`

Selamat datang di `opticargo-shared`! Repositori ini berfungsi sebagai **sumber kebenaran tunggal (*Single Source of Truth*)** untuk seluruh skema data, *enum*, dan *state* AI pada platform OptiCargo AI. Paket ini dikonsumsi oleh tim Backend, Frontend, dan AI (`opticargo-gateway-api`, `opticargo-agents`, dll.) agar bentuk data konsisten di seluruh layanan.

---

## Struktur Direktori & Tugas Tiap Folder

- **`src/opticargo_shared/models/`**
  Berisi skema entitas inti (Pydantic). Setiap model di sini selaras 1:1 dengan struktur tabel *database* PostgreSQL. Tidak mengandung logika bisnis atau dependensi ke SQLAlchemy.
  
- **`src/opticargo_shared/agent_state/`**
  Berisi model Pydantic yang mendefinisikan *state* untuk agen-agen AI (LangGraph) yang beroperasi di `opticargo-agents`.

- **`src/opticargo_shared/api/`**
  Berisi skema generik untuk respons API, seperti format paginasi dan pesan *error*. Membantu memastikan konsistensi *endpoint* di *gateway*.

- **`src/opticargo_shared/enums.py`**
  Mendefinisikan *enum* status dan tipe yang dipakai lintas layanan (misal: `ShipStatus`, `VoyageStatus`).

- **`src/opticargo_shared/constants.py`**
  Menyimpan nilai-nilai konstan (misalnya default ukuran halaman) agar tidak ada *magic numbers* yang di-hardcode.

- **`tests/`**
  Berisi file pengujian (`test_models.py`, `test_api_schemas.py`, `test_agent_state.py`) untuk memvalidasi kelayakan setiap skema menggunakan `pytest`.

---

## Cara Menjalankan & Instalasi Lokal

Sebagai pengembang, jika Anda ingin menggunakan atau mengembangkan repositori ini secara lokal, ikuti langkah berikut:

### 1. Instalasi (Mode Editable)
Pastikan Anda berada di direktori akar (`opticargo-shared`) yang memiliki file `pyproject.toml`, lalu jalankan:
```bash
pip install -e .
```
Jika Anda berencana untuk berkontribusi dan menjalankan pengujian (testing) atau linting, instal beserta *tools* pengembangannya:
```bash
pip install -e ".[test,lint]"
```

### 2. Contoh Pemakaian
Setelah terinstal, Anda dapat langsung mengimpornya dalam proyek Python Anda seperti ini:
```python
from opticargo_shared.models.ship import Ship
from opticargo_shared.enums import ShipStatus

# Menggunakan model
kapal = Ship(
    id="b839bb04-f655-46b0-96b6-397c0f16e379",
    name="KM Nusantara Jaya",
    imo_number="IMO1234567",
    ship_type="General Cargo",
    gross_tonnage=5000,
    deadweight_tonnage=7000,
    cargo_capacity_m3=8500,
    operator_id="a123bb04-f655-46b0-96b6-111111111111",
    flag="Indonesia",
    status=ShipStatus.active,
    created_at="2026-07-24T12:00:00Z"
)
print(kapal.name)
```

### 3. Menjalankan Pengujian (Testing)
Pastikan paket sudah diinstal bersama `[test]`. Jalankan:
```bash
pytest tests/ -v
```
Seluruh fungsi wajib memberikan hasil `PASSED` hijau sebelum kode dapat digabungkan (*merge*).

---

## 4. Instalasi Lintas Repo
Bagi tim konsumen (seperti tim Backend di `opticargo-gateway-api` atau tim AI di `opticargo-agents`), Anda tidak perlu mengkloning repositori ini. Cukup instal paket ini langsung dari GitHub menggunakan *tag* versi yang disepakati.

Jalankan perintah berikut di terminal proyek Anda:
```bash
pip install git+[https://github.com/opticargo-ai/opticargo-shared.git@v0.1.0](https://github.com/opticargo-ai/opticargo-shared.git@v0.1.0)

---

## Informasi Penting: Aturan Kontribusi & Perubahan

### Semantic Versioning (Semver)
Repositori ini sangat sensitif terhadap perubahan karena digunakan oleh seluruh tim. 
- Jika Anda mengubah tipe data, menghapus, atau merename *field* yang sudah ada -> **Naikkan Versi MAJOR** (contoh: 0.1.0 menjadi 1.0.0). Ini disebut *Breaking Change*.
- Jika Anda hanya menambahkan *field* opsional baru -> **Naikkan Versi MINOR** (contoh: 0.1.0 menjadi 0.2.0).
- Pembaruan versi dilakukan dengan mengubah nilai `version` di dalam `pyproject.toml`.