## 🚀 Công nghệ sử dụng

| Thông tin             | Chi tiết                                                                                             |
| --------------------- | ---------------------------------------------------------------------------------------------------- |
| Ngôn ngữ lập trình    | Python 3.13                                                                                          |
| Framework Backend     | Django 5                                                                                             |
| Cơ sở dữ liệu         | SQLite3 / PostgreSQL                                                                                 |
| Bộ nhớ đệm & Hàng đợi | Redis                                                                                                |
| Task & Lịch trình     | Celery + Celery Beat                                                                                 |
| Dịch vụ Email         | Celery                                                                                               |
| Giám sát & Quan sát   | Flower<br>Prometheus<br>- django-exporter<br>- celery-exporter<br>- black-exporter<br>- AlertManager |

<br>

## ⚙️ Môi trường ảo (tùy chọn)
Tạo và kích hoạt môi trường ảo:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

> [!CAUTION]
> Nếu gặp lỗi khi kích hoạt, mở **PowerShell** với quyền Admin và chạy:
>
> ```powershell
> Set-ExecutionPolicy Unrestricted -Force
> ```

<br>

## 🐳 Chạy bằng Docker (khuyên dùng, yêu cầu cấu hình mạnh)
### Cài đặt Docker Desktop
👉 https://www.docker.com/

### Chạy bằng script dựng sẵn
```powershell
.\run_docker.bat
```

<br>

## 🖥️ Chạy thủ công (không dùng Docker)
### Chạy bằng script dựng sẵn
```powershell
.\run_server.bat
```

<br>

## Sơ đồ của hệ thống
![Infra diagram](./docs/infra.drawio.svg)
