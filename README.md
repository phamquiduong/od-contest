## Công nghệ phát triển
- Python 3.13
- Django 5
- SQLite3/ PostgreSQL
- Redis
- Gửi mail bằng Celery
- Quản lý lập lịch bằng Celery Beat
- Giám sát hệ thống với Flower và hệ sinh thái Prometheus

<br>

## Cài đặt môi trường ảo cho Python (không bắt buộc)
#### Tạo môi trường ảo
```powershell
python -m venv .venv
```

#### Kích hoạt môi trường ảo
```powershell
.\.venv\Scripts\Activate.ps1
```

> [!CAUTION]
> Nếu bị lỗi thì mở **PowerShell** với quyền admin, chạy lệnh sau và thử lại
> ```powershell
> Set-ExecutionPolicy Unrestricted -Force
> ```

<br>

## Cài đặt các phần mềm hỗ trợ
> [!NOTE]
> **Yêu cầu của server:**<br>
> - **PostgreSQL** (Không bắt buộc): Cơ sở dữ liệu. Bạn có thể cài đặt dùng **SQLite3** khi tắt `DB_ENGINE` và `DB_NAME` trong file `.env`<br>
> - **Redis** (Không bắt buộc): Nó được dùng cho tính năng lưu Session, CSRF. Bạn có thể cài đặt dùng **SQlite3** bằng cách tắt `SESSION_ENGINE` trong `.env`. Tuy nhiên, khi bạn dùng tính năng gửi email bằng **Celery**, bạn bắt buộc phải bật hoặc chuyển qua loại Broken mới trong `settings.py`.

#### Cách 1: Tự động bằng Docker (yêu cầu cấu hình mạnh)
> - Truy cập https://www.docker.com/ để tải và cài đặt Docker Desktop<br>
> - Chạy docker-compose
>   ```powershell
>   .\run_docker.bat
>   ```
>   - Bạn có thể cấu hình kết nối ở file `docker/.env` sau đó chạy lại file `run_docker.bat` để cập nhật cài đặt.<br>
>   - Khi chạy script này nó sẽ hỏi bạn có chạy các cấu hình dịch vụ như `server`, `database`, `celery` và `monitoring`

#### Cách 2: Cài đặt thủ công
> - Tải và cài ứng dụng Redis ở địa chỉ https://github.com/tporadowski/redis/releases
> - Tải và cài đặt PostgreSQL tại địa chỉ https://www.postgresql.org/download/

<br>

## Chuẩn bị cho dự án
#### Bước 1: Cài đặt file môi trường cho dự án
> - Tạo ra file `.env` (Có thể dựa từ file `.env.example`)<br>
> - Sau đó mở file `.env` ra và cài đặt thông số phù hợp với dự án.

#### Bước 2: Cài đặt gói thư viện cho Python
> - Chạy lệnh cài đặt gói cho server
>   ```powershell
>   pip install -r requirements.txt
>   ```
> - Chạy lệnh cài đặt gói phục vụ quá trình phát triển
>   ```powershell
>   pip install -r requirements.dev.txt
>   ```

#### Bước 3: Cập nhật cấu trúc Database
> - Chuyển vào thư mục `src` và chạy lệnh
>   ```powershell
>   python manage.py migrate
>   ```

<br>

## Chạy server
```powershell
.\run_server.bat
```

> [!NOTE]
> - Khi bắt đầu chạy script sẽ hỏi bạn về `cổng mạng (port)` của server. Nếu để trống mặc định là **80**.<br>
> - Bạn truy cập http://localhost:80 để vào được website.

<br>

## Hệ thống Celery gửi mail (Chỉ cần bật khi cần tính năng gửi mail)
#### Chạy Worker
```powershell
.\run_email_worker.bat
```
