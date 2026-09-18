def to_mau_do_thi_giai_tay():
    # 5 khu vực tương ứng với Đỉnh 1 đến 5 (trong code là index 0 đến 4)
    n = 5

    # Ma trận kề dựa trên hình vẽ bản đồ
    ma_tran_ke = [
        [0, 1, 0, 0, 0],  # Đỉnh 1 giáp 2
        [1, 0, 1, 0, 0],  # Đỉnh 2 giáp 1, 3
        [0, 1, 0, 1, 1],  # Đỉnh 3 giáp 2, 4, 5
        [0, 0, 1, 0, 1],  # Đỉnh 4 giáp 3, 5
        [0, 0, 1, 1, 0]   # Đỉnh 5 giáp 3, 4
    ]

    # Khởi tạo mảng Bậc ban đầu y hệt dòng đầu tiên trong ảnh
    bac = [1, 2, 3, 2, 2]

    # Mảng lưu màu đã tô (-1 là chưa tô)
    mau_da_to = [-1] * n

    # Quy định màu giống hệt ghi chú trong ảnh
    ten_mau = ["Đỏ", "Xanh", "Vàng"]

    print(f"Trạng thái ban đầu Bậc: {bac}")
    print("-" * 50)

    for buoc in range(n):
        # 1. TÌM ĐỈNH CHƯA TÔ CÓ BẬC CAO NHẤT
        max_bac = -1
        dinh_chon = -1

        for i in range(n):
            if mau_da_to[i] == -1 and bac[i] > max_bac:
                max_bac = bac[i]
                dinh_chon = i

        # 2. CHỌN MÀU
        mau_hop_le = 0
        while True:
            xung_dot = False
            for j in range(n):
                if ma_tran_ke[dinh_chon][j] == 1 and mau_da_to[j] == mau_hop_le:
                    xung_dot = True
                    break

            if not xung_dot:
                break
            mau_hop_le += 1

        # Tô màu cho đỉnh được chọn
        mau_da_to[dinh_chon] = mau_hop_le

        # 3. CẬP NHẬT MẢNG BẬC
        bac[dinh_chon] = -1  # Đánh dấu đỉnh này đã tô (đưa về -1)

        # Giảm bậc các đỉnh kề chưa tô đi 1
        for j in range(n):
            if ma_tran_ke[dinh_chon][j] == 1 and mau_da_to[j] == -1:
                bac[j] -= 1

        # In kết quả từng bước
        print(f"Bước {buoc + 1}: Chọn Đỉnh {dinh_chon + 1} -> Tô {ten_mau[mau_hop_le]}")
        print(f"Cập nhật mảng Bậc : {bac}")
        print("-" * 50)


    # === In nhóm màu đã tô
    ten_tinh = ["Kon Tum", "Gia Lai", "Đắk Lắk", "Đắk Nông", "Lâm Đồng"]
    nhom_mau = {}

    for i in range(n):
        mau = mau_da_to[i]
        if mau not in nhom_mau:
            nhom_mau[mau] = []
        nhom_mau[mau].append(ten_tinh[i])

    print("\n--- NHÓM THEO MÀU ---")
    for mau, cac_tinh in nhom_mau.items():
        print(f"Màu {mau + 1} ({ten_mau[mau]}): {', '.join(cac_tinh)}")

    so_mau_can_dung = max(mau_da_to) + 1
    print(f"\n=> Số màu tối thiểu cần sử dụng: {so_mau_can_dung} màu")


# Chạy chương trình
to_mau_do_thi_giai_tay()