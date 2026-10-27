def cari(data, nim):
    return data.get(nim, "data tidak ditemukan")
mahasiswa = {
    "A001": {"nama": "Ayu", "nilai": 85},
    "A002": {"nama": "paji", "nilai": 75}
}
print(cari(mahasiswa, "A002"))
print(cari(mahasiswa, "A003"))