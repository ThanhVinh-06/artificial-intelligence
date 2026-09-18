def phan_cong_cong_viec(t, so_may):
    so_viec = len(t[0])  # Số công việc (số cột)
    so_nguoi = len(t)    # Số người (số hàng)

    # Tính trung bình thời gian của mỗi công việc theo cột (AVG)
    avg = []
    for j in range(so_viec):
        trung_binh = sum(t[i][j] for i in range(so_nguoi)) / so_nguoi
        avg.append((j, round(trung_binh, 2)))  # Lưu (chỉ số việc, avg)

    # NGUYÊN LÝ THỨ TỰ: Sắp xếp công việc theo AVG giảm dần
    avg.sort(key=lambda x: x[1], reverse=True)

    # Khởi tạo tổng thời gian làm việc của mỗi người = 0
    tong_thoi_gian = [0] * so_may

    # Khởi tạo danh sách công việc được phân cho từng người (ban đầu rỗng)
    nguoi = [[] for _ in range(so_may)]

    # NGUYÊN LÝ THAM LAM: Lặp qua từng công việc theo thứ tự AVG giảm dần
    for chi_so_viec, _ in avg:

        # Với công việc hiện tại, tìm người sao cho
        # (tổng thời gian hiện tại + t_ij) là nhỏ nhất
        min_tong = float('inf')
        nguoi_chon = -1

        for i in range(so_nguoi):
            tong_moi = tong_thoi_gian[i] + t[i][chi_so_viec]
            if tong_moi < min_tong:
                min_tong = tong_moi
                nguoi_chon = i

        # Phân công việc cho người được chọn
        nguoi[nguoi_chon].append((chi_so_viec + 1, t[nguoi_chon][chi_so_viec]))

        # Cập nhật tổng thời gian của người đó
        tong_thoi_gian[nguoi_chon] += t[nguoi_chon][chi_so_viec]

    return nguoi, tong_thoi_gian


# === Dữ liệu đầu vào
# Ma trận t[i][j]: thời gian người i thực hiện công việc j
t = [
    [5, 5, 4, 10, 8, 6, 12, 8],   # Người 1
    [7, 5, 7,  3, 9, 7,  8, 5],   # Người 2
    [10, 6, 7, 8, 10, 6, 5, 7],   # Người 3
]

so_may = 3

# === Gọi hàm phân công
nguoi, tong_thoi_gian = phan_cong_cong_viec(t, so_may)

# ==================== XUẤT KẾT QUẢ ====================
print("KET QUA PHAN CONG")
print("--------------------------")

for i in range(so_may):
    print(f"Nguoi {i + 1}:")

    for ma_cv, tg in nguoi[i]:
        print("  Cong viec thu: " + str(ma_cv), "=", tg)

    print("  Tong thoi gian =", tong_thoi_gian[i])
    print()

print("--------------------------")
print("Thoi gian hoan thanh tat ca cong viec =", max(tong_thoi_gian))