def phan_cong_luan_van(danh_sach_lv, toc_do_danh_may):
    # toc_do_danh_may là mảng chứa số trang/giờ của từng người
    so_nguoi = len(toc_do_danh_may)

    # Sắp xếp luận văn theo số trang giảm dần (Nguyên lý thứ tự)
    # x[1] là số trang của luận văn
    lv_da_sap_xep = sorted(danh_sach_lv, key=lambda x: x[1], reverse=True)

    tong_thoi_gian = [0.0] * so_nguoi
    phan_cong = [[] for _ in range(so_nguoi)]

    # Phân công (Nguyên lý tham lam)
    for ten_lv, so_trang in lv_da_sap_xep:
        # Tính thử thời gian hoàn thành nếu giao cho từng người
        thoi_gian_du_kien = []
        for i in range(so_nguoi):
            tg_go_xong = so_trang / toc_do_danh_may[i]
            thoi_gian_du_kien.append(tong_thoi_gian[i] + tg_go_xong)

        # Chọn người có thời gian hoàn thành sau khi giao là thấp nhất
        nguoi_chon = thoi_gian_du_kien.index(min(thoi_gian_du_kien))

        # Giao việc và cập nhật
        tg_thuc_te = so_trang / toc_do_danh_may[nguoi_chon]
        phan_cong[nguoi_chon].append((ten_lv, so_trang))
        tong_thoi_gian[nguoi_chon] += tg_thuc_te

    return phan_cong, tong_thoi_gian


# === Dữ liệu đề bài
luan_van = [
    ("Q1", 205), ("Q2", 135), ("Q3", 80), ("Q4", 90),
    ("Q5", 70), ("Q6", 110), ("Q7", 60), ("Q8", 85),
    ("Q9", 200), ("Q10", 140), ("Q11", 170), ("Q12", 120)
]

# Tốc độ làm việc: Nhân viên = 8 trang/h, Quản lý = 4 trang/h
toc_do_cau_a = [8, 8, 8]  # 3 nhân viên
toc_do_cau_b = [8, 8, 8, 4]  # 3 nhân viên + 1 quản lý

# === Câu a
print("=== CÂU A: 3 NHÂN VIÊN ===")
pc_a, tg_a = phan_cong_luan_van(luan_van, toc_do_cau_a)
for i in range(3):
    chi_tiet = ", ".join([f"{ten} ({trang}tr)" for ten, trang in pc_a[i]])
    print(f"Nhân viên {i + 1}: {chi_tiet} -> Tổng thời gian: {tg_a[i]:.2f} giờ")
print(f"=> THỜI GIAN HOÀN THÀNH SỚM NHẤT: {max(tg_a):.2f} giờ\n")

# === Câu b
print("=== CÂU B: 3 NHÂN VIÊN + 1 QUẢN LÝ ===")
pc_b, tg_b = phan_cong_luan_van(luan_van, toc_do_cau_b)
for i in range(4):
    vai_tro = "Nhân viên" if i < 3 else "Quản lý"
    chi_tiet = ", ".join([f"{ten} ({trang}tr)" for ten, trang in pc_b[i]])
    print(f"{vai_tro} {i + 1 if i < 3 else ''}: {chi_tiet} -> Tổng thời gian: {tg_b[i]:.2f} giờ")
print(f"=> THỜI GIAN HOÀN THÀNH SỚM NHẤT: {max(tg_b):.2f} giờ")