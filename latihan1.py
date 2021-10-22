
nama_lengkap = str(input("Masukan Nama Lengkap Anda = "))
nama_mhs = str(input("Masukan Nama Panggilan Anda = "))
nim_mhs = str(input("Masukan NIM Anda = "))
kelas_mhs = str(input("Masukan Kelas Anda = "))
tempat_mhs = str(input("Masukan Tempat Lahir Anda = "))
umur = str(input("Masukan Umur Anda = "))
alamat = str(input("Masukan Alamat Anda = "))
no_mhs = str(input("Masukan Nomer Anda = "))

print("")
print("")
tampilInfoMhs = "Detail dari Informasi Anda..\n\nNama Lengkap Anda Adalah : "+nama_lengkap+"\nNama panggilan Anda Adalah : "+nama_mhs+"\nNim Anda Adalah : "+nim_mhs+"\nAnda berada dikelas : "+kelas_mhs+"\nTempat lahir Anda Adalah : "+tempat_mhs+"\nBerumur : "+umur 
print(tampilInfoMhs)
print("Nama Lengkap Anda adalah {} Nama panggilan Anda {} dengan nim {} bernama {} dan berumur {}".format(nama_lengkap, nama_mhs , nim_mhs, kelas_mhs, umur))