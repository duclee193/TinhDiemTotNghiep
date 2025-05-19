from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Điểm vào cho Vercel
@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            # Lấy điểm lớp 10
            diem_lop10 = []
            for i in range(1, 8):
                val = request.form.get(f'lop10_{i}', '')
                diem_lop10.append(float(val) if val else 0)
                
            # Lấy điểm lớp 11
            diem_lop11 = []
            for i in range(1, 8):
                val = request.form.get(f'lop11_{i}', '')
                diem_lop11.append(float(val) if val else 0)
                
            # Lấy điểm lớp 12
            diem_lop12 = []
            for i in range(1, 8):
                val = request.form.get(f'lop12_{i}', '')
                diem_lop12.append(float(val) if val else 0)
            
            # Lấy điểm khuyến khích và ưu tiên
            diem_kk = float(request.form.get('diem_kk', 0) or 0)
            diem_ut = float(request.form.get('diem_ut', 0) or 0)
            
            # Tính điểm trung bình các năm học
            tb_lop_10 = sum(diem_lop10) / len(diem_lop10)
            tb_lop_11 = sum(diem_lop11) / len(diem_lop11)
            tb_lop_12 = sum(diem_lop12) / len(diem_lop12)
            
            # Tính điểm xét tốt nghiệp
            diem_tb_nam_hoc = (tb_lop_10 + tb_lop_11 * 2 + tb_lop_12 * 3) / 6
            diem_tot_nghiep = diem_tb_nam_hoc
            
            # Tính điểm cần đạt trong kỳ thi
            diem_can_dat_tot_nghiep = 5.0
            tong_diem_4_mon = 4 * (2 * (diem_can_dat_tot_nghiep - diem_ut) - diem_tb_nam_hoc) - diem_kk
            diem_trung_binh_can_dat = tong_diem_4_mon / 4
            
            result = {
                'tb_lop_10': tb_lop_10,
                'tb_lop_11': tb_lop_11,
                'tb_lop_12': tb_lop_12,
                'diem_tot_nghiep': diem_tot_nghiep,
                'tong_diem_4_mon': tong_diem_4_mon,
                'diem_trung_binh_can_dat': diem_trung_binh_can_dat
            }
        except Exception as e:
            result = {'error': str(e)}
    
    return render_template('index.html', result=result)

# Handler for Vercel serverless function
handler = app
