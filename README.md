## 🚀 Công nghệ sử dụng
- **Backend:** Python 3.13, Django 5
- **Database:** SQLite3 / PostgreSQL
- **Caching & Queue:** Redis
- **Task & Scheduling:** Celery + Celery Beat
- **Email Service:** Celery
- **Monitoring:** Flower, Prometheus ecosystem

<br>

## ⚙️ Môi trường ảo (tùy chọn)
Tạo và kích hoạt môi trường ảo:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

> [!CAUTION]
> Nếu bị lỗi khi kích hoạt, mở **PowerShell** với quyền Admin và chạy:
> ```powershell
> Set-ExecutionPolicy Unrestricted -Force
> ```

<br>

## 🐳 Cài đặt & chạy bằng Docker (khuyên dùng, cần cấu hình mạnh)
### 1. Cài đặt Docker Desktop
👉 https://www.docker.com/

### 2. Chạy bằng script dựng sẵn
```powershell
.\run_docker.bat
```
- Lần đầu chạy sẽ dừng lại để bạn cấu hình `.env.docker` và `docker/.env`.
- Có thể chọn bật các dịch vụ: `server`, `database`, `celery`, `monitoring`.

### 3. Chạy thủ công
```powershell
docker-compose --profile database --profile server up --build -d
```
- Dùng `--profile *` để bật tất cả.
- Hoặc bật riêng từng service:
  ```powershell
  docker-compose up [tên_service] --build -d
  ```

<br>

## 🖥️ Chạy thủ công (không dùng Docker)
### 1. Cài đặt phần mềm hỗ trợ
- Redis (Windows): https://github.com/tporadowski/redis/releases
- PostgreSQL: https://www.postgresql.org/download/

### 2. Cấu hình
- Tạo file `.env` (tham khảo `.env.example`).
- Thiết lập PostgreSQL, Redis và SMTP server.

### 3. Chạy bằng script dựng sẵn
- **Server**
  ```powershell
  .\run_server.bat
  ```
  > - Script sẽ hỏi cổng server, mặc định **80**.
  > - Truy cập http://localhost:80 để vào website.

- **Email Worker**
  ```powershell
  .\run_email_worker.bat
  ```

<br>

## 🛠️ Lệnh thường dùng
- Cài gói cho server
  ```powershell
  pip install -r requirements.txt
  ```

- Cài gói cho môi trường dev
  ```powershell
  pip install -r requirements.dev.txt
  ```

- Tạo migrations
  ```powershell
  python manage.py makemigrations
  ```

- Cập nhật DB schema
  ```powershell
  python manage.py migrate
  ```

- Chạy server dev
  ```powershell
  python manage.py runserver 0.0.0.0:80
  ```
