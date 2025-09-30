🔧 Cấu hình cơ bản:
FastAPI app với database connection (PostgreSQL)
Database dependency (get_db()) để quản lý session
Auto-create tables khi khởi động ứng dụng
JWT Authentication với OAuth2PasswordBearer

Hướng dẫn cài đặt:
Tạo file .env với:
# JWT Authentication
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Database Configuration
DATABASE_URL=postgresql://username:password@localhost:5432/dbname


📋 API Endpoints:
1. Service Info
GET / - Trả về thông tin service (tên, version, status)

2. Authentication (Xác thực)
POST /auth/register - Đăng ký người dùng mới
   • Input: username, email, password, full_name (optional), user_type (PASSENGER/DRIVER)
   • Kiểm tra email đã tồn tại chưa
   • Mã hóa password và lưu vào database

POST /auth/login - Đăng nhập người dùng
   • Input: email/username + password (OAuth2 form)
   • Xác thực thông tin đăng nhập
   • Trả về JWT access token

POST /auth/logout - Đăng xuất người dùng
   • Yêu cầu authentication
   • Trả về thông báo đăng xuất thành công

3. User Management (Quản lý người dùng)
GET /users/me - Lấy thông tin người dùng hiện tại
   • Yêu cầu authentication
   • Trả về thông tin chi tiết của user đang đăng nhập

4. Driver Management (Quản lý tài xế)
POST /drivers/profile - Tạo hồ sơ tài xế
   • Yêu cầu authentication (chỉ DRIVER)
   • Input: license_num, birth, card_num
   • Lưu thông tin hồ sơ tài xế vào database

POST /drivers/vehicles - Đăng ký xe cho tài xế
   • Yêu cầu authentication (chỉ DRIVER)
   • Input: license_plate, seat_type
   • Lưu thông tin xe vào database
🔒 Bảo mật:
JWT token authentication với OAuth2PasswordBearer
Password hashing (bcrypt)
Email validation với EmailStr
Duplicate email checking
Protected routes yêu cầu valid JWT token
Role-based access control (chỉ DRIVER có thể tạo profile và đăng ký xe)

📊 Database Models hỗ trợ:
User: 
   • user_id (UUID), username, email, password, full_name
   • user_type (PASSENGER/DRIVER)
   • created_at, updated_at (timestamps)

DriverProfile:
   • user_id (UUID, Foreign Key), license_num, birth
   • rating_score (decimal), card_num

Vehicle:
   • vehicle_id (UUID), user_id (Foreign Key)
   • license_plate, seat_type (integer)