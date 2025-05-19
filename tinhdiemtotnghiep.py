# filepath: c:\Users\ducor\Desktop\app tính điểm\tinhdiemtotnghiep.py

# Program tính điểm trung bình 7 môn học trong 3 năm lớp 10, 11, 12
# và tính điểm trung bình tốt nghiệp

def nhap_diem(lop):
    """Hàm nhập điểm cho 7 môn học của một lớp"""
    print(f"\nNhập điểm cho lớp {lop}:")
    diem_mon_hoc = []
    
    for i in range(7):
        while True:
            try:
                diem = float(input(f"Nhập điểm môn học {i+1}: "))
                if 0 <= diem <= 10:
                    diem_mon_hoc.append(diem)
                    break
                else:
                    print("Điểm phải nằm trong khoảng từ 0 đến 10.")
            except ValueError:
                print("Vui lòng nhập một số hợp lệ.")
    
    return diem_mon_hoc

def tinh_diem_trung_binh(diem_mon_hoc):
    """Hàm tính điểm trung bình của các môn học"""
    return sum(diem_mon_hoc) / len(diem_mon_hoc)

def tinh_diem_4_mon_can_dat(dtb_cac_nam, diem_kk, diem_ut, dxtn_muc_tieu=5):
    """Tính điểm 4 môn thi cần đạt để đạt được ĐXTN mục tiêu"""
    # ĐXTN = [(Tổng điểm 4 môn thi + Tổng điểm KK (nếu có))/4 + ĐTB các năm học]/2 + Điểm ƯT (nếu có)
    # => Tổng điểm 4 môn thi = 4 * [2 * (ĐXTN - Điểm ƯT) - ĐTB các năm học] - Tổng điểm KK
    
    tong_diem_4_mon = 4 * (2 * (dxtn_muc_tieu - diem_ut) - dtb_cac_nam) - diem_kk
    diem_trung_binh_can_dat = tong_diem_4_mon / 4
    
    return tong_diem_4_mon, diem_trung_binh_can_dat

def main():
    print("CHƯƠNG TRÌNH TÍNH ĐIỂM TRUNG BÌNH TỐT NGHIỆP")
    print("=============================================")
    
    # Nhập điểm cho các lớp
    diem_lop_10 = nhap_diem(10)
    diem_lop_11 = nhap_diem(11)
    diem_lop_12 = nhap_diem(12)
    
    # Tính điểm trung bình từng lớp
    tb_lop_10 = tinh_diem_trung_binh(diem_lop_10)
    tb_lop_11 = tinh_diem_trung_binh(diem_lop_11)
    tb_lop_12 = tinh_diem_trung_binh(diem_lop_12)
    
    # Tính điểm trung bình tổng hợp theo công thức
    diem_tot_nghiep = (tb_lop_10 * 1 + tb_lop_11 * 2 + tb_lop_12 * 3) / 6
    
    # In kết quả
    print("\nKẾT QUẢ TÍNH ĐIỂM:")
    print(f"Điểm trung bình lớp 10: {tb_lop_10:.2f}")
    print(f"Điểm trung bình lớp 11: {tb_lop_11:.2f}")
    print(f"Điểm trung bình lớp 12: {tb_lop_12:.2f}")
    print(f"Điểm trung bình các năm học: {diem_tot_nghiep:.2f}")
    
    # Tính điểm cần đạt để đủ tốt nghiệp (ĐXTN = 5)
    print("\nTÍNH ĐIỂM CẦN ĐẠT ĐỂ ĐỦ TỐT NGHIỆP (ĐXTN = 5)")
    
    # Nhập điểm khuyến khích và ưu tiên
    while True:
        try:
            diem_kk = float(input("Nhập tổng điểm khuyến khích KK (0 nếu không có): "))
            if diem_kk >= 0:
                break
            else:
                print("Điểm khuyến khích không được âm.")
        except ValueError:
            print("Vui lòng nhập một số hợp lệ.")
    
    while True:
        try:
            diem_ut = float(input("Nhập điểm ưu tiên UT (0 nếu không có): "))
            if diem_ut >= 0:
                break
            else:
                print("Điểm ưu tiên không được âm.")
        except ValueError:
            print("Vui lòng nhập một số hợp lệ.")
    
    # Tính điểm 4 môn thi cần đạt
    tong_diem_4_mon, diem_trung_binh_can_dat = tinh_diem_4_mon_can_dat(diem_tot_nghiep, diem_kk, diem_ut)
    
    print(f"\nVới điểm trung bình các năm học là {diem_tot_nghiep:.2f}, điểm KK là {diem_kk:.1f}, và điểm UT là {diem_ut:.1f}:")
    print(f"Tổng điểm 4 môn thi cần đạt: {tong_diem_4_mon:.2f}")
    print(f"Điểm trung bình 4 môn thi cần đạt: {diem_trung_binh_can_dat:.2f}")
    
    if diem_trung_binh_can_dat <= 0:
        print("\nBạn đã đủ điểm tốt nghiệp ngay cả khi điểm 4 môn thi bằng 0!")
    elif diem_trung_binh_can_dat > 10:
        print("\nKhông thể đạt đủ điểm tốt nghiệp với các điểm hiện tại (vì điểm trung bình cần đạt vượt quá 10).")
    
if __name__ == "__main__":
    main()