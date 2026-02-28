import kurs
import konverter
from tabulate import tabulate

def menampilkan_menu():
    print('=== KONVERTER MATA UANG ===')
    tabel_data = [[k, n] for k, n in kurs.data_kurs.items()]
    print(tabulate(tabel_data, headers=['Kode', 'Kurs'],tablefmt='grid'))


def main():
    menampilkan_menu()

    dari= input('\nDari (IDR/USD/EUR/SGD/JPY) : ')
    ke = input('ke (IDR/USD/EUR/SGD/JPY) : ')
    jumlah = float(input('jumlah :'))

    if dari ==  'IDR' and ke in kurs.data_kurs:
        hasil = konverter.idr_ke_asing(jumlah, ke)
        print(f'\nRp {jumlah:.0f} = {hasil:.2f} {ke}')
    elif dari in kurs.data_kurs and ke == 'IDR':
        hasil = konverter.asing_ke_idr(jumlah, dari)
        print(f'\n {jumlah} {dari} = Rp {hasil:.0f}')
    else:
        print('\nOpsi tidak tersedia atau kode salah. Silakan masukkan opsi yang ada dan kode yang benar')

if __name__ == '__main__':
    main()