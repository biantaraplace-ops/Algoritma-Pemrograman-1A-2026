undangan = set()
webinar_a = set()
webinar_b = set()

print("Masukkan nama undangan:")
undangan.update(input().split(","))

print("\nMasukkan peserta Webinar A:")
webinar_a.update(input().split(","))

print("\nMasukkan peserta Webinar B:")
webinar_b.update(input().split(","))

semua_peserta = webinar_a.union(webinar_b)
hadir_keduanya = webinar_a.intersection(webinar_b)
satu_webinar = webinar_a.symmetric_difference(webinar_b)
tidak_hadir = undangan.difference(semua_peserta)

print("\n=== HASIL DATA WEBINAR ===")
print("Semua peserta:", semua_peserta)
print("Hadir di kedua webinar:", hadir_keduanya)
print("Hanya hadir di satu webinar:", satu_webinar)
print("Undangan tidak hadir:", tidak_hadir)