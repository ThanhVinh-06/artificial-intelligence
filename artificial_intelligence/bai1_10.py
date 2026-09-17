def phan_cong_cong_viec(thoi_gian, so_may):
    # Tạo danh sách các cặp (mã công việc, thời gian thực hiện)
    # Đánh số công việc từ 1 đến n
    cong_viec = []
    for i in range(len(thoi_gian)):
        cong_viec.append((i + 1, thoi_gian[i]))

    # NGUYÊN LÝ THỨ TỰ: Sắp xếp công việc theo thời gian GIẢM DẦN
    cong_viec.sort(key=lambda x: x[1], reverse=True)

    # Khởi tạo tổng thời gian làm việc của mỗi máy = 0
    tong_thoi_gian = [0] * so_may

    # Khởi tạo danh sách công việc được phân cho từng máy (ban đầu rỗng)
    may = [[] for _ in range(so_may)]

    # Lặp qua từng công việc đã sắp xếp (từ việc nặng nhất đến nhẹ nhất)
    for ma_cv, thoi_gian_cv in cong_viec:

        # NGUYÊN LÝ THAM LAM: Tìm máy có tổng thời gian thấp nhất (máy rảnh nhất)
        vi_tri_may = tong_thoi_gian.index(min(tong_thoi_gian))

        # Phân công việc hiện tại cho máy rảnh nhất
        may[vi_tri_may].append((ma_cv, thoi_gian_cv))

        # Cập nhật tổng thời gian của máy đó
        tong_thoi_gian[vi_tri_may] += thoi_gian_cv

    # Trả về kết quả: danh sách phân công và tổng thời gian mỗi máy
    return may, tong_thoi_gian


# === Dữ liệu đầu vào
# Thời gian thực hiện 12 công việc: t1=5, t2=7, ..., t12=10
thoi_gian = [5, 7, 15, 3, 18, 40, 15, 7, 20, 14, 6, 10]

# Số lượng máy
so_may = 3

# === Gọi hàm phân công
may, tong_thoi_gian = phan_cong_cong_viec(thoi_gian, so_may)

# === Xuất kết quả
print("KET QUA PHAN CONG")
print("--------------------------")

# In chi tiết phân công của từng máy
for i in range(so_may):
    print("May", i + 1, ":")

    # In từng công việc được giao cho máy i
    for ma_cv, tg in may[i]:
        print("  Cong viec thu: " + str(ma_cv), "=", tg)

    # In tổng thời gian của máy i
    print("  Tong thoi gian =", tong_thoi_gian[i])
    print()

print("--------------------------")
# Thời gian hoàn thành = thời gian của máy bận nhất (giá trị lớn nhất)
print("Thoi gian hoan thanh tat ca cong viec =", max(tong_thoi_gian))