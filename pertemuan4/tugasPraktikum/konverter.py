import kurs

def idr_ke_asing(jumlah, kode_asing):
    nilai_kurs = kurs.data_kurs.get(kode_asing)
    if nilai_kurs:
        return jumlah / nilai_kurs
    return None

def asing_ke_idr(jumlah, kode_asing):
    nilai_kurs = kurs.data_kurs.get(kode_asing)
    if nilai_kurs:
        return jumlah * nilai_kurs
    return None