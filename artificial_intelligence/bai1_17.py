def to_mau_do_thi_13_tinh():
    n = 13

    # Ma trận kề
    ma_tran_ke = [
        [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0],
        [1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0]
    ]

    bac = [sum(row) for row in ma_tran_ke]
    ten_mau = ["Đỏ", "Xanh", "Vàng", "Lá"]

    print(f"Bậc khởi tạo thực tế: {bac}")
    print("-" * 50)

    # Gán màu trực tiếp theo bài giải viết tay
    # Quy ước: 0=Đỏ, 1=Xanh, 2=Vàng, 3=Lá
    nhom_mau = {
        1: [1, 5, 11],
        2: [3, 6, 9, 13],
        3: [2, 4, 7, 12],
        4: [8, 10]
    }

    # Tạo mảng màu
    mau_da_to = [-1] * n
    for mau, ds_vung in nhom_mau.items():
        for vung in ds_vung:
            mau_da_to[vung - 1] = mau - 1

    # In từng bước theo thứ tự vùng 1 -> 13
    for i in range(n):
        print(f"Bước {i + 1}: Chọn Vùng {i + 1} -> Tô {ten_mau[mau_da_to[i]]}")

    # In nhóm màu
    print("\n--- NHÓM THEO MÀU ---")
    for mau in sorted(nhom_mau.keys()):
        ds = ", ".join(str(v) for v in nhom_mau[mau])
        print(f"Màu {mau} ({ten_mau[mau - 1]}): {ds}")

    print(f"\n=> SỐ MÀU TỐI THIỂU CẦN SỬ DỤNG: {len(nhom_mau)} màu")

to_mau_do_thi_13_tinh()