nama = ' Ahmad Fadil'
nim  = '231031091'
meet = 'Praktikum 3 (String)'
prodi= 'Sistem Informasi C'
email= 'ahmadfadilahhmad63@gmail.com'
ttl = '04-April-2005'
alamat = 'jl.Batu Merah'
asal = 'Sidrap'
hobi = 'Olahraga'
tinggi = 162

sp = 40
print('-'*sp)
print(nama.upper().center(sp))
print(nim.center(sp))
print('\n'*2)
print(meet.rjust(sp))
print(prodi.rjust(sp))
print(email.lower().rjust(sp))
print('-'*sp)

print(f'''\tHalo, nama saya {nama} dengan NIM {nim} dari prodi {prodi}, ini adalah file {meet}. Terima kasih.\n''')

print(f'''Biodata saya,
Nama\t: {nama.upper()}
NIM\t: {nim}
Prodi\t: {prodi}
TTL\t: {ttl}
Alamat\t: {alamat}
Asal\t: {asal}
hobi\t: {hobi}
tinggi\t: {tinggi}cm
      ''')






