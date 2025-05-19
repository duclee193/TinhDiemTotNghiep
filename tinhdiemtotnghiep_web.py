from flask import Flask, render_template, request

app = Flask(__name__)

def tinh_diem_trung_binh(diem_mon_hoc):
    return sum(diem_mon_hoc) / len(diem_mon_hoc)

def tinh_diem_4_mon_can_dat(dtb_cac_nam, diem_kk, diem_ut, dxtn_muc_tieu=5):
    tong_diem_4_mon = 4 * (2 * (dxtn_muc_tieu - diem_ut) - dtb_cac_nam) - diem_kk
    diem_trung_binh_can_dat = tong_diem_4_mon / 4
    return tong_diem_4_mon, diem_trung_binh_can_dat

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            diem_lop_10 = [float(request.form.get(f'lop10_{i+1}', 0)) for i in range(7)]
            diem_lop_11 = [float(request.form.get(f'lop11_{i+1}', 0)) for i in range(7)]
            diem_lop_12 = [float(request.form.get(f'lop12_{i+1}', 0)) for i in range(7)]
            diem_kk = float(request.form.get('diem_kk', 0))
            diem_ut = float(request.form.get('diem_ut', 0))
            tb_lop_10 = tinh_diem_trung_binh(diem_lop_10)
            tb_lop_11 = tinh_diem_trung_binh(diem_lop_11)
            tb_lop_12 = tinh_diem_trung_binh(diem_lop_12)
            diem_tot_nghiep = (tb_lop_10 * 1 + tb_lop_11 * 2 + tb_lop_12 * 3) / 6
            tong_diem_4_mon, diem_trung_binh_can_dat = tinh_diem_4_mon_can_dat(diem_tot_nghiep, diem_kk, diem_ut)
            result = {
                'tb_lop_10': tb_lop_10,
                'tb_lop_11': tb_lop_11,
                'tb_lop_12': tb_lop_12,
                'diem_tot_nghiep': diem_tot_nghiep,
                'tong_diem_4_mon': tong_diem_4_mon,
                'diem_trung_binh_can_dat': diem_trung_binh_can_dat
            }
        except Exception as ex:
            result = {'error': str(ex)}
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
