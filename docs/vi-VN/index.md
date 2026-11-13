---
title: Đại lý AI
description: Mở tác nhân lập trình từ máy tính để bàn ARGVUS.
---

`argvus-ai` là phần tích hợp máy tính để bàn tùy chọn dành cho **OpenCode**, **OpenAI Codex** và **Claude Code**. Nó cung cấp bộ chọn Rofi được chia sẻ, các mục khởi chạy ứng dụng và biểu tượng robot trong nhóm tiện ích trên thanh tác vụ. Nhân viên chạy trong cửa sổ đầu cuối ARGVUS mới và giữ lại thư mục làm việc của người gọi.

Mở bộ chọn bằng **SUPER + A** hoặc nhấp vào **nf-md-robot** trên thanh tác vụ, bên cạnh các điều khiển micrô và âm thanh. Bạn cũng có thể chọn một tác nhân riêng lẻ trong trình khởi chạy ứng dụng.

OpenCode và Codex được cài đặt dưới dạng gói phụ thuộc. Mã Claude chỉ được cài đặt với tư cách là người dùng của bạn khi bạn chọn nó lần đầu tiên. Cài đặt gói, mở/hủy bộ chọn hoặc kiểm tra trạng thái không bao giờ tải xuống Claude. Gói không định cấu hình tài khoản, khóa API hoặc đăng ký; làm theo lời nhắc xác thực của tác nhân đã chọn.

Đọc [Cài đặt](/docs/argvus-ai/installation/) và [Cách sử dụng và khắc phục sự cố](/docs/argvus-ai/usage/).

## Ngôn ngữ

Hạt `ai` Danh mục được cung cấp trong tất cả 18 ARGVUS Ngôn ngữ giao diện và sử dụng các ngôn ngữ chia sẻ `argvus i18n` Chọn lọc và phản công tiếng Anh. Ngôn ngữ giao diện đã chọn được cất giữ như `ARGVUS_LANGUAGE` trong người dùng `locale.conf`; hệ thống khu vực địa phương vẫn còn tách biệt. Các bản dịch được cài đặt làm dữ liệu mà không cần ghi cấu hình người dùng.

## Đại lý được hỗ trợ

Tích hợp này hỗ trợ OpenCode, Codex và Qwen Code có trong gói; Claude Code thông qua mise; Antigravity nếu được cài riêng; cùng Hermes, Cursor CLI và Kimi được cài bằng trình cài đặt chính thức khi chạy lần đầu. Xem [hướng dẫn sử dụng](usage/) để biết cách liệt kê và gỡ cài đặt các tác nhân bên ngoài do ARGVUS quản lý.

Gemini CLI được cung cấp qua phụ thuộc Arch `gemini-cli` và xuất hiện trong bộ chọn khi lệnh `gemini` khả dụng.
