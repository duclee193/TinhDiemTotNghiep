import tkinter as tk
from tkinter import messagebox

class TinhDiemTotNghiepApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tính điểm tốt nghiệp THPT")
        self.entries = {}
        self.create_widgets()

    def create_widgets(self):
        row = 0
        tk.Label(self.root, text="Nhập điểm 7 môn lớp 10", font=("Arial", 10, "bold")).grid(row=row, column=0, columnspan=7, pady=5)
        row += 1
        self.entries['lop10'] = []
        for i in range(7):
            tk.Label(self.root, text=f"Môn {i+1}").grid(row=row, column=i)
            e = tk.Entry(self.root, width=5)
            e.grid(row=row+1, column=i)
            self.entries['lop10'].append(e)
        row += 2

        tk.Label(self.root, text="Nhập điểm 7 môn lớp 11", font=("Arial", 10, "bold")).grid(row=row, column=0, columnspan=7, pady=5)
        row += 1
        self.entries['lop11'] = []
        for i in range(7):
            tk.Label(self.root, text=f"Môn {i+1}").grid(row=row, column=i)
            e = tk.Entry(self.root, width=5)
            e.grid(row=row+1, column=i)
            self.entries['lop11'].append(e)
        row += 2

        tk.Label(self.root, text="Nhập điểm 7 môn lớp 12", font=("Arial", 10, "bold")).grid(row=row, column=0, columnspan=7, pady=5)
        row += 1
        self.entries['lop12'] = []
        for i in range(7):
            tk.Label(self.root, text=f"Môn {i+1}").grid(row=row, column=i)
            e = tk.Entry(self.root, width=5)
            e.grid(row=row+1, column=i)
            self.entries['lop12'].append(e)
        row += 2

        tk.Label(self.root, text="Tổng điểm khuyến khích (nếu có):").grid(row=row, column=0, columnspan=3, sticky='e')
        self.diem_kk_entry = tk.Entry(self.root, width=7)
        self.diem_kk_entry.grid(row=row, column=3)
        self.diem_kk_entry.insert(0, "0")
        row += 1
        tk.Label(self.root, text="Điểm ưu tiên (nếu có):").grid(row=row, column=0, columnspan=3, sticky='e')
        self.diem_ut_entry = tk.Entry(self.root, width=7)
        self.diem_ut_entry.grid(row=row, column=3)
        self.diem_ut_entry.insert(0, "0")
        row += 1

        self.calc_btn = tk.Button(self.root, text="Tính điểm", command=self.tinh_diem, bg="#4CAF50", fg="white", font=("Arial", 11, "bold"))
        self.calc_btn.grid(row=row, column=0, columnspan=7, pady=10)
        row += 1

        self.result_text = tk.Text(self.root, height=8, width=60, font=("Arial", 10))
        self.result_text.grid(row=row, column=0, columnspan=7, pady=5)
        self.result_text.config(state=tk.DISABLED)

    def tinh_diem_trung_binh(self, diem_mon_hoc):
        return sum(diem_mon_hoc) / len(diem_mon_hoc)

    def tinh_diem_4_mon_can_dat(self, dtb_cac_nam, diem_kk, diem_ut, dxtn_muc_tieu=5):
        tong_diem_4_mon = 4 * (2 * (dxtn_muc_tieu - diem_ut) - dtb_cac_nam) - diem_kk
        diem_trung_binh_can_dat = tong_diem_4_mon / 4
        return tong_diem_4_mon, diem_trung_binh_can_dat

    def tinh_diem(self):
        try:
            diem_lop_10 = [float(e.get()) for e in self.entries['lop10']]
            diem_lop_11 = [float(e.get()) for e in self.entries['lop11']]
            diem_lop_12 = [float(e.get()) for e in self.entries['lop12']]
            for ds in [diem_lop_10, diem_lop_11, diem_lop_12]:
                for d in ds:
                    if d < 0 or d > 10:
                        raise ValueError("Điểm phải từ 0 đến 10")
            diem_kk = float(self.diem_kk_entry.get())
            diem_ut = float(self.diem_ut_entry.get())
            if diem_kk < 0 or diem_ut < 0:
                raise ValueError("Điểm khuyến khích và ưu tiên không được âm")
        except Exception as ex:
            messagebox.showerror("Lỗi nhập liệu", str(ex))
            return

        tb_lop_10 = self.tinh_diem_trung_binh(diem_lop_10)
        tb_lop_11 = self.tinh_diem_trung_binh(diem_lop_11)
        tb_lop_12 = self.tinh_diem_trung_binh(diem_lop_12)
        diem_tot_nghiep = (tb_lop_10 * 1 + tb_lop_11 * 2 + tb_lop_12 * 3) / 6
        tong_diem_4_mon, diem_trung_binh_can_dat = self.tinh_diem_4_mon_can_dat(diem_tot_nghiep, diem_kk, diem_ut)

        result = f"Điểm trung bình lớp 10: {tb_lop_10:.2f}\n"
        result += f"Điểm trung bình lớp 11: {tb_lop_11:.2f}\n"
        result += f"Điểm trung bình lớp 12: {tb_lop_12:.2f}\n"
        result += f"Điểm trung bình các năm học: {diem_tot_nghiep:.2f}\n"
        result += f"\nTổng điểm 4 môn thi cần đạt: {tong_diem_4_mon:.2f}\n"
        result += f"Điểm trung bình 4 môn thi cần đạt: {diem_trung_binh_can_dat:.2f}\n"
        if diem_trung_binh_can_dat <= 0:
            result += "\nBạn đã đủ điểm tốt nghiệp ngay cả khi điểm 4 môn thi bằng 0!"
        elif diem_trung_binh_can_dat > 10:
            result += "\nKhông thể đạt đủ điểm tốt nghiệp với các điểm hiện tại (vì điểm trung bình cần đạt vượt quá 10)."
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result)
        self.result_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = TinhDiemTotNghiepApp(root)
    root.mainloop()
