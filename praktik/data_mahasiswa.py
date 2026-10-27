def cari_mahasiswa(data, nim):
    return data.get(nim)
def rata_rata_nilai(data):
    if len(data) == 0:
        return 0
    total = 0
    for info in data.values():
        total += info["nilai"]
    return total / len(data)

data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "B", "nilai": 85},
    "A002": {"nama": "paji", "kelas": "A", "nilai": 75},
    "A003": {"nama": " citra", "kelas": "B", "nilai": 78},
    "A004": {"nama": "deni", "kelas": "A", "nilai": 88},
    "A005": {"nama": "eka", "kelas": "B", "nilai": 80}
}
nim = "A003"
hasil = cari_mahasiswa(data_mahasiswa, nim)
if hasil is not None:
    print(f"{nim}: {hasil}")
else:
    print("data tidak ditemukan")
data_mahasiswa["A006"] = {
    "nama": "fajar",
    "kelas": "A",
    "nilai": 80
}
data_mahasiswa["A002"]["nilai"] = 82
for nim, info in data_mahasiswa.items():
    print(nim, info)
print(f"rata-rata = {rata_rata_nilai(data_mahasiswa):.2f}")